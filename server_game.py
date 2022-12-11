import pygame
import time
from online_game import OnlineGame
from content.camera import Camera
import content.game_function as gf
from Web.Modules.OptType import OptType


class ServerGame(OnlineGame):
    def __init__(self, settings, net, room_id, map_name, player_names, addresses: dict={}):
        super().__init__(settings, None, net, room_id, map_name, player_names)

        self.new_bullets = dict()  # 上次发消息到这次发消息新增的子弹
        self.dead_bullets_id = set()  # 上次发消息到这次发消息减少的子弹

        # self.camera = None  # TODO：调试完成后去掉screen和camera
        self.addresses = addresses  # {player_name: address}

        self.send_bullets_beg = 0  # 这次发送子弹消息的起始index
        self.send_bullets_num = 50  # 每次发送多少子弹的消息

    def main(self):
        """最终要调用的函数"""
        gf.init_pygame_window()
        # self.camera = Camera(self.settings, self.screen)

        print('开始校时')
        # 校时并确定每个player对应的address
        while len(self.addresses) != len(self.player_names):
            # print(self.addresses)
            pass
        print('完成校时')

        super().main()

    def restart(self):
        """重置状态到游戏开始"""
        super().restart()
        self.new_bullets.clear()
        self.dead_bullets_id.clear()
        self.sended_tick = 20 * self.physics_dt

    def get_start_time(self) -> float:
        print('开始发送游戏开始时间')
        start_time = gf.get_time()+3.5
        time.sleep(0.5)
        self.send_start_game_time(start_time)
        print('游戏开始时间发送成功')
        return start_time

    def send_start_game_time(self, start_time):
        """向所有玩家广播游戏开始时间"""
        msg = {
            'opt': OptType.ServerStartGameTime,
            'time': start_time,
            'args': [self.room_id],
            'kwargs': {}
        }
        self.send_all(msg)

    def send_all(self, msg: dict):
        """向所有玩家广播msg"""
        for address in self.addresses.values():
            self.net.send(address, msg)

    def physic_update(self):
        """每个物理dt的更新行为"""
        super().physic_update()  # 发消息，收消息，更新时间
        self.check_collisions()
        self.gm.all_move(self.physics_dt)
        self.ships_fire_bullet()

    def send_msgs_physic_loop(self):
        """发送消息"""
        self.send_all_ships_msg()
        self.send_add_del_bullets_msg()

        # self.send_part_bullets_msg()

    def send_add_del_bullets_msg(self):
        """广播new_bullets和dead_bullets"""
        msg = {
            'opt': OptType.AddDelBullets,
            'tick': self.now_tick,
            'args': [self.make_new_bullets_msg(),
                     self.make_dead_bullets_msg()]
        }
        self.send_all(msg)

    def send_all_ships_msg(self):
        """广播all_ships"""
        msg = {
            'opt': OptType.AllShips,
            'tick': self.now_tick,
            'args': [self.gm.make_ships_msg(), self.gm.make_dead_players_name_msg()]
        }
        self.send_all(msg)

    def send_part_bullets_msg(self):
        """发送所有子弹的消息"""
        msg = {
            'opt': OptType.Bullets,
            'tick': self.now_tick,
            'args': self.make_part_bullets_msg()
        }
        self.send_all(msg)

    def make_part_bullets_msg(self) -> list:
        """返回部分bullets的消息，每次轮转"""
        bullets_msg = []
        l = len(self.gm.bullets)
        if self.send_bullets_beg >= l:
            self.send_bullets_beg = 0
        end = self.send_bullets_beg + self.send_bullets_num
        if end >= l:
            end = l - 1
        for bullet in self.gm.bullets.sprites()[self.send_bullets_beg:end]:
            bullets_msg.append(bullet.make_msg())
        self.send_bullets_beg = end + 1
        return bullets_msg

    def load_ctrl_msg(self, player_name, ctrl_msg):
        """加载操作信息"""
        ship = gf.find_player_ship(self.gm.ships, player_name)
        if ship is not None:
            ship.load_ctrl_msg(ctrl_msg)

    def send_check_clock_msg(self, player_name, addr):
        """对玩家发送校时消息"""
        self.addresses[player_name] = addr

        msg = {
            'opt': OptType.CheckClock,
            'time': gf.get_time(),
            'args': [self.room_id, player_name],
            'kwargs': {}
        }
        self.net.send(self.addresses[player_name], msg)

    def check_events(self):
        """服务器不需要处理消息"""
        # TODO：调试完成后把此函数pass
        return
        self.mouse_loc.update(pygame.mouse.get_pos())
        self.mouse_d_loc.update(pygame.mouse.get_rel())
        self.camera.mouse_loc.update(self.mouse_loc)

        event = pygame.event.poll()
        while event:
            if event.type == pygame.QUIT:
                self.is_run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 2:  # 是否按下鼠标中键
                    self.camera.change_mode()
            elif event.type == pygame.MOUSEMOTION:
                mouse_keys = pygame.mouse.get_pressed()
                if mouse_keys[2]:  # 如果鼠标右键被按下
                    self.camera.d_loc.update(self.mouse_d_loc)
            elif event.type == pygame.MOUSEWHEEL:
                self.camera.d_zoom = event.y

            event = pygame.event.poll()

    def display(self):
        """更新屏幕"""
        return
        # TODO：调试完成后本函数删除
        surplus_ratio = self.surplus_dt / self.physics_dt
        gf.update_screen(self.settings, self.gm, self.camera, [], surplus_ratio)

    def check_collisions(self):
        """检查碰撞"""
        self.gm.check_ships_ships_collisions()
        self.gm.check_ships_planets_collisions()
        bulletss = self.gm.check_ships_bullets_collisions().values()
        bullets = self.gm.check_bullets_planets_collisions().keys()

        for bullet in bullets:
            self.dead_bullets_id.add(bullet.id)
        for bullets in bulletss:
            for bullet in bullets:
                self.dead_bullets_id.add(bullet.id)

    def bullets_disappear(self) -> list:
        del_ids = super().bullets_disappear()
        for del_id in del_ids:
            self.dead_bullets_id.add(del_id)
        return del_ids

    def ships_fire_bullet(self):
        """飞船发射子弹"""
        for bullet in self.gm.ships_fire_bullet():
            self.new_bullets[bullet.id] = bullet

    def make_new_bullets_msg(self) -> list:
        """生成new_bullets消息"""
        for new_id in self.new_bullets.keys():
            if new_id in self.dead_bullets_id:
                del self.new_bullets[new_id]
                self.dead_bullets_id.remove(new_id)
        msg = []
        for bullet in self.new_bullets.values():
            msg.append(bullet.make_msg())
        self.new_bullets.clear()
        return msg

    def make_dead_bullets_msg(self) -> list:
        msg = []
        for bullet_id in self.dead_bullets_id:
            msg.append(bullet_id)
        self.dead_bullets_id.clear()
        return msg

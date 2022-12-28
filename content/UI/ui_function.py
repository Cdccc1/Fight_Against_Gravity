import pygame
from pygame import Rect
from content.maps.map_obj import Map
from content.UI.button_class import Button
from content.UI.inputbox_class import InputBox
from content.UI.panel_class import Panel
from content.UI.scrollable_panel_class import ScrollablePanel
from content.UI.label_class import Label
from content.scene.scene_font import SceneFont


class UIFunction:
    @staticmethod
    def new_start_logo(scene):
        """开始界面的logo"""
        start_title = pygame.image.load(scene.path + "assets\\texture\\FAGWhite.png")  # 用作画图
        start_title = pygame.transform.smoothscale(start_title, (514, 200))
        start_title = start_title.convert_alpha()
        return start_title

    @staticmethod
    def new_online_button(scene):
        """开始界面的在线游戏按钮"""
        start_font = SceneFont.start_font
        start_rect = Rect(0.4*scene.width, 0.275*scene.height, 290, 80)
        online_game_button = Button("onlinegame", scene.online_is_clicked, start_rect,
                                    scene.path + "assets\\Img\\start_unpressed.png", 1, '在线游戏', start_font)  # 用作画图
        online_game_button.add_img(scene.path + "assets\\Img\\start_press.png")
        return online_game_button

    @staticmethod
    def new_login_button(scene):
        """开始界面的登录按钮"""
        login_rect = Rect(0.933*scene.width, 0.025*scene.height, 60, 40)
        login_button = Button("login", scene.login_is_clicked, login_rect,
                              scene.settings.btbg_light, 0, '登录', SceneFont.log_font)
        login_button.add_img(scene.settings.btbg_light_pressed)
        return login_button

    @staticmethod
    def new_local_button(scene):
        """开始界面的本地登录按钮"""
        local_rect = Rect(0.4*scene.width, 0.4375*scene.height, 290, 80)
        local_button = Button('local game', scene.local_is_clicked, local_rect,
                              scene.path + "assets\\Img\\start_unpressed.png", 0, '本地游戏', SceneFont.start_font)
        local_button.add_img(scene.path + "assets\\Img\\start_press.png")
        return local_button

    @staticmethod
    def new_exit_button(scene):
        exit_rect = Rect(0.4*scene.width, 0.7625*scene.height, 290, 80)
        exit_button = Button('exit', scene.exit_is_clicked, exit_rect, scene.path + "assets\\Img\\start_unpressed.png",
                                 0, '退出游戏', SceneFont.start_font)
        exit_button.add_img(scene.path + "assets\\Img\\start_press.png")
        return exit_button
    @staticmethod
    def new_reg_labels(scene):
        """注册界面四个输入框之前的文本提示"""
        r_email_label = Label(scene.width*0.28, 0.225*scene.height, 98, "请输入您的邮箱", SceneFont.white_font)
        r_id_label = Label(scene.width*0.28, 0.325*scene.height, 106, "请输入您的用户名", SceneFont.white_font)
        r_password_label = Label(scene.width*0.28, 0.425*scene.height, 42, "设置您的密码", SceneFont.white_font)
        r_check_label = Label(scene.width*0.28, 0.525*scene.height, 40, "验证码", SceneFont.white_font)
        labels = [r_email_label, r_id_label, r_password_label, r_check_label]
        return labels

    @staticmethod
    def new_reg_boxes(scene):
        """注册界面的四个输入框，分别是邮箱、用户名、密码、验证码"""
        r_email_box = InputBox(Rect(0.42*scene.width, 0.225*scene.height, 0.292*scene.width, 0.04375*scene.height))
        r_id_box = InputBox(Rect(0.42*scene.width, 0.325*scene.height, 0.292*scene.width, 0.04375*scene.height))
        r_password_box = InputBox(Rect(0.42*scene.width, 0.425*scene.height, 0.292*scene.width, 0.04375*scene.height))
        r_check_box = InputBox(Rect(0.42*scene.width, 0.525*scene.height, 0.292*scene.width, 0.04375*scene.height))
        boxes = [r_email_box, r_id_box, r_password_box, r_check_box]
        return boxes

    @staticmethod
    def new_register_buttons(scene):
        """注册界面的 确认注册 和 发送验证码 按钮"""
        r_rect = Rect(0.542*scene.width, 0.625*scene.height, 0.0833*scene.width, 0.05*scene.height)
        r_button = Button("r", scene.confirm_reg_clicked, r_rect,
                          scene.settings.btbg_light, 0, '确认注册', SceneFont.log_font)
        r_button.add_img(scene.settings.btbg_light_pressed)
        check_rect = Rect(0.3583*scene.width, 0.625*scene.height, 0.09167*scene.width, 0.05*scene.height)
        r_check_button = Button('check', scene.send_checkcode_clicked, check_rect,
                                scene.settings.btbg_light, 0, '发送验证码', SceneFont.log_font)
        r_check_button.add_img(scene.settings.btbg_light_pressed)
        buttons = [r_button, r_check_button, scene.back]  # 包含了返回
        return buttons

    @staticmethod
    def new_select_map_button(scene, name):
        path = scene.path + "assets\\texture\\thumbnail\\" + name + ".png"
        temp_rect = Rect(0, 0, 250, 250)
        select_map_button = Button(name, lambda: scene.select_map_button_clicked(name),
                                   temp_rect, path, 1, name, SceneFont.map_list_font)
        return select_map_button

    @staticmethod
    def new_select_map_panel(scene):  # 770 x 550
        buttons = []
        for name in Map.maps_info.keys():
            buttons.append(UIFunction.new_select_map_button(scene, name))
        buttons[0].r_xy = 0.007, 0.133
        buttons[1].r_xy = 0.338, 0.133
        buttons[2].r_xy = 0.669, 0.133
        buttons[3].r_xy = 0.007, 0.565
        buttons[4].r_xy = 0.338, 0.565
        buttons[5].r_xy = 0.669, 0.565

        close_rect = Rect(0, 0, 20, 20)
        close_button = Button('close', scene.close_is_clicked, close_rect,
                                   scene.path + 'assets\\Img\\close_unclicked.png', 0)
        close_button.r_xy = 0.968, 0.020
        close_button.add_img(scene.path + 'assets\\Img\\close_clicked.png')

        buttons.append(close_button)

        map_rect = Rect(0, 0, 770, 590)
        map_rect.center = scene.screen.get_rect().center
        map_panel = Panel(map_rect, "地图选择", 28, buttons, text_pos=0)
        return map_panel

    @staticmethod
    def new_all_room_list_panel(scene) -> Panel:
        """服务器大厅使用的房间列表panel"""
        screen_rect = scene.screen.get_rect()

        rooms_name_label = Label(0, 0, 100, '房间名')
        rooms_name_label.r_xy = (0.01, 0.01)
        rooms_owner_label = Label(0, 0, 100, '房主')
        rooms_owner_label.r_xy = (0.21, 0.01)
        rooms_map_label = Label(0, 0, 100, '地图')
        rooms_map_label.r_xy = (0.41, 0.01)
        rooms_player_num_label = Label(0, 0, 100, '玩家数量')
        rooms_player_num_label.r_xy = (0.61, 0.01)
        rooms_is_play_label = Label(0, 0, 100, '是否游戏中')
        rooms_is_play_label.r_xy = (0.81, 0.01)
        others = [rooms_name_label, rooms_owner_label, rooms_map_label, rooms_player_num_label, rooms_is_play_label]
        ctrlrs = [UIFunction.new_room_list_panel(scene, [], '')]
        all_room_list_panel_rect = Rect(5, 80, screen_rect.width-10, screen_rect.height-85)
        all_room_list_panel = Panel(all_room_list_panel_rect, '', 10, ctrlrs=ctrlrs, others=others, border_radius=10)
        return all_room_list_panel

    @staticmethod
    def new_room_list_panel(scene, room_list, key: str) -> ScrollablePanel:
        """
        返回只显示房间的可滚动panel
        room_list：由一个个字典组成的列表，为接收到的房间消息，具体见OptType
        key：搜索栏的关键字，用于筛选
        """
        screen_rect = scene.screen.get_rect()
        r_y = 0
        ry = 0.06
        room_list_panel_rect = Rect(0, 0, screen_rect.width-10, (1-ry)*(screen_rect.height-85)-10)
        ctrlrs = []
        for room in room_list:

            if key in room['roomname']:
                room_bar_panel = UIFunction.new_room_bar_panel(scene, room['roomid'],
                    room['roomname'], room['owner'], room['roommap'], room['size'], room['started'])
                room_bar_panel.r_xy = (0, r_y)
                r_y += (5+room_bar_panel.rect.height)/room_list_panel_rect.height
                ctrlrs.append(room_bar_panel)

        room_list_panel = ScrollablePanel(scene.settings, room_list_panel_rect, '', 10, ctrlrs=ctrlrs)
        room_list_panel.color = (20, 20, 20)
        room_list_panel.r_xy = (0, ry)
        return room_list_panel

    @staticmethod
    def new_room_bar_panel(scene, room_id: str, name: str, owner: str,
                           map_name: str, player_num: int, is_play: bool) -> Panel:
        """
        scene：场景
        name：房间名
        owner：房主名
        map_name：地图名
        player_num：玩家数量
        is_play：是否游戏中
        """
        screen_width = scene.screen.get_width()
        width = screen_width - 25
        max_num = len(Map(map_name).ships_info)
        name_label = Label(0, 0, 100, name)
        name_label.r_xy = 0.01*(screen_width-10)/width, 0
        owner_label = Label(0, 0, 100, owner)
        owner_label.r_xy = 0.21*(screen_width-10)/width, 0
        map_label = Label(0, 0, 100, map_name)
        map_label.r_xy = 0.41*(screen_width-10)/width, 0
        player_num_label = Label(0, 0, 100, str(player_num)+'/'+str(max_num))
        player_num_label.r_xy = 0.61*(screen_width-10)/width, 0
        if is_play == 'YES':
            is_play = '游戏中'
        else:
            is_play = '房间中'
        is_play_label = Label(0, 0, 100, is_play)
        is_play_label.r_xy = 0.81*(screen_width-10)/width, 0
        others = [name_label, owner_label, map_label, player_num_label, is_play_label]

        height = name_label.rect.height
        room_bar_rect = Rect(0, 0, width, height)
        room_bar_button = Button('join_room', lambda: scene.room_bar_clicked(room_id), room_bar_rect.copy(),
                                 scene.path+'assets/texture/void.png', 0)
        room_bar_button.add_img(scene.path+'assets/texture/translucent20.png')
        room_bar_panel = Panel(room_bar_rect, '', 10, ctrlrs=[room_bar_button], others=others, border_radius=0)
        room_bar_panel.color = (60, 60, 60)
        return room_bar_panel

    @staticmethod
    def new_join_fail_panel(scene):
        """room_list_scene中的加入房间失败提示panel"""
        confirm_button_rect = Rect(0, 0, 100, 50)
        confirm_button = Button('确定', scene.join_fail_panel_button_clicked, confirm_button_rect,
                                scene.settings.btbg_light, 0, '确定', SceneFont.log_font)
        confirm_button.add_img(scene.settings.btbg_light_pressed)
        confirm_button.r_xy = (0.375, 0.7)
        hint_label = Label(0, 0, 400, '加入失败！请刷新房间列表！', SceneFont.map_list_font)
        hint_label.r_xy = (0, 0.2)
        join_fail_panel_rect = Rect(0, 0, 400, 200)
        join_fail_panel_rect.center = scene.screen.get_rect().center
        join_fail_panel = Panel(join_fail_panel_rect, '', 23, ctrlrs=[confirm_button], others=[hint_label])
        join_fail_panel.color = (80, 80, 80)
        join_fail_panel.is_show = join_fail_panel.is_able = False
        return join_fail_panel

    @staticmethod
    def new_change_room_name_panel(scene):
        """RoomScene中点击更改房间名按钮呼出的panel"""
        confirm_button_rect = Rect(0, 0, 100, 50)
        confirm_button = Button('确定', scene.change_room_name_confirm_button_clicked, confirm_button_rect,
                                scene.settings.btbg_light, 0, '确定', SceneFont.log_font)
        confirm_button.add_img(scene.settings.btbg_light_pressed)
        confirm_button.r_xy = (0.125, 0.7)
        cancel_button_rect = Rect(0, 0, 100, 50)
        cancel_button = Button('取消', scene.change_room_name_cancel_button_clicked, cancel_button_rect,
                               scene.settings.btbg_light, 0, '取消', SceneFont.log_font)
        cancel_button.add_img(scene.settings.btbg_light_pressed)
        cancel_button.r_xy = (0.625, 0.7)
        hint_label = Label(0, 0, 400, '请输入新的房间名:', SceneFont.map_list_font)
        hint_label.r_xy = (0, 0.1)
        box_rect = Rect(0, 0, 200, 35)
        box = InputBox(box_rect)
        box.r_xy = (0.25, 0.3)
        change_room_name_panel_rect = Rect(0, 0, 400, 250)
        change_room_name_panel_rect.center = scene.screen.get_rect().center
        change_room_name_panel = Panel(change_room_name_panel_rect, '', 23, ctrlrs=[confirm_button, cancel_button], boxes=[box], others=[hint_label])
        change_room_name_panel.color = (80, 80, 80)
        change_room_name_panel.is_show = change_room_name_panel.is_able = False
        return change_room_name_panel

    @staticmethod
    def new_pause_panel(scene) -> Panel:
        """用于游戏场景的暂停panel"""
        button_rect = Rect(0, 0, 0.25*scene.width, 0.08125*scene.height)
        continue_button = Button('继续游戏', scene.continue_button_clicked, button_rect.copy(),
                                 scene.settings.btbg_light, 0, '继续游戏', SceneFont.log_font)
        continue_button.add_img(scene.settings.btbg_light_pressed)
        continue_button.r_xy = 0.25, 0.15
        settings_button = Button('设置', scene.settings_button_clicked, button_rect.copy(),
                                 scene.settings.btbg_light, 0, '设置', SceneFont.log_font)
        settings_button.add_img(scene.settings.btbg_light_pressed)
        settings_button.r_xy = 0.25, 0.4
        quit_button = Button('退出对局', scene.quit_button_clicked, button_rect.copy(),
                             scene.settings.btbg_light, 0, '退出对局', SceneFont.log_font)
        quit_button.add_img(scene.settings.btbg_light_pressed)
        quit_button.r_xy = 0.25, 0.65

        pause_panel_rect = Rect(0.25*scene.width, 0.22*scene.height, 0.5*scene.width, 0.625*scene.height)
        pause_panel = Panel(pause_panel_rect, '已暂停', 23,
                            ctrlrs=[continue_button, settings_button, quit_button], text_pos=0)
        return pause_panel

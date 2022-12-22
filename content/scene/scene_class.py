import pygame
import sys
from content.UI.button_class import Button
from content.UI.inputbox_class import InputBox
from content.scene.scene_player_class import ScenePlayer
from content.scene.scene_font import SceneFont
from content.UI.panel_class import Panel


class Scene:
    screen = None
    settings = None
    client = None
    path = None

    def __init__(self):
        self.loaded = {'img': [], 'label': [], 'box': [], 'button': [], 'panel': []}
        """全局组件，返回按钮、设置按钮、关闭按钮"""
        back_rect = pygame.Rect(20, 20, 45, 45)
        self.back = Button("back", self.back_is_clicked, back_rect, self.path + "assets\\Img\\back.png", 1)
        self.reminder_panel_rect = (200, 300, 800, 200)
        self.reminder_panel_rect_small = (450, 300, 300, 100)
        self.menu_like_panel_rect = (300, 200, 600, 400)
        set_rect = pygame.Rect(1120, 745, 35, 35)
        self.set_button = Button('setting', self.set_is_clicked, set_rect, self.path + "assets/Img/setting_light.png",
                                 1)
        self.set_button.add_img(self.path + "assets/Img/setting_light_pressed.png")
        self.switcher = 0
        self.box_is_able = True
        close_rect = pygame.Rect(0, 0, 20, 20)
        self.close_button = Button('close', self.close_is_clicked, close_rect,
                                   self.path + 'assets\\Img\\close_unclicked.png', 0)
        self.close_button.add_img(self.path + 'assets\\Img\\close_clicked.png')
        """用于判断按下回车键时是否相应，如果是登录界面，敲下回车应该等同于登录，如果注册界面，敲下回车等同于进行注册"""
        self.id = 0  # 0对应登录，1对应注册，2对应设置改键，3对应无响应。
        # 设置界面

        # 确认修改键位P1
        set_boxes = []

        for i in range(10):
            set_boxes.append(InputBox(pygame.Rect(0, 0, 80, 35)))
        set_key_confirm_rect = pygame.Rect(450, 200, 150, 50)
        r_pos = {"button": [[0.95, 0.03], [0.25, 0.4]],
                 "box": [[i / 5 - 0.15, j / 10] for i in range(1, 6) for j in range(1, 3)]}
        set_key_confirm_button = Button('确认修改', self.set_key_clicked, set_key_confirm_rect,
                                        self.settings.btbg_light, 0, "确认修改", SceneFont.log_font)
        self.set_panel = Panel((200, 50, 800, 700), '设置', 25, [self.close_button, set_key_confirm_button], set_boxes,
                               r_pos, text_pos=0, has_scrollbar=True)

    def ban_inputbox(self):
        self.box_is_able = False

    def deal_event(self, e):
        """将对应页面加载了的组件全部进行状态更新，会post新的event"""
        if self.loaded['panel'] is not None:
            for pn in self.loaded['panel']:
                pn.update(e)
        if self.loaded['button'] is not None:
            for bt in self.loaded['button']:
                bt.update(e)
        if self.loaded['box'] is not None and self.box_is_able:
            if e.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(self.loaded['box'])):
                    if self.loaded['box'][i].boxBody.collidepoint(e.pos):  # 若按下鼠标且位置在文本框
                        self.loaded['box'][i].switch()
                        self.switcher = i
                    else:
                        self.loaded['box'][i].active = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_TAB:
                    for m in self.loaded['box']:
                        m.active = False
                    self.switcher = (self.switcher + 1) % len(self.loaded['box'])
                    self.loaded['box'][self.switcher].active = True
            for bx in self.loaded['box']:
                bx.deal_event(e)

    def deal_events(self):
        """获取并处理所有消息"""
        for event in pygame.event.get():
            ScenePlayer.STACK[-1].deal_event(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.deal_events()

    def draw_elements(self):
        if self.loaded['button'] is not None:
            for bt in self.loaded['button']:
                bt.render(self.screen)
        if self.loaded['label'] is not None:
            for lb in self.loaded['label']:
                lb.render(self.screen)
        if self.loaded['box'] is not None:
            for bx in self.loaded['box']:
                bx.render(self.screen)
        if self.loaded['panel'] is not None:
            for pn in self.loaded['panel']:
                pn.render(self.screen)

    def back_is_clicked(self):
        ScenePlayer.pop()

    def set_is_clicked(self):
        self.loaded['panel'] = [self.set_panel]

    def set_key_clicked(self):
        pass

    def close_is_clicked(self):
        self.loaded['panel'] = []

    def show(self):
        pass

    @staticmethod
    def init(settings, screen, client):
        Scene.settings = settings
        Scene.path = settings.path
        Scene.screen = screen
        Scene.client = client
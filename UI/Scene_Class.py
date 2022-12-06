import pygame
import os
import sys
from Button_Class import Button
from Label_Class import Label
from InputBox_Class import InputBox

class Scene:
    pygame.init()
    UI_current_directory = os.getcwd()  # UI文件夹路径
    fag_directory = os.path.dirname(UI_current_directory)  # FAG文件夹路径
    font_path_light = "UI/Font/SourceHanSans-Light.ttc"
    font_path_normal = "UI/Font/SourceHanSans-Normal.ttc"
    btbg_light = "UI/Img/light_butbg_unpressed.png"  # 按钮浅灰底，未按版
    btbg_light_pressed = "UI/Img/light_butbg.png"  # 鼠标移动反响
    os.chdir(fag_directory)
    log_font = {
        'font': pygame.font.Font(font_path_normal, 22),
        'tc': (36, 41, 47),
        'bc': None,
        'align': 1,
        'valign': 1
    }  # 黑字用于白底
    r_font = {
        'font': pygame.font.Font(font_path_normal, 16),
        'tc': (169, 183, 198),
        'bc': None,
        'align': 0,
        'valign': 0
    }  # 白字用于黑底
    menu_font = {
        'font': pygame.font.Font(font_path_normal, 60),
        'tc': (36, 41, 47),
        'bc': None,
        'align': 1,
        'valign': 1
    }

    """事件"""
    switcher = 0
    START = pygame.USEREVENT + 1
    BACK = pygame.USEREVENT + 2
    REGISTER = pygame.USEREVENT + 3
    SENDREGISTER = pygame.USEREVENT + 4
    LOGIN = pygame.USEREVENT + 5
    SENDCHECK = pygame.USEREVENT + 6
    LOCAL = pygame.USEREVENT + 7
    ONLINE = pygame.USEREVENT + 8
    SETTING = pygame.USEREVENT + 9

    # """全局组件，返回按钮和设置按钮"""
    # back_rect = pygame.Rect(20, 20, 45, 45)
    # back = Button("back", BACK, back_rect, "UI/Img/back.png", 1)
    #
    # set_rect = pygame.Rect(1050, 700, 60, 60)
    # set_button = Button('setting', SETTING, set_rect, "UI/Img/setting_light.png", 1)
    # set_button.add_img("UI/Img/setting_light_pressed.png")



    def __init__(self):
        self.loaded = {'img': None, 'label': None, 'box': None, 'button': None}

    def update_event(self, e):
        """将对应页面加载了的组件全部进行状态更新，会post新的event"""
        if self.loaded['button'] is not None:
            for bt in self.loaded['button']:
                bt.update(e)
        if self.loaded['box'] is not None:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_TAB:
                    self.loaded['box'][self.switcher].active = False
                    self.switcher = (self.switcher + 1) % len(self.loaded['box'])
                    self.loaded['box'][self.switcher].active = True
            for bx in self.loaded['box']:
                bx.deal_event(e)

    def draw_elements(self, surface):
        if self.loaded['button'] is not None:
            for bt in self.loaded['button']:
                bt.render(surface)
        if self.loaded['label'] is not None:
            for lb in self.loaded['label']:
                lb.render(surface)
        if self.loaded['box'] is not None:
            for bx in self.loaded['box']:
                bx.draw(surface)



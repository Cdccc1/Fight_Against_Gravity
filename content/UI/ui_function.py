from content.UI.button_class import Button
from content.UI.inputbox_class import InputBox
from content.UI.scrollbar import ScrollBar
from content.UI.panel_class import Panel
from content.UI.label_class import Label
from settings.all_settings import Settings
from content.scene.scene_font import SceneFont
import pygame


class UIFunction:
    @staticmethod
    def new_start_logo(scene):
        start_title = pygame.image.load(scene.path + "assets\\texture\\FAGWhite.png")  # 用作画图
        start_title = pygame.transform.smoothscale(start_title, (514, 200))
        start_title = start_title.convert_alpha()
        return start_title

    @staticmethod
    def new_online_button(scene):
        start_font = SceneFont.start_font
        start_rect = pygame.Rect(455, 280, 290, 100)
        online_game_button = Button("onlinegame", scene.online_is_clicked, start_rect,
                                    scene.path + "assets\\Img\\start_unpressed.png", 1, '在线游戏', start_font)  # 用作画图
        online_game_button.add_img(scene.path + "assets\\Img\\start_press.png")
        return online_game_button

    @staticmethod
    def new_login_button(scene):
        login_rect = pygame.Rect(1120, 20, 60, 40)
        login_button = Button("login", scene.login_is_clicked, login_rect,
                              scene.settings.btbg_light, 0, '登录', SceneFont.log_font)
        login_button.add_img(scene.settings.btbg_light_pressed)
        return login_button

    @staticmethod
    def new_local_button(scene):
        local_rect = pygame.Rect(455, 450, 290, 100)
        local_button = Button('local game', scene.local_is_clicked, local_rect,
                              scene.path + "assets\\Img\\start_unpressed.png", 0, '本地游戏', SceneFont.start_font)
        local_button.add_img(scene.path + "assets\\Img\\start_press.png")
        return local_button
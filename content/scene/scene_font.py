import pygame


class SceneFont:

    log_font = {}
    white_font = {}
    menu_font = {}
    start_font = {}
    map_list_font = {}
    nickname_font = {}
    hp_value_font = {}

    @staticmethod
    def init(scene_settings):
        """类变量初始化"""
        SceneFont.start_font = {
            'font': pygame.font.Font(scene_settings.font_path_light, 65),
            'tc': (36, 41, 47),
            'bc': None,
            'align': 1,
            'valign': 1
        }
        SceneFont.log_font = {
            'font': pygame.font.Font(scene_settings.font_path_normal, 22),
            'tc': (36, 41, 47),
            'bc': None,
            'align': 1,
            'valign': 1
        }  # 黑字用于白底
        SceneFont.white_font = {
            'font': pygame.font.Font(scene_settings.font_path_normal, 16),
            'tc': (169, 183, 198),
            'bc': None,
            'align': 0,
            'valign': 0
        }  # 白字用于黑底
        SceneFont.menu_font = {
            'font': pygame.font.Font(scene_settings.font_path_normal, 58),
            'tc': (36, 41, 47),
            'bc': None,
            'align': 1,
            'valign': 1
        }
        SceneFont.map_list_font = {
            'font': pygame.font.Font(scene_settings.font_path_normal, 25),
            'tc': (255, 255, 255),
            'bc': None,
            'align': 1,
            'valign': 1
        }
        SceneFont.nickname_font = {
            'font': pygame.font.Font(scene_settings.font_path_normal, 11),
            'tc': (255, 255, 255),
            'bc': None,
            'align': 0,
            'valign': 1
        }
        SceneFont.hp_value_font = {
            'font': pygame.font.Font(scene_settings.font_path_normal, 9),
            'tc': (255, 255, 255),
            'bc': None,
            'align': 1,
            'valign': 1
        }

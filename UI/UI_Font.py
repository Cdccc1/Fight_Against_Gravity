import pygame


class UIFont:

    log_font = {}
    r_font = {}
    menu_font = {}
    start_font = {}

    @staticmethod
    def init(scene_settings):
        """类变量初始化"""
        UIFont.start_font = {
            'font': pygame.font.Font(scene_settings.font_path_light, 65),
            'tc': (36, 41, 47),
            'bc': None,
            'align': 1,
            'valign': 1
        }
        UIFont.log_font = {
            'font': pygame.font.Font(scene_settings.font_path_normal, 22),
            'tc': (36, 41, 47),
            'bc': None,
            'align': 1,
            'valign': 1
        }  # 黑字用于白底
        UIFont.r_font = {
            'font': pygame.font.Font(scene_settings.font_path_normal, 16),
            'tc': (169, 183, 198),
            'bc': None,
            'align': 0,
            'valign': 0
        }  # 白字用于黑底
        UIFont.menu_font = {
            'font': pygame.font.Font(scene_settings.font_path_normal, 60),
            'tc': (36, 41, 47),
            'bc': None,
            'align': 1,
            'valign': 1
        }


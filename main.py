"""程序入口"""
import sys
import os
from Server import client_main
from settings.all_settings import Settings
import pygame
from content.scene.start_scene_class import StartScene
from content.scene.scene_settings import SceneSetting
from content.scene.scene_player_class import ScenePlayer
if hasattr(sys, 'frozen'):
    path = os.path.dirname(sys.executable) + '/'
else:
    path = os.path.dirname(os.path.realpath(__file__)) + '/'

sys.path.append(path)
"""
游戏操作：
wasd：玩家1的移动
e：玩家1的发射子弹
ijkl：玩家2的移动
u：玩家2的发射子弹u

按住鼠标右键并拖动：移动视角（视角自由移动模式下可用）
鼠标中键：切换视角模式（自由移动模式or跟随飞船模式）
鼠标滚轮：视角缩放
"""
pygame.init()
settings = Settings(path)  # 初始化设置类
_debug_ = "--debug" in sys.argv
s = client_main.ClientMain(path, _debug_=_debug_)
print(os.getcwd())
sc = pygame.display.set_mode((1200, 800))
scene_setting = SceneSetting()
begin = StartScene(scene_setting, s)
sp = ScenePlayer(sc, scene_setting)
ScenePlayer.push(begin)
sp.show_scene()
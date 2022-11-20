"""
使用for循环嵌套语句结合鼠标点击绘制随机彩色同心圆平铺画面
"""
import pgzrun
import random
WIDTH = 1200
HEIGHT = 800
R = 100


def draw():
    screen.fill('white')
    for y in range(R, HEIGHT, 2 * R):
        for x in range(R, WIDTH, 2 * R):
            for r in range(1, R, 10):  # 绘制每一个同心圆的个数
                screen.draw.filled_circle((x, y), R-r,
                                          (random.randint(0, 255),
                                           random.randint(0, 255),
                                           random.randint(0, 255)))


# 鼠标点击动作，重新绘制随机彩色圆圈
def on_mouse_down():
    draw()  # 点击鼠标之后，重新绘制彩色圆圈

pgzrun.go()

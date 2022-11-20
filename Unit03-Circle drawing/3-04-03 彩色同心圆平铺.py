"""
使用for循环嵌套语句绘制彩色同心圆平铺画面
"""
import pgzrun
import random
R = 100
random.randint(0,255)
def draw():
    screen.fill('white')
    for y in range(R, 600, 2 * R):
        for x in range(R, 800, 2 * R):
            for r in range(R,0,-10):
                screen.draw.filled_circle((x, y), r,\
                (random.randint(0, 255), \
                random.randint(0, 255), \
                random.randint(0, 255)))


pgzrun.go()

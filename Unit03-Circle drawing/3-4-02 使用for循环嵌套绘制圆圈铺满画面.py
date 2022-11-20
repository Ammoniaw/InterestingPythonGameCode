"""
使用for循环嵌套语句铺满画面
"""
import pgzrun
R = 50


def draw():
    screen.fill('white')
    for y in range(R, 600, 2 * R):
        for x in range(R, 800, 2 * R):
            screen.draw.filled_circle((x, y), R, 'blue')


pgzrun.go()

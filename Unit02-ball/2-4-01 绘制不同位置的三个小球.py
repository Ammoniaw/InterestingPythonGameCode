import pgzrun


def draw():
    # 修改背景颜色
    screen.fill('white')
    # 绘制三个不同位置的小球
    screen.draw.filled_circle((150, 300),100,'red')
    screen.draw.filled_circle((400, 300), 100, 'yellow')
    screen.draw.filled_circle((650, 300), 100, 'blue')


pgzrun.go()

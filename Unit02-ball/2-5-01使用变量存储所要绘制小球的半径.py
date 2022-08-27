import pgzrun


def draw():
    # 修改背景颜色
    screen.fill('white')

    # 使用变量存储所绘制小球的半径
    r = 100

    # 绘制三个不同位置的小球
    screen.draw.filled_circle((150, 300), r,'red')
    screen.draw.filled_circle((400, 300), r, 'yellow')
    screen.draw.filled_circle((650, 300), r, 'blue')


pgzrun.go()

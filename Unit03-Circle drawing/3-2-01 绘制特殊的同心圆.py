# 绘制特殊的同心圆
import pgzrun


def draw():
    # 绘制背景
    screen.fill('white')
    for r in range(100,1,-20):  # 指定range函数的步长
        screen.draw.filled_circle((400, 300), r , 'black')
        screen.draw.filled_circle((400, 300), r-5 , 'white')


# 开始绘制
pgzrun.go()

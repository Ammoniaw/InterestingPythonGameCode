# 绘制多层同心圆
import pgzrun 
def draw():
    # 绘制背景
    screen.fill('white')
    for r in range(10,51,10):  # 指定range函数的步长
        screen.draw.circle((400,400), r,'black')

# 开始绘制
pgzrun.go()
# 使用rgb颜色分量绘制同心圆
import pgzrun


def draw():
    # 绘制背景
    HEIGHTH = 1000
    WIDTH = 1200
    screen.fill((255, 255, 255))  # 白色背景
    # # 绘制外黑内红的渐变圆
    # for r in range(0, 256, 1):
    #     screen.draw.filled_circle((400,300), 255-r,(r,0,0))
    # # 绘制外黑内黄的渐变圆
    # for r in range(0, 256, 1):
    #     screen.draw.filled_circle((400, 300), 255-r, (r, r, 0))
    # 绘制外灰内黑的渐变圆
    for r in range(150, 0, -1):
        screen.draw.filled_circle((400, 300), r, (r, r, r))


# 开始绘制
pgzrun.go()

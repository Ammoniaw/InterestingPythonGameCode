# 使用rgb颜色分量绘制同心圆
import pgzrun


def draw():
    # 绘制背景
    screen.fill((255, 255, 255))
    for r in range(250, 50, -50):
        screen.draw.filled_circle((400, 300), r, (r, 0, 0))


# 开始绘制
pgzrun.go()

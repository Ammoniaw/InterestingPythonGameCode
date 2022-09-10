# 使用rgb颜色分量绘制同心圆
import pgzrun


def draw():
    # 绘制背景
    screen.fill((255,255,255))
    for r in range(1, 251, 50):
        screen.draw.circle((400, 300), r, (255, 0, 0))


# 开始绘制
pgzrun.go()

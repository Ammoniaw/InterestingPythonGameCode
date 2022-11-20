# 使用rgb颜色分量绘制同心圆
import pgzrun
import random # 导入random库

# 随机颜色分量-取[0-255]之间的随机整数
R = random.randint(0, 255)
G = random.randint(0, 255)
B = random.randint(0, 255)



def draw():
    # 绘制背景
    screen.fill((255,255,255))  # 白色背景
    for r in range(250, 0, -20):
        screen.draw.filled_circle((400, 300), r, (R, G, B))


# 开始绘制
pgzrun.go()

import pgzrun

# 绘制窗口的代销
HEIGHT = 600
WIDTH = 800

# 设定小球的初始Y坐标
y = 100

# 设定小球下降和上升的速度
speed_y = 3

# 小球的半径r
r = 30
def draw():
    # 修改背景颜色
    screen.fill('white')

    screen.draw.filled_circle((WIDTH / 2, y), r, 'blue')

# 添加更新代码
def update():
    global y, speed_y # 使用global语句对变量y,speed_y进行全局修改
    y += speed_y
    if y >= HEIGHT - r or y <= r : # 小球碰触到最底部时或者碰触到最顶部时
        speed_y = -speed_y


pgzrun.go()

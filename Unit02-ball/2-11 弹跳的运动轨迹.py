import pgzrun

# 绘制窗口的代销
HEIGHT = 600
WIDTH = 800

# 设定小球的初始X Y坐标
x = 100
y = 100

# 设定小球下降和上升的速度
speed_y = 6
speed_x = 5

# 小球的半径r
r = 5  # 缩小小球的半径


def draw():
    # 不绘制背景
    # screen.fill('white')

    screen.draw.filled_circle((x, y), r, 'blue')

# 添加更新代码


def update():
    global y, speed_y, x, speed_x  # 使用global语句对变量y,speed_y进行全局修改
    y += speed_y
    x += speed_x
    if y >= HEIGHT - r or y <= r:  # 小球碰触到最底部时或者碰触到最顶部时
        speed_y = -speed_y
    if x >= WIDTH - r or x <= r:  # 小球碰到左右边界时回弹
        speed_x = -speed_x


pgzrun.go()

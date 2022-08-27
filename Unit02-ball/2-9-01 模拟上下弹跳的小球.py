import pgzrun

# 设定小球的初始Y坐标
y = 100

# 设定小球下降和上升的速度
speed_y = 3
def draw():
    # 修改背景颜色
    screen.fill('white')

    screen.draw.filled_circle((400, y), 30, 'blue')

# 添加更新代码
def update():
    global y, speed_y # 使用global语句对变量y,speed_y进行全局修改
    y += speed_y
    if y >= 570 or y <= 30 : # 小球碰触到最底部时或者碰触到最顶部时
        speed_y = -speed_y


pgzrun.go()

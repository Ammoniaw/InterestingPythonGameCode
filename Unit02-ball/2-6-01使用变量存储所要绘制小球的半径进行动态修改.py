import pgzrun

# 使用变量存储所绘制小球的半径
r = 100

def draw():
    # 修改背景颜色
    screen.fill('white')

    screen.draw.filled_circle((400, 300), r, 'blue')

# 添加更新代码
def update():
    global r  # 使用global语句对变量r进行全局修改
    r += 1


pgzrun.go()

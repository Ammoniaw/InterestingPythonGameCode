import pgzrun

# 设定小球的初始Y坐标
y = 100
def draw():
    # 修改背景颜色
    screen.fill('white')

    screen.draw.filled_circle((400, y), 30, 'blue')

# 添加更新代码
def update():
    global y # 使用global语句对变量y进行全局修改
    y += 1
    if y >= 630: # 下落到最底部小时
        y = -30  # 回到最顶部


pgzrun.go()

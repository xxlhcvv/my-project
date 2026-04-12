import turtle

# ====================== 配置参数（强制铺满窗口） ======================
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BOARD_SIZE = 15
# 计算最大可用格子大小，确保棋盘完全居中、铺满
CELL_SIZE = min(SCREEN_WIDTH, SCREEN_HEIGHT) // (BOARD_SIZE + 1)
# 计算居中边距，让棋盘在窗口正中间，完全占满
PADDING = (min(SCREEN_WIDTH, SCREEN_HEIGHT) - CELL_SIZE * (BOARD_SIZE - 1)) // 2
WIN_LENGTH = 5

# 颜色配置
BG_COLOR = "#D2B48C"
LINE_COLOR = "#000000"
BLACK_COLOR = "#000000"
WHITE_COLOR = "#FFFFFF"
TEXT_COLOR = "#FF3333"
SHADOW_COLOR = "#888888"

# 全局变量
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
current_player = 1  # 1:黑棋, 2:白棋
game_over = False
history = []

# ====================== 初始化窗口（最大化适配） ======================
wn = turtle.Screen()
wn.title("五子棋双人对战")
wn.bgcolor(BG_COLOR)
wn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
wn.tracer(0)
# 强制窗口居中
wn.setworldcoordinates(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

# ====================== 画笔初始化 ======================
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(2)

piece_pen = turtle.Turtle()
piece_pen.speed(0)
piece_pen.hideturtle()
piece_pen.pensize(1)

info_pen = turtle.Turtle()
info_pen.speed(0)
info_pen.hideturtle()
info_pen.color(TEXT_COLOR)


# ====================== 绘制棋盘（完全铺满窗口） ======================
def draw_board():
    pen.clear()
    # 绘制横线（从左到右，铺满整个宽度）
    for i in range(BOARD_SIZE):
        pen.penup()
        pen.goto(PADDING, PADDING + i * CELL_SIZE)
        pen.pendown()
        pen.goto(SCREEN_WIDTH - PADDING, PADDING + i * CELL_SIZE)
    # 绘制竖线（从上到下，铺满整个高度）
    for i in range(BOARD_SIZE):
        pen.penup()
        pen.goto(PADDING + i * CELL_SIZE, PADDING)
        pen.pendown()
        pen.goto(PADDING + i * CELL_SIZE, SCREEN_HEIGHT - PADDING)
    # 绘制天元和星位
    star_points = [(3, 3), (3, 11), (7, 7), (11, 3), (11, 11)]
    for x, y in star_points:
        pen.penup()
        pen.goto(PADDING + x * CELL_SIZE, PADDING + y * CELL_SIZE)
        pen.dot(6, LINE_COLOR)
    wn.update()


# ====================== 绘制棋子 ======================
def draw_piece(x, y, player):
    piece_pen.penup()
    piece_pen.goto(PADDING + x * CELL_SIZE, PADDING + y * CELL_SIZE)
    if player == 1:
        piece_pen.dot(int(CELL_SIZE * 0.7), BLACK_COLOR)
    else:
        piece_pen.dot(int(CELL_SIZE * 0.7), WHITE_COLOR)
        piece_pen.pencolor(SHADOW_COLOR)
        piece_pen.circle(int(CELL_SIZE * 0.35))
    wn.update()


# ====================== 更新信息显示 ======================
def update_info():
    info_pen.clear()
    info_pen.penup()
    info_pen.goto(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20)
    if game_over:
        winner = "黑棋" if current_player == 1 else "白棋"
        info_pen.write(f"{winner}获胜！按R重新开始，按U悔棋", align="center", font=("Arial", 16, "bold"))
    else:
        turn = "黑棋" if current_player == 1 else "白棋"
        info_pen.write(f"当前回合：{turn}  按U悔棋", align="center", font=("Arial", 16, "bold"))
    wn.update()


# ====================== 胜负判定 ======================
def check_win(x, y, player):
    # 横向
    count = 1
    i = x - 1
    while i >= 0 and board[y][i] == player:
        count += 1
        i -= 1
    i = x + 1
    while i < BOARD_SIZE and board[y][i] == player:
        count += 1
        i += 1
    if count >= WIN_LENGTH:
        return True

    # 纵向
    count = 1
    j = y - 1
    while j >= 0 and board[j][x] == player:
        count += 1
        j -= 1
    j = y + 1
    while j < BOARD_SIZE and board[j][x] == player:
        count += 1
        j += 1
    if count >= WIN_LENGTH:
        return True

    # 左上-右下
    count = 1
    i, j = x - 1, y - 1
    while i >= 0 and j >= 0 and board[j][i] == player:
        count += 1
        i -= 1
        j -= 1
    i, j = x + 1, y + 1
    while i < BOARD_SIZE and j < BOARD_SIZE and board[j][i] == player:
        count += 1
        i += 1
        j += 1
    if count >= WIN_LENGTH:
        return True

    # 右上-左下
    count = 1
    i, j = x + 1, y - 1
    while i < BOARD_SIZE and j >= 0 and board[j][i] == player:
        count += 1
        i += 1
        j -= 1
    i, j = x - 1, y + 1
    while i >= 0 and j < BOARD_SIZE and board[j][i] == player:
        count += 1
        i -= 1
        j += 1
    if count >= WIN_LENGTH:
        return True

    return False


# ====================== 鼠标点击事件 ======================
def on_click(x, y):
    global current_player, game_over
    if game_over:
        return

    # 转换为棋盘坐标（适配新的坐标系）
    grid_x = round((x - PADDING) / CELL_SIZE)
    grid_y = round((y - PADDING) / CELL_SIZE)

    # 检查坐标合法性
    if grid_x < 0 or grid_x >= BOARD_SIZE or grid_y < 0 or grid_y >= BOARD_SIZE:
        return
    if board[grid_y][grid_x] != 0:
        return

    # 落子
    board[grid_y][grid_x] = current_player
    history.append((grid_x, grid_y, current_player))
    draw_piece(grid_x, grid_y, current_player)

    # 检查胜负
    if check_win(grid_x, grid_y, current_player):
        game_over = True
        update_info()
        return

    # 切换玩家
    current_player = 3 - current_player
    update_info()


# ====================== 悔棋 ======================
def undo():
    global current_player, game_over
    if not history or game_over:
        return

    # 撤销最后一步
    x, y, player = history.pop()
    board[y][x] = 0
    # 重绘棋盘
    piece_pen.clear()
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != 0:
                draw_piece(j, i, board[i][j])
    # 切换回上一个玩家
    current_player = player
    game_over = False
    update_info()


# ====================== 重新开始 ======================
def restart():
    global board, current_player, game_over, history
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    current_player = 1
    game_over = False
    history = []
    piece_pen.clear()
    draw_board()
    update_info()


# ====================== 绑定事件 ======================
wn.onscreenclick(on_click)
wn.onkey(undo, "u")
wn.onkey(restart, "r")
wn.listen()

# ====================== 启动游戏 ======================
draw_board()
update_info()
wn.mainloop()
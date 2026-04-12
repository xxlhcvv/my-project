def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    win = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]] == player:
            return True
    return False

def tic_tac_toe():
    board = list("123456789")
    current = "X"
    print("欢迎来到井字棋！输入数字下棋")

    for _ in range(9):
        print_board(board)
        while True:
            move = input(f"玩家 {current}，请输入位置（1-9）：")
            if move.isdigit() and 1 <= int(move) <=9:
                idx = int(move)-1
                if board[idx] in "123456789":
                    board[idx] = current
                    break
            print("输入无效！")

        if check_win(board, current):
            print_board(board)
            print(f"🎉 玩家 {current} 获胜！")
            return
        current = "O" if current=="X" else "X"

    print_board(board)
    print("🤝 平局！")

tic_tac_toe()
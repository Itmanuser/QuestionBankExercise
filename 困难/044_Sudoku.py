"""
数独（Sudoku）是一款大众喜爱的数字逻辑游戏。玩家需要根据9X9盘面上的已知数字，推算出所有剩余空格的数字，
并且满足每一行、每一列、每一个3X3粗线宫内的数字均含1-9，并且不重复。
"""

def isValue(board, x, y):
    # 检查已经填入的坐标是否和列中有的元素相等
    for i in range(9): 
        if i != x and board[i][y] == board[x][y]:
            return False
    # 检查已经填入的坐标是否和行中有的元素相等
    for j in range(9): 
        if j != y and board[x][j] == board[x][y]:
            return False
    # 检查每个正方形是否符合（粗线框内只有1~9） 
    m, n = 3*(x // 3), 3*(y // 3)  # 这里求出的是3x3网格的左上角的坐标 
    for i in range(3):
        for j in range(3):
            if(i+m != x or j+n != y) and board[i+m][j+n] == board[x][y]:
                return False  
    return True

def dfs(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for k in '123456789':  # 从里面选择一个
                    board[i][j] = int(k)
                    if isValue(board, i, j) and dfs(board):
                        return True
                    # 回溯
                    board[i][j] = 0
                # 都不行，说明上次的数字不合理
                return False
    # 全部便利完，返回True
    return True

while True:
    try:
        board = []
        for i in range(9):
            row = list(map(int, input().split()))
            board.append(row)
        dfs(board)
        for i in range(9):
            board[i] = list(map(str, board[i]))
            print(' '.join(board[i]))
    except:
        break


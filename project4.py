def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):
            row_str += value
            if j!= len(row) -1:
                row_str += " | "
        
        print(row_str)
        if i != len(board) -1:
            print("---------------")
            
def get_move(turn, board):
    while True:
        row = int(input("Row = "))  
        col = int(input("Column = "))  
        
        #checks if the row is valid.
        if row < 1 or row > len(board):
            print("Invalid row, try again")
        #checks if the col is valid.
        elif col < 1 or col > len(board[row -1]):
            print("Invalid column, try again")
        #ckecks if the position in empty.
        elif board[row -1][col -1] != " ":
            print("Already taken, try again")
        else:
            break
    board[row -1][col -1] = turn
    
board = [
    [" X ", " ", " "],
    [" ", " 0 ", " "],
    [" ", " ", " "],
]

print_board(board)
get_move("X", board)
print_board(board)
get_move("O", board)
print_board(board)


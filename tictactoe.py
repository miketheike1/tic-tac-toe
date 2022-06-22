def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Game match set!!! winner!!! great game good playing. ") 

def create_board():
    board = []
    for square in range(49):
        board.append(square + 1)
    return board



def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}|{board[3]}|{board[4]}|{board[5]}|{board[6]}|")
    print('-+-+-+-+-+-+-+')
    print(f"{board[7]}|{board[8]}|{board[9]}|{board[10]}|{board[11]}|{board[12]}|{board[13]}|")
    print('- + - + - + - + - + - + -')
    print(f"{board[14]}|{board[15]}|{board[16]}|{board[17]}|{board[18]}|{board[19]}|{board[20]}|")
    print('- + - + - + - + - + - + -')
    print(f"{board[21]}|{board[22]}|{board[23]}|{board[24]}|{board[25]}|{board[26]}|{board[27]}|")
    print('- + - + - + - + - + - + -')
    print(f"{board[28]}|{board[29]}|{board[30]}|{board[31]}|{board[32]}|{board[33]}|{board[34]}|")
    print('- + - + - + - + - + - + -')
    print(f"{board[35]}|{board[36]}|{board[37]}|{board[38]}|{board[39]}|{board[40]}|{board[41]}|")
    print('- + - + - + - + - + - + -')
    print(f"{board[42]}|{board[43]}|{board[44]}|{board[45]}|{board[46]}|{board[47]}|{board[48]}|")
    print()

def is_a_draw(board):
        for square in range(49):
            if board[square] != "x" and board[square] != "o":
                return False
        return True 

def has_winner(board):
    return (board[0] == board[1] == board[2] == board[3] == board[4] == board[5] == board[6] or
            board[7] == board[8] == board[9] == board[10] == board[11] == board[12] == board[13] or
            board[14] == board[15] == board[16] == board[17] == board[18] == board[19] == board[20] or
            board[21] == board[22] == board[23] == board[24] == board[25] == board[26] == board[27] or
            board[28] == board[29] == board[30] == board[31] == board[32] == board[33] == board[34] or
            board[35] == board[36] == board[37] == board[38] == board[39] == board[40] == board[41] or
            board[42] == board[43] == board[44] == board[45] == board[46] == board[47] == board[48] or
            board[0] == board[7] == board[14] == board[21] == board[28] == board[35] == board[42] or
            board[1] == board[8] == board[15] == board[22] == board[29] == board[36] == board[43] or
            board[2] == board[9] == board[16] == board[23] == board[30] == board[37] == board[44] or
            board[3] == board[10] == board[17] == board[24] == board[31] == board[38] == board[45] or
            board[4] == board[11] == board[18] == board[25] == board[32] == board[39] == board[46] or
            board[5] == board[12] == board[19] == board[26] == board[33] == board[40] == board[47] or
            board[6] == board[14] == board[20] == board[27] == board[34] == board[41] == board[48] or
            board[0] == board[8] == board[16] == board[24] == board[32] == board[40] == board[48] or
            board[42] == board[36] == board[30] == board[24] == board[18] == board[12] == board[6])
def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-48): "))
    board[square - 1] = player
def next_player(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"

if __name__== "__main__":
    main()
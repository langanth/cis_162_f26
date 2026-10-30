"""
Today your goal is to write the logic for a game of tic tac toe to
determine the overall winner. You are provided with a basic board filled
with strings that can be changed out when a player makes a selection.

"""

def horizontal_win(board, player):
    pass

def vertical_win(board, player):
    pass

def diagonal_left(board, player):
    pass

def diagonal_right(board, player):
    pass

def print_board(board):
    flag = True
    count = 1
    for i in board:
        print(f' {i[0]} | {i[1]} | {i[2]}')
        if count == len(board):
            flag = False
        if flag:
            print('_________')

        count += 1


if __name__ == "__main__":
    player1 = input("Please enter the name of the player playing as x: ")
    player2 = input("Please enter the name of the player playing as o: ")
    board = [['-' for x in range(3)] for _ in range(3)]
    players = [player1, player2]
    current_player = players[0]
    markers = ['x', 'o']
    current_marker = markers[0]
    turns = 1
    print_board(board)
    while True:
        print(f'Turn {turns}:')
        print_board(board)
        row = int(input(f'{current_player}, please select a row to place your {current_marker} [0, 1, or 2]: '))
        column = int(input(f'{current_player}, please select a column to place your {current_marker} [0, 1, or 2]: '))
        if board[row][column] != '-':
            print('Invalid placement, try selecting again!')
            continue
        board[row][column] = current_marker
        if horizontal_win(board, current_marker) or vertical_win(board, current_marker) or diagonal_left(board, current_marker) or diagonal_right(board, current_marker):
            print(f'{current_player} wins!')
            break
        turn += 1
        current_player = players[turns % 2]
        current_marker = markers[turns % 2]
        print_board(board)



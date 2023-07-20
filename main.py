def generate_board():
    newboard = []
    for i in range(3):
        newboard.append([' ' for _ in range(3)])
    return newboard


def showing_the_board(board):
    for row in board:
        print(row)
    return board


def check_board(board, player):
    possibleWinners = [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]],
                       [[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]],
                       [[0, 0], [1, 1], [2, 2]], [[2, 0], [1, 1], [0, 2]]]
    for winner in possibleWinners:
        if player in board[winner[0][0]][winner[0][1]] \
                and player in board[winner[1][0]][winner[1][1]] \
                and player in board[winner[2][0]][winner[2][1]]:
            return player


def player_choice_and_showing_board(playerId):
    global moves
    while True:
        showing_the_board(board)
        try:
            YCoord = int(input(f'Your turn (Which coordinates do you want to place {playerId}?) X coord: '))
        except ValueError or IndexError:
            print("You passed variable with wrong type or value is too big!")
            continue
        try:
            XCoord = int(input(f'Your turn (Which coordinates do you want to place {playerId}?) Y coord: '))
        except ValueError or IndexError:
            print("You passed variable with wrong type or value is too big!")
            continue
        try:
            if board[XCoord][YCoord] == 'X' or board[XCoord][YCoord] == 'O':
                print("The grid is not empty! Choose other coordinates!")
                continue
        except IndexError:
            print("The coords you picked are out of board range!")
            continue
        else:
            try:
                board[XCoord][YCoord] = playerId
                moves += 1
                break
            except IndexError:
                print("The coord you write are out of board range!")
                continue


board = generate_board()
i = 1
player = ''
moves = 0
endOfTheGame = False
while moves < 9:
    player = 'O' if player == 'X' else 'X'
    player_choice_and_showing_board(player)
    if moves >= 5:
        winner = check_board(board, player)
        if winner:
            showing_the_board(board)
            print(f"The winner is: {player}!")
            endOfTheGame = True
        elif moves == 9:
            print("Draw!")
            endOfTheGame = True
        if endOfTheGame:
            againOrExit = input("Do you want to play again? (Y/N): ").lower()
            if againOrExit == 'y':
                moves = 0
                player = 'O'
                board = generate_board()
            elif againOrExit == 'n':
                break
            else:
                break






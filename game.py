import random

def display_board(board):
    print("Current State of the Board:")
    for i in range(0, 9):
        if i > 0 and i % 3 == 0:
            print()
        if board[i] == 0:
            print("_", end=" ")
        elif board[i] == 1:
            print("X", end=" ")
        elif board[i] == 2:
            print("O", end=" ")
    print()

def user_turn(board, player):
    while True:
        try:
            pos = int(input(f"Player {player}, enter position (1-9): "))
            if 1 <= pos <= 9 and board[pos - 1] == 0:
                board[pos - 1] = player
                break
            else:
                print("Invalid input. Please enter a number between 1 and 9 for an empty position.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_turn(board, player):
    while True:
        pos = random.randint(1, 9)
        if board[pos - 1] == 0:
            board[pos - 1] = player
            break

def choose_player():
    while True:
        player = input("Choose your player ('X' or 'O'): ").upper()
        if player == 'X':
            return 1
        elif player == 'O':
            return 2
        else:
            print("Invalid player choice. Please choose 'X' or 'O'.")

def check_winner(board):
    lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for line in lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != 0:
            return board[line[0]]
    if 0 not in board:
        return -1  # Draw
    return 0  # Continue playing

def main():
    print("Welcome to Tic-Tac-Toe!\n")
    game_mode = input("Choose game mode ('uc' for user vs. computer, 'computer' for computer vs. computer, 'user_user' for user vs. user): ")
    if game_mode == "user_user":
        player1 = choose_player()
        player2 = 3 - player1
    elif game_mode == "computer":
        player1 = 2
        player2 = 2
    else:
        player1 = choose_player()
        player2 = 2 if player1 == 1 else 1
    
    board = [0] * 9

    print(f"Player 1 (X) {'user' if player1 == 1 else 'computer'}, Player 2 (O) {'user' if player2 == 1 else 'computer'}")

    while True:
        display_board(board)
        if player1 == 1:
            user_turn(board, player1)
        else:
            user_turn(board, player1)
        winner = check_winner(board)
        if winner:
            display_board(board)
            if winner == -1:
                print("It's a draw!")
            else:
                print(f"Player {winner} wins!")
            break
        player1, player2 = player2, player1  # Switch players

if __name__ == "__main__":
    main()

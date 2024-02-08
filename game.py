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
    board = [0] * 9
    player = 1  # Player 1 starts

    while True:
        display_board(board)
        user_turn(board, player)
        winner = check_winner(board)
        if winner:
            display_board(board)
            if winner == -1:
                print("It's a draw!")
            else:
                print(f"Player {winner} wins!")
            break
        player = 3 - player  # Switch player (1 <-> 2)

if __name__ == "__main__":
    main()

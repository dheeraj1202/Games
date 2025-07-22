# Tic Tac Toe game

# Function to print the board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if someone has won
def check_win(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontal
                        (0, 3, 6), (1, 4, 7), (2, 5, 8), # vertical
                        (0, 4, 8), (2, 4, 6)] # diagonal

    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Function to handle the game logic
def play_game():
    board = [' '] * 9
    current_player = 'X'
    print("Tic Tac Toe Game!")
    print_board(board)

    while True:
        try:
            # Player input
            move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1

            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move! Try again.")
                continue

            board[move] = current_player
            print_board(board)

            # Check if the current player wins
            if check_win(board, current_player):
                print(f"Player {current_player} wins!")
                break

            # Check if the board is full (draw)
            if is_board_full(board):
                print("It's a draw!")
                break

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

# Start the game
if __name__ == "__main__":
    play_game()

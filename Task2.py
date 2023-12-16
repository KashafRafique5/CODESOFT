import random

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_winner(board, player):
    return any(all(cell == player for cell in row) for row in board) \
        or any(all(row[i] == player for row in board) for i in range(3)) \
        or all(board[i][i] == player for i in range(3)) \
        or all(board[i][2 - i] == player for i in range(3))

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_move = None
    best_eval = float('-inf')
    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        eval = minimax(board, 0, False)
        board[i][j] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)
    return best_move

def choose_user_sign():
    while True:
        user_sign = input("Choose your sign ('X' or 'O'): ")
        if user_sign.upper() in ['X', 'O']:
            return user_sign.upper()
        else:
            print("Invalid choice. Please choose 'X' or 'O'.")

def play_game():
    user_sign = choose_user_sign()
    ai_sign = 'O' if user_sign == 'X' else 'X'

    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = user_sign

        while True:
            print_board(board)

            if current_player == user_sign:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if board[row][col] == ' ':
                    board[row][col] = user_sign
                else:
                    print("Cell already taken. Let's try again.")
                    continue
            else:
                row, col = get_best_move(board)
                board[row][col] = ai_sign

            if is_winner(board, current_player):
                print_board(board)
                print(f"{current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = ai_sign if current_player == user_sign else user_sign

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == 'no':
            print("AI: Ahh!OK:(")
            break
        elif play_again.lower() == 'yes':
            print("AI: Sure, why not?")
        else:
            print("AI: I'll take that as a 'yes'!")
            
if __name__ == "__main__":
    play_game()

from TicTacToe import*

def generate_position(board):
    for i in range(3):
        for j in range(3):
            if isinstance(board[i][j], int):  # Findet eine Position, die eine Zahl ist (leere Position)
                return board[i][j]

def get_input_computer(board):
    print_board(board)
    place_number = generate_position(board)
    if place_number is not None:
        place_number = int(place_number)
        number_position1 = (place_number - 1) // 3
        number_position2 = (place_number - 1) % 3
        board[number_position1][number_position2] = "O"
    else:
        print("Kein gültiger Zug für den Computer möglich.")



def game_computer(board):
    for i in range(5):
        print(f"Du bist am Zug!")
        get_input("X", board)
        if check_game(board):
            print(f"Du hast gewonnen!")
            print_board(board)
            return
        if i == 4:
            print("Unentschieden!")
            return
        get_input_computer(board)
        if check_game(board):
            print(f"Ich hab gewonnen!")
            print_board(board)
            return


def main():
    Spielfeld = [[1, 2, 3], 
                 [4, 5, 6],
                 [7, 8, 9]]
    game_computer(Spielfeld)

if __name__ == "__main__":
    main()
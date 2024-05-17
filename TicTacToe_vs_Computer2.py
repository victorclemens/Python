

def print_board(board):
    for number in range(3):
        for i in range(3):
            print(board[number][i], end="")
            print("|", end="")
        print("")


def generate_position(board):
    # Helferfunktion zur Überprüfung eines potenziellen Gewinns
    def can_win(board, player):
        for i in range(3):
            for j in range(3):
                if isinstance(board[i][j], int):
                    board[i][j] = player
                    if check_win(board, player):
                        board[i][j] = i * 3 + j + 1  # Rückgängig machen
                        return (i, j)
                    board[i][j] = i * 3 + j + 1  # Rückgängig machen
        return None

    # Überprüft, ob der Computer (O) gewinnen kann
    win_position = can_win(board, 'O')
    if win_position:
        return win_position[0] * 3 + win_position[1] + 1

    # Überprüft, ob der Gegner (X) gewinnen kann und blockiert ihn
    block_position = can_win(board, 'X')
    if block_position:
        return block_position[0] * 3 + block_position[1] + 1

    # Überprüft die Mitte des Spielfelds
    if isinstance(board[1][1], int):
        return board[1][1]
    
    # Durchläuft das gesamte Spielfeld, um die erste leere Position zu finden
    for i in range(3):
        for j in range(3):
            if isinstance(board[i][j], int):  # Findet eine Position, die eine Zahl ist (leere Position)
                return board[i][j]
    
    return None  # Wenn kein Platz gefunden wird

def check_win(board, player):
    # Überprüft Zeilen, Spalten und Diagonalen auf einen Gewinn
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def get_input(player, board):
    print_board(board)
    place_number = input(f"Bitte trage die Nummer ein, wo du dein {player} setzten möchtest\n")
    place_number = int(place_number)
    number_position1= (place_number - 1) // 3
    number_position2= (place_number - 1) % 3
    number_position1 = int(number_position1)
    number_position2 = int(number_position2)
    if board[number_position1][number_position2] in ["X", "O"]:
        print(f"Dort kannst du dein {player} nicht setzten! ")
    else:
        board[number_position1][number_position2] = player

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

def check_game(board):
    # Horizontal and vertical checks
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] or board[0][i] == board[1][i] == board[2][i]:
            return True
    # Diagonal checks
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return True
    return False

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
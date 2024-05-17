import math


def print_board(board):
    for number in range(3):
        for i in range(3):
            print(board[number][i], end="")
            print("|", end="")
        print("")

def get_input(player, board):
    print_board(board)
    place_number = input(f"Bitte trage die Nummer ein, wo du dein {player} setzten möchtest\n")
    place_number = int(place_number)
    number_position1= math.ceil(place_number-1)/3
    number_position2= math.ceil(place_number-1) % 3
    number_position1 = int(number_position1)
    number_position2 = int(number_position2)
    if board[number_position1][number_position2] in ["X", "O"]:
        print(f"Dort kannst du dein {player} nicht setzten! ")
    else:
        board[number_position1][number_position2] = player


def check_game(board):
    # Horizontal and vertical checks
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] or board[0][i] == board[1][i] == board[2][i]:
            return True
    # Diagonal checks
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return True
    return False

        
def game(board):
    players = ["X", "O", "X", "O", "X", "O","X", "O", "X"]
    for player in players:
        print(f"Spieler {player} ist am Zug:")
        get_input(player, board)
        if check_game(board):
            print(f"Spieler {player} hat gewonnen!")
            print_board(board)
            return
    print("Das Spiel endet unentschieden!")

def main():
    Spielfeld = [[1, 2, 3], 
                 [4, 5, 6],
                 [7, 8, 9]]
    game(Spielfeld)

if __name__ == "__main__":
    main()
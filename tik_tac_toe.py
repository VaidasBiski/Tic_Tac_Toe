import random


def display_board(board):
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[1] + " | " + board[2] + " | " + board[3])


def player_input():
    marker = ""
    while not (marker == "X" or marker == "O"):
        marker = input("Pradėkite pasirinkdami 'X' ar 'O': ").upper()

    if marker == "X":
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or

            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or

            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))


def choose_first():
    if random.randint(0, 1) == 0:
        return "Žaidėjas 2"
    else:
        return "Žaidėjas 1"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Pasirinkite langelį nuo 1 iki 9: "))
    return position


def replay():
    choice = input("Dar kartą?: Taip arba Ne: ")
    return choice == 'Taip'


def main():
    print("Pažaiskime 'Kryžiukus - nuliukus!'")

    while True:

        the_board = [" "] * 10
        player1_marker, player2_marker = player_input()

        turn = choose_first()
        print(turn + " pradės pirmas")

        game_on = True
        while game_on:
            if turn == "Žaidėjas 1":
                print(turn + " jūsų eilė")

                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player1_marker, position)

                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print("Laimėjo Žaidėjas1!")
                    game_on = False

                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("Lygiosios")
                        break

                    else:
                        turn = "Žaidėjas 2"

            else:

                print(turn + " jūsų eilė")
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player2_marker, position)

                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print("Laimėjo Žaidėjas2!")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("Lygiosios!")
                        break
                    else:
                        turn = "Žaidėjas 1"

        if not replay():
            print("Geros kloties!!!!")
            break


main()

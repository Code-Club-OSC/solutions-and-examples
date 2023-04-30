from random import randint
import time

PLAYER_HIT_BOARD = [
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
]

PLAYER_SHIPS_BOARD = [
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
]

COMP_SHIPS_BOARD = [
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
]


def assign_ship(ships_board):
    SHIP_LENGTH = 3

    is_vertical = False
    is_horizontal = False

    if randint(1, 2) == 1:
        is_vertical = True
    else:
        is_horizontal = True

    if is_horizontal == True:
        selected_row = randint(0, 7)
        selected_col = randint(0, 5)
        for i in range(SHIP_LENGTH):
            ships_board[selected_row][selected_col] = "1"
            selected_col += 1
    elif is_vertical == True:
        selected_row = randint(0, 5)
        selected_col = randint(0, 7)
        for i in range(SHIP_LENGTH):
            ships_board[selected_row][selected_col] = "1"
            selected_row += 1
    print(ships_board)


def player_check_hit():
    col = int(input("Enter x coordinate 1-8: ")) - 1
    row = int(input("Enter y coordinate 1-8: ")) - 1

    if COMP_SHIPS_BOARD[row][col] == "1":
        print("Player hit")
        PLAYER_HIT_BOARD[row][col] = "X"
    elif COMP_SHIPS_BOARD[row][col] == "0":
        print("Player missed")
        PLAYER_HIT_BOARD[row][col] = "*"
    else:
        print("You have already targeted this coordinate!")


def comp_turn():
    time.sleep(0.2)
    row = randint(0, 7)
    col = randint(0, 7)

    if PLAYER_SHIPS_BOARD[row][col] == "0":
        print("Computer missed")
        PLAYER_SHIPS_BOARD[row][col] = "*"
    elif PLAYER_SHIPS_BOARD[row][col] == "1":
        print("Computer hit!")
        PLAYER_SHIPS_BOARD[row][col] = "X"
    else:
        comp_turn()


def check_win_condition():
    hit_var = 0
    other_hit_var = 0
    for i in PLAYER_HIT_BOARD:
        for j in i:
            if j == "X":
                hit_var += 1
    for i in PLAYER_SHIPS_BOARD:
        for j in i:
            if j == "X":
                other_hit_var += 1
    if hit_var == 3 and other_hit_var == 3:
        quit("Stalemate. Both ships sunk!")
    if hit_var == 3:
        quit("Victory. You sunk the enemy battleship!")
    if other_hit_var == 3:
        quit("Defeat. Your battleship was sunk!")


assign_ship(PLAYER_SHIPS_BOARD)
assign_ship(COMP_SHIPS_BOARD)

while True:
    print("Your ships: ")
    [print(i) for i in PLAYER_SHIPS_BOARD]
    print("----------")
    print("Your hits")
    [print(i) for i in PLAYER_HIT_BOARD]

    player_check_hit()

    comp_turn()

    check_win_condition()

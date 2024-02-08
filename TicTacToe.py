import time

board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

turn = True

row1 = ((((str(board[0])).replace("'", "")).replace(",", "")).replace("[", "")).replace("]", "")
row2 = ((((str(board[1])).replace("'", "")).replace(",", "")).replace("[", "")).replace("]", "")
row3 = ((((str(board[2])).replace("'", "")).replace(",", "")).replace("[", "")).replace("]", "")


def display_board():
    for i in range(0, 50):
        print("\n")
    print(row1)
    print(row2)
    print(row3)


def alternate_turn():
    global turn
    if turn:
        turn = False
    else:
        turn = True


def update_rows():
    global row1, row2, row3
    row1 = ((((str(board[0])).replace("'", "")).replace(",", "")).replace("[", "")).replace("]", "")
    row2 = ((((str(board[1])).replace("'", "")).replace(",", "")).replace("[", "")).replace("]", "")
    row3 = ((((str(board[2])).replace("'", "")).replace(",", "")).replace("[", "")).replace("]", "")


def move(space):
    if space == 'top-right':
        if board[0][2] == "-":
            if turn:
                board[0][2] = "X"
                update_rows()
            else:
                board[0][2] = "O"
                update_rows()
            return True
        else:
            print("Occupied try again")
            return False
    elif space == "top-left":
        if board[0][0] == "-":
            if turn:
                board[0][0] = "X"
                update_rows()
            else:
                board[0][0] = "O"
                update_rows()
            return True
        else:
            print("Occupied try again")
            return False
    elif space == "top-center":
        if board[0][1] == "-":
            if turn:
                board[0][1] = "X"
                update_rows()
            else:
                board[0][1] = "O"
                update_rows()
            return True
        else:
            print("Occupied try again")
            return False
    elif space == "middle-left":
        if board[1][0] == "-":
            if turn:
                board[1][0] = "X"
                update_rows()
            else:
                board[1][0] = "O"
                update_rows()
            return True
        else:
            print("Occupied try again")
            return False
    elif space == "middle-right":
        if board[1][2] == "-":
            if turn:
                board[1][2] = "X"
                update_rows()
            else:
                board[1][2] = "O"
                update_rows()
            return True
        else:
            print("Occupied try again")
            return False
    elif space == "middle-center":
        if board[1][1] == "-":
            if turn:
                board[1][1] = "X"
                update_rows()
            else:
                board[1][1] = "O"
                update_rows()
            return True
        else:
            print("Occupied try again")
            return False
    elif space == "bottom-left":
        if board[2][0] == "-":
            if turn:
                board[2][0] = "X"
                update_rows()
            else:
                board[2][0] = "O"
                update_rows()
            return True
        else:
            print("Occupied try again")
            return False
    elif space == "bottom-right":
        if board[2][2] == "-":
            if turn:
                board[2][2] = "X"
                update_rows()
            else:
                board[2][2] = "O"
                update_rows()
            return True
        else:
            print("Occupied try again")
            return False
    elif space == "bottom-center":
        if board[2][1] == "-":
            if turn:
                board[2][1] = "X"
                update_rows()
            else:
                board[2][1] = "O"
                update_rows()
            return True
        else:
            print("Occupied try again")
            return False
    else:
        print("Invalid option!")
        return False


def check_for_three():
    if board[0][0] == board[0][1] and board[0][2] == board[0][0] and board[0][0] != "-":
        if turn:
            display_board()
            print("O Wins")
            time.sleep(3)
            return True
        else:
            display_board()
            print("X Wins")
            time.sleep(3)
            return True
    elif board[1][0] == board[1][1] and board[1][2] == board[1][1] and board[1][0] != "-":
        if turn:
            display_board()
            print("O Wins")
            time.sleep(3)
            return True
        else:
            display_board()
            print("X Wins")
            time.sleep(3)
            return True
    elif board[2][0] == board[2][1] and board[2][2] == board[2][0] and board[2][0] != "-":
        if turn:
            display_board()
            print("O Wins")
            time.sleep(3)
            return True
        else:
            display_board()
            print("X Wins")
            time.sleep(3)
            return True
    # Horizontal Wins ^
    elif board[0][0] == board[1][1] and board[2][2] == board[0][0] and board[0][0] != "-":
        if turn:
            display_board()
            print("O Wins")
            time.sleep(3)
            return True
        else:
            display_board()
            print("X Wins")
            time.sleep(3)
            return True
    elif board[0][2] == board[1][1] and board[2][0] == board[0][2] and board[2][0] != "-":
        if turn:
            display_board()
            print("O Wins")
            time.sleep(3)
            return True
        else:
            display_board()
            print("X Wins")
            time.sleep(3)
            return True
    # Diagonal Wins ^
    elif board[0][0] == board[1][0] and board[2][0] == board[0][0] and board[2][0] != "-":
        if turn:
            display_board()
            print("O Wins")
            time.sleep(3)
            return True
        else:
            display_board()
            print("X Wins")
            time.sleep(3)
            return True
    elif board[0][1] == board[1][1] and board[2][1] == board[0][1] and board[0][1] != "-":
        if turn:
            display_board()
            print("O Wins")
            time.sleep(3)
            return True
        else:
            display_board()
            print("X Wins")
            time.sleep(3)
            return True
    elif board[0][2] == board[2][2] and board[2][2] == board[0][2] and board[0][2] != "-":
        if turn:
            display_board()
            print("O Wins")
            time.sleep(3)
            return True
        else:
            display_board()
            print("X Wins")
            time.sleep(3)
            return True
    # Vertical Wins ^
if __name__ == "__main__":
    def main():
        check_for_three()
        display_board()
        choice = input("Select an unoccupied space egs:(top-left, middle-center, bottom-right): ")
        if move(choice):
            alternate_turn()
        else:
            time.sleep(3)
        check_for_three()
        main()


    main()

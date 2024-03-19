#game Tic tac toe
ml = [["_","_","_"],["_","_","_"],["_","_","_"]]

def print_board():
    for i in range(3):
        print(" ".join(ml[i]) + "\n")

def check():
        for i in range(3):
            if ml[i][0] == ml[i][1] == ml[i][2] != "_":
                    return ml[i][0]
            if ml[0][i] == ml[1][i] == ml[2][i] != "_":
                    return ml[0][i]

        if ml[0][2] == ml[1][1] == ml[2][0] != "_":
            return ml[0][2]
        if ml[0][0] == ml[1][1] == ml[2][2] != "_":
            return ml[0][0]
        return None


def logic_game():
    count = 0
    while True:
        variant = input("Enter X or O: ")
        if variant == "X":
            dig = int(input("(X),Enter 1-9: "))
            row = (dig - 1) // 3
            col = (dig - 1) % 3

            if ml[row][col] == "_":
                ml[row][col] = variant
                print_board()
        if variant == "O":
            variant= "O"
            gig = int(input("(O),Enter 1-9: "))
            row = (gig - 1) // 3
            col = (gig - 1) % 3

            if ml[row][col] == "_":
                ml[row][col] = variant
                print_board()
        if check():
            return f"player {check()} win "
        elif all([cell != '_' for row in ml for cell in row]):
            return "Its a draw"

print(logic_game())


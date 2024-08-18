import os

mazelayout = [["X", "|", "END", "|", "X", "|", "X"],
        ["X", "|", " ", "|", "X", "|", "X"],
        ["X", "|", " ", "|", " ", "|", "X"],
        ["X", "|", "X", "|", " ", "|", " "]]

O_Val = [3, 6]
N_Val = O_Val
Boolean = False

def maze():
    clear()
    global Boolean
    x,y = N_Val
    if mazelayout[x][y] != "END":
        mazelayout[x][y] = "O"
        mazeupdate()
    else:
        print("Congrats you won!")
        Boolean = True

def mazeupdate():
    for i in mazelayout:
        for j in i:
            print(f"{j:4}", end = "")
        print()
    print()

def moveleft():
    global N_Val
    x, y = N_Val
    if mazelayout[x][y] == "O":
        mazelayout[x][y] = " "
        if y >= 2 and mazelayout[x][y-2] != "X":
            y -= 2
    N_Val = [x, y]
    maze()

def moveright():
    global N_Val
    x, y = N_Val
    if mazelayout[x][y] == "O":
        mazelayout[x][y] = " "
        if y <= 4 and mazelayout[x][y+2] != "X":
            y += 2
    N_Val = [x, y]
    maze()

def moveup():
    global N_Val
    x, y = N_Val
    if mazelayout[x][y] == "O":
        mazelayout[x][y] = " "
        if x >= 1 and mazelayout[x-1][y] != "X":
            x -= 1
    N_Val = [x, y]
    maze()

def movedown():
    global N_Val
    x, y = N_Val
    if mazelayout[x][y] == "O":
        mazelayout[x][y] = " "
        if x <= 2 and mazelayout[x+1][y] != "X":
            x += 1
    N_Val = [x, y]
    maze()

def clear():
    os.system("cls")

maze()
while Boolean == False:
    print("""press 1 to move left
press 2 to move right
press 3 to move up
press 4 to move down""")
    
    action = int(input("Enter num: "))

    if action == 1:
        moveleft()
    elif action == 2:
        moveright()
    elif action == 3:
        moveup()
    elif action == 4:
        movedown()
    else:
        print("Try again!")
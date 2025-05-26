import random

xsize = 50
ysize = 25

def colorizeText(text):
    colors = {"R": "31", "W": "37", "B": "34", "G": "32", "O": "38;5;208", "Y": "33"}
    result = ""
    for char in text:
        if char in colors:
            result += f"\033[{colors[char]}m{char}\033[0m"
        else:
            result += char
    return result

def drawCube(i, front, colors):
    xcord = i%xsize
    ycord = int(i/xsize)

    x = (float(xcord) - float(xsize)/2)/2+8
    y = (float(ycord) - float(ysize)/2)*-1-6
    if not front:
        y = (float(ycord) - float(ysize)/2)-6

    f1 = (-1/2*x-2 < y)
    f2 = (1/2*x-2 < y)
    f3 = (-1/2*x+2 > y)
    f4 = (1/2*x+2 > y)

    f5 = (-1/2*x+6 < y)
    f6 = (1/2*x-10 < y)
    f7 = (-1/2*x+10 > y)
    f8 = (1/2*x-6 > y)

    f9 = (1/2*x-2 > y) # f2
    f10 = (-1/2*x+2 < y) # f3
    f11 = (-1/2*x+6 > y) # f5
    f12 = (1/2*x-6 < y) # f8

    g1 = (-1/2*x-2 > y) # f1
    g2 = (-1/2*x-6 < y)
    g3 = (-1/2*x-10 > y)
    g4 = (-1/2*x-14 < y)

    g5 = (-1/2*x-6 > y) # g2
    g6 = (-1/2*x-10 < y) # g3

    h1 = (1/2*x-10 > y) # f6
    h2 = (1/2*x-14 < y)
    h3 = (1/2*x-18 > y)
    h4 = (1/2*x-22 < y)

    h5 = (1/2*x-14 > y) # h2
    h6 = (1/2*x-18 < y) # h3


    if f1 and f2 and f3 and f4:
        return colors[0]
    if f1 and f9 and f3 and f12:
        return colors[1]
    elif f1 and f3 and f6 and f8:
        return colors[2]
    elif f2 and f10 and f4 and f11:
        return colors[3]
    elif f9 and f10 and f11 and f12:
        return colors[4]
    elif f10 and f11 and f6 and f8:
        return colors[5]
    elif f2 and f4 and f5 and f7:
        return colors[6]
    elif f9 and f5 and f7 and f12:
        return colors[7]
    elif f5 and f6 and f7 and f8:
        return colors[8]

    elif g1 and g2 and x < 1 and x > -3:
        return colors[9]
    elif g5 and g6 and x < 1 and x > -3:
        return colors[10]
    elif g3 and g4 and x < 1 and x > -3:
        return colors[11]
    elif g1 and g2 and x < 5 and x > -3:
        return colors[12]
    elif g5 and g6 and x < 5 and x > -3:
        return colors[13]
    elif g3 and g4 and x < 5 and x > -3:
        return colors[14]
    elif g1 and g2 and x < 8 and x > 4:
        return colors[15]
    elif g5 and g6 and x < 8 and x > 4:
        return colors[16]
    elif g3 and g4 and x < 8 and x > 4:
        return colors[17]

    elif h1 and h2 and x < 12 and x > 8:
        return colors[18]
    elif h5 and h6 and x < 12 and x > 8:
        return colors[19]
    elif h3 and h4 and x < 12 and x > 8:
        return colors[20]
    elif h1 and h2 and x < 15.5 and x > 11:
        return colors[21]
    elif h5 and h6 and x < 15.5 and x > 11:
        return colors[22]
    elif h3 and h4 and x < 15.5 and x > 11:
        return colors[23]
    elif h1 and h2 and x < 19 and x > 15:
        return colors[24]
    elif h5 and h6 and x < 19 and x > 15:
        return colors[25]
    elif h3 and h4 and x < 19 and x > 15:
        return colors[26]
    else:
        return " "


cube = [
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
    ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
]

def printCube():
    global cube
    front = ""
    back = ""
    for i in range(xsize*ysize):
        if i % xsize == 0 and i != 0:
            front += "\n"
            back += "\n"
            #print();
        #print(drawCube(i, True), end="")
        front += drawCube(i, True, "".join(cube[0])+"".join(cube[1])+"".join(cube[2]))
        back += drawCube(i, False, "".join(cube[3])+"".join(cube[4])[::-1]+"".join(cube[5])[::-1])

    front = front.splitlines()
    back = back.splitlines()

    for i in range(ysize):
        print(colorizeText(front[i]+back[i]))

def rotateFace(face, clockwise):
    if clockwise:
        return [face[2], face[5], face[8], face[1], face[4], face[7], face[0], face[3], face[6]]
    # Could be used in the future?
    return [face[6], face[3], face[0], face[7], face[4], face[1], face[8], face[5], face[2]]

def solved():
    global cube
    for i in range(len(cube)):
        for j in range(len(cube[i])-1):
            if cube[i][0] != cube[i][j+1]:
                return False
    return True

def moveCube(move):
    global cube
    tempCube = []
    for i in range(len(cube)):
        tempCube.append([])
        for j in range(len(cube[i])):
            tempCube[i].append(cube[i][j])
    if move == "u":
        # Rotate white face
        tempCube[0] = rotateFace(cube[0], True)
        # Change top of red to blue
        tempCube[1][0] = cube[2][0]
        tempCube[1][3] = cube[2][3]
        tempCube[1][6] = cube[2][6]
        # Change top of blue to orange
        tempCube[2][0] = cube[5][0]
        tempCube[2][3] = cube[5][3]
        tempCube[2][6] = cube[5][6]
        # Change top of green to red
        tempCube[4][0] = cube[1][0]
        tempCube[4][3] = cube[1][3]
        tempCube[4][6] = cube[1][6]
        # Change top of orange to green
        tempCube[5][0] = cube[4][0]
        tempCube[5][3] = cube[4][3]
        tempCube[5][6] = cube[4][6]
    elif move == "d":
        # Rotate yellow face
        tempCube[3] = rotateFace(cube[3], True)
        # Change bottom of red to green
        tempCube[1][2] = cube[4][2]
        tempCube[1][5] = cube[4][5]
        tempCube[1][8] = cube[4][8]
        # Change bottom of blue to red
        tempCube[2][2] = cube[1][2]
        tempCube[2][5] = cube[1][5]
        tempCube[2][8] = cube[1][8]
        # Change bottom of green to orange
        tempCube[4][2] = cube[5][2]
        tempCube[4][5] = cube[5][5]
        tempCube[4][8] = cube[5][8]
        # Change bottom of orange to blue
        tempCube[5][2] = cube[2][2]
        tempCube[5][5] = cube[2][5]
        tempCube[5][8] = cube[2][8]
    elif move == "r":
        # Rotate blue face
        tempCube[2] = rotateFace(cube[2], True)
        # Change right of red to right of yellow
        tempCube[1][6] = cube[3][6]
        tempCube[1][7] = cube[3][7]
        tempCube[1][8] = cube[3][8]
        # Change bottom of white to right of red
        tempCube[0][2] = cube[1][8]
        tempCube[0][5] = cube[1][7]
        tempCube[0][8] = cube[1][6]
        # Change left of orange to bottom of white
        tempCube[5][0] = cube[0][2]
        tempCube[5][1] = cube[0][5]
        tempCube[5][2] = cube[0][8]
        # Change left of yellow to left of orange
        tempCube[3][6] = cube[5][2]
        tempCube[3][7] = cube[5][1]
        tempCube[3][8] = cube[5][0]
    elif move == "l":
        # Rotate green face
        tempCube[4] = rotateFace(cube[4], True)
        # Change left of red to top of white
        tempCube[1][0] = cube[0][6]
        tempCube[1][1] = cube[0][3]
        tempCube[1][2] = cube[0][0]
        # Change top of white to right of orange
        tempCube[0][0] = cube[5][6]
        tempCube[0][3] = cube[5][7]
        tempCube[0][6] = cube[5][8]
        # Change right of orange to top of yellow
        tempCube[5][6] = cube[3][2]
        tempCube[5][7] = cube[3][1]
        tempCube[5][8] = cube[3][0]
        # Change top of yellow to left of red
        tempCube[3][0] = cube[1][0]
        tempCube[3][1] = cube[1][1]
        tempCube[3][2] = cube[1][2]
    elif move == "f":
        # Rotate red face
        tempCube[1] = rotateFace(cube[1], True)
        # Change right of green to left of yellow
        tempCube[4][6] = cube[3][0]
        tempCube[4][7] = cube[3][3]
        tempCube[4][8] = cube[3][6]
        # Change left of white to right of green
        tempCube[0][0] = cube[4][8]
        tempCube[0][1] = cube[4][7]
        tempCube[0][2] = cube[4][6]
        # Change left of blue to left of white
        tempCube[2][0] = cube[0][0]
        tempCube[2][1] = cube[0][1]
        tempCube[2][2] = cube[0][2]
        # Change left of yellow to left of blue
        tempCube[3][0] = cube[2][2]
        tempCube[3][3] = cube[2][1]
        tempCube[3][6] = cube[2][0]
    elif move == "b":
        # Rotate orange face
        tempCube[5] = rotateFace(cube[5], True)
        # Change right of white to right of blue
        tempCube[0][6] = cube[2][6]
        tempCube[0][7] = cube[2][7]
        tempCube[0][8] = cube[2][8]
        # Change right of blue to right of yellow
        tempCube[2][6] = cube[3][8]
        tempCube[2][7] = cube[3][5]
        tempCube[2][8] = cube[3][2]
        # Change right of yellow to left of green
        tempCube[3][2] = cube[4][0]
        tempCube[3][5] = cube[4][1]
        tempCube[3][8] = cube[4][2]
        # Change left of green to right of white
        tempCube[4][0] = cube[0][8]
        tempCube[4][1] = cube[0][7]
        tempCube[4][2] = cube[0][6]
    cube = tempCube

moves = ["u", "d", "r", "l", "f", "b"]

if input("Shuffle cube? (y/n): ").lower()[0] == "y":
    for i in range(random.randint(10, 50)):
        moveCube(moves[random.randint(0, 5)])

count = 0
printCube()
while(not solved() or count == 0):
    print("Moves: u, d, r, l, f, b\n(u' reverses, u2 does a move twice, q to quit)")
    move = input("Enter move: ")
    move = move.lower()+" "
    print()
    if move[0] in moves:
        count += 1
        print("Moves: "+str(count))
        if len(move) > 1 and move[1] == "'":
            moveCube(move[0])
            moveCube(move[0])
            moveCube(move[0])
        elif len(move) > 1 and move[1] == "2":
            moveCube(move[0])
            moveCube(move[0])
        else:
            moveCube(move[0])
        printCube()
    elif move[0] == "q":
        print("Exiting...")
        break
    else:
        print("Not a valid move!")
if solved():
    print("You solved it!")

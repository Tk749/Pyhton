import table
import myFunctions
import random
XOX = [None]*9

while True:
    playerKey = " "

    myFunctions.reKey(XOX)

    table.printTable(XOX)

    playerKey = myFunctions.side()

    move = random.choice([True, False])

    while myFunctions.gameFinishControl(XOX):
        move = myFunctions.moveMaker(move, XOX, playerKey)
        table.printTable(XOX)
        myFunctions.gameFinishControl(XOX)

    if move == True:
        print("Computer WİN.")
    else:
        print("CONGRATULATİONS, you win.")

    ch = input("QUİT(Q) Continue(C)")
    if ch == "Q" or ch == "q":
        break

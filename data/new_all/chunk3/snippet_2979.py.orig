#Source: https://stackoverflow.com/questions/56070136/typeerror-running-tic-tac-toe-game
import turtle
import time
import random 

pieces = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
turn = "X"
def drawgame(brd):
    # draw board
    turtle.setup(600, 600)
    turtle.bgcolor("silver")
    turtle.color("white")
    turtle.width(10)
    turtle.up()

    # Horizontal bars
    turtle.goto(-300, 100)
    turtle.down()
    turtle.forward(600)
    turtle.up()
    turtle.goto(-300, -100)
    turtle.down()
    turtle.forward(600)
    turtle.up()

    # Vertical bars
    turtle.goto(-100, 300)
    turtle.setheading(-90)
    turtle.down()
    turtle.forward(600)
    turtle.up()
    turtle.goto(100, 300)
    turtle.down()
    turtle.forward(600)
    turtle.up()
    turtle.color("blue")
    x, y = -300, 300
    for pos in pieces:
        if pos == "X":
            # Draw X
            turtle.up()
            turtle.goto(x + 20, y - 20)
            turtle.setheading(-45)
            turtle.down()
            turtle.forward(226)
            turtle.up()
            turtle.goto(x + 180, y - 20)
            turtle.setheading(-135)
            turtle.down()
            turtle.forward(226)
            turtle.up()

        elif pos == "O":
            #Draw O
            turtle.up()
            turtle.goto(x + 100, y - 180)
            turtle.setheading(0)
            turtle.down()
            turtle.circle(80)
            turtle.up()
        x += 200
        if x > 100:
            x = -300
            y -= 200


def clicked(board, x, y):
    #sig: list(str), int, int -> bool 
    #THIS FUNCTION MUST RETURN A BOOL, true if operation is successful, false otherwise
    global turn, pieces

    done = True

    turtle.onscreenclick(None)  # disabling handler when inside handler
    column = (x + 300) // 200
    row = (y - 300) // -200
    square = int(row * 3 + column)
    print("User clicked ", x, ",", y, " at square ", square)

    if pieces[square] == "_":
        pieces[square] = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        drawgame(pieces)
    else:
        print("That square is already taken")
        done = False
    turtle.onscreenclick(clicked)

    return done


def computer_AI(board):
    #sig: list(str) -> NoneType
    #construct an AI that competes against the user

    #Random AI selection
    AI_selection = random.randint(0,8) 

    #check for an empty space
    while pieces[AI_selection] != "_":
        AI_selection = random.randint(0,8)

    #Mark
    pieces[AI_selection] = "O"

    print("Computer Mark at :",AI_selection)

    drawgame(pieces)

def check(P,table):
    win = False

    '''ROWS'''
    #check 1 row
    if (table[0] == P) and (table[1] == P) and (table[2] == P):
        win = True  
    #check 2 row
    if (table[3] == P) and (table[4] == P) and (table[5] == P):
        win = True 
    #check3 row
    if (table[6] == P) and (table[7] == P) and (table[8] == P):
        win = True

    '''COLUMNS'''
    #check 1 Col
    if (table[0] == P) and (table[3] == P) and (table[6] == P):
        win = True
    #check 2 Col
    if (table[1] == P) and (table[4] == P) and (table[7] == P):
        win = True
    #check 3 Col
    if (table[2] == P) and (table[5] == P) and (table[8] == P):
        win = True

    ''' Diag's '''
    #check 1 Diag
    if (table[0] == P) and (table[4] == P) and (table[8] == P):
        win = True
    #check 2 diag
    if (table[2] == P) and (table[4] == P) and (table[6] == P):
        win = True

    return win

def gameover(board):
    #sig: list(str) -> bool
    #checks gameover on board if there is a three in a row pattern or not, check who wins

    game_over = False
    #change font size here
    font_size = 30

    if "_" not in pieces:
        game_over = True

    #when game over == true
    if(game_over):
        player_wins = check("X",pieces)
        computer_wins = check("O",pieces)

        if(player_wins):
            print("Player Wins!")
            turtle.write("Player Wins!", align="center", font = ("Arial",font_size,bold) )
        elif(computer_wins):
            print("Computer Wins!")
            turtle.write("Computer Wins!", align="center", font = ("Arial",font_size,bold) )
        else:
            print("No Winner!")
            turtle.write("No Winner!", align="center", font = ("Arial",font_size,bold) )


    return game_over


def handler(x, y):
    #sig: int, int -> NoneType
    if clicked(pieces, x, y):
        drawgame(pieces)
        if not gameover(pieces):
            computer_AI(pieces)
            drawgame(pieces)
            gameover(pieces)


def main():
    #Runs the game 
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(handler)
    drawgame(pieces)
    turtle.mainloop()

main()
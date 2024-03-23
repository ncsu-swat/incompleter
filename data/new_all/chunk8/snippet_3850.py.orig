#Source: https://stackoverflow.com/questions/66552353/pillow-attributeerror-photoimage-object-has-no-attribute-photoimage-photo
import tkinter as tk
from PIL import Image, ImageTk 
import pathlib

win = tk.Tk()
win.title('Chess')








#this class controls the viewing of the game and calculating the legal moves. eg if a pawn on e2 can move to e5 and drawing the board
class Game:

    #start of the Game class
    #start of the Game class
    #start of the Game class
    #start of the Game class
    #start of the Game class

    #init
    def __init__(self,root):

        print('The class has been declared')

        #creates the canvas
        self.base = tk.Canvas(win,bg='#f0d9b5',width='400',height='400')



    #function to draw the base chess board(the squares)
    def drawBoard(self):       

        #variable declarations

        i = 1
        x = 0
        y = 0

        #test
        self.base.create_rectangle(0,0,100,100,fill='#b58862',)

        #create crucial isWhite variable
        isWhite = True

        #board drawing  loop
        while i < 65:

            
            i += 1

            #if statement draws all the brown squares on the board
            if isWhite == False:

                self.base.create_rectangle(x,y,x+100,y+100,fill='#b58862',outline = '#b58862')
                #debug
                print('drew a brown square at coordinates x =', x ,'y =', y)
                
                #some logic to know how and where to draw the next square
                if x == 350:
                    y += 50
                    x = 0
                    continue
                
                else:
                    x += 50
                    isWhite = True
                    continue
                
                
            #if statement draws all the white squares on the board
            if isWhite:
                self.base.create_rectangle(x,y,x+100,y+100,fill='#f0d9b5', outline='#f0d9b5')
                #debug
                print('drew a white square at coordinates x =', x ,'y =', y)
                
                #some logic to know how and where to draw the next square
                if x == 350:
                    y += 50
                    x = 0
                    continue
                
                else:
                    x += 50
                    isWhite = False
                    continue
        #packs canvas                      
        self.base.pack()

    #end of drawBoard()

    #this class draws the pieces from an array of the pieces' locations
    def drawPieces(self):
        
        path = str(pathlib.Path(__file__).parent.absolute()) + '/Sprites/W_K.png'
        print('Path:' , path)
        norm_img = Image.open(path)
        img = norm_img.resize((50,50))
        photo = ImageTk.PhotoImage(image=img)
        king = self.base.create_image((100,100),image=photo)

#end of the Game class
#end of the Game class
#end of the Game class
#end of the Game class
#end of the Game class
#end of the Game class





#creates new instance of the Game class
game = Game(win)

#runs the drawBoard function
game.drawBoard()

#runs the drawPieces function
game.drawPieces()

#main loop
win.mainloop()
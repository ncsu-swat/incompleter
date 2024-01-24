# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66552353/pillow-attributeerror-photoimage-object-has-no-attribute-photoimage-photo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(631650)

except ImportError:
    pass
try:
    from PIL import Image, ImageTk
    _l_(631652)

except ImportError:
    pass
try:
    import pathlib
    _l_(631654)

except ImportError:
    pass

win = _c_(631657, _a_(631656, _n_(631655, "tk", lambda: tk), "Tk"))
_l_(631658)
_c_(631661, _a_(631660, _n_(631659, "win", lambda: win), "title"), 'Chess')
_l_(631662)








#this class controls the viewing of the game and calculating the legal moves. eg if a pawn on e2 can move to e5 and drawing the board
class Game:
    _l_(631774)


    #start of the Game class
    #start of the Game class
    #start of the Game class
    #start of the Game class
    #start of the Game class

    #init
    def __init__(self,root):
        _l_(631672)


        _c_(631664, _n_(631663, "print", lambda: print), 'The class has been declared')
        _l_(631665)

        #creates the canvas
        _n_(631666, "self", lambda: self).base = _c_(631670, _a_(631668, _n_(631667, "tk", lambda: tk), "Canvas"), _n_(631669, "win", lambda: win),bg='#f0d9b5',width='400',height='400')
        _l_(631671)



    #function to draw the base chess board(the squares)
    def drawBoard(self):
        _l_(631738)


        #variable declarations

        i = 1
        _l_(631673)
        x = 0
        _l_(631674)
        y = 0
        _l_(631675)

        #test
        _c_(631679, _a_(631678, _a_(631677, _n_(631676, "self", lambda: self), "base"), "create_rectangle"), 0,0,100,100,fill='#b58862',)
        _l_(631680)

        #create crucial isWhite variable
        isWhite = True
        _l_(631681)

        #board drawing  loop
        while _n_(631682, "i", lambda: i) < 65:
            _l_(631732)


            
            i += 1
            _l_(631683)

            #if statement draws all the brown squares on the board
            if _n_(631684, "isWhite", lambda: isWhite) == False:
                _l_(631707)


                _c_(631692, _a_(631687, _a_(631686, _n_(631685, "self", lambda: self), "base"), "create_rectangle"), _n_(631688, "x", lambda: x),_n_(631689, "y", lambda: y),_n_(631690, "x", lambda: x)+100,_n_(631691, "y", lambda: y)+100,fill='#b58862',outline = '#b58862')
                _l_(631693)
                #debug
                _c_(631697, _n_(631694, "print", lambda: print), 'drew a brown square at coordinates x =', _n_(631695, "x", lambda: x) ,'y =', _n_(631696, "y", lambda: y))
                _l_(631698)
                
                #some logic to know how and where to draw the next square
                if _n_(631699, "x", lambda: x) == 350:
                    _l_(631706)

                    y += 50
                    _l_(631700)
                    x = 0
                    _l_(631701)
                    continue
                    _l_(631702)
                
                else:
                    x += 50
                    _l_(631703)
                    isWhite = True
                    _l_(631704)
                    continue
                    _l_(631705)
            #if statement draws all the white squares on the board
            if _n_(631708, "isWhite", lambda: isWhite):
                _l_(631731)

                _c_(631716, _a_(631711, _a_(631710, _n_(631709, "self", lambda: self), "base"), "create_rectangle"), _n_(631712, "x", lambda: x),_n_(631713, "y", lambda: y),_n_(631714, "x", lambda: x)+100,_n_(631715, "y", lambda: y)+100,fill='#f0d9b5', outline='#f0d9b5')
                _l_(631717)
                #debug
                _c_(631721, _n_(631718, "print", lambda: print), 'drew a white square at coordinates x =', _n_(631719, "x", lambda: x) ,'y =', _n_(631720, "y", lambda: y))
                _l_(631722)
                
                #some logic to know how and where to draw the next square
                if _n_(631723, "x", lambda: x) == 350:
                    _l_(631730)

                    y += 50
                    _l_(631724)
                    x = 0
                    _l_(631725)
                    continue
                    _l_(631726)
                
                else:
                    x += 50
                    _l_(631727)
                    isWhite = False
                    _l_(631728)
                    continue
                    _l_(631729)
        #packs canvas                      
        _c_(631736, _a_(631735, _a_(631734, _n_(631733, "self", lambda: self), "base"), "pack"))
        _l_(631737)

    #end of drawBoard()

    #this class draws the pieces from an array of the pieces' locations
    def drawPieces(self):
        _l_(631773)

        
        path = _c_(631747, _n_(631739, "str", lambda: str), _c_(631746, _a_(631745, _a_(631744, _c_(631743, _a_(631741, _n_(631740, "pathlib", lambda: pathlib), "Path"), _n_(631742, "__file__", lambda: __file__)), "parent"), "absolute"))) + '/Sprites/W_K.png'
        _l_(631748)
        _c_(631751, _n_(631749, "print", lambda: print), 'Path:' , _n_(631750, "path", lambda: path))
        _l_(631752)
        norm_img = _c_(631756, _a_(631754, _n_(631753, "Image", lambda: Image), "open"), _n_(631755, "path", lambda: path))
        _l_(631757)
        img = _c_(631760, _a_(631759, _n_(631758, "norm_img", lambda: norm_img), "resize"), (50,50))
        _l_(631761)
        photo = _c_(631765, _a_(631763, _n_(631762, "ImageTk", lambda: ImageTk), "PhotoImage"), image=_n_(631764, "img", lambda: img))
        _l_(631766)
        king = _c_(631771, _a_(631769, _a_(631768, _n_(631767, "self", lambda: self), "base"), "create_image"), (100,100),image=_n_(631770, "photo", lambda: photo))
        _l_(631772)

#end of the Game class
#end of the Game class
#end of the Game class
#end of the Game class
#end of the Game class
#end of the Game class





#creates new instance of the Game class
game = _c_(631777, _n_(631775, "Game", lambda: Game), _n_(631776, "win", lambda: win))
_l_(631778)

#runs the drawBoard function
_c_(631781, _a_(631780, _n_(631779, "game", lambda: game), "drawBoard"))
_l_(631782)

#runs the drawPieces function
_c_(631785, _a_(631784, _n_(631783, "game", lambda: game), "drawPieces"))
_l_(631786)

#main loop
_c_(631789, _a_(631788, _n_(631787, "win", lambda: win), "mainloop"))
_l_(631790)
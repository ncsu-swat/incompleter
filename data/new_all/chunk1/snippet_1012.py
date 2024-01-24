# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54858231/python3-6-and-pyautogui-pixel-commands-typeerror-new-takes-4-position
#
# IMPORT ALL NECESSARY THINGS
#

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
     import os, time, sys, pyautogui as gui, argparse as arg
     _l_(406427)

except ImportError:
     pass

#
# FAILSAFES
#

_n_(406428, "gui", lambda: gui).FAILSAFE = True
_l_(406429)
_n_(406430, "gui", lambda: gui).PAUSE = 0.1
_l_(406431)

#
# SET UP ARGUMENT PARSER
#

parser = _c_(406434, _a_(406433, _n_(406432, "arg", lambda: arg), "ArgumentParser"), description='A machine learning script powered by TensorFlow designed to be run on "chess.com" using Python.')
_l_(406435)
_c_(406439, _a_(406437, _n_(406436, "parser", lambda: parser), "add_argument"), "-s", "--sleep", nargs='?', type=_n_(406438, "int", lambda: int), default='5', help='Number of seconds that the program should sleep before starting. This gives you time to move over to the website before the program looks for the gamboard on screen.')
_l_(406440)
args = _c_(406443, _a_(406442, _n_(406441, "parser", lambda: parser), "parse_args"))
_l_(406444)

#
# ASKS USER FOR WHAT SIDE IT IS ON
#

side = _c_(406446, _n_(406445, "input", lambda: input), "Are you white or black?  ")
_l_(406447)

if _n_(406448, "side", lambda: side) == "W" or _n_(406449, "side", lambda: side) == "w" or _n_(406450, "side", lambda: side) == "white" or _n_(406451, "side", lambda: side) == "White":
     _l_(406467)

     side = "W"
     _l_(406452)
elif _n_(406453, "side", lambda: side) == "B" or _n_(406454, "side", lambda: side) == "b" or _n_(406455, "side", lambda: side) == "black" or _n_(406456, "side", lambda: side) == "Black":
     _l_(406466)

     side = "B"
     _l_(406457)
else:
    _c_(406459, _n_(406458, "print", lambda: print), "Invalid selection for which side!")
    _l_(406460)
    side = None
    _l_(406461)
    _c_(406464, _a_(406463, _n_(406462, "sys", lambda: sys), "exit"), 0)
    _l_(406465)

#
# PRINT "READY" AND THEN WAIT FOR SPECIFIED AMOUNT OF TIME - DEFAULT 5 SECONDS
#

_c_(406473, _n_(406468, "print", lambda: print), "Ready! Waiting for " + _c_(406472, _n_(406469, "str", lambda: str), _a_(406471, _n_(406470, "args", lambda: args), "sleep")) + " seconds!")
_l_(406474)
_c_(406481, _a_(406476, _n_(406475, "time", lambda: time), "sleep"), _c_(406480, _n_(406477, "int", lambda: int), _a_(406479, _n_(406478, "args", lambda: args), "sleep")))
_l_(406482)

#
# GET AREA OF GAMEBOARD ON SCREEN
#

if _n_(406483, "side", lambda: side) == "W":
     _l_(406526)

     gameboard = _c_(406486, _a_(406485, _n_(406484, "gui", lambda: gui), "locateOnScreen"), './img/white/chessboard_white.png', confidence=0.55, grayscale=True)
     _l_(406487)
     left = _a_(406489, _n_(406488, "gameboard", lambda: gameboard), "left") - 10
     _l_(406490)
     top = _a_(406492, _n_(406491, "gameboard", lambda: gameboard), "top") - 5
     _l_(406493)
     right = _a_(406495, _n_(406494, "gameboard", lambda: gameboard), "left") + _a_(406497, _n_(406496, "gameboard", lambda: gameboard), "width") + 10
     _l_(406498)
     bottom = _a_(406500, _n_(406499, "gameboard", lambda: gameboard), "top") + _a_(406502, _n_(406501, "gameboard", lambda: gameboard), "height") + 15
     _l_(406503)
elif _n_(406504, "side", lambda: side) == "B":
     _l_(406525)

     gameboard = _c_(406507, _a_(406506, _n_(406505, "gui", lambda: gui), "locateOnScreen"), './img/black/chessboard_black.png', confidence=0.55, grayscale=True)
     _l_(406508)
     left = _a_(406510, _n_(406509, "gameboard", lambda: gameboard), "left") - 10
     _l_(406511)
     top = _a_(406513, _n_(406512, "gameboard", lambda: gameboard), "top") - 5
     _l_(406514)
     right = _a_(406516, _n_(406515, "gameboard", lambda: gameboard), "left") + _a_(406518, _n_(406517, "gameboard", lambda: gameboard), "width") + 10
     _l_(406519)
     bottom = _a_(406521, _n_(406520, "gameboard", lambda: gameboard), "top") + _a_(406523, _n_(406522, "gameboard", lambda: gameboard), "height") + 15
     _l_(406524)

widthInterval = (_n_(406527, "right", lambda: right) - _a_(406529, _n_(406528, "gameboard", lambda: gameboard), "left")) / 8
_l_(406530)
heightInterval = (_n_(406531, "bottom", lambda: bottom) - _a_(406533, _n_(406532, "gameboard", lambda: gameboard), "top")) / 8
_l_(406534)

#
# DEFINES A FUNCTION THAT COUNTS THE SCORE 
# - NUMBER OF YOU SIDE AND THEN SUBTRACT THE NUMBER OF OPPOSITE SIDE
#

def Score():
     _l_(406566)

     for i in _c_(406536, _n_(406535, "range", lambda: range), 8):
          _l_(406555)

          for j in _c_(406538, _n_(406537, "range", lambda: range), 8):
               _l_(406554)

               tempX = 32 + (_n_(406539, "i", lambda: i) * _n_(406540, "widthInterval", lambda: widthInterval))
               _l_(406541)
               tempY = 32 + (_n_(406542, "j", lambda: j) * _n_(406543, "heightInterval", lambda: heightInterval))
               _l_(406544)
               if _c_(406549, _a_(406546, _n_(406545, "gui", lambda: gui), "pixelMatchesColor"), _n_(406547, "tempX", lambda: tempX), _n_(406548, "tempY", lambda: tempY), (87, 83, 82), tolerance=20):
                    _l_(406553)

                    _c_(406551, _n_(406550, "print", lambda: print), "True!")
                    _l_(406552)
     
     if _n_(406556, "side", lambda: side) == "W":
          _l_(406565)

          _c_(406558, _n_(406557, "print", lambda: print), "White!")
          _l_(406559)
     elif _n_(406560, "side", lambda: side) == "B":
          _l_(406564)

          _c_(406562, _n_(406561, "print", lambda: print), "Black!")
          _l_(406563)


_c_(406568, _n_(406567, "Score", lambda: Score))
_l_(406569)
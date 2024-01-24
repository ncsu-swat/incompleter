# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34245525/typeerror-when-user-cancels-input-dialog
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
""" A simple typing program

Press "H" to draw an H
Press "E" to draw an E
Press "L" to draw a L
Press "O" to draw an O
Press "W" to draw a W
Press "R" to draw a R
Press "D" to draw a D
Press "ENTER" to go to the next line
Press "TAB" to make an indent
Press "BACKSPACE" to go backwards an indent
Press the "Up" or "Down" arrow keys to move the turtle up or down the canvas
Press "SPACE" to clear the canvas of your drawings
Press "ESC" to exit the program
Press any number from 1-0 on the key board (1 = 1, 0 = 10) to set the letter thickness
Press any key from F1-F10 to set a random color of the letter
(F1-F8 = colors, F9 = Custom Color, F10 = Original color)

That is all you need to know! Enjoy! """
try:
    from turtle import *
    _l_(675387)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(675389)

except ImportError:
    pass
try:
    import math
    _l_(675391)

except ImportError:
    pass
try:
    from tkinter.colorchooser import *
    _l_(675393)

except ImportError:
    pass
try:
    import copy
    _l_(675395)

except ImportError:
    pass

# Function variables

space_width = 30 # Default value: 30
_l_(675396) # Default value: 30
letter_height = 100 # Default value: 100
_l_(675397) # Default value: 100
letter_width = 50 # Default value: 50
_l_(675398) # Default value: 50



change = _c_(675400, _n_(675399, "input", lambda: input), "Would you like to change the size of the letters from the defult value? y/any other input: ")
_l_(675401)

y = ("yes")
_l_(675402)
n = ("no")
_l_(675403)


if _n_(675404, "change", lambda: change) in _n_(675405, "y", lambda: y):
    _l_(675524)

    try:
        _l_(675517)

        while True:
            _l_(675418)

            try:
                _l_(675417)

                letter_height = _c_(675409, _n_(675406, "int", lambda: int), _c_(675408, _n_(675407, "input", lambda: input), "Enter a value from 1-170 to set the height of each letter in pixels: "))
                _l_(675410)
                break
                _l_(675411)
            except _n_(675412, "ValueError", lambda: ValueError):
                _l_(675416)

                _c_(675414, _n_(675413, "print", lambda: print), "That is not an integer! Please enter an integer from 1-170!")
                _l_(675415)
        while _n_(675419, "letter_height", lambda: letter_height) > 170:
            _l_(675438)

            try:
                _l_(675437)

                letter_height = _c_(675423, _n_(675420, "int", lambda: int), _c_(675422, _n_(675421, "input", lambda: input), "That value is too much. Please reenter a value from 1-170: "))
                _l_(675424)
                while _n_(675425, "letter_height", lambda: letter_height) < 1:
                    _l_(675431)

                    letter_height = _c_(675429, _n_(675426, "int", lambda: int), _c_(675428, _n_(675427, "input", lambda: input), "That value is too little. Please reenter a value from 1-170: "))
                    _l_(675430)
            except _n_(675432, "ValueError", lambda: ValueError):
                _l_(675436)

                _c_(675434, _n_(675433, "print", lambda: print), "That is not an integer! Please enter an integer from 1-170!")
                _l_(675435)
        while _n_(675439, "letter_height", lambda: letter_height) < 1:
            _l_(675458)

            try:
                _l_(675457)

                letter_height = _c_(675443, _n_(675440, "int", lambda: int), _c_(675442, _n_(675441, "input", lambda: input), "That value is too little. Please reenter a value from 1-170: "))
                _l_(675444)
                while _n_(675445, "letter_height", lambda: letter_height) > 170:
                    _l_(675451)

                    letter_height = _c_(675449, _n_(675446, "int", lambda: int), _c_(675448, _n_(675447, "input", lambda: input), "That value is too much. Please reenter a value from 1-170: "))
                    _l_(675450)
            except _n_(675452, "ValueError", lambda: ValueError):
                _l_(675456)

                _c_(675454, _n_(675453, "print", lambda: print), "That is not an integer! Please enter an integer from 1-170!")
                _l_(675455)
        while True:
            _l_(675471)

            try:
                _l_(675470)

                letter_width = _c_(675462, _n_(675459, "int", lambda: int), _c_(675461, _n_(675460, "input", lambda: input), "Enter a value from 1-170 to set the width of each letter in pixels: "))
                _l_(675463)
                break
                _l_(675464)
            except _n_(675465, "ValueError", lambda: ValueError):
                _l_(675469)

                _c_(675467, _n_(675466, "print", lambda: print), "That is not an integer! Please enter an integer from 1-170!")
                _l_(675468)
        while _n_(675472, "letter_width", lambda: letter_width) > 170:
            _l_(675491)

            try:
                _l_(675490)

                letter_width = _c_(675476, _n_(675473, "int", lambda: int), _c_(675475, _n_(675474, "input", lambda: input), "That value is too much. Please reenter a value from 1-170: "))
                _l_(675477)
                while _n_(675478, "letter_width", lambda: letter_width) < 1:
                    _l_(675484)

                    letter_width = _c_(675482, _n_(675479, "int", lambda: int), _c_(675481, _n_(675480, "input", lambda: input), "That value is too little. Please reenter a value from 1-170: "))
                    _l_(675483)
            except _n_(675485, "ValueError", lambda: ValueError):
                _l_(675489)

                _c_(675487, _n_(675486, "print", lambda: print), "That is not an integer! Please enter an integer from 1-170!")
                _l_(675488)
        while _n_(675492, "letter_width", lambda: letter_width) < 1:
            _l_(675512)

            try:
                _l_(675510)

                letter_width = _c_(675496, _n_(675493, "int", lambda: int), _c_(675495, _n_(675494, "input", lambda: input), "That value is too little. Please reenter a value from 1-170: "))
                _l_(675497)
                while _n_(675498, "letter_width", lambda: letter_width) > 170:
                    _l_(675504)

                    letter_width = _c_(675502, _n_(675499, "int", lambda: int), _c_(675501, _n_(675500, "input", lambda: input), "That value is too much. Please reenter a value from 1-170: "))
                    _l_(675503)
            except _n_(675505, "ValueError", lambda: ValueError):
                _l_(675509)

                _c_(675507, _n_(675506, "print", lambda: print), "That is not an integer! Please enter an integer from 1-170!")
                _l_(675508)
            break
            _l_(675511)
    except:
        _l_(675516)

        _c_(675514, _n_(675513, "input", lambda: input), "That is not an answer! Please enter either y or n!: ")
        _l_(675515)

elif _n_(675518, "change", lambda: change) in _n_(675519, "n", lambda: n):
    _l_(675523)

    space_width = 30 # Default value: 30
    _l_(675520) # Default value: 30
    letter_height = 100 # Default value: 100
    _l_(675521) # Default value: 100
    letter_width = 50 # Default value: 50
    _l_(675522) # Default value: 50

#The 'while' loop below will tell the user to choose a color name, but if the color is invalid, an exception is thrown, and the user must reenter a color name until a valid color name is entered. 

while True:
    _l_(675538)

    try:
        _l_(675537)

        pen_color=_c_(675526, _n_(675525, "input", lambda: input), "Enter a color name to set the pen color: ")
        _l_(675527)
        _c_(675530, _n_(675528, "pencolor", lambda: pencolor), _n_(675529, "pen_color", lambda: pen_color))
        _l_(675531)
        break
        _l_(675532)
    except:
        _l_(675536)

        _c_(675534, _n_(675533, "print", lambda: print), "That is either not an available color or not a valid color name. Please reenter the name of another color or a valid one.")
        _l_(675535)

def NewLetterDimensions():
    _l_(675564)

    global letter_height
    _l_(675539)
    letter_height = _c_(675541, _n_(675540, "numinput", lambda: numinput), "New Letter Height", "Please set the new letter height: ", minval = 10, maxval = 170)
    _l_(675542)

    global letter_width
    _l_(675543)
    letter_width = _c_(675545, _n_(675544, "numinput", lambda: numinput), "New Letter Width", "Please set the new letter width: ", minval = 10, maxval = 170)
    _l_(675546)

    _c_(675548, _n_(675547, "penup", lambda: penup))
    _l_(675549)
    _c_(675556, _n_(675550, "goto", lambda: goto), _c_(675552, _n_(675551, "xcor", lambda: xcor)), _c_(675554, _n_(675553, "ycor", lambda: ycor)) +_n_(675555, "letter_height", lambda: letter_height))
    _l_(675557)
    _c_(675559, _n_(675558, "pendown", lambda: pendown))
    _l_(675560)
    _c_(675562, _n_(675561, "listen", lambda: listen))
    _l_(675563)

def draw_space():
    _l_(675575)

    # Add a space 30 pixels wide.
    _c_(675566, _n_(675565, "penup", lambda: penup))
    _l_(675567)
    _c_(675570, _n_(675568, "forward", lambda: forward), _n_(675569, "space_width", lambda: space_width))
    _l_(675571)
    _c_(675573, _n_(675572, "pendown", lambda: pendown))
    _l_(675574)

def move_turtle():
    _l_(675585)

    # Pick up the turtle and move it to its starting location.
    _c_(675577, _n_(675576, "penup", lambda: penup))
    _l_(675578)
    _c_(675580, _n_(675579, "goto", lambda: goto), -200, 100)
    _l_(675581)
    _c_(675583, _n_(675582, "pendown", lambda: pendown))
    _l_(675584)

def draw_H():
    _l_(675621)

    # Draw the left leg of H.
    # The turtle starts at the bottom left of the letter, pointing right.
    _c_(675587, _n_(675586, "left", lambda: left), 90)
    _l_(675588)
    _c_(675591, _n_(675589, "forward", lambda: forward), _n_(675590, "letter_height", lambda: letter_height))
    _l_(675592)
    # Draw the bar of the H.
    # The turtle starts at the top of the left leg, pointing up.
    _c_(675595, _n_(675593, "forward", lambda: forward), -_n_(675594, "letter_height", lambda: letter_height)/2)
    _l_(675596)
    _c_(675598, _n_(675597, "right", lambda: right), 90)
    _l_(675599)
    _c_(675602, _n_(675600, "forward", lambda: forward), _n_(675601, "letter_width", lambda: letter_width))
    _l_(675603)
    # Draw the right leg of the H.
    # The turtle starts at the right side of the bar, pointing right.
    _c_(675605, _n_(675604, "left", lambda: left), 90)
    _l_(675606)
    _c_(675609, _n_(675607, "forward", lambda: forward), _n_(675608, "letter_height", lambda: letter_height)/2)
    _l_(675610)
    _c_(675613, _n_(675611, "forward", lambda: forward), -_n_(675612, "letter_height", lambda: letter_height))
    _l_(675614)
    _c_(675616, _n_(675615, "right", lambda: right), 90)
    _l_(675617)
    # The H is drawn.
    # The turtle is in the top right, pointing right.
    _c_(675619, _n_(675618, "draw_space", lambda: draw_space))
    _l_(675620)


def draw_E():
    _l_(675675)

    # Draw an E.
    _c_(675623, _n_(675622, "left", lambda: left), 90)
    _l_(675624)
    _c_(675627, _n_(675625, "forward", lambda: forward), _n_(675626, "letter_height", lambda: letter_height))
    _l_(675628)
    _c_(675630, _n_(675629, "right", lambda: right), 90)
    _l_(675631)
    _c_(675634, _n_(675632, "forward", lambda: forward), _n_(675633, "letter_width", lambda: letter_width))
    _l_(675635)
    _c_(675638, _n_(675636, "forward", lambda: forward), -_n_(675637, "letter_width", lambda: letter_width))
    _l_(675639)
    _c_(675641, _n_(675640, "right", lambda: right), 90)
    _l_(675642)
    _c_(675645, _n_(675643, "forward", lambda: forward), _n_(675644, "letter_height", lambda: letter_height)/2)
    _l_(675646)
    _c_(675648, _n_(675647, "left", lambda: left), 90)
    _l_(675649)
    _c_(675652, _n_(675650, "forward", lambda: forward), _n_(675651, "letter_width", lambda: letter_width))
    _l_(675653)
    _c_(675656, _n_(675654, "forward", lambda: forward), -_n_(675655, "letter_width", lambda: letter_width))
    _l_(675657)
    _c_(675659, _n_(675658, "right", lambda: right), 90)
    _l_(675660)
    _c_(675663, _n_(675661, "forward", lambda: forward), _n_(675662, "letter_height", lambda: letter_height)/2)
    _l_(675664)
    _c_(675666, _n_(675665, "left", lambda: left), 90)
    _l_(675667)
    _c_(675670, _n_(675668, "forward", lambda: forward), _n_(675669, "letter_width", lambda: letter_width))
    _l_(675671)
    _c_(675673, _n_(675672, "draw_space", lambda: draw_space))
    _l_(675674)

def draw_L():
    _l_(675697)

    # Draw an L
    _c_(675677, _n_(675676, "left", lambda: left), 90)
    _l_(675678)
    _c_(675681, _n_(675679, "forward", lambda: forward), _n_(675680, "letter_height", lambda: letter_height))
    _l_(675682)
    _c_(675685, _n_(675683, "forward", lambda: forward), -_n_(675684, "letter_height", lambda: letter_height))
    _l_(675686)
    _c_(675688, _n_(675687, "right", lambda: right), 90)
    _l_(675689)
    _c_(675692, _n_(675690, "forward", lambda: forward), _n_(675691, "letter_width", lambda: letter_width))
    _l_(675693)
    _c_(675695, _n_(675694, "draw_space", lambda: draw_space))
    _l_(675696)

def draw_O():
    _l_(675733)

    # Draw an O
    _c_(675700, _n_(675698, "forward", lambda: forward), _n_(675699, "letter_width", lambda: letter_width))
    _l_(675701)
    _c_(675703, _n_(675702, "left", lambda: left), 90)
    _l_(675704)
    _c_(675707, _n_(675705, "forward", lambda: forward), _n_(675706, "letter_height", lambda: letter_height))
    _l_(675708)
    _c_(675710, _n_(675709, "left", lambda: left), 90)
    _l_(675711)
    _c_(675714, _n_(675712, "forward", lambda: forward), _n_(675713, "letter_width", lambda: letter_width))
    _l_(675715)
    _c_(675717, _n_(675716, "left", lambda: left), 90)
    _l_(675718)
    _c_(675721, _n_(675719, "forward", lambda: forward), _n_(675720, "letter_height", lambda: letter_height))
    _l_(675722)
    _c_(675724, _n_(675723, "left", lambda: left), 90)
    _l_(675725)
    _c_(675728, _n_(675726, "forward", lambda: forward), _n_(675727, "letter_width", lambda: letter_width))
    _l_(675729)
    _c_(675731, _n_(675730, "draw_space", lambda: draw_space))
    _l_(675732)

def draw_newline():
    _l_(675748)

    # This funtion will pick up the turtle and move it to a second line below HELLO
    _c_(675735, _n_(675734, "penup", lambda: penup))
    _l_(675736)
    _c_(675743, _n_(675737, "goto", lambda: goto), _c_(675739, _n_(675738, "xcor", lambda: xcor)), _c_(675741, _n_(675740, "ycor", lambda: ycor)) -_n_(675742, "letter_height", lambda: letter_height)-5)
    _l_(675744)
    _c_(675746, _n_(675745, "pendown", lambda: pendown))
    _l_(675747)

def draw_W():
    _l_(675797)

    # This function will draw a W
    _c_(675750, _n_(675749, "left", lambda: left), 105)
    _l_(675751)
    _c_(675754, _n_(675752, "forward", lambda: forward), _n_(675753, "letter_height", lambda: letter_height))
    _l_(675755)
    _c_(675758, _n_(675756, "backward", lambda: backward), _n_(675757, "letter_height", lambda: letter_height))
    _l_(675759)
    _c_(675761, _n_(675760, "right", lambda: right), 40)
    _l_(675762)
    _c_(675765, _n_(675763, "forward", lambda: forward), _n_(675764, "letter_height", lambda: letter_height)/2)
    _l_(675766)
    _c_(675768, _n_(675767, "right", lambda: right), 131)
    _l_(675769)
    _c_(675772, _n_(675770, "forward", lambda: forward), _n_(675771, "letter_height", lambda: letter_height)/2)
    _l_(675773)
    _c_(675775, _n_(675774, "left", lambda: left), 141)
    _l_(675776)
    _c_(675779, _n_(675777, "forward", lambda: forward), _n_(675778, "letter_height", lambda: letter_height))
    _l_(675780)
    _c_(675782, _n_(675781, "right", lambda: right), 165)
    _l_(675783)
    _c_(675785, _n_(675784, "penup", lambda: penup))
    _l_(675786)
    _c_(675789, _n_(675787, "forward", lambda: forward), _n_(675788, "letter_height", lambda: letter_height))
    _l_(675790)
    _c_(675792, _n_(675791, "left", lambda: left), 90)
    _l_(675793)
    _c_(675795, _n_(675794, "draw_space", lambda: draw_space))
    _l_(675796)

def draw_second_O():
    _l_(675846)

    # This function will draw the O in "world"
    _c_(675800, _n_(675798, "forward", lambda: forward), _n_(675799, "letter_width", lambda: letter_width))
    _l_(675801)
    _c_(675803, _n_(675802, "right", lambda: right), 90)
    _l_(675804)
    _c_(675807, _n_(675805, "forward", lambda: forward), _n_(675806, "letter_height", lambda: letter_height))
    _l_(675808)
    _c_(675810, _n_(675809, "right", lambda: right), 90)
    _l_(675811)
    _c_(675814, _n_(675812, "forward", lambda: forward), _n_(675813, "letter_width", lambda: letter_width))
    _l_(675815)
    _c_(675817, _n_(675816, "right", lambda: right), 90)
    _l_(675818)
    _c_(675821, _n_(675819, "forward", lambda: forward), _n_(675820, "letter_height", lambda: letter_height))
    _l_(675822)
    _c_(675824, _n_(675823, "right", lambda: right), 90)
    _l_(675825)
    _c_(675827, _n_(675826, "penup", lambda: penup))
    _l_(675828)
    _c_(675831, _n_(675829, "forward", lambda: forward), _n_(675830, "letter_width", lambda: letter_width))
    _l_(675832)
    _c_(675834, _n_(675833, "right", lambda: right), 90)
    _l_(675835)
    _c_(675838, _n_(675836, "forward", lambda: forward), _n_(675837, "letter_height", lambda: letter_height))
    _l_(675839)
    _c_(675841, _n_(675840, "left", lambda: left), 90)
    _l_(675842)
    _c_(675844, _n_(675843, "draw_space", lambda: draw_space))
    _l_(675845)

def draw_R(letter_width, letter_height):
    _l_(675907)

    # This function will draw an R

    slant_height = _c_(675851, _a_(675848, _n_(675847, "math", lambda: math), "sqrt"), _n_(675849, "letter_width", lambda: letter_width)**2 + (_n_(675850, "letter_height", lambda: letter_height)/2)**2)
    _l_(675852)
    slant_angle = (90+(90-_c_(675860, _a_(675854, _n_(675853, "math", lambda: math), "degrees"), _c_(675859, _a_(675856, _n_(675855, "math", lambda: math), "acos"), _n_(675857, "letter_width", lambda: letter_width)/_n_(675858, "slant_height", lambda: slant_height)))))
    _l_(675861)
    space_angle = (180 - _n_(675862, "slant_angle", lambda: slant_angle))
    _l_(675863)

    _c_(675865, _n_(675864, "left", lambda: left), 90)
    _l_(675866)
    _c_(675869, _n_(675867, "forward", lambda: forward), _n_(675868, "letter_height", lambda: letter_height))
    _l_(675870)
    _c_(675872, _n_(675871, "right", lambda: right), 90)
    _l_(675873)
    _c_(675876, _n_(675874, "forward", lambda: forward), _n_(675875, "letter_width", lambda: letter_width))
    _l_(675877)
    _c_(675879, _n_(675878, "right", lambda: right), 90)
    _l_(675880)
    _c_(675883, _n_(675881, "forward", lambda: forward), _n_(675882, "letter_height", lambda: letter_height)/2)
    _l_(675884)
    _c_(675886, _n_(675885, "right", lambda: right), 90)
    _l_(675887)
    _c_(675890, _n_(675888, "forward", lambda: forward), _n_(675889, "letter_width", lambda: letter_width))
    _l_(675891)
    _c_(675894, _n_(675892, "left", lambda: left), _n_(675893, "slant_angle", lambda: slant_angle))
    _l_(675895)
    _c_(675898, _n_(675896, "forward", lambda: forward), _n_(675897, "slant_height", lambda: slant_height))
    _l_(675899)
    _c_(675902, _n_(675900, "left", lambda: left), _n_(675901, "space_angle", lambda: space_angle))
    _l_(675903)
    _c_(675905, _n_(675904, "draw_space", lambda: draw_space))
    _l_(675906)

def draw_D(letter_width, letter_height):
    _l_(675979)

    # This function will draw a REAL D

    angle_height = _c_(675912, _a_(675909, _n_(675908, "math", lambda: math), "sqrt"), _n_(675910, "letter_width", lambda: letter_width)**2 + (_n_(675911, "letter_height", lambda: letter_height)/2)**2)
    _l_(675913)
    D_angle = (90+_c_(675921, _a_(675915, _n_(675914, "math", lambda: math), "degrees"), _c_(675920, _a_(675917, _n_(675916, "math", lambda: math), "acos"), _n_(675918, "letter_width", lambda: letter_width)/_n_(675919, "angle_height", lambda: angle_height))))
    _l_(675922)
    Second_D_angle = ((90 - (_n_(675923, "D_angle", lambda: D_angle)-90)) + (90-_c_(675931, _a_(675925, _n_(675924, "math", lambda: math), "degrees"), _c_(675930, _a_(675927, _n_(675926, "math", lambda: math), "acos"), _n_(675928, "letter_width", lambda: letter_width)/_n_(675929, "angle_height", lambda: angle_height)))))
    _l_(675932)
    D_space_angle = _c_(675940, _a_(675934, _n_(675933, "math", lambda: math), "degrees"), _c_(675939, _a_(675936, _n_(675935, "math", lambda: math), "atan"), _n_(675937, "letter_width", lambda: letter_width)/(_n_(675938, "letter_height", lambda: letter_height)/2)))
    _l_(675941)

    _c_(675943, _n_(675942, "left", lambda: left), 90)
    _l_(675944)
    _c_(675947, _n_(675945, "forward", lambda: forward), _n_(675946, "letter_height", lambda: letter_height))
    _l_(675948)
    _c_(675951, _n_(675949, "right", lambda: right), _n_(675950, "D_angle", lambda: D_angle))
    _l_(675952)
    _c_(675955, _n_(675953, "forward", lambda: forward), _n_(675954, "angle_height", lambda: angle_height))
    _l_(675956)
    _c_(675959, _n_(675957, "right", lambda: right), _n_(675958, "Second_D_angle", lambda: Second_D_angle))
    _l_(675960)
    _c_(675963, _n_(675961, "forward", lambda: forward), _n_(675962, "angle_height", lambda: angle_height))
    _l_(675964)
    _c_(675967, _n_(675965, "left", lambda: left), 90+_n_(675966, "D_space_angle", lambda: D_space_angle))
    _l_(675968)
    _c_(675970, _n_(675969, "penup", lambda: penup))
    _l_(675971)
    _c_(675974, _n_(675972, "forward", lambda: forward), _n_(675973, "letter_width", lambda: letter_width))
    _l_(675975)
    _c_(675977, _n_(675976, "draw_space", lambda: draw_space))
    _l_(675978)

def skip(x, y):
    _l_(675991)

    _c_(675981, _n_(675980, "penup", lambda: penup))
    _l_(675982)
    _c_(675986, _n_(675983, "goto", lambda: goto), _n_(675984, "x", lambda: x), _n_(675985, "y", lambda: y))
    _l_(675987)
    _c_(675989, _n_(675988, "pendown", lambda: pendown))
    _l_(675990)

def back():
    _l_(676003)

    _c_(675993, _n_(675992, "penup", lambda: penup))
    _l_(675994)
    _c_(675998, _n_(675995, "bk", lambda: bk), _n_(675996, "letter_width", lambda: letter_width) + _n_(675997, "space_width", lambda: space_width))
    _l_(675999)
    _c_(676001, _n_(676000, "pendown", lambda: pendown))
    _l_(676002)

def walk():
    _l_(676015)

    _c_(676005, _n_(676004, "penup", lambda: penup))
    _l_(676006)
    _c_(676010, _n_(676007, "forward", lambda: forward), _n_(676008, "letter_width", lambda: letter_width) + _n_(676009, "space_width", lambda: space_width))
    _l_(676011)
    _c_(676013, _n_(676012, "pendown", lambda: pendown))
    _l_(676014)

def soar():
    _l_(676032)

    _c_(676017, _n_(676016, "penup", lambda: penup))
    _l_(676018)
    _c_(676020, _n_(676019, "left", lambda: left), 90)
    _l_(676021)
    _c_(676024, _n_(676022, "forward", lambda: forward), _n_(676023, "letter_height", lambda: letter_height) + 5)
    _l_(676025)
    _c_(676027, _n_(676026, "right", lambda: right), 90)
    _l_(676028)
    _c_(676030, _n_(676029, "pendown", lambda: pendown))
    _l_(676031)

def fall():
    _l_(676049)

    _c_(676034, _n_(676033, "penup", lambda: penup))
    _l_(676035)
    _c_(676037, _n_(676036, "right", lambda: right), 90)
    _l_(676038)
    _c_(676041, _n_(676039, "forward", lambda: forward), _n_(676040, "letter_height", lambda: letter_height) + 5)
    _l_(676042)
    _c_(676044, _n_(676043, "left", lambda: left), 90)
    _l_(676045)
    _c_(676047, _n_(676046, "pendown", lambda: pendown))
    _l_(676048)

_c_(676051, _n_(676050, "setup", lambda: setup), 1.0, 1.0)
_l_(676052)

def RotateRight():
    _l_(676056)

    _c_(676054, _n_(676053, "right", lambda: right), 90)
    _l_(676055)

def RotateLeft():
    _l_(676060)

    _c_(676058, _n_(676057, "left", lambda: left), 90)
    _l_(676059)

def Up():
    _l_(676075)

    _c_(676062, _n_(676061, "penup", lambda: penup))
    _l_(676063)
    _c_(676070, _n_(676064, "goto", lambda: goto), _c_(676066, _n_(676065, "xcor", lambda: xcor)),_c_(676068, _n_(676067, "ycor", lambda: ycor))+(_n_(676069, "letter_height", lambda: letter_height)+5))
    _l_(676071)
    _c_(676073, _n_(676072, "pendown", lambda: pendown))
    _l_(676074)

def width1():
    _l_(676079)

    _c_(676077, _n_(676076, "width", lambda: width), 1)
    _l_(676078)

def width2():
    _l_(676083)

    _c_(676081, _n_(676080, "width", lambda: width), 2)
    _l_(676082)

def width3():
    _l_(676087)

    _c_(676085, _n_(676084, "width", lambda: width), 3)
    _l_(676086)

def width4():
    _l_(676091)

    _c_(676089, _n_(676088, "width", lambda: width), 4)
    _l_(676090)

def width5():
    _l_(676095)

    _c_(676093, _n_(676092, "width", lambda: width), 5)
    _l_(676094)

def width6():
    _l_(676099)

    _c_(676097, _n_(676096, "width", lambda: width), 6)
    _l_(676098)

def width7():
    _l_(676103)

    _c_(676101, _n_(676100, "width", lambda: width), 7)
    _l_(676102)

def width8():
    _l_(676107)

    _c_(676105, _n_(676104, "width", lambda: width), 8)
    _l_(676106)

def width9():
    _l_(676111)

    _c_(676109, _n_(676108, "width", lambda: width), 9)
    _l_(676110)

def width10():
    _l_(676115)

    _c_(676113, _n_(676112, "width", lambda: width), 10)
    _l_(676114)

def Blue():
    _l_(676119)

    _c_(676117, _n_(676116, "color", lambda: color), "blue")
    _l_(676118)

def Red():
    _l_(676123)

    _c_(676121, _n_(676120, "color", lambda: color), "red")
    _l_(676122)

def DarkGreen():
    _l_(676127)

    _c_(676125, _n_(676124, "color", lambda: color), "dark green")
    _l_(676126)

def Purple():
    _l_(676131)

    _c_(676129, _n_(676128, "color", lambda: color), "purple")
    _l_(676130)

def Pink():
    _l_(676135)

    _c_(676133, _n_(676132, "color", lambda: color), "pink")
    _l_(676134)

def Brown():
    _l_(676139)

    _c_(676137, _n_(676136, "color", lambda: color), "brown")
    _l_(676138)

def Orange():
    _l_(676143)

    _c_(676141, _n_(676140, "color", lambda: color), "orange")
    _l_(676142)

def Black():
    _l_(676147)

    _c_(676145, _n_(676144, "color", lambda: color), "Black")
    _l_(676146)

def OriginalColor():
    _l_(676152)

    _c_(676150, _n_(676148, "color", lambda: color), _n_(676149, "pen_color", lambda: pen_color))
    _l_(676151)

def getColor():
    _l_(676165)

    Color = _c_(676154, _n_(676153, "askcolor", lambda: askcolor))
    _l_(676155)
    color_name = _n_(676156, "Color", lambda: Color)[1]
    _l_(676157)
    _c_(676159, _n_(676158, "colormode", lambda: colormode), 255)
    _l_(676160)
    _c_(676163, _n_(676161, "color", lambda: color), _n_(676162, "color_name", lambda: color_name))
    _l_(676164)

_c_(676167, _n_(676166, "move_turtle", lambda: move_turtle))
_l_(676168)
_c_(676170, _n_(676169, "speed", lambda: speed), 0)
_l_(676171)
_c_(676174, _n_(676172, "color", lambda: color), _n_(676173, "pen_color", lambda: pen_color))
_l_(676175)
_c_(676177, _n_(676176, "listen", lambda: listen))
_l_(676178)
##onkey(Color, "F10")
_c_(676181, _n_(676179, "onkey", lambda: onkey), _n_(676180, "NewLetterDimensions", lambda: NewLetterDimensions), "k")
_l_(676182)
_c_(676185, _n_(676183, "onkey", lambda: onkey), _n_(676184, "width1", lambda: width1), "1")
_l_(676186)
_c_(676189, _n_(676187, "onkey", lambda: onkey), _n_(676188, "width2", lambda: width2), "2")
_l_(676190)
_c_(676193, _n_(676191, "onkey", lambda: onkey), _n_(676192, "width3", lambda: width3), "3")
_l_(676194)
_c_(676197, _n_(676195, "onkey", lambda: onkey), _n_(676196, "width4", lambda: width4), "4")
_l_(676198)
_c_(676201, _n_(676199, "onkey", lambda: onkey), _n_(676200, "width5", lambda: width5), "5")
_l_(676202)
_c_(676205, _n_(676203, "onkey", lambda: onkey), _n_(676204, "width6", lambda: width6), "6")
_l_(676206)
_c_(676209, _n_(676207, "onkey", lambda: onkey), _n_(676208, "width7", lambda: width7), "7")
_l_(676210)
_c_(676213, _n_(676211, "onkey", lambda: onkey), _n_(676212, "width8", lambda: width8), "8")
_l_(676214)
_c_(676217, _n_(676215, "onkey", lambda: onkey), _n_(676216, "width9", lambda: width9), "9")
_l_(676218)
_c_(676221, _n_(676219, "onkey", lambda: onkey), _n_(676220, "width10", lambda: width10), "0")
_l_(676222)
_c_(676225, _n_(676223, "onkey", lambda: onkey), _n_(676224, "Blue", lambda: Blue), "F1")
_l_(676226)
_c_(676229, _n_(676227, "onkey", lambda: onkey), _n_(676228, "Red", lambda: Red), "F2")
_l_(676230)
_c_(676233, _n_(676231, "onkey", lambda: onkey), _n_(676232, "DarkGreen", lambda: DarkGreen), "F3")
_l_(676234)
_c_(676237, _n_(676235, "onkey", lambda: onkey), _n_(676236, "Purple", lambda: Purple), "F4")
_l_(676238)
_c_(676241, _n_(676239, "onkey", lambda: onkey), _n_(676240, "Pink", lambda: Pink), "F5")
_l_(676242)
_c_(676245, _n_(676243, "onkey", lambda: onkey), _n_(676244, "Brown", lambda: Brown), "F6")
_l_(676246)
_c_(676249, _n_(676247, "onkey", lambda: onkey), _n_(676248, "Orange", lambda: Orange), "F7")
_l_(676250)
_c_(676253, _n_(676251, "onkey", lambda: onkey), _n_(676252, "Black", lambda: Black), "F8")
_l_(676254)
_c_(676257, _n_(676255, "onkey", lambda: onkey), _n_(676256, "getColor", lambda: getColor), "F9")
_l_(676258)
_c_(676261, _n_(676259, "onkey", lambda: onkey), _n_(676260, "OriginalColor", lambda: OriginalColor), "F10")
_l_(676262)
_c_(676265, _n_(676263, "onscreenclick", lambda: onscreenclick), _n_(676264, "goto", lambda: goto))
_l_(676266)
_c_(676269, _n_(676267, "onscreenclick", lambda: onscreenclick), _n_(676268, "skip", lambda: skip))
_l_(676270)
_c_(676273, _n_(676271, "onkey", lambda: onkey), _n_(676272, "clear", lambda: clear), "space")
_l_(676274)
_c_(676277, _n_(676275, "onkey", lambda: onkey), _n_(676276, "back", lambda: back), "BackSpace")
_l_(676278)
_c_(676281, _n_(676279, "onkey", lambda: onkey), _n_(676280, "walk", lambda: walk), "Tab")
_l_(676282)
_c_(676285, _n_(676283, "onkey", lambda: onkey), _n_(676284, "Up", lambda: Up), "Up")
_l_(676286)
_c_(676289, _n_(676287, "onkey", lambda: onkey), _n_(676288, "draw_H", lambda: draw_H), "h")
_l_(676290)
_c_(676293, _n_(676291, "onkey", lambda: onkey), _n_(676292, "bye", lambda: bye), "Escape")
_l_(676294)
_c_(676297, _n_(676295, "onkey", lambda: onkey), _n_(676296, "draw_E", lambda: draw_E), "e")
_l_(676298)
_c_(676301, _n_(676299, "onkey", lambda: onkey), _n_(676300, "draw_L", lambda: draw_L), "l")
_l_(676302)
_c_(676305, _n_(676303, "onkey", lambda: onkey), _n_(676304, "draw_O", lambda: draw_O), "o")
_l_(676306)
_c_(676309, _n_(676307, "onkey", lambda: onkey), _n_(676308, "draw_W", lambda: draw_W), "w")
_l_(676310)
_c_(676316, _n_(676311, "onkey", lambda: onkey), lambda: _c_(676315, _n_(676312, "draw_R", lambda: draw_R), _n_(676313, "letter_width", lambda: letter_width), _n_(676314, "letter_height", lambda: letter_height)), "r")
_l_(676317)
_c_(676323, _n_(676318, "onkey", lambda: onkey), lambda: _c_(676322, _n_(676319, "draw_D", lambda: draw_D), _n_(676320, "letter_width", lambda: letter_width), _n_(676321, "letter_height", lambda: letter_height)), "d")
_l_(676324)
_c_(676327, _n_(676325, "onkey", lambda: onkey), _n_(676326, "draw_newline", lambda: draw_newline), "Return")
_l_(676328)
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
    _l_(682393)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(682395)

except ImportError:
    pass
try:
    import math
    _l_(682397)

except ImportError:
    pass
try:
    from tkinter.colorchooser import *
    _l_(682399)

except ImportError:
    pass
try:
    import copy
    _l_(682401)

except ImportError:
    pass

# Function variables

space_width = 30 # Default value: 30
_l_(682402) # Default value: 30
letter_height = 100 # Default value: 100
_l_(682403) # Default value: 100
letter_width = 50 # Default value: 50
_l_(682404) # Default value: 50



change = _c_(682406, _n_(682405, "input", lambda: input), "Would you like to change the size of the letters from the defult value? y/any other input: ")
_l_(682407)

y = ("yes")
_l_(682408)
n = ("no")
_l_(682409)


if _n_(682410, "change", lambda: change) in _n_(682411, "y", lambda: y):
    _l_(682530)

    try:
        _l_(682523)

        while True:
            _l_(682424)

            try:
                _l_(682423)

                letter_height = _c_(682415, _n_(682412, "int", lambda: int), _c_(682414, _n_(682413, "input", lambda: input), "Enter a value from 1-170 to set the height of each letter in pixels: "))
                _l_(682416)
                break
                _l_(682417)
            except _n_(682418, "ValueError", lambda: ValueError):
                _l_(682422)

                _c_(682420, _n_(682419, "print", lambda: print), "That is not an integer! Please enter an integer from 1-170!")
                _l_(682421)
        while _n_(682425, "letter_height", lambda: letter_height) > 170:
            _l_(682444)

            try:
                _l_(682443)

                letter_height = _c_(682429, _n_(682426, "int", lambda: int), _c_(682428, _n_(682427, "input", lambda: input), "That value is too much. Please reenter a value from 1-170: "))
                _l_(682430)
                while _n_(682431, "letter_height", lambda: letter_height) < 1:
                    _l_(682437)

                    letter_height = _c_(682435, _n_(682432, "int", lambda: int), _c_(682434, _n_(682433, "input", lambda: input), "That value is too little. Please reenter a value from 1-170: "))
                    _l_(682436)
            except _n_(682438, "ValueError", lambda: ValueError):
                _l_(682442)

                _c_(682440, _n_(682439, "print", lambda: print), "That is not an integer! Please enter an integer from 1-170!")
                _l_(682441)
        while _n_(682445, "letter_height", lambda: letter_height) < 1:
            _l_(682464)

            try:
                _l_(682463)

                letter_height = _c_(682449, _n_(682446, "int", lambda: int), _c_(682448, _n_(682447, "input", lambda: input), "That value is too little. Please reenter a value from 1-170: "))
                _l_(682450)
                while _n_(682451, "letter_height", lambda: letter_height) > 170:
                    _l_(682457)

                    letter_height = _c_(682455, _n_(682452, "int", lambda: int), _c_(682454, _n_(682453, "input", lambda: input), "That value is too much. Please reenter a value from 1-170: "))
                    _l_(682456)
            except _n_(682458, "ValueError", lambda: ValueError):
                _l_(682462)

                _c_(682460, _n_(682459, "print", lambda: print), "That is not an integer! Please enter an integer from 1-170!")
                _l_(682461)
        while True:
            _l_(682477)

            try:
                _l_(682476)

                letter_width = _c_(682468, _n_(682465, "int", lambda: int), _c_(682467, _n_(682466, "input", lambda: input), "Enter a value from 1-170 to set the width of each letter in pixels: "))
                _l_(682469)
                break
                _l_(682470)
            except _n_(682471, "ValueError", lambda: ValueError):
                _l_(682475)

                _c_(682473, _n_(682472, "print", lambda: print), "That is not an integer! Please enter an integer from 1-170!")
                _l_(682474)
        while _n_(682478, "letter_width", lambda: letter_width) > 170:
            _l_(682497)

            try:
                _l_(682496)

                letter_width = _c_(682482, _n_(682479, "int", lambda: int), _c_(682481, _n_(682480, "input", lambda: input), "That value is too much. Please reenter a value from 1-170: "))
                _l_(682483)
                while _n_(682484, "letter_width", lambda: letter_width) < 1:
                    _l_(682490)

                    letter_width = _c_(682488, _n_(682485, "int", lambda: int), _c_(682487, _n_(682486, "input", lambda: input), "That value is too little. Please reenter a value from 1-170: "))
                    _l_(682489)
            except _n_(682491, "ValueError", lambda: ValueError):
                _l_(682495)

                _c_(682493, _n_(682492, "print", lambda: print), "That is not an integer! Please enter an integer from 1-170!")
                _l_(682494)
        while _n_(682498, "letter_width", lambda: letter_width) < 1:
            _l_(682518)

            try:
                _l_(682516)

                letter_width = _c_(682502, _n_(682499, "int", lambda: int), _c_(682501, _n_(682500, "input", lambda: input), "That value is too little. Please reenter a value from 1-170: "))
                _l_(682503)
                while _n_(682504, "letter_width", lambda: letter_width) > 170:
                    _l_(682510)

                    letter_width = _c_(682508, _n_(682505, "int", lambda: int), _c_(682507, _n_(682506, "input", lambda: input), "That value is too much. Please reenter a value from 1-170: "))
                    _l_(682509)
            except _n_(682511, "ValueError", lambda: ValueError):
                _l_(682515)

                _c_(682513, _n_(682512, "print", lambda: print), "That is not an integer! Please enter an integer from 1-170!")
                _l_(682514)
            break
            _l_(682517)
    except:
        _l_(682522)

        _c_(682520, _n_(682519, "input", lambda: input), "That is not an answer! Please enter either y or n!: ")
        _l_(682521)

elif _n_(682524, "change", lambda: change) in _n_(682525, "n", lambda: n):
    _l_(682529)

    space_width = 30 # Default value: 30
    _l_(682526) # Default value: 30
    letter_height = 100 # Default value: 100
    _l_(682527) # Default value: 100
    letter_width = 50 # Default value: 50
    _l_(682528) # Default value: 50

#The 'while' loop below will tell the user to choose a color name, but if the color is invalid, an exception is thrown, and the user must reenter a color name until a valid color name is entered. 

while True:
    _l_(682544)

    try:
        _l_(682543)

        pen_color=_c_(682532, _n_(682531, "input", lambda: input), "Enter a color name to set the pen color: ")
        _l_(682533)
        _c_(682536, _n_(682534, "pencolor", lambda: pencolor), _n_(682535, "pen_color", lambda: pen_color))
        _l_(682537)
        break
        _l_(682538)
    except:
        _l_(682542)

        _c_(682540, _n_(682539, "print", lambda: print), "That is either not an available color or not a valid color name. Please reenter the name of another color or a valid one.")
        _l_(682541)

def NewLetterDimensions():
    _l_(682570)

    global letter_height
    _l_(682545)
    letter_height = _c_(682547, _n_(682546, "numinput", lambda: numinput), "New Letter Height", "Please set the new letter height: ", minval = 10, maxval = 170)
    _l_(682548)

    global letter_width
    _l_(682549)
    letter_width = _c_(682551, _n_(682550, "numinput", lambda: numinput), "New Letter Width", "Please set the new letter width: ", minval = 10, maxval = 170)
    _l_(682552)

    _c_(682554, _n_(682553, "penup", lambda: penup))
    _l_(682555)
    _c_(682562, _n_(682556, "goto", lambda: goto), _c_(682558, _n_(682557, "xcor", lambda: xcor)), _c_(682560, _n_(682559, "ycor", lambda: ycor)) +_n_(682561, "letter_height", lambda: letter_height))
    _l_(682563)
    _c_(682565, _n_(682564, "pendown", lambda: pendown))
    _l_(682566)
    _c_(682568, _n_(682567, "listen", lambda: listen))
    _l_(682569)

def draw_space():
    _l_(682581)

    # Add a space 30 pixels wide.
    _c_(682572, _n_(682571, "penup", lambda: penup))
    _l_(682573)
    _c_(682576, _n_(682574, "forward", lambda: forward), _n_(682575, "space_width", lambda: space_width))
    _l_(682577)
    _c_(682579, _n_(682578, "pendown", lambda: pendown))
    _l_(682580)

def move_turtle():
    _l_(682591)

    # Pick up the turtle and move it to its starting location.
    _c_(682583, _n_(682582, "penup", lambda: penup))
    _l_(682584)
    _c_(682586, _n_(682585, "goto", lambda: goto), -200, 100)
    _l_(682587)
    _c_(682589, _n_(682588, "pendown", lambda: pendown))
    _l_(682590)

def draw_H():
    _l_(682627)

    # Draw the left leg of H.
    # The turtle starts at the bottom left of the letter, pointing right.
    _c_(682593, _n_(682592, "left", lambda: left), 90)
    _l_(682594)
    _c_(682597, _n_(682595, "forward", lambda: forward), _n_(682596, "letter_height", lambda: letter_height))
    _l_(682598)
    # Draw the bar of the H.
    # The turtle starts at the top of the left leg, pointing up.
    _c_(682601, _n_(682599, "forward", lambda: forward), -_n_(682600, "letter_height", lambda: letter_height)/2)
    _l_(682602)
    _c_(682604, _n_(682603, "right", lambda: right), 90)
    _l_(682605)
    _c_(682608, _n_(682606, "forward", lambda: forward), _n_(682607, "letter_width", lambda: letter_width))
    _l_(682609)
    # Draw the right leg of the H.
    # The turtle starts at the right side of the bar, pointing right.
    _c_(682611, _n_(682610, "left", lambda: left), 90)
    _l_(682612)
    _c_(682615, _n_(682613, "forward", lambda: forward), _n_(682614, "letter_height", lambda: letter_height)/2)
    _l_(682616)
    _c_(682619, _n_(682617, "forward", lambda: forward), -_n_(682618, "letter_height", lambda: letter_height))
    _l_(682620)
    _c_(682622, _n_(682621, "right", lambda: right), 90)
    _l_(682623)
    # The H is drawn.
    # The turtle is in the top right, pointing right.
    _c_(682625, _n_(682624, "draw_space", lambda: draw_space))
    _l_(682626)


def draw_E():
    _l_(682681)

    # Draw an E.
    _c_(682629, _n_(682628, "left", lambda: left), 90)
    _l_(682630)
    _c_(682633, _n_(682631, "forward", lambda: forward), _n_(682632, "letter_height", lambda: letter_height))
    _l_(682634)
    _c_(682636, _n_(682635, "right", lambda: right), 90)
    _l_(682637)
    _c_(682640, _n_(682638, "forward", lambda: forward), _n_(682639, "letter_width", lambda: letter_width))
    _l_(682641)
    _c_(682644, _n_(682642, "forward", lambda: forward), -_n_(682643, "letter_width", lambda: letter_width))
    _l_(682645)
    _c_(682647, _n_(682646, "right", lambda: right), 90)
    _l_(682648)
    _c_(682651, _n_(682649, "forward", lambda: forward), _n_(682650, "letter_height", lambda: letter_height)/2)
    _l_(682652)
    _c_(682654, _n_(682653, "left", lambda: left), 90)
    _l_(682655)
    _c_(682658, _n_(682656, "forward", lambda: forward), _n_(682657, "letter_width", lambda: letter_width))
    _l_(682659)
    _c_(682662, _n_(682660, "forward", lambda: forward), -_n_(682661, "letter_width", lambda: letter_width))
    _l_(682663)
    _c_(682665, _n_(682664, "right", lambda: right), 90)
    _l_(682666)
    _c_(682669, _n_(682667, "forward", lambda: forward), _n_(682668, "letter_height", lambda: letter_height)/2)
    _l_(682670)
    _c_(682672, _n_(682671, "left", lambda: left), 90)
    _l_(682673)
    _c_(682676, _n_(682674, "forward", lambda: forward), _n_(682675, "letter_width", lambda: letter_width))
    _l_(682677)
    _c_(682679, _n_(682678, "draw_space", lambda: draw_space))
    _l_(682680)

def draw_L():
    _l_(682703)

    # Draw an L
    _c_(682683, _n_(682682, "left", lambda: left), 90)
    _l_(682684)
    _c_(682687, _n_(682685, "forward", lambda: forward), _n_(682686, "letter_height", lambda: letter_height))
    _l_(682688)
    _c_(682691, _n_(682689, "forward", lambda: forward), -_n_(682690, "letter_height", lambda: letter_height))
    _l_(682692)
    _c_(682694, _n_(682693, "right", lambda: right), 90)
    _l_(682695)
    _c_(682698, _n_(682696, "forward", lambda: forward), _n_(682697, "letter_width", lambda: letter_width))
    _l_(682699)
    _c_(682701, _n_(682700, "draw_space", lambda: draw_space))
    _l_(682702)

def draw_O():
    _l_(682739)

    # Draw an O
    _c_(682706, _n_(682704, "forward", lambda: forward), _n_(682705, "letter_width", lambda: letter_width))
    _l_(682707)
    _c_(682709, _n_(682708, "left", lambda: left), 90)
    _l_(682710)
    _c_(682713, _n_(682711, "forward", lambda: forward), _n_(682712, "letter_height", lambda: letter_height))
    _l_(682714)
    _c_(682716, _n_(682715, "left", lambda: left), 90)
    _l_(682717)
    _c_(682720, _n_(682718, "forward", lambda: forward), _n_(682719, "letter_width", lambda: letter_width))
    _l_(682721)
    _c_(682723, _n_(682722, "left", lambda: left), 90)
    _l_(682724)
    _c_(682727, _n_(682725, "forward", lambda: forward), _n_(682726, "letter_height", lambda: letter_height))
    _l_(682728)
    _c_(682730, _n_(682729, "left", lambda: left), 90)
    _l_(682731)
    _c_(682734, _n_(682732, "forward", lambda: forward), _n_(682733, "letter_width", lambda: letter_width))
    _l_(682735)
    _c_(682737, _n_(682736, "draw_space", lambda: draw_space))
    _l_(682738)

def draw_newline():
    _l_(682754)

    # This funtion will pick up the turtle and move it to a second line below HELLO
    _c_(682741, _n_(682740, "penup", lambda: penup))
    _l_(682742)
    _c_(682749, _n_(682743, "goto", lambda: goto), _c_(682745, _n_(682744, "xcor", lambda: xcor)), _c_(682747, _n_(682746, "ycor", lambda: ycor)) -_n_(682748, "letter_height", lambda: letter_height)-5)
    _l_(682750)
    _c_(682752, _n_(682751, "pendown", lambda: pendown))
    _l_(682753)

def draw_W():
    _l_(682803)

    # This function will draw a W
    _c_(682756, _n_(682755, "left", lambda: left), 105)
    _l_(682757)
    _c_(682760, _n_(682758, "forward", lambda: forward), _n_(682759, "letter_height", lambda: letter_height))
    _l_(682761)
    _c_(682764, _n_(682762, "backward", lambda: backward), _n_(682763, "letter_height", lambda: letter_height))
    _l_(682765)
    _c_(682767, _n_(682766, "right", lambda: right), 40)
    _l_(682768)
    _c_(682771, _n_(682769, "forward", lambda: forward), _n_(682770, "letter_height", lambda: letter_height)/2)
    _l_(682772)
    _c_(682774, _n_(682773, "right", lambda: right), 131)
    _l_(682775)
    _c_(682778, _n_(682776, "forward", lambda: forward), _n_(682777, "letter_height", lambda: letter_height)/2)
    _l_(682779)
    _c_(682781, _n_(682780, "left", lambda: left), 141)
    _l_(682782)
    _c_(682785, _n_(682783, "forward", lambda: forward), _n_(682784, "letter_height", lambda: letter_height))
    _l_(682786)
    _c_(682788, _n_(682787, "right", lambda: right), 165)
    _l_(682789)
    _c_(682791, _n_(682790, "penup", lambda: penup))
    _l_(682792)
    _c_(682795, _n_(682793, "forward", lambda: forward), _n_(682794, "letter_height", lambda: letter_height))
    _l_(682796)
    _c_(682798, _n_(682797, "left", lambda: left), 90)
    _l_(682799)
    _c_(682801, _n_(682800, "draw_space", lambda: draw_space))
    _l_(682802)

def draw_second_O():
    _l_(682852)

    # This function will draw the O in "world"
    _c_(682806, _n_(682804, "forward", lambda: forward), _n_(682805, "letter_width", lambda: letter_width))
    _l_(682807)
    _c_(682809, _n_(682808, "right", lambda: right), 90)
    _l_(682810)
    _c_(682813, _n_(682811, "forward", lambda: forward), _n_(682812, "letter_height", lambda: letter_height))
    _l_(682814)
    _c_(682816, _n_(682815, "right", lambda: right), 90)
    _l_(682817)
    _c_(682820, _n_(682818, "forward", lambda: forward), _n_(682819, "letter_width", lambda: letter_width))
    _l_(682821)
    _c_(682823, _n_(682822, "right", lambda: right), 90)
    _l_(682824)
    _c_(682827, _n_(682825, "forward", lambda: forward), _n_(682826, "letter_height", lambda: letter_height))
    _l_(682828)
    _c_(682830, _n_(682829, "right", lambda: right), 90)
    _l_(682831)
    _c_(682833, _n_(682832, "penup", lambda: penup))
    _l_(682834)
    _c_(682837, _n_(682835, "forward", lambda: forward), _n_(682836, "letter_width", lambda: letter_width))
    _l_(682838)
    _c_(682840, _n_(682839, "right", lambda: right), 90)
    _l_(682841)
    _c_(682844, _n_(682842, "forward", lambda: forward), _n_(682843, "letter_height", lambda: letter_height))
    _l_(682845)
    _c_(682847, _n_(682846, "left", lambda: left), 90)
    _l_(682848)
    _c_(682850, _n_(682849, "draw_space", lambda: draw_space))
    _l_(682851)

def draw_R(letter_width, letter_height):
    _l_(682913)

    # This function will draw an R

    slant_height = _c_(682857, _a_(682854, _n_(682853, "math", lambda: math), "sqrt"), _n_(682855, "letter_width", lambda: letter_width)**2 + (_n_(682856, "letter_height", lambda: letter_height)/2)**2)
    _l_(682858)
    slant_angle = (90+(90-_c_(682866, _a_(682860, _n_(682859, "math", lambda: math), "degrees"), _c_(682865, _a_(682862, _n_(682861, "math", lambda: math), "acos"), _n_(682863, "letter_width", lambda: letter_width)/_n_(682864, "slant_height", lambda: slant_height)))))
    _l_(682867)
    space_angle = (180 - _n_(682868, "slant_angle", lambda: slant_angle))
    _l_(682869)

    _c_(682871, _n_(682870, "left", lambda: left), 90)
    _l_(682872)
    _c_(682875, _n_(682873, "forward", lambda: forward), _n_(682874, "letter_height", lambda: letter_height))
    _l_(682876)
    _c_(682878, _n_(682877, "right", lambda: right), 90)
    _l_(682879)
    _c_(682882, _n_(682880, "forward", lambda: forward), _n_(682881, "letter_width", lambda: letter_width))
    _l_(682883)
    _c_(682885, _n_(682884, "right", lambda: right), 90)
    _l_(682886)
    _c_(682889, _n_(682887, "forward", lambda: forward), _n_(682888, "letter_height", lambda: letter_height)/2)
    _l_(682890)
    _c_(682892, _n_(682891, "right", lambda: right), 90)
    _l_(682893)
    _c_(682896, _n_(682894, "forward", lambda: forward), _n_(682895, "letter_width", lambda: letter_width))
    _l_(682897)
    _c_(682900, _n_(682898, "left", lambda: left), _n_(682899, "slant_angle", lambda: slant_angle))
    _l_(682901)
    _c_(682904, _n_(682902, "forward", lambda: forward), _n_(682903, "slant_height", lambda: slant_height))
    _l_(682905)
    _c_(682908, _n_(682906, "left", lambda: left), _n_(682907, "space_angle", lambda: space_angle))
    _l_(682909)
    _c_(682911, _n_(682910, "draw_space", lambda: draw_space))
    _l_(682912)

def draw_D(letter_width, letter_height):
    _l_(682985)

    # This function will draw a REAL D

    angle_height = _c_(682918, _a_(682915, _n_(682914, "math", lambda: math), "sqrt"), _n_(682916, "letter_width", lambda: letter_width)**2 + (_n_(682917, "letter_height", lambda: letter_height)/2)**2)
    _l_(682919)
    D_angle = (90+_c_(682927, _a_(682921, _n_(682920, "math", lambda: math), "degrees"), _c_(682926, _a_(682923, _n_(682922, "math", lambda: math), "acos"), _n_(682924, "letter_width", lambda: letter_width)/_n_(682925, "angle_height", lambda: angle_height))))
    _l_(682928)
    Second_D_angle = ((90 - (_n_(682929, "D_angle", lambda: D_angle)-90)) + (90-_c_(682937, _a_(682931, _n_(682930, "math", lambda: math), "degrees"), _c_(682936, _a_(682933, _n_(682932, "math", lambda: math), "acos"), _n_(682934, "letter_width", lambda: letter_width)/_n_(682935, "angle_height", lambda: angle_height)))))
    _l_(682938)
    D_space_angle = _c_(682946, _a_(682940, _n_(682939, "math", lambda: math), "degrees"), _c_(682945, _a_(682942, _n_(682941, "math", lambda: math), "atan"), _n_(682943, "letter_width", lambda: letter_width)/(_n_(682944, "letter_height", lambda: letter_height)/2)))
    _l_(682947)

    _c_(682949, _n_(682948, "left", lambda: left), 90)
    _l_(682950)
    _c_(682953, _n_(682951, "forward", lambda: forward), _n_(682952, "letter_height", lambda: letter_height))
    _l_(682954)
    _c_(682957, _n_(682955, "right", lambda: right), _n_(682956, "D_angle", lambda: D_angle))
    _l_(682958)
    _c_(682961, _n_(682959, "forward", lambda: forward), _n_(682960, "angle_height", lambda: angle_height))
    _l_(682962)
    _c_(682965, _n_(682963, "right", lambda: right), _n_(682964, "Second_D_angle", lambda: Second_D_angle))
    _l_(682966)
    _c_(682969, _n_(682967, "forward", lambda: forward), _n_(682968, "angle_height", lambda: angle_height))
    _l_(682970)
    _c_(682973, _n_(682971, "left", lambda: left), 90+_n_(682972, "D_space_angle", lambda: D_space_angle))
    _l_(682974)
    _c_(682976, _n_(682975, "penup", lambda: penup))
    _l_(682977)
    _c_(682980, _n_(682978, "forward", lambda: forward), _n_(682979, "letter_width", lambda: letter_width))
    _l_(682981)
    _c_(682983, _n_(682982, "draw_space", lambda: draw_space))
    _l_(682984)

def skip(x, y):
    _l_(682997)

    _c_(682987, _n_(682986, "penup", lambda: penup))
    _l_(682988)
    _c_(682992, _n_(682989, "goto", lambda: goto), _n_(682990, "x", lambda: x), _n_(682991, "y", lambda: y))
    _l_(682993)
    _c_(682995, _n_(682994, "pendown", lambda: pendown))
    _l_(682996)

def back():
    _l_(683009)

    _c_(682999, _n_(682998, "penup", lambda: penup))
    _l_(683000)
    _c_(683004, _n_(683001, "bk", lambda: bk), _n_(683002, "letter_width", lambda: letter_width) + _n_(683003, "space_width", lambda: space_width))
    _l_(683005)
    _c_(683007, _n_(683006, "pendown", lambda: pendown))
    _l_(683008)

def walk():
    _l_(683021)

    _c_(683011, _n_(683010, "penup", lambda: penup))
    _l_(683012)
    _c_(683016, _n_(683013, "forward", lambda: forward), _n_(683014, "letter_width", lambda: letter_width) + _n_(683015, "space_width", lambda: space_width))
    _l_(683017)
    _c_(683019, _n_(683018, "pendown", lambda: pendown))
    _l_(683020)

def soar():
    _l_(683038)

    _c_(683023, _n_(683022, "penup", lambda: penup))
    _l_(683024)
    _c_(683026, _n_(683025, "left", lambda: left), 90)
    _l_(683027)
    _c_(683030, _n_(683028, "forward", lambda: forward), _n_(683029, "letter_height", lambda: letter_height) + 5)
    _l_(683031)
    _c_(683033, _n_(683032, "right", lambda: right), 90)
    _l_(683034)
    _c_(683036, _n_(683035, "pendown", lambda: pendown))
    _l_(683037)

def fall():
    _l_(683055)

    _c_(683040, _n_(683039, "penup", lambda: penup))
    _l_(683041)
    _c_(683043, _n_(683042, "right", lambda: right), 90)
    _l_(683044)
    _c_(683047, _n_(683045, "forward", lambda: forward), _n_(683046, "letter_height", lambda: letter_height) + 5)
    _l_(683048)
    _c_(683050, _n_(683049, "left", lambda: left), 90)
    _l_(683051)
    _c_(683053, _n_(683052, "pendown", lambda: pendown))
    _l_(683054)

_c_(683057, _n_(683056, "setup", lambda: setup), 1.0, 1.0)
_l_(683058)

def RotateRight():
    _l_(683062)

    _c_(683060, _n_(683059, "right", lambda: right), 90)
    _l_(683061)

def RotateLeft():
    _l_(683066)

    _c_(683064, _n_(683063, "left", lambda: left), 90)
    _l_(683065)

def Up():
    _l_(683081)

    _c_(683068, _n_(683067, "penup", lambda: penup))
    _l_(683069)
    _c_(683076, _n_(683070, "goto", lambda: goto), _c_(683072, _n_(683071, "xcor", lambda: xcor)),_c_(683074, _n_(683073, "ycor", lambda: ycor))+(_n_(683075, "letter_height", lambda: letter_height)+5))
    _l_(683077)
    _c_(683079, _n_(683078, "pendown", lambda: pendown))
    _l_(683080)

def width1():
    _l_(683085)

    _c_(683083, _n_(683082, "width", lambda: width), 1)
    _l_(683084)

def width2():
    _l_(683089)

    _c_(683087, _n_(683086, "width", lambda: width), 2)
    _l_(683088)

def width3():
    _l_(683093)

    _c_(683091, _n_(683090, "width", lambda: width), 3)
    _l_(683092)

def width4():
    _l_(683097)

    _c_(683095, _n_(683094, "width", lambda: width), 4)
    _l_(683096)

def width5():
    _l_(683101)

    _c_(683099, _n_(683098, "width", lambda: width), 5)
    _l_(683100)

def width6():
    _l_(683105)

    _c_(683103, _n_(683102, "width", lambda: width), 6)
    _l_(683104)

def width7():
    _l_(683109)

    _c_(683107, _n_(683106, "width", lambda: width), 7)
    _l_(683108)

def width8():
    _l_(683113)

    _c_(683111, _n_(683110, "width", lambda: width), 8)
    _l_(683112)

def width9():
    _l_(683117)

    _c_(683115, _n_(683114, "width", lambda: width), 9)
    _l_(683116)

def width10():
    _l_(683121)

    _c_(683119, _n_(683118, "width", lambda: width), 10)
    _l_(683120)

def Blue():
    _l_(683125)

    _c_(683123, _n_(683122, "color", lambda: color), "blue")
    _l_(683124)

def Red():
    _l_(683129)

    _c_(683127, _n_(683126, "color", lambda: color), "red")
    _l_(683128)

def DarkGreen():
    _l_(683133)

    _c_(683131, _n_(683130, "color", lambda: color), "dark green")
    _l_(683132)

def Purple():
    _l_(683137)

    _c_(683135, _n_(683134, "color", lambda: color), "purple")
    _l_(683136)

def Pink():
    _l_(683141)

    _c_(683139, _n_(683138, "color", lambda: color), "pink")
    _l_(683140)

def Brown():
    _l_(683145)

    _c_(683143, _n_(683142, "color", lambda: color), "brown")
    _l_(683144)

def Orange():
    _l_(683149)

    _c_(683147, _n_(683146, "color", lambda: color), "orange")
    _l_(683148)

def Black():
    _l_(683153)

    _c_(683151, _n_(683150, "color", lambda: color), "Black")
    _l_(683152)

def OriginalColor():
    _l_(683158)

    _c_(683156, _n_(683154, "color", lambda: color), _n_(683155, "pen_color", lambda: pen_color))
    _l_(683157)

def getColor():
    _l_(683171)

    Color = _c_(683160, _n_(683159, "askcolor", lambda: askcolor))
    _l_(683161)
    color_name = _n_(683162, "Color", lambda: Color)[1]
    _l_(683163)
    _c_(683165, _n_(683164, "colormode", lambda: colormode), 255)
    _l_(683166)
    _c_(683169, _n_(683167, "color", lambda: color), _n_(683168, "color_name", lambda: color_name))
    _l_(683170)

_c_(683173, _n_(683172, "move_turtle", lambda: move_turtle))
_l_(683174)
_c_(683176, _n_(683175, "speed", lambda: speed), 0)
_l_(683177)
_c_(683180, _n_(683178, "color", lambda: color), _n_(683179, "pen_color", lambda: pen_color))
_l_(683181)
_c_(683183, _n_(683182, "listen", lambda: listen))
_l_(683184)
##onkey(Color, "F10")
_c_(683187, _n_(683185, "onkey", lambda: onkey), _n_(683186, "NewLetterDimensions", lambda: NewLetterDimensions), "k")
_l_(683188)
_c_(683191, _n_(683189, "onkey", lambda: onkey), _n_(683190, "width1", lambda: width1), "1")
_l_(683192)
_c_(683195, _n_(683193, "onkey", lambda: onkey), _n_(683194, "width2", lambda: width2), "2")
_l_(683196)
_c_(683199, _n_(683197, "onkey", lambda: onkey), _n_(683198, "width3", lambda: width3), "3")
_l_(683200)
_c_(683203, _n_(683201, "onkey", lambda: onkey), _n_(683202, "width4", lambda: width4), "4")
_l_(683204)
_c_(683207, _n_(683205, "onkey", lambda: onkey), _n_(683206, "width5", lambda: width5), "5")
_l_(683208)
_c_(683211, _n_(683209, "onkey", lambda: onkey), _n_(683210, "width6", lambda: width6), "6")
_l_(683212)
_c_(683215, _n_(683213, "onkey", lambda: onkey), _n_(683214, "width7", lambda: width7), "7")
_l_(683216)
_c_(683219, _n_(683217, "onkey", lambda: onkey), _n_(683218, "width8", lambda: width8), "8")
_l_(683220)
_c_(683223, _n_(683221, "onkey", lambda: onkey), _n_(683222, "width9", lambda: width9), "9")
_l_(683224)
_c_(683227, _n_(683225, "onkey", lambda: onkey), _n_(683226, "width10", lambda: width10), "0")
_l_(683228)
_c_(683231, _n_(683229, "onkey", lambda: onkey), _n_(683230, "Blue", lambda: Blue), "F1")
_l_(683232)
_c_(683235, _n_(683233, "onkey", lambda: onkey), _n_(683234, "Red", lambda: Red), "F2")
_l_(683236)
_c_(683239, _n_(683237, "onkey", lambda: onkey), _n_(683238, "DarkGreen", lambda: DarkGreen), "F3")
_l_(683240)
_c_(683243, _n_(683241, "onkey", lambda: onkey), _n_(683242, "Purple", lambda: Purple), "F4")
_l_(683244)
_c_(683247, _n_(683245, "onkey", lambda: onkey), _n_(683246, "Pink", lambda: Pink), "F5")
_l_(683248)
_c_(683251, _n_(683249, "onkey", lambda: onkey), _n_(683250, "Brown", lambda: Brown), "F6")
_l_(683252)
_c_(683255, _n_(683253, "onkey", lambda: onkey), _n_(683254, "Orange", lambda: Orange), "F7")
_l_(683256)
_c_(683259, _n_(683257, "onkey", lambda: onkey), _n_(683258, "Black", lambda: Black), "F8")
_l_(683260)
_c_(683263, _n_(683261, "onkey", lambda: onkey), _n_(683262, "getColor", lambda: getColor), "F9")
_l_(683264)
_c_(683267, _n_(683265, "onkey", lambda: onkey), _n_(683266, "OriginalColor", lambda: OriginalColor), "F10")
_l_(683268)
_c_(683271, _n_(683269, "onscreenclick", lambda: onscreenclick), _n_(683270, "goto", lambda: goto))
_l_(683272)
_c_(683275, _n_(683273, "onscreenclick", lambda: onscreenclick), _n_(683274, "skip", lambda: skip))
_l_(683276)
_c_(683279, _n_(683277, "onkey", lambda: onkey), _n_(683278, "clear", lambda: clear), "space")
_l_(683280)
_c_(683283, _n_(683281, "onkey", lambda: onkey), _n_(683282, "back", lambda: back), "BackSpace")
_l_(683284)
_c_(683287, _n_(683285, "onkey", lambda: onkey), _n_(683286, "walk", lambda: walk), "Tab")
_l_(683288)
_c_(683291, _n_(683289, "onkey", lambda: onkey), _n_(683290, "Up", lambda: Up), "Up")
_l_(683292)
_c_(683295, _n_(683293, "onkey", lambda: onkey), _n_(683294, "draw_H", lambda: draw_H), "h")
_l_(683296)
_c_(683299, _n_(683297, "onkey", lambda: onkey), _n_(683298, "bye", lambda: bye), "Escape")
_l_(683300)
_c_(683303, _n_(683301, "onkey", lambda: onkey), _n_(683302, "draw_E", lambda: draw_E), "e")
_l_(683304)
_c_(683307, _n_(683305, "onkey", lambda: onkey), _n_(683306, "draw_L", lambda: draw_L), "l")
_l_(683308)
_c_(683311, _n_(683309, "onkey", lambda: onkey), _n_(683310, "draw_O", lambda: draw_O), "o")
_l_(683312)
_c_(683315, _n_(683313, "onkey", lambda: onkey), _n_(683314, "draw_W", lambda: draw_W), "w")
_l_(683316)
_c_(683322, _n_(683317, "onkey", lambda: onkey), lambda: _c_(683321, _n_(683318, "draw_R", lambda: draw_R), _n_(683319, "letter_width", lambda: letter_width), _n_(683320, "letter_height", lambda: letter_height)), "r")
_l_(683323)
_c_(683329, _n_(683324, "onkey", lambda: onkey), lambda: _c_(683328, _n_(683325, "draw_D", lambda: draw_D), _n_(683326, "letter_width", lambda: letter_width), _n_(683327, "letter_height", lambda: letter_height)), "d")
_l_(683330)
_c_(683333, _n_(683331, "onkey", lambda: onkey), _n_(683332, "draw_newline", lambda: draw_newline), "Return")
_l_(683334)
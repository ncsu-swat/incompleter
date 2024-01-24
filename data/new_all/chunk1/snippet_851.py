# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62729755/when-i-ran-this-code-in-python3-it-gives-this-error-nameerror-name-x-is-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(386187)

except ImportError:
    pass

def callback(r,c):
    _l_(386226)

    global player
    _l_(386188)
    if _n_(386189, "player", lambda: player) == ' X ' and _n_(386190, "states", lambda: states)[_n_(386191, "x", lambda: x)][_n_(386192, "y", lambda: y)] == 0 and _n_(386193, "stop_game", lambda: stop_game)==False:
        _l_(386205)

        _c_(386198, _a_(386197, _n_(386194, "b", lambda: b)[_n_(386195, "r", lambda: r)][_n_(386196, "c", lambda: c)], "configure"), text= ' X ' , fg= ' blue ' , bg= ' white ' )
        _l_(386199)
        _n_(386200, "states", lambda: states)[_n_(386201, "r", lambda: r)][_n_(386202, "c", lambda: c)] = ' X '
        _l_(386203)
        player = ' O '
        _l_(386204)

    if _n_(386206, "player", lambda: player) == ' O ' and _n_(386207, "states", lambda: states)[_n_(386208, "r", lambda: r)][_n_(386209, "c", lambda: c)] == 0 and _n_(386210, "stop_game", lambda: stop_game)==False:
        _l_(386222)

        _c_(386215, _a_(386214, _n_(386211, "b", lambda: b)[_n_(386212, "r", lambda: r)][_n_(386213, "c", lambda: c)], "configure"), text= ' O ' , fg= ' orange ' , bg= ' black ' )
        _l_(386216)
        _n_(386217, "states", lambda: states)[_n_(386218, "r", lambda: r)][_n_(386219, "c", lambda: c)] = ' O '
        _l_(386220)
        player = ' X '
        _l_(386221)

    _c_(386224, _n_(386223, "check_for_winner", lambda: check_for_winner))
    _l_(386225)

def check_for_winner():
    _l_(386314)

    global stop_game
    _l_(386227)
    for i in _c_(386229, _n_(386228, "range", lambda: range), 3):
        _l_(386253)

        if _n_(386230, "states", lambda: states)[_n_(386231, "i", lambda: i)][0]==_n_(386232, "states", lambda: states)[_n_(386233, "i", lambda: i)][1]==_n_(386234, "states", lambda: states)[_n_(386235, "i", lambda: i)][2]!=0:
            _l_(386252)

            _c_(386239, _a_(386238, _n_(386236, "b", lambda: b)[_n_(386237, "i", lambda: i)][0], "configure"), bg= ' grey ' )
            _l_(386240)
            _c_(386244, _a_(386243, _n_(386241, "b", lambda: b)[_n_(386242, "i", lambda: i)][1], "configure"), bg= ' grey ' )
            _l_(386245)
            _c_(386249, _a_(386248, _n_(386246, "b", lambda: b)[_n_(386247, "i", lambda: i)][2], "configure"), bg= ' grey ' )
            _l_(386250)
            stop_game = True
            _l_(386251)

    for i in _c_(386255, _n_(386254, "range", lambda: range), 3):
        _l_(386279)

        if _n_(386256, "states", lambda: states)[0][_n_(386257, "i", lambda: i)]==_n_(386258, "states", lambda: states)[1][_n_(386259, "i", lambda: i)]==_n_(386260, "states", lambda: states)[2][_n_(386261, "i", lambda: i)]!=0:
            _l_(386278)

            _c_(386265, _a_(386264, _n_(386262, "b", lambda: b)[0][_n_(386263, "i", lambda: i)], "configure"), bg= ' grey ' )
            _l_(386266)
            _c_(386270, _a_(386269, _n_(386267, "b", lambda: b)[1][_n_(386268, "i", lambda: i)], "configure"), bg= ' grey ' )
            _l_(386271)
            _c_(386275, _a_(386274, _n_(386272, "b", lambda: b)[2][_n_(386273, "i", lambda: i)], "configure"), bg= ' grey ' )
            _l_(386276)
            stop_game = True
            _l_(386277)

    if _n_(386280, "states", lambda: states)[0][0]==_n_(386281, "states", lambda: states)[1][1]==_n_(386282, "states", lambda: states)[2][2]!=0:
        _l_(386296)

        _c_(386285, _a_(386284, _n_(386283, "b", lambda: b)[0][0], "configure"), bg= ' grey ' )
        _l_(386286)
        _c_(386289, _a_(386288, _n_(386287, "b", lambda: b)[1][1], "configure"), bg= ' grey ' )
        _l_(386290)
        _c_(386293, _a_(386292, _n_(386291, "b", lambda: b)[2][2], "configure"), bg= ' grey ' )
        _l_(386294)
        stop_game = True
        _l_(386295)

    if _n_(386297, "states", lambda: states)[2][0]==_n_(386298, "states", lambda: states)[1][1]==_n_(386299, "states", lambda: states)[0][2]!=0:
        _l_(386313)

        _c_(386302, _a_(386301, _n_(386300, "b", lambda: b)[2][0], "configure"), bg= ' grey ' )
        _l_(386303)
        _c_(386306, _a_(386305, _n_(386304, "b", lambda: b)[1][1], "configure"), bg= ' grey ' )
        _l_(386307)
        _c_(386310, _a_(386309, _n_(386308, "b", lambda: b)[0][2], "configure"), bg= ' grey ' )
        _l_(386311)
        stop_game = True
        _l_(386312)

root = _c_(386316, _n_(386315, "Tk", lambda: Tk))
_l_(386317)
b = [[0,0,0],
     [0,0,0],
     [0,0,0]]
_l_(386318)

states = [[0,0,0],
          [0,0,0],
          [0,0,0]]
_l_(386319)

for i in _c_(386321, _n_(386320, "range", lambda: range), 3):
    _l_(386345)

    for j in _c_(386323, _n_(386322, "range", lambda: range), 3):
        _l_(386344)

        _n_(386324, "b", lambda: b)[_n_(386325, "i", lambda: i)][_n_(386326, "j", lambda: j)] = _c_(386334, _n_(386327, "Button", lambda: Button), font=( ' Verdana ' , 56), width=3, bg= 'yellow' , command = lambda r=_n_(386328, "i", lambda: i),c=_n_(386329, "j", lambda: j): _c_(386333, _n_(386330, "callback", lambda: callback), _n_(386331, "r", lambda: r),_n_(386332, "c", lambda: c)))
        _l_(386335)
        _c_(386342, _a_(386339, _n_(386336, "b", lambda: b)[_n_(386337, "i", lambda: i)][_n_(386338, "j", lambda: j)], "grid"), row = _n_(386340, "i", lambda: i), column = _n_(386341, "j", lambda: j))
        _l_(386343)

player = ' X '
_l_(386346)
stop_game = False
_l_(386347)

_c_(386349, _n_(386348, "mainloop", lambda: mainloop))
_l_(386350)
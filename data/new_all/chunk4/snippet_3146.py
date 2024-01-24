# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39114176/typeerror-unorderable-types-int-guessing-game
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import*
    _l_(623526)

except ImportError:
    pass
try:
    import random
    _l_(623528)

except ImportError:
    pass

class Application(_n_(623529, "Frame", lambda: Frame)):
    _l_(623673)


    def __init__(self, master):
        _l_(623549)

        _c_(623535, _a_(623533, _n_(623530, "super", lambda: super)(_n_(623531, "Application", lambda: Application), _n_(623532, "self", lambda: self)), "__init__"), _n_(623534, "master", lambda: master))
        _l_(623536)
        _c_(623539, _a_(623538, _n_(623537, "self", lambda: self), "grid"))
        _l_(623540)
        _c_(623543, _a_(623542, _n_(623541, "self", lambda: self), "widgets"))
        _l_(623544)
        _n_(623545, "self", lambda: self).answer = _c_(623547, _n_(623546, "Guessing_game", lambda: Guessing_game), starting_number = 0,
                                    ending_number = 100)
        _l_(623548)

    def widgets(self):
        _l_(623596)


        _c_(623555, _a_(623553, _c_(623552, _n_(623550, "Label", lambda: Label), _n_(623551, "self", lambda: self),
              text = "Hello welcome to new_version of the Guess My Number!"
              ), "grid"), row = 0, column = 0, sticky = _n_(623554, "W", lambda: W))
        _l_(623556)

        _c_(623562, _a_(623560, _c_(623559, _n_(623557, "Label", lambda: Label), _n_(623558, "self", lambda: self),
              text = "Guess the number(0-100):"
              ), "grid"), row = 1, column = 0, sticky = _n_(623561, "W", lambda: W))
        _l_(623563)

        _n_(623564, "self", lambda: self).user_answer = _c_(623567, _n_(623565, "Entry", lambda: Entry), _n_(623566, "self", lambda: self))
        _l_(623568)
        _c_(623573, _a_(623571, _a_(623570, _n_(623569, "self", lambda: self), "user_answer"), "grid"), row = 1, column = 1, sticky = _n_(623572, "W", lambda: W))
        _l_(623574)

        _c_(623582, _a_(623580, _c_(623579, _n_(623575, "Button", lambda: Button), _n_(623576, "self", lambda: self),
               text = "submit",
               command = _a_(623578, _n_(623577, "self", lambda: self), "submit")
               ), "grid"), row = 3, column = 0, sticky = _n_(623581, "W", lambda: W))
        _l_(623583)

        _n_(623584, "self", lambda: self).txt = _c_(623588, _n_(623585, "Text", lambda: Text), _n_(623586, "self", lambda: self), width = 50, height = 20, wrap = _n_(623587, "WORD", lambda: WORD))
        _l_(623589)
        _c_(623594, _a_(623592, _a_(623591, _n_(623590, "self", lambda: self), "txt"), "grid"), row = 4, column = 0, columnspan = 4, sticky = _n_(623593, "W", lambda: W))
        _l_(623595)

    def submit(self):
        _l_(623672)


        user_answer = _c_(623600, _a_(623599, _a_(623598, _n_(623597, "self", lambda: self), "user_answer"), "get"))    
        _l_(623601)    

        if _n_(623602, "user_answer", lambda: user_answer) != None:
            _l_(623607)

            _c_(623605, _n_(623603, "int", lambda: int), _n_(623604, "user_answer", lambda: user_answer)) 
            _l_(623606) 
        if _c_(623610, _n_(623608, "int", lambda: int), _n_(623609, "user_answer", lambda: user_answer)) not in _c_(623612, _n_(623611, "range", lambda: range), 101):
            _l_(623671)

            _c_(623617, _a_(623615, _a_(623614, _n_(623613, "self", lambda: self), "txt"), "delete"), 0.0, _n_(623616, "END", lambda: END))
            _l_(623618)
            _c_(623622, _a_(623621, _a_(623620, _n_(623619, "self", lambda: self), "txt"), "insert"), 0.0, "Your guess is not in proper range")
            _l_(623623)
        elif _c_(623626, _n_(623624, "int", lambda: int), _n_(623625, "user_answer", lambda: user_answer)) > _a_(623628, _n_(623627, "self", lambda: self), "answer"):
            _l_(623670)

            _c_(623633, _a_(623631, _a_(623630, _n_(623629, "self", lambda: self), "txt"), "delete"), 0.0, _n_(623632, "END", lambda: END))
            _l_(623634)
            _c_(623638, _a_(623637, _a_(623636, _n_(623635, "self", lambda: self), "txt"), "insert"), 0.0, "Your guess is higher than the answer")
            _l_(623639)
        elif _c_(623642, _n_(623640, "int", lambda: int), _n_(623641, "user_answer", lambda: user_answer)) < _a_(623644, _n_(623643, "self", lambda: self), "answer"):
            _l_(623669)

            _c_(623649, _a_(623647, _a_(623646, _n_(623645, "self", lambda: self), "txt"), "delete"), 0.0, _n_(623648, "END", lambda: END))
            _l_(623650)
            _c_(623654, _a_(623653, _a_(623652, _n_(623651, "self", lambda: self), "txt"), "insert"), 0.0, "Your guess is lower than the answer")
            _l_(623655)
        else:
            _c_(623660, _a_(623658, _a_(623657, _n_(623656, "self", lambda: self), "txt"), "delete"), 0.0, _n_(623659, "END", lambda: END))
            _l_(623661)
            _c_(623667, _a_(623664, _a_(623663, _n_(623662, "self", lambda: self), "txt"), "insert"), 0.0, "Your guess is right! the number is", _a_(623666, _n_(623665, "self", lambda: self), "answer"))
            _l_(623668)

class Guessing_game(_n_(623674, "object", lambda: object)):
    _l_(623687)

    def __init__(self, starting_number, ending_number):
        _l_(623682)

        _n_(623675, "self", lambda: self).answer = _c_(623680, _a_(623677, _n_(623676, "random", lambda: random), "randint"), _n_(623678, "starting_number", lambda: starting_number),_n_(623679, "ending_number", lambda: ending_number))
        _l_(623681)

    def __str__(self):
        _l_(623686)

        aux = _a_(623684, _n_(623683, "self", lambda: self), "answer")
        _l_(623685)
        return aux
#main
root = _c_(623689, _n_(623688, "Tk", lambda: Tk))
_l_(623690)
app = _c_(623693, _n_(623691, "Application", lambda: Application), _n_(623692, "root", lambda: root))
_l_(623694)
_c_(623697, _a_(623696, _n_(623695, "root", lambda: root), "mainloop"))
_l_(623698)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54161685/dont-understand-why-this-attributeerror-occurs-in-for-loop
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Questions:
    _l_(551488)

    def __init__(self, question, answer):
        _l_(551487)

        _n_(551481, "self", lambda: self).question = _n_(551482, "question", lambda: question)
        _l_(551483)
        _n_(551484, "self", lambda: self).answer = _n_(551485, "answer", lambda: answer)
        _l_(551486)

q_dict = [
    """Q1 Why is it important to scan your target network slowly?\n
    A. To avoid alerting the IDS
    B. It is not necessary to scan the network slowly."""'\n\n\n',

    """Q2 What is the difference between a traditional firewall and an IPS?
    A. Firewalls do not generate logs.
    D. IPS can dissect packets"""'\n\n\n',

    """Q3 What tool is able to conduct a man-in-the-Middle Attack on an 802.3 environment?
    A. Ettercap
    B. Cain & Abel"""'\n\n\n'
]
_l_(551489)

a_dict = [
    _c_(551492, _n_(551490, "Questions", lambda: Questions), _n_(551491, "q_dict", lambda: q_dict)[0], "A"),
    _c_(551495, _n_(551493, "Questions", lambda: Questions), _n_(551494, "q_dict", lambda: q_dict)[1], "D"),
    _c_(551498, _n_(551496, "Questions", lambda: Questions), _n_(551497, "q_dict", lambda: q_dict)[2], "B")
]
_l_(551499)

def start(a_dict):
    _l_(551520)

    points = 0
    _l_(551500)
    for question in _n_(551501, "a_dict", lambda: a_dict):
        _l_(551512)

        answer = _c_(551505, _n_(551502, "input", lambda: input), _a_(551504, _n_(551503, "q_dict", lambda: q_dict), "question"))
        _l_(551506)
        if _n_(551507, "answer", lambda: answer) == _a_(551509, _n_(551508, "a_dict", lambda: a_dict), "answer"):
            _l_(551511)

            points += 10
            _l_(551510)
    _c_(551514, _n_(551513, "print", lambda: print), "You got 10 points")
    _l_(551515)
    _c_(551518, _n_(551516, "print", lambda: print), "Total points: %s" % _n_(551517, "points", lambda: points))
    _l_(551519)

_c_(551523, _n_(551521, "start", lambda: start), _n_(551522, "a_dict", lambda: a_dict))
_l_(551524)
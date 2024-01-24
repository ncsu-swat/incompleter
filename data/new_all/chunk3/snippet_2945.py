# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57480494/how-to-fix-nameerror-name-password-is-not-defined
#Displays what I have learnt so far : Variable assignment, comparision operators, arithmetic operators, value operators, logical operators,

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(553500, _n_(553499, "print", lambda: print), 'Welcome')
_l_(553501)
_c_(553503, _n_(553502, "print", lambda: print), 'Enter Username')
_l_(553504)
username = _c_(553506, _n_(553505, "input", lambda: input))
_l_(553507)
if _n_(553508, "username", lambda: username) == 'Evan' :
    _l_(553515)

    _c_(553510, _n_(553509, "print", lambda: print), 'Enter Password')
    _l_(553511)
else:
    _c_(553513, _n_(553512, "print", lambda: print), 'Wrong Username. Program terminated.')
    _l_(553514)

if _n_(553516, "username", lambda: username) == 'Evan' :
    _l_(553528)

    password = _c_(553518, _n_(553517, "input", lambda: input))
    _l_(553519)
    if _n_(553520, "password", lambda: password) == 'Great' :
        _l_(553527)

        _c_(553522, _n_(553521, "print", lambda: print), 'Additional identification confirmation required.')
        _l_(553523)
    else:
        _c_(553525, _n_(553524, "print", lambda: print), 'Wrong password. Program terminated.')
        _l_(553526)

if _n_(553529, "password", lambda: password) == 'Great':
    _l_(553557)

    _c_(553531, _n_(553530, "print", lambda: print), 'What is your age?')
    _l_(553532)
    years = (27)
    _l_(553533)
    age = _c_(553537, _n_(553534, "int", lambda: int), _c_(553536, _n_(553535, "input", lambda: input)))
    _l_(553538)
    if _n_(553539, "age", lambda: age) < _n_(553540, "years", lambda: years) :
        _l_(553556)

        _c_(553542, _n_(553541, "print", lambda: print), 'Seriously?')
        _l_(553543)
    elif _n_(553544, "age", lambda: age) > _n_(553545, "years", lambda: years) :
        _l_(553555)

        _c_(553547, _n_(553546, "print", lambda: print), '-_-"')
        _l_(553548)
    else:
        _n_(553549, "age", lambda: age) == _n_(553550, "years", lambda: years)
        _l_(553551)
        _c_(553553, _n_(553552, "print", lambda: print), 'Welcome Evan!')
        _l_(553554)

if _n_(553558, "age", lambda: age) == _n_(553559, "years", lambda: years):
    _l_(553576)

    _c_(553561, _n_(553560, "print", lambda: print), 'Name one of the RGB colours.')
    _l_(553562)
    rgb = 'Red' or 'Green' or 'Blue'
    _l_(553563)
    colours = _c_(553565, _n_(553564, "input", lambda: input))
    _l_(553566)
    if _n_(553567, "colours", lambda: colours) == _n_(553568, "rgb", lambda: rgb) :
        _l_(553575)

        _c_(553570, _n_(553569, "print", lambda: print), 'Good')
        _l_(553571)
    else:
        _c_(553573, _n_(553572, "print", lambda: print), 'Wrong Answer')
        _l_(553574)

if _n_(553577, "age", lambda: age) == _n_(553578, "years", lambda: years) :
    _l_(553586)

    _c_(553580, _n_(553579, "print", lambda: print), 'Type Rock & Roll.')
    _l_(553581)
    answer = 'Rock & Roll'
    _l_(553582)
    ans = _c_(553584, _n_(553583, "input", lambda: input))
    _l_(553585)
if _n_(553587, "ans", lambda: ans) != _n_(553588, "answer", lambda: answer) :
    _l_(553595)

    _c_(553590, _n_(553589, "print", lambda: print), 'Learn to type.')
    _l_(553591)
else:
    _c_(553593, _n_(553592, "print", lambda: print), 'Good job!')
    _l_(553594)

if _n_(553596, "age", lambda: age) == _n_(553597, "years", lambda: years):
    _l_(553601)

    _c_(553599, _n_(553598, "print", lambda: print), 'Let me show you some math for entertainment :D')
    _l_(553600)
result = '= '
_l_(553602)
_c_(553604, _n_(553603, "print", lambda: print), '2+2')
_l_(553605)
_c_(553612, _n_(553606, "print", lambda: print), _n_(553607, "result", lambda: result) + _c_(553611, _n_(553608, "str", lambda: str), _c_(553610, _n_(553609, "int", lambda: int), 2+2)))
_l_(553613)
_c_(553615, _n_(553614, "print", lambda: print), '')
_l_(553616)
_c_(553618, _n_(553617, "print", lambda: print), '3 - 2')
_l_(553619)
_c_(553626, _n_(553620, "print", lambda: print), _n_(553621, "result", lambda: result) + _c_(553625, _n_(553622, "str", lambda: str), _c_(553624, _n_(553623, "int", lambda: int), 3-2)))
_l_(553627)
_c_(553629, _n_(553628, "print", lambda: print), '')
_l_(553630)
_c_(553632, _n_(553631, "print", lambda: print), '2 x 2')
_l_(553633)
_c_(553640, _n_(553634, "print", lambda: print), _n_(553635, "result", lambda: result) + _c_(553639, _n_(553636, "str", lambda: str), _c_(553638, _n_(553637, "int", lambda: int), 2*2)))
_l_(553641)
_c_(553643, _n_(553642, "print", lambda: print), '')
_l_(553644)
_c_(553646, _n_(553645, "print", lambda: print), '7 / 3')
_l_(553647)
_c_(553649, _n_(553648, "print", lambda: print), 7/3)
_l_(553650)
_c_(553652, _n_(553651, "print", lambda: print), '')
_l_(553653)
_c_(553655, _n_(553654, "print", lambda: print), '3 modulus 7')
_l_(553656)
_c_(553663, _n_(553657, "print", lambda: print), _n_(553658, "result", lambda: result) + _c_(553662, _n_(553659, "str", lambda: str), _c_(553661, _n_(553660, "int", lambda: int), 3%7)))
_l_(553664)
_c_(553666, _n_(553665, "print", lambda: print), '')
_l_(553667)
_c_(553669, _n_(553668, "print", lambda: print), '2 exponent 10')
_l_(553670)
_c_(553677, _n_(553671, "print", lambda: print), _n_(553672, "result", lambda: result) + _c_(553676, _n_(553673, "str", lambda: str), _c_(553675, _n_(553674, "int", lambda: int), 2**10)))
_l_(553678)
_c_(553680, _n_(553679, "print", lambda: print), '')
_l_(553681)
_c_(553683, _n_(553682, "print", lambda: print), '23 floor division 9')
_l_(553684)
_c_(553691, _n_(553685, "print", lambda: print), _n_(553686, "result", lambda: result) + _c_(553690, _n_(553687, "str", lambda: str), _c_(553689, _n_(553688, "int", lambda: int), 23//9)))
_l_(553692)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40901405/yielding-a-typeerror-input-expected-at-most-1-arguments-got-4-this-error-was
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def randomLetters():
    _l_(681858)

    numbers = [_c_(681845, _a_(681844, _n_(681843, "random", lambda: random), "randint"), 0, 25), _c_(681848, _a_(681847, _n_(681846, "random", lambda: random), "randint"), 0, 25)]
    _l_(681849)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    _l_(681850)
    letters = [_n_(681851, "alphabet", lambda: alphabet)[_n_(681852, "numbers", lambda: numbers)[0]], _n_(681853, "alphabet", lambda: alphabet)[_n_(681854, "numbers", lambda: numbers)[1]]]
    _l_(681855)
    aux = _n_(681856, "letters", lambda: letters)
    _l_(681857)
    return aux

letters = _c_(681860, _n_(681859, "randomLetters", lambda: randomLetters))
_l_(681861)
_c_(681864, _n_(681862, "print", lambda: print), _n_(681863, "letters", lambda: letters))
_l_(681865)
_c_(681868, _n_(681866, "print", lambda: print), _n_(681867, "letters", lambda: letters)[0])
_l_(681869)
user_input = _c_(681873, _n_(681870, "input", lambda: input), 'Enter a word that begins with', "'" + _n_(681871, "letters", lambda: letters)[0] + "'", 'and ends with', "'" + _n_(681872, "letters", lambda: letters)[1] + "': ")
_l_(681874)
new_user_input = _c_(681877, _a_(681876, _n_(681875, "user_input", lambda: user_input), "lower"))
_l_(681878)

while (_n_(681879, "new_user_input", lambda: new_user_input)[0] != _n_(681880, "letters", lambda: letters)[0]) and (_n_(681881, "new_user_input", lambda: new_user_input)[_c_(681884, _n_(681882, "len", lambda: len), _n_(681883, "new_user_input", lambda: new_user_input)) - 1] != _n_(681885, "letters", lambda: letters)[1]):
    _l_(681894)

    _c_(681887, _n_(681886, "print", lambda: print), 'Invalid input. Try again.')
    _l_(681888)
    new_user_input = _c_(681892, _n_(681889, "input", lambda: input), 'Enter a word that begins with', "'" + _n_(681890, "letters", lambda: letters)[0] + "'", 'and ends with', "'" + _n_(681891, "letters", lambda: letters)[1] + "': ")
    _l_(681893)
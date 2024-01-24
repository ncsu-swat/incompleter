# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55066562/getting-error-typeerror-nonetype-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def user_test():
    _l_(443614)

    '''
    :return: hold user input
    '''
    _l_(443589)
    global user_string
    _l_(443590)
    global user_character
    _l_(443591)
    user_string = _c_(443595, _n_(443592, "print", lambda: print), _c_(443594, _n_(443593, "input", lambda: input), "What is the string you would like to use:"))
    _l_(443596)
    user_character = _c_(443600, _n_(443597, "print", lambda: print), _c_(443599, _n_(443598, "input", lambda: input), "What is the character you would like to use:"))
    _l_(443601)
    _c_(443605, _n_(443602, "character_count", lambda: character_count), _n_(443603, "user_string", lambda: user_string), _n_(443604, "user_character", lambda: user_character))
    _l_(443606)
    _c_(443609, _n_(443607, "reverse", lambda: reverse), _n_(443608, "user_string", lambda: user_string))
    _l_(443610)
    aux = _n_(443611, "user_string", lambda: user_string), _n_(443612, "user_character", lambda: user_character)
    _l_(443613)
    return aux

def reverse(user_string):
    _l_(443628)

    '''
    :param: string
    :return: reverses a string
    '''
    _l_(443615)
    string = _n_(443616, "user_string", lambda: user_string)
    _l_(443617)
    _c_(443624, _n_(443618, "print", lambda: print), _c_(443623, _n_(443619, "list", lambda: list), _c_(443622, _n_(443620, "reversed", lambda: reversed), _n_(443621, "string", lambda: string))))
    _l_(443625)
    aux = _n_(443626, "string", lambda: string)
    _l_(443627)
    return aux

def character_count(user_string, user_character):
    _l_(443645)

    '''
    :return: counts the number of occurances of a character in a string
    '''
    _l_(443629)
    string = _n_(443630, "user_string", lambda: user_string)
    _l_(443631)
    toCount = _n_(443632, "user_character", lambda: user_character)
    _l_(443633)
    counter = 0
    _l_(443634)

    for letter in _n_(443635, "string", lambda: string):
        _l_(443640)

        if( _n_(443636, "letter", lambda: letter) == _n_(443637, "toCount", lambda: toCount)):
            _l_(443639)

            counter += 1
            _l_(443638)
    _c_(443643, _n_(443641, "print", lambda: print), _n_(443642, "counter", lambda: counter))
    _l_(443644)

def main():
    _l_(443649)

    _c_(443647, _n_(443646, "user_test", lambda: user_test))
    _l_(443648)


_c_(443651, _n_(443650, "main", lambda: main))
_l_(443652)
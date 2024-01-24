# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64532267/typeerror-init-missing-4-required-positional-arguments
#! usr/bin/python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(373514)

except ImportError:
    pass
try:
    import random
    _l_(373516)

except ImportError:
    pass

_c_(373518, _n_(373517, "print", lambda: print), "HI WELCOME TO HANGMAN !")
_l_(373519)
_c_(373521, _n_(373520, "print", lambda: print), "\n")
_l_(373522)
_c_(373525, _a_(373524, _n_(373523, "time", lambda: time), "sleep"), 1.5)
_l_(373526)
name = _c_(373528, _n_(373527, "input", lambda: input), "Enter your name :")
_l_(373529)
_c_(373531, _n_(373530, "print", lambda: print), "\n")
_l_(373532)
_c_(373535, _n_(373533, "print", lambda: print), "HEY " + _n_(373534, "name", lambda: name) + " HOPE YOU HAVE A GOOD TIME PLAYING HANGMAN TODAY")
_l_(373536)
_c_(373538, _n_(373537, "print", lambda: print), "\n")
_l_(373539)
_c_(373542, _a_(373541, _n_(373540, "time", lambda: time), "sleep"), 1.5)
_l_(373543)
_c_(373545, _n_(373544, "print", lambda: print), "YOUR GAME IS ABOUT TO BEGIN IN A FEW SECONDS")
_l_(373546)
_c_(373549, _a_(373548, _n_(373547, "time", lambda: time), "sleep"), 1)
_l_(373550)


class Hangman():
    _l_(373793)

    def __init__(self, word, guesses, count, limit) :
        _l_(373576)

        _n_(373551, "self", lambda: self).count = _n_(373552, "count", lambda: count)
        _l_(373553)
        _n_(373554, "self", lambda: self).display= "_" * _a_(373556, _n_(373555, "self", lambda: self), "length") 
        _l_(373557) 
        _n_(373558, "self", lambda: self).word = _n_(373559, "word", lambda: word) 
        _l_(373560) 
        _n_(373561, "self", lambda: self).length = _c_(373564, _n_(373562, "len", lambda: len), _n_(373563, "word", lambda: word))
        _l_(373565)
        _n_(373566, "self", lambda: self).guessed = []
        _l_(373567)
        _n_(373568, "self", lambda: self).guesses = _n_(373569, "guesses", lambda: guesses)
        _l_(373570)
        _n_(373571, "self", lambda: self).Continue = ""
        _l_(373572)
        _n_(373573, "self", lambda: self).limit = _n_(373574, "limit", lambda: limit)
        _l_(373575)

    def get_word(self):
        _l_(373584)

        words = ["book" ,"paper", "computer", "movie", "mouse", "laptop", "national"]
        _l_(373577)
        _n_(373578, "self", lambda: self).word = _c_(373582, _a_(373580, _n_(373579, "random", lambda: random), "choice"), _n_(373581, "words", lambda: words))
        _l_(373583)
    
    def play_loop(self):
        _l_(373604)

        _n_(373585, "self", lambda: self).Continue = _c_(373587, _n_(373586, "input", lambda: input), "Do you wish to play another round? y = yes, n = no")
        _l_(373588)
        if _a_(373590, _n_(373589, "self", lambda: self), "Continue") == 'y':
            _l_(373603)

            _c_(373592, _n_(373591, "Hangman", lambda: Hangman))
            _l_(373593)
        elif _a_(373595, _n_(373594, "self", lambda: self), "Continue") == "n":
            _l_(373602)

            _c_(373597, _n_(373596, "print", lambda: print), "thanks for playing! hope you had a good time :)")
            _l_(373598)
            aux = ""
            _l_(373601)
            exit(aux)

    def play(self,guesses):
        _l_(373792)

        _n_(373605, "self", lambda: self).count = 5
        _l_(373606)
        _c_(373610, _n_(373607, "print", lambda: print), "your word is " + _a_(373609, _n_(373608, "self", lambda: self), "word") + "enter your guesses ")
        _l_(373611)
        _n_(373612, "self", lambda: self).guesses = _c_(373615, _a_(373614, _n_(373613, "guesses", lambda: guesses), "strip"))
        _l_(373616)
        if _c_(373621, _n_(373617, "len", lambda: len), _c_(373620, _a_(373619, _n_(373618, "guesses", lambda: guesses), "strip"))) == 0:
            _l_(373683)

            _c_(373623, _n_(373622, "print", lambda: print), "Invalid input, please enter a letter \n")
            _l_(373624)
        elif _c_(373629, _n_(373625, "len", lambda: len), _c_(373628, _a_(373627, _n_(373626, "guesses", lambda: guesses), "strip"))) >=2:
            _l_(373682)

            _c_(373631, _n_(373630, "print", lambda: print), "Invalid input, please enter one letter at a time \n")
            _l_(373632)

        elif _a_(373634, _n_(373633, "self", lambda: self), "guesses") in _a_(373636, _n_(373635, "self", lambda: self), "word") :
            _l_(373681)

            _c_(373642, _a_(373639, _a_(373638, _n_(373637, "self", lambda: self), "guessed"), "extend"), _a_(373641, _n_(373640, "self", lambda: self), "guesses"))
            _l_(373643)
            _n_(373644, "self", lambda: self).index = _c_(373650, _a_(373647, _a_(373646, _n_(373645, "self", lambda: self), "word"), "find"), _a_(373649, _n_(373648, "self", lambda: self), "guesses"))
            _l_(373651)
            _n_(373652, "self", lambda: self).word = _a_(373654, _n_(373653, "self", lambda: self), "word")[_a_(373656, _n_(373655, "self", lambda: self), "index")] + '_' + _a_(373658, _n_(373657, "self", lambda: self), "word")[_a_(373660, _n_(373659, "self", lambda: self), "index") + 1]
            _l_(373661)
            _n_(373662, "self", lambda: self).display = _a_(373664, _n_(373663, "self", lambda: self), "display")[:_a_(373666, _n_(373665, "self", lambda: self), "index")] + _a_(373668, _n_(373667, "self", lambda: self), "guesses") + _a_(373670, _n_(373669, "self", lambda: self), "display")[:_a_(373672, _n_(373671, "self", lambda: self), "index") + 1]
            _l_(373673)
            _c_(373677, _n_(373674, "print", lambda: print), _a_(373676, _n_(373675, "self", lambda: self), "display") + "\n")
            _l_(373678)

        else:
            _n_(373679, "self", lambda: self).count +=1
            _l_(373680)

        if _a_(373685, _n_(373684, "self", lambda: self), "count") == 1:
            _l_(373772)

            _c_(373688, _a_(373687, _n_(373686, "time", lambda: time), "sleep"), 1)
            _l_(373689)
            _c_(373691, _n_(373690, "print", lambda: print), "   _____ \n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                   "__|__\n")
            _l_(373692)
            _c_(373700, _n_(373693, "print", lambda: print), " wrong guess,you have" + _c_(373699, _n_(373694, "str", lambda: str), _a_(373696, _n_(373695, "self", lambda: self), "limit") - _a_(373698, _n_(373697, "self", lambda: self), "count")) + "guesses remaining")
            _l_(373701)
        
        elif _a_(373703, _n_(373702, "self", lambda: self), "count") == 2:
            _l_(373771)

            _c_(373706, _a_(373705, _n_(373704, "time", lambda: time), "sleep"), 1)
            _l_(373707)
            _c_(373709, _n_(373708, "print", lambda: print), "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
            _l_(373710)
            _c_(373718, _n_(373711, "print", lambda: print), "wrong guess, you have " + _c_(373717, _n_(373712, "str", lambda: str), _a_(373714, _n_(373713, "self", lambda: self), "limit") - _a_(373716, _n_(373715, "self", lambda: self), "count")) + "guesses remaining")
            _l_(373719)

        elif _a_(373721, _n_(373720, "self", lambda: self), "count") == 3:
            _l_(373770)

            _c_(373724, _a_(373723, _n_(373722, "time", lambda: time), "sleep"), 1)
            _l_(373725)
            _c_(373727, _n_(373726, "print", lambda: print), "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
            _l_(373728)
            _c_(373730, _n_(373729, "print", lambda: print), "wrong guess, you have") + _c_(373736, _n_(373731, "str", lambda: str), _a_(373733, _n_(373732, "self", lambda: self), "limit") - _a_(373735, _n_(373734, "self", lambda: self), "count")) + "guesses remaining"
            _l_(373737)

        elif _a_(373739, _n_(373738, "self", lambda: self), "count") == 4:
            _l_(373769)

            _c_(373742, _a_(373741, _n_(373740, "time", lambda: time), "sleep"), 1)
            _l_(373743)
            _c_(373745, _n_(373744, "print", lambda: print), "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
            _l_(373746)

        elif _a_(373748, _n_(373747, "self", lambda: self), "count") == 5:
            _l_(373768)

            _c_(373751, _a_(373750, _n_(373749, "time", lambda: time), "sleep"), 1)
            _l_(373752)
            _c_(373754, _n_(373753, "print", lambda: print), "   _____ \n"
                "  |     | \n"
                "  |     |\n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |    / \ \n"
                "__|__\n")
            _l_(373755)
            _c_(373757, _n_(373756, "print", lambda: print), "wrong guesses, you are hanged!")
            _l_(373758)
            _c_(373762, _n_(373759, "print", lambda: print), "the word was" , _a_(373761, _n_(373760, "self", lambda: self), "word"))
            _l_(373763)
            _c_(373766, _a_(373765, _n_(373764, "Hangman", lambda: Hangman), "play_loop"))
            _l_(373767)

        if _a_(373774, _n_(373773, "self", lambda: self), "display"):
            _l_(373791)

            _c_(373776, _n_(373775, "print", lambda: print), "congrats you won !")
            _l_(373777)
            _c_(373780, _a_(373779, _n_(373778, "Hangman", lambda: Hangman), "play_loop"))
            _l_(373781)
        elif _a_(373783, _n_(373782, "self", lambda: self), "count") != _a_(373785, _n_(373784, "self", lambda: self), "limit"):
            _l_(373790)

            _c_(373788, _a_(373787, _n_(373786, "Hangman", lambda: Hangman), "play_loop"))
            _l_(373789)

Hangman_game = _c_(373795, _n_(373794, "Hangman", lambda: Hangman))
_l_(373796)
_c_(373798, _n_(373797, "Hangman_game", lambda: Hangman_game))   
_l_(373799)   
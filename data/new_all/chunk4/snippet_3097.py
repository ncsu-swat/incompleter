# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46612281/python-3-rock-paper-scissors-game-nameerror-name-computer-choice-rock-is-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(599030)

except ImportError:
    pass

def rps():
    _l_(599048)

    computer_choice = _c_(599033, _a_(599032, _n_(599031, "random", lambda: random), "randint"), 1,3)
    _l_(599034)
    if _n_(599035, "computer_choice", lambda: computer_choice) == 1:
        _l_(599047)

        _c_(599037, _n_(599036, "comuter_choice_rock", lambda: comuter_choice_rock))
        _l_(599038)
    elif _n_(599039, "computer_choice", lambda: computer_choice) == 2:
        _l_(599046)

        _c_(599041, _n_(599040, "comuter_choice_paper", lambda: comuter_choice_paper))
        _l_(599042)
    else:
        _c_(599044, _n_(599043, "comuter_choice_scissors", lambda: comuter_choice_scissors))
        _l_(599045)

def computer_choice_rock():
    _l_(599082)

    user_choice = _c_(599050, _n_(599049, "input", lambda: input), "1 for Rock, 2 for Paper, 3 for Scissors: ")
    _l_(599051)
    if _n_(599052, "user_choice", lambda: user_choice) == "1":
        _l_(599059)

        _c_(599054, _n_(599053, "print", lambda: print), "It's a Tie!")
        _l_(599055)
        _c_(599057, _n_(599056, "try_again", lambda: try_again))
        _l_(599058)
    if _n_(599060, "user_choice", lambda: user_choice) == "2":
        _l_(599067)

        _c_(599062, _n_(599061, "print", lambda: print), "You Win! Paper covers Rock!")
        _l_(599063)
        _c_(599065, _n_(599064, "try_again", lambda: try_again))
        _l_(599066)
    if _n_(599068, "user_choice", lambda: user_choice) == "3":
        _l_(599081)

        _c_(599070, _n_(599069, "print", lambda: print), "I Win and You Lose! Rock crushes Scissors!")
        _l_(599071)
        _c_(599073, _n_(599072, "try_again", lambda: try_again))
        _l_(599074)
    else:
        _c_(599076, _n_(599075, "print", lambda: print), "Please type in 1, 2, or 3")
        _l_(599077)
        _c_(599079, _n_(599078, "computer_choice_rock", lambda: computer_choice_rock))
        _l_(599080)

def computer_choice_paper():
    _l_(599116)

    user_choice = _c_(599084, _n_(599083, "input", lambda: input), "1 for Rock, 2 for Paper, 3 for Scissors: ")
    _l_(599085)
    if _n_(599086, "user_choice", lambda: user_choice) == "1":
        _l_(599093)

        _c_(599088, _n_(599087, "print", lambda: print), "I Win and You Lose! Paper covers Rock!")
        _l_(599089)
        _c_(599091, _n_(599090, "try_again", lambda: try_again))
        _l_(599092)
    if _n_(599094, "user_choice", lambda: user_choice) == "2":
        _l_(599101)

        _c_(599096, _n_(599095, "print", lambda: print), "It's a Tie!")
        _l_(599097)
        _c_(599099, _n_(599098, "try_again", lambda: try_again))
        _l_(599100)
    if _n_(599102, "user_choice", lambda: user_choice) == "3":
        _l_(599115)

        _c_(599104, _n_(599103, "print", lambda: print), "You Win! Scissors cut Paper!")
        _l_(599105)
        _c_(599107, _n_(599106, "try_again", lambda: try_again))
        _l_(599108)
    else:
        _c_(599110, _n_(599109, "print", lambda: print), "Please type in 1, 2, or 3")
        _l_(599111)
        _c_(599113, _n_(599112, "computer_choice_paper", lambda: computer_choice_paper))
        _l_(599114)

def computer_choice_paper():
    _l_(599150)

    user_choice = _c_(599118, _n_(599117, "input", lambda: input), "1 for Rock, 2 for Paper, 3 for Scissors: ")
    _l_(599119)
    if _n_(599120, "user_choice", lambda: user_choice) == ("1"):
        _l_(599127)

        _c_(599122, _n_(599121, "print", lambda: print), "You Win! Rock crushes Scissors")
        _l_(599123)
        _c_(599125, _n_(599124, "try_again", lambda: try_again))
        _l_(599126)
    if _n_(599128, "user_choice", lambda: user_choice) == "2":
        _l_(599135)

        _c_(599130, _n_(599129, "print", lambda: print), "I Win! Scissors cut Paper!")
        _l_(599131)
        _c_(599133, _n_(599132, "try_again", lambda: try_again))
        _l_(599134)
    if _n_(599136, "user_choice", lambda: user_choice) == "3":
        _l_(599149)

        _c_(599138, _n_(599137, "print", lambda: print), "It's a Tie!")
        _l_(599139)
        _c_(599141, _n_(599140, "try_again", lambda: try_again))
        _l_(599142)
    else:
        _c_(599144, _n_(599143, "print", lambda: print), "Please type in 1, 2, or 3")
        _l_(599145)
        _c_(599147, _n_(599146, "computer_choice_paper", lambda: computer_choice_paper))
        _l_(599148)

def try_again():
    _l_(599179)

    choice = _c_(599152, _n_(599151, "input", lambda: input), "Would you like to play again? Y/N: ")
    _l_(599153)
    if _n_(599154, "choice", lambda: choice) == "Y" or _n_(599155, "choice", lambda: choice) == "y" or _n_(599156, "choice", lambda: choice) == "Yes" or _n_(599157, "choice", lambda: choice) == "yes":
        _l_(599178)

        _c_(599159, _n_(599158, "rps", lambda: rps))
        _l_(599160)
    elif _n_(599161, "choice", lambda: choice) == "n" or _n_(599162, "choice", lambda: choice) == "N" or _n_(599163, "choice", lambda: choice) == "No" or _n_(599164, "choice", lambda: choice) == "no":
        _l_(599177)

        _c_(599166, _n_(599165, "print", lambda: print), "Thanks for Playing!")
        _l_(599167)
        _c_(599169, _n_(599168, "quit", lambda: quit))
        _l_(599170)
    else:
        _c_(599172, _n_(599171, "print", lambda: print), "Please type Y or N")
        _l_(599173)
        _c_(599175, _n_(599174, "try_again", lambda: try_again))
        _l_(599176)

_c_(599181, _n_(599180, "rps", lambda: rps))
_l_(599182)
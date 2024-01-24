# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50048804/name-error-in-python3-when-name-is-defined
#Module 4 project
#4/25/18
#Henry Degner
#This project is meant to determine whether or not certain people are qualified to go to an exclusive concert

#create function askAge, which will use an input statement and comparison operators to see if the user is old enough
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def askAge():
    _l_(461733)

    age = _c_(461717, _n_(461714, "int", lambda: int), _c_(461716, _n_(461715, "input", lambda: input), "How old are you? "))
    _l_(461718)
    if( _n_(461719, "age", lambda: age) >= 18 ):
        _l_(461732)

        ageReq = "true"
        _l_(461720)
    elif( _n_(461721, "age", lambda: age) < 18 ):
        _l_(461731)

        ageReq = "false"
        _l_(461722)
    else:
        _c_(461724, _n_(461723, "print", lambda: print), "Please print you're age with only numerical characters, in years")
        _l_(461725)
        age = _c_(461729, _n_(461726, "int", lambda: int), _c_(461728, _n_(461727, "input", lambda: input), "How old are you? "))
        _l_(461730)
#create function askHearing, yes or no question to do you have sensitive hearing
def askHearing():
    _l_(461757)

    hearing = _c_(461737, _n_(461734, "str", lambda: str), _c_(461736, _n_(461735, "input", lambda: input), "Do you have sensitive hearing? "))
    _l_(461738)
    if( _c_(461741, _n_(461739, "str", lambda: str), _n_(461740, "hearing", lambda: hearing)) == "yes","y" ):
        _l_(461756)

        hearingReq = "do"
        _l_(461742)
    elif( _c_(461745, _n_(461743, "str", lambda: str), _n_(461744, "hearing", lambda: hearing)) == "no","n"):
        _l_(461755)

        hearingReq = "don't"
        _l_(461746)
    else:
        _c_(461748, _n_(461747, "print", lambda: print), "Please type yes, or y, if you have sensitivehearing. If not, type no or n.")
        _l_(461749)
        hearing = _c_(461753, _n_(461750, "str", lambda: str), _c_(461752, _n_(461751, "input", lambda: input), "Do you have sensitive hearing? "))
        _l_(461754)
#create function askTicket, yes or no question to do you have a ticket
def askTicket():
    _l_(461781)

    ticket = _c_(461761, _n_(461758, "str", lambda: str), _c_(461760, _n_(461759, "input", lambda: input), "Do you have a ticket for the concert? "))
    _l_(461762)
    if( _c_(461765, _n_(461763, "str", lambda: str), _n_(461764, "ticket", lambda: ticket)) == "yes","y" ):
        _l_(461780)

        ticketReq = "do"
        _l_(461766)
    elif( _c_(461769, _n_(461767, "str", lambda: str), _n_(461768, "ticket", lambda: ticket)) == "no","n"):
        _l_(461779)

        ticketReq = "don't"
        _l_(461770)
    else:
        _c_(461772, _n_(461771, "print", lambda: print), "Please type yes if you have a ticket, or no if you don't.")
        _l_(461773)
        ticketReq = _c_(461777, _n_(461774, "str", lambda: str), _c_(461776, _n_(461775, "input", lambda: input), "Do you have a ticket for the concert"))
        _l_(461778)
#create function askFun, yes or no question to are you willing to have an awesome time
def askFun():
    _l_(461805)

    fun = _c_(461785, _n_(461782, "str", lambda: str), _c_(461784, _n_(461783, "input", lambda: input), "Are you willing to have a great time?"))
    _l_(461786)
    if( _c_(461789, _n_(461787, "str", lambda: str), _n_(461788, "fun", lambda: fun)) == "yes","y"):
        _l_(461804)

        funReq = "do"
        _l_(461790)
    elif( _c_(461793, _n_(461791, "str", lambda: str), _n_(461792, "fun", lambda: fun)) == "no","n" ):
        _l_(461803)

        funReq = "don't"
        _l_(461794)
    else:
        _c_(461796, _n_(461795, "print", lambda: print), "Please type 'yes' or 'no'")
        _l_(461797)
        fun = _c_(461801, _n_(461798, "str", lambda: str), _c_(461800, _n_(461799, "input", lambda: input), "Are you willing to have a great time?"))
        _l_(461802)
#use def main():
def main():
    _l_(461828)

#print situation, will ask some questions to see if you can attend concert
    _c_(461807, _n_(461806, "print", lambda: print), "Welcome to the Henry Degner Concert Venue! We have to ask you a few questions before we let you into the venue.")
    _l_(461808)
#use askAge
    _c_(461810, _n_(461809, "askAge", lambda: askAge))
    _l_(461811)
#use askHearing
    _c_(461813, _n_(461812, "askHearing", lambda: askHearing))
    _l_(461814)
#use askTicket
    _c_(461816, _n_(461815, "askTicket", lambda: askTicket))
    _l_(461817)
#use askFun
    _c_(461819, _n_(461818, "askFun", lambda: askFun))
    _l_(461820)
#print user's answers
    _c_(461826, _n_(461821, "print", lambda: print), "You said you are " + _n_(461822, "age", lambda: age) + " years old, you " + _n_(461823, "hearingReq", lambda: hearingReq) + " have sensitive hearing, you " + _n_(461824, "ticketReq", lambda: ticketReq) + " have a ticket, and you " + _n_(461825, "funReq", lambda: funReq) + " want to have a great time!")
    _l_(461827)
#use if-else statement, if all three conditions match requirements, print you can attend concert. If not, print you can't attend

#use main()
_c_(461830, _n_(461829, "main", lambda: main))
_l_(461831)
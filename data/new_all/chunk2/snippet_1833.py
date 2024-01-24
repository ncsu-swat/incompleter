# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51412753/attributeerror-str-object-has-no-attribute-timeud-variable-calling
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import timelines
    _l_(426635)

except ImportError:
    pass
#x(forward-back) Axies
global x
_l_(426636)
x = 0
_l_(426637)
#y(left-right) Axies
global y
_l_(426638)
y = 0
_l_(426639)
#z(up) Axies
global z
_l_(426640)
z = 0
_l_(426641)
#t(time) Axies
global t
_l_(426642)
t = 0
_l_(426643)
#u(universe) Axies
global u
_l_(426644)
u = 1
_l_(426645)
#how much time moves by per-turn, string
global time_change
_l_(426646)
time_change = 'doggos'
_l_(426647)
#the timeline, nets of exctinction
timelines = 'Universal Development\nSolar Development\nPlanetary Development\nEvolution\nIntelligence\nContinental Drift\nSpeech\nReligion/Beliefs\nAgriculture\nTechnological Innovation\nSocial Politics\nCommunities\nCivilizations\nWar/Conflicts\nEconomy\nLaw\n----------------------------------------------'
_l_(426648)
global loop
_l_(426649)
def checkAction():
    _l_(426669)

    ca_loop = 1
    _l_(426650)
    while( _n_(426651, "ca_loop", lambda: ca_loop) == 1 ):
        _l_(426668)

        if _n_(426652, "turn_action", lambda: turn_action) == 'timeline':
            _l_(426667)

            which_timeline = _c_(426655, _n_(426653, "input", lambda: input), "What timeline would you like to view?\n----------------------------------------------\n" + _n_(426654, "timelines", lambda: timelines) + "\n[Timelines]~| ")
            _l_(426656)
            if _n_(426657, "which_timeline", lambda: which_timeline) == "Universal Development":
                _l_(426666)

                _c_(426661, _n_(426658, "print", lambda: print), _a_(426660, _n_(426659, "timelines", lambda: timelines), "TimeUD"))
                _l_(426662)
            else:
                _c_(426664, _n_(426663, "print", lambda: print), "~|Improper Input|~\n")
                _l_(426665)
def turn1( tc ):
    _l_(426693)

    t = 0
    _l_(426670)
    global turn_action
    _l_(426671)
    while ( _n_(426672, "loop", lambda: loop) == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 ):
        _l_(426692)

        t = _n_(426673, "t", lambda: t) + _n_(426674, "tc", lambda: tc)
        _l_(426675)
        _c_(426681, _n_(426676, "print", lambda: print), "The current " + _n_(426677, "time_change", lambda: time_change) + "s is " + _c_(426680, _n_(426678, "str", lambda: str), _n_(426679, "t", lambda: t)))
        _l_(426682)
        turn_action = _c_(426684, _n_(426683, "input", lambda: input), "~| ")
        _l_(426685)
        _c_(426687, _n_(426686, "checkAction", lambda: checkAction))
        _l_(426688)
        _c_(426690, _n_(426689, "input", lambda: input), "~|Press enter to continue to the next Time-Period|~")
        _l_(426691)

loop_select = 1
_l_(426694)
while ( _n_(426695, "loop_select", lambda: loop_select) == 1 ):
    _l_(426767)

    loop = _c_(426699, _n_(426696, "int", lambda: int), _c_(426698, _n_(426697, "input", lambda: input), "~|Choose a time-change per turn|~\n\n~| "))
    _l_(426700)
    if _n_(426701, "loop", lambda: loop) == 1:
        _l_(426766)

        _c_(426703, _n_(426702, "print", lambda: print), "The time-change is set to miliseconds.\n\n")
        _l_(426704)
        time_change = 'Milisecond'
        _l_(426705)
        loop_select = 0
        _l_(426706)
    elif _n_(426707, "loop", lambda: loop) == 2:
        _l_(426765)

        _c_(426709, _n_(426708, "print", lambda: print), "The time-change is set to seconds.\n\n")
        _l_(426710)
        time_change = 'Second'
        _l_(426711)
        loop_select = 0
        _l_(426712)
    elif _n_(426713, "loop", lambda: loop) == 3:
        _l_(426764)

        _c_(426715, _n_(426714, "print", lambda: print), "The time-change is set to minutes.\n\n")
        _l_(426716)
        time_change = 'Minute'
        _l_(426717)
        loop_select = 0
        _l_(426718)
    elif _n_(426719, "loop", lambda: loop) == 4:
        _l_(426763)

        _c_(426721, _n_(426720, "print", lambda: print), "The time-change is set to hours.\n\n")
        _l_(426722)
        time_change = 'Hour'
        _l_(426723)
        loop_select = 0
        _l_(426724)
    elif _n_(426725, "loop", lambda: loop) == 5:
        _l_(426762)

        _c_(426727, _n_(426726, "print", lambda: print), "The time-change is set to days.\n\n")
        _l_(426728)
        time_change = 'Day'
        _l_(426729)
        loop_select = 0
        _l_(426730)
    elif _n_(426731, "loop", lambda: loop) == 6:
        _l_(426761)

        _c_(426733, _n_(426732, "print", lambda: print), "The time-change is set to months.\n\n")
        _l_(426734)
        time_change = 'Month'
        _l_(426735)
        loop_select = 0
        _l_(426736)
    elif _n_(426737, "loop", lambda: loop) == 7:
        _l_(426760)

        _c_(426739, _n_(426738, "print", lambda: print), "The time-change is set to years.\n\n")
        _l_(426740)
        time_change = 'Year'
        _l_(426741)
        loop_select = 0
        _l_(426742)
    elif _n_(426743, "loop", lambda: loop) == 8:
        _l_(426759)

        _c_(426745, _n_(426744, "print", lambda: print), "The time-change is set to cosmic seconds.(a really long time)")
        _l_(426746)

        time_change = 'Cosmic Second'
        _l_(426747)
        loop_select = 0
        _l_(426748)
    elif _n_(426749, "loop", lambda: loop) == _a_(426751, _n_(426750, "type", lambda: type), "str"):
        _l_(426758)

        _c_(426753, _n_(426752, "print", lambda: print), "~|Improper Input|~")
        _l_(426754)
    else:
        _c_(426756, _n_(426755, "print", lambda: print), "Input is currently inapplicable, try again.\n")
        _l_(426757)

if _n_(426768, "loop", lambda: loop) == 1:
    _l_(426777)

    _c_(426770, _n_(426769, "turn1", lambda: turn1), 0.1 )
    _l_(426771)
elif _n_(426772, "loop", lambda: loop) == 2 or 3 or 4 or 5 or 6 or 7 or 8:
    _l_(426776)

    _c_(426774, _n_(426773, "turn1", lambda: turn1), 1 )
    _l_(426775)
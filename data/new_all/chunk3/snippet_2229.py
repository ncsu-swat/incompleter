# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56590944/attributeerror-int-object-has-no-attribute-move
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def __init__(self, p2):
    _l_(540676)

    _n_(540669, "self", lambda: self).p1 = _c_(540671, _n_(540670, "HumanPlayer", lambda: HumanPlayer))
    _l_(540672)
    _n_(540673, "self", lambda: self).p2 = _n_(540674, "p2", lambda: p2)
    _l_(540675)

def play_round(self):
    _l_(540745)

    move1 = _c_(540680, _a_(540679, _a_(540678, _n_(540677, "self", lambda: self), "p1"), "move"))
    _l_(540681)
    move2 = _c_(540685, _a_(540684, _a_(540683, _n_(540682, "self", lambda: self), "p2"), "move"))
    _l_(540686)
    _c_(540690, _n_(540687, "print", lambda: print), f"Player 1: {_n_(540688, 'move1', lambda: move1)} <> Player 2: {_n_(540689, 'move2', lambda: move2)}")
    _l_(540691)
    _c_(540697, _a_(540694, _a_(540693, _n_(540692, "self", lambda: self), "p1"), "learn"), _n_(540695, "move1", lambda: move1), _n_(540696, "move2", lambda: move2))
    _l_(540698)
    _c_(540704, _a_(540701, _a_(540700, _n_(540699, "self", lambda: self), "p2"), "learn"), _n_(540702, "move2", lambda: move2), _n_(540703, "move1", lambda: move1))
    _l_(540705)
    if _c_(540709, _n_(540706, "beats", lambda: beats), _n_(540707, "move1", lambda: move1), _n_(540708, "move2", lambda: move2)):
        _l_(540726)

        _n_(540710, "self", lambda: self).p1_score += 1
        _l_(540711)
        _c_(540713, _n_(540712, "print", lambda: print), '* Player 1 wins! *')
        _l_(540714)
    else:
        if _n_(540715, "move1", lambda: move1) == _n_(540716, "move2", lambda: move2):
            _l_(540725)

            _c_(540718, _n_(540717, "print", lambda: print), '* Tie *')
            _l_(540719)
        else:
            _n_(540720, "self", lambda: self).p2_score += 1
            _l_(540721)
            _c_(540723, _n_(540722, "print", lambda: print), '* Player 2 wins! *')
            _l_(540724)

    _c_(540734, _n_(540727, "print", lambda: print), f"Player:{_a_(540731, _a_(540730, _a_(540729, _n_(540728, 'self', lambda: self), 'p1'), '__class__'), '__name__')}, Score:{_a_(540733, _n_(540732, 'self', lambda: self), 'p1_score')}")
    _l_(540735)
    _c_(540743, _n_(540736, "print", lambda: print), f"Player:{_a_(540740, _a_(540739, _a_(540738, _n_(540737, 'self', lambda: self), 'p2'), '__class__'), '__name__')}, Score:{_a_(540742, _n_(540741, 'self', lambda: self), 'p2_score')}")
    _l_(540744)

# This will call a tourney
def play_game(self):
    _l_(540793)

    _c_(540747, _n_(540746, "print", lambda: print), "Game Start!")
    _l_(540748)
    for round in _c_(540750, _n_(540749, "range", lambda: range), 3):
        _l_(540759)

        _c_(540753, _n_(540751, "print", lambda: print), f"Round {_n_(540752, 'round', lambda: round)}:")
        _l_(540754)
        _c_(540757, _a_(540756, _n_(540755, "self", lambda: self), "play_round"))
        _l_(540758)
    if _a_(540761, _n_(540760, "self", lambda: self), "p1_score") > _a_(540763, _n_(540762, "self", lambda: self), "p2_score"):
        _l_(540778)

        _c_(540765, _n_(540764, "print", lambda: print), '** Congrats! Player 1 WINS! **')
        _l_(540766)
    elif _a_(540768, _n_(540767, "self", lambda: self), "p2_score") > _a_(540770, _n_(540769, "self", lambda: self), "p1_score"):
        _l_(540777)

        _c_(540772, _n_(540771, "print", lambda: print), '** Sadly Player 2 WINS! **')
        _l_(540773)
    else:
        _c_(540775, _n_(540774, "print", lambda: print), '** The match was a tie! **')
        _l_(540776)
    _c_(540788, _n_(540779, "print", lambda: print), 'The final score is: ' + _c_(540783, _n_(540780, "str", lambda: str), _a_(540782, _n_(540781, "self", lambda: self), "p1_score")) + ' TO ' +
          _c_(540787, _n_(540784, "str", lambda: str), _a_(540786, _n_(540785, "self", lambda: self), "p2_score")))
    _l_(540789)
    _c_(540791, _n_(540790, "print", lambda: print), "Game over!")
    _l_(540792)

# This will call a singe game.
def play_single(self):
    _l_(540834)

    _c_(540795, _n_(540794, "print", lambda: print), "Single Game Start!")
    _l_(540796)
    _c_(540798, _n_(540797, "print", lambda: print), f"Round 1 of 1:")
    _l_(540799)
    _c_(540802, _a_(540801, _n_(540800, "self", lambda: self), "play_round"))
    _l_(540803)
    if _a_(540805, _n_(540804, "self", lambda: self), "p1_score") > _a_(540807, _n_(540806, "self", lambda: self), "p2_score"):
        _l_(540822)

        _c_(540809, _n_(540808, "print", lambda: print), '** Congrats! Player 1 WINS! **')
        _l_(540810)
    elif _a_(540812, _n_(540811, "self", lambda: self), "p1_score") < _a_(540814, _n_(540813, "self", lambda: self), "p2_score"):
        _l_(540821)

        _c_(540816, _n_(540815, "print", lambda: print), '** Sadly Player 2 WINS! **')
        _l_(540817)
    else:
        _c_(540819, _n_(540818, "print", lambda: print), '** The game was a tie! **')
        _l_(540820)
    _c_(540832, _n_(540823, "print", lambda: print), 'The final score: ' + _c_(540827, _n_(540824, "str", lambda: str), _a_(540826, _n_(540825, "self", lambda: self), "p1_score")) + ' TO ' +
          _c_(540831, _n_(540828, "str", lambda: str), _a_(540830, _n_(540829, "self", lambda: self), "p2_score")))
    _l_(540833)


if _n_(540835, "__name__", lambda: __name__) == '__main__':
    _l_(540845)

    p2 = {
        "1": _c_(540837, _n_(540836, "Player", lambda: Player)),
        "2": _c_(540839, _n_(540838, "RandomPlayer", lambda: RandomPlayer)),
        "3": _c_(540841, _n_(540840, "CyclePlayer", lambda: CyclePlayer)),
        "4": _c_(540843, _n_(540842, "ReflectPlayer", lambda: ReflectPlayer))
        }
    _l_(540844)

# Selecting Opponent
while True:
    _l_(540865)

    try:
        _l_(540857)

        p2 = _c_(540849, _n_(540846, "int", lambda: int), _c_(540848, _n_(540847, "input", lambda: input), "Select the strategy "
                       "you want to play against:  "
                       "1 - Rock Player "
                       "2 - Random Player "
                       "3 - Cycle Player "
                       "4 - Reflect Player: "))
        _l_(540850)


  #"Select strategy:
    except _n_(540851, "ValueError", lambda: ValueError):
        _l_(540856)

        _c_(540853, _n_(540852, "print", lambda: print), "Sorry, I didn't understand that.")
        _l_(540854)
        continue
        _l_(540855)

    if _n_(540858, "p2", lambda: p2) > 4:
        _l_(540864)

        _c_(540860, _n_(540859, "print", lambda: print), "Sorry, you must select [1-4]: ")
        _l_(540861)
        continue
        _l_(540862)
    else:
        break
        _l_(540863)


# Slecting 1 or 3 games
rounds = _c_(540867, _n_(540866, "input", lambda: input), 'Enter for [s]ingle game or [f]ull game: ')
_l_(540868)
Game = _c_(540871, _n_(540869, "Game", lambda: Game), _n_(540870, "p2", lambda: p2))
_l_(540872)
while True:
    _l_(540893)

    if _n_(540873, "rounds", lambda: rounds) == 's':
        _l_(540892)

        _c_(540876, _a_(540875, _n_(540874, "Game", lambda: Game), "play_single"))
        _l_(540877)
        break
        _l_(540878)
    elif _n_(540879, "rounds", lambda: rounds) == 'f':
        _l_(540891)

        _c_(540882, _a_(540881, _n_(540880, "Game", lambda: Game), "play_game"))
        _l_(540883)
        break
        _l_(540884)
    else:
        _c_(540886, _n_(540885, "print", lambda: print), 'Please select again')
        _l_(540887)
        rounds = _c_(540889, _n_(540888, "input", lambda: input), 'Enter [s] for a single'
                       'game and [f] for a full game: ')
        _l_(540890)
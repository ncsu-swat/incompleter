# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75044667/i-dont-know-what-to-change-about-this-code-does-anyone-know-why-it-keeps-givin
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Card(_n_(574662, "object", lambda: object)):
    _l_(574682)

    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    _l_(574663)
    SUITS = ["D", "S", "H", "C"]
    _l_(574664)

    def __init__(self, rank, suit):
        _l_(574671)

        _n_(574665, "self", lambda: self).rank = _n_(574666, "rank", lambda: rank)
        _l_(574667)
        _n_(574668, "self", lambda: self).suit = _n_(574669, "suit", lambda: suit)
        _l_(574670)

    def __str__(self):
        _l_(574681)

        rep = _a_(574673, _n_(574672, "self", lambda: self), "rank") + _a_(574675, _n_(574674, "self", lambda: self), "suit")
        _l_(574676)
        aux = _c_(574679, _n_(574677, "str", lambda: str), _n_(574678, "rep", lambda: rep))
        _l_(574680)
        return aux


class Hand(_n_(574683, "object", lambda: object)):
    _l_(574724)

    """a hand of playing cards"""
    def __init__(self):
        _l_(574686)

        _n_(574684, "self", lambda: self).cards = []
        _l_(574685)

    def __str__(self):
        _l_(574701)

        if _a_(574688, _n_(574687, "self", lambda: self), "cards"):
            _l_(574700)

            rep = ""
            _l_(574689)
            for card in _a_(574691, _n_(574690, "self", lambda: self), "cards"):
                _l_(574696)

                rep += _c_(574694, _n_(574692, "str", lambda: str), _n_(574693, "card", lambda: card)) + "  "
                _l_(574695)
        else:
            rep = "<empty>"
            _l_(574697)
            aux = _n_(574698, "rep", lambda: rep)
            _l_(574699)
            return aux

    def clear(self):
        _l_(574704)

        _n_(574702, "self", lambda: self).cards = []
        _l_(574703)

    def add(self, card):
        _l_(574711)

        _c_(574709, _a_(574707, _a_(574706, _n_(574705, "self", lambda: self), "cards"), "append"), _n_(574708, "card", lambda: card))
        _l_(574710)

    def give(self, card, other_hand):
        _l_(574723)

        _c_(574716, _a_(574714, _a_(574713, _n_(574712, "self", lambda: self), "cards"), "remove"), _n_(574715, "card", lambda: card))
        _l_(574717)
        _c_(574721, _a_(574719, _n_(574718, "other_hand", lambda: other_hand), "add"), _n_(574720, "card", lambda: card))
        _l_(574722)


card1 = _c_(574726, _n_(574725, "Card", lambda: Card), rank="A", suit="c")
_l_(574727)
_c_(574730, _n_(574728, "print", lambda: print), _n_(574729, "card1", lambda: card1))
_l_(574731)
card2 = _c_(574733, _n_(574732, "Card", lambda: Card), rank="2", suit="c")
_l_(574734)
card3 = _c_(574736, _n_(574735, "Card", lambda: Card), rank="3", suit="c")
_l_(574737)
card4 = _c_(574739, _n_(574738, "Card", lambda: Card), rank="4", suit="c")
_l_(574740)
card5 = _c_(574742, _n_(574741, "Card", lambda: Card), rank="5", suit="c")
_l_(574743)
_c_(574746, _n_(574744, "print", lambda: print), _n_(574745, "card2", lambda: card2))
_l_(574747)
_c_(574750, _n_(574748, "print", lambda: print), _n_(574749, "card3", lambda: card3))
_l_(574751)
_c_(574754, _n_(574752, "print", lambda: print), _n_(574753, "card4", lambda: card4))
_l_(574755)
_c_(574758, _n_(574756, "print", lambda: print), _n_(574757, "card5", lambda: card5))
_l_(574759)

my_hand = _c_(574761, _n_(574760, "Hand", lambda: Hand))
_l_(574762)
_c_(574765, _n_(574763, "print", lambda: print), "my hand before i add cards\n", _n_(574764, "my_hand", lambda: my_hand))
_l_(574766)
_c_(574770, _a_(574768, _n_(574767, "my_hand", lambda: my_hand), "add"), _n_(574769, "card1", lambda: card1))
_l_(574771)
_c_(574775, _a_(574773, _n_(574772, "my_hand", lambda: my_hand), "add"), _n_(574774, "card2", lambda: card2))
_l_(574776)
_c_(574780, _a_(574778, _n_(574777, "my_hand", lambda: my_hand), "add"), _n_(574779, "card3", lambda: card3))
_l_(574781)
_c_(574785, _a_(574783, _n_(574782, "my_hand", lambda: my_hand), "add"), _n_(574784, "card4", lambda: card4))
_l_(574786)
_c_(574790, _a_(574788, _n_(574787, "my_hand", lambda: my_hand), "add"), _n_(574789, "card5", lambda: card5))
_l_(574791)
_c_(574793, _n_(574792, "print", lambda: print), "my hand after adding 5 cards: ")
_l_(574794)
_c_(574797, _n_(574795, "print", lambda: print), _n_(574796, "my_hand", lambda: my_hand))
_l_(574798)

your_hand = _c_(574800, _n_(574799, "Hand", lambda: Hand))
_l_(574801)
_c_(574806, _a_(574803, _n_(574802, "my_hand", lambda: my_hand), "give"), _n_(574804, "card1", lambda: card1), _n_(574805, "your_hand", lambda: your_hand))
_l_(574807)
_c_(574812, _a_(574809, _n_(574808, "my_hand", lambda: my_hand), "give"), _n_(574810, "card2", lambda: card2), _n_(574811, "your_hand", lambda: your_hand))
_l_(574813)
_c_(574815, _n_(574814, "print", lambda: print), "your hand: ")
_l_(574816)
_c_(574819, _n_(574817, "print", lambda: print), _n_(574818, "your_hand", lambda: your_hand))
_l_(574820)
_c_(574822, _n_(574821, "print", lambda: print), "my hand: ")
_l_(574823)
_c_(574826, _n_(574824, "print", lambda: print), _n_(574825, "my_hand", lambda: my_hand))
_l_(574827)

_c_(574830, _a_(574829, _n_(574828, "my_hand", lambda: my_hand), "clear"))
_l_(574831)
_c_(574833, _n_(574832, "print", lambda: print), "my hand now: ")
_l_(574834)
_c_(574837, _n_(574835, "print", lambda: print), _n_(574836, "my_hand", lambda: my_hand))
_l_(574838)
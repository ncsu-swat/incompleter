# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73821647/why-does-newdeck-pop0-give-an-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for i in _c_(531350, _n_(531349, "range", lambda: range), 2):
    _l_(531375)

    drawnCard = _c_(531353, _a_(531352, _n_(531351, "newDeck", lambda: newDeck), "pop"), 0)
    _l_(531354)
    _c_(531358, _a_(531356, _n_(531355, "playerList", lambda: playerList), "append"), _n_(531357, "drawnCard", lambda: drawnCard))
    _l_(531359)
    if (_n_(531360, "drawnCard", lambda: drawnCard)[:1] == "J" or _n_(531361, "drawnCard", lambda: drawnCard)[:1] == "Q" or _n_(531362, "drawnCard", lambda: drawnCard)[:1] == "K"):
        _l_(531374)

        playerSum += 10
        _l_(531363)
    elif (_n_(531364, "drawnCard", lambda: drawnCard)[:1] == "A"):
        _l_(531373)

        playerSum += 11
        _l_(531365)
    elif ((_n_(531366, "drawnCard", lambda: drawnCard)[:2]) == "10"):
        _l_(531372)

        playerSum += 10
        _l_(531367)
    else:
        playerSum += _c_(531370, _n_(531368, "int", lambda: int), _n_(531369, "drawnCard", lambda: drawnCard)[:1])
        _l_(531371)
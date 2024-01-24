# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61047626/best-way-to-deal-with-a-filenotfounderror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
while True:
    _l_(592832)

    try:
        _l_(592831)

        with _c_(592804, _n_(592803, "open", lambda: open), "etalons.txt", "r") as fichier:
            _l_(592820)

            etalons = []
            _l_(592805)
            for ligne in _n_(592806, "fichier", lambda: fichier):
                _l_(592819)

                temp = _c_(592809, _a_(592808, _n_(592807, "ligne", lambda: ligne), "split"), ',')
                _l_(592810)
                ets = {
                        'conc' : _n_(592811, "temp", lambda: temp)[0],
                        'abs' :  _n_(592812, "temp", lambda: temp)[1]
                        }
                _l_(592813)
                _c_(592817, _a_(592815, _n_(592814, "etalons", lambda: etalons), "append"), _n_(592816, "ets", lambda: ets)) # stockage des dicos dans liste
                _l_(592818) # stockage des dicos dans liste
        break
        _l_(592821)
    except _n_(592822, "FileNotFoundError", lambda: FileNotFoundError):
        _l_(592830)

        _c_(592824, _n_(592823, "print", lambda: print), "File not found. Check if the file is in the folder and it's name. ")
        _l_(592825)
        _c_(592828, _a_(592827, _n_(592826, "time", lambda: time), "sleep"), 20)
        _l_(592829)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/24314545/unexpected-typeerror-unsupported-operand-types-for-int-and-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def main():
        _l_(618677)


        months = [0] * 12
        _l_(618640)
        name_months = ['Jan','Feb','Mar','Apr','May','Jun', \
                   'Jul','Aug','Sep','Oct','Nov','Dec']
        _l_(618641)

        def total(months):
                _l_(618649)

                total = 0
                _l_(618642)
                for num in _n_(618643, "months", lambda: months):
                        _l_(618646)

                        total += _n_(618644, "num", lambda: num)
                        _l_(618645)
                aux = _n_(618647, "total", lambda: total)
                _l_(618648)
                return aux

        for index in _c_(618651, _n_(618650, "range", lambda: range), 12):
                _l_(618662)

                _c_(618653, _n_(618652, "print", lambda: print), 'Please enter the amount of rain in')
                _l_(618654)
                _n_(618655, "months", lambda: months)[_n_(618656, "index", lambda: index)] = _c_(618660, _n_(618657, "input", lambda: input), _n_(618658, "name_months", lambda: name_months)[_n_(618659, "index", lambda: index)] + ': ')
                _l_(618661)
        _c_(618664, _n_(618663, "print", lambda: print), 'The total is'), _c_(618667, _n_(618665, "total", lambda: total), _n_(618666, "months", lambda: months)),'mm.'
        _l_(618668)


        avarage = _c_(618671, _n_(618669, "total", lambda: total), _n_(618670, "months", lambda: months)) / 12.0
        _l_(618672)
        _c_(618674, _n_(618673, "print", lambda: print), 'The avarage rainfall is'), _n_(618675, "avarage", lambda: avarage),'mm.'
        _l_(618676)

_c_(618679, _n_(618678, "main", lambda: main))
_l_(618680)
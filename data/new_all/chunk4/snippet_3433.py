# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74286153/typeerror-economico-missing-2-required-positional-arguments-carro-and-con
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def entrada_carro():
    _l_(588403)

    carro = []
    _l_(588391)
    for i in _c_(588393, _n_(588392, "range", lambda: range), 4):
        _l_(588400)

        _c_(588398, _a_(588395, _n_(588394, "carro", lambda: carro), "append"), _c_(588397, _n_(588396, "input", lambda: input), "Digite o modelo do carro: "))
        _l_(588399)
    aux = _n_(588401, "carro", lambda: carro)
    _l_(588402)
    return aux

def entrada_consumo():
    _l_(588418)

    consumo = []
    _l_(588404)
    for i in _c_(588406, _n_(588405, "range", lambda: range), 4):
        _l_(588415)

        _c_(588413, _a_(588408, _n_(588407, "consumo", lambda: consumo), "append"), _c_(588412, _n_(588409, "int", lambda: int), _c_(588411, _n_(588410, "input", lambda: input), "Digite o consumo do carro: ")))
        _l_(588414)
    aux = _n_(588416, "consumo", lambda: consumo)
    _l_(588417)
    return aux

def economico(carro, consumo):
    _l_(588437)

    menor = _n_(588419, "consumo", lambda: consumo)[0]
    _l_(588420)
    for i in _c_(588422, _n_(588421, "range", lambda: range), 1,4):
        _l_(588430)

        if _n_(588423, "consumo", lambda: consumo)[_n_(588424, "i", lambda: i)] < _n_(588425, "menor", lambda: menor):
            _l_(588429)

            menor = _n_(588426, "consumo", lambda: consumo)[_n_(588427, "i", lambda: i)]
            _l_(588428)
    aux = _n_(588431, "carro", lambda: carro)[_c_(588435, _a_(588433, _n_(588432, "consumo", lambda: consumo), "index"), _n_(588434, "menor", lambda: menor))]
    _l_(588436)
    return aux

def main():
    _l_(588451)

    carro = _c_(588439, _n_(588438, "entrada_carro", lambda: entrada_carro))
    _l_(588440)
    consumo = _c_(588442, _n_(588441, "entrada_consumo", lambda: entrada_consumo))
    _l_(588443)
    _c_(588449, _n_(588444, "print", lambda: print), "O carro mais economico é o", _c_(588448, _n_(588445, "economico", lambda: economico), _n_(588446, "carro", lambda: carro), _n_(588447, "consumo", lambda: consumo)))
    _l_(588450)

_c_(588453, _n_(588452, "main", lambda: main))
_l_(588454)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51215537/nameerror-name-xxxxx-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
str_horas= _c_(335955, _n_(335954, "input", lambda: input), 'Digite as horas: ')
_l_(335956)
str_taxa=_c_(335958, _n_(335957, "input", lambda: input), 'Digite a taxa: ')
_l_(335959)
#calcula_pagamento = ( )
total_salario = _c_(335963, _n_(335960, "calcula_pagamento", lambda: calcula_pagamento), _n_(335961, "str_horas", lambda: str_horas),_n_(335962, "str_taxa", lambda: str_taxa))
_l_(335964)
def calcular_pagamento (qtd_horas, valor_hora):
    _l_(335990)

    horas = _c_(335967, _n_(335965, "float", lambda: float), _n_(335966, "qtd_horas", lambda: qtd_horas))
    _l_(335968)
    taxa = _c_(335971, _n_(335969, "float", lambda: float), _n_(335970, "valor_hora", lambda: valor_hora))
    _l_(335972)
    if _n_(335973, "horas", lambda: horas) <= 40:
        _l_(335985)

        salario = _n_(335974, "horas", lambda: horas)*_n_(335975, "taxa", lambda: taxa)
        _l_(335976)
    else:
        h_excd = _n_(335977, "horas", lambda: horas) - 40
        _l_(335978)
        salario = 40*_n_(335979, "taxa", lambda: taxa)+(_n_(335980, "h_excd", lambda: h_excd)*(1.5*_n_(335981, "taxa", lambda: taxa)))
        _l_(335982)
        aux = _n_(335983, "salario", lambda: salario)
        _l_(335984)
        return aux
    _c_(335988, _n_(335986, "print", lambda: print), 'O valor de seus rendimentos é R$',_n_(335987, "total_salario", lambda: total_salario))
    _l_(335989)
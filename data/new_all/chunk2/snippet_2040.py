# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67506988/attributeerror-function-object-has-no-attribute-destroy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(428002)

except ImportError:
    pass
try:
    import os
    _l_(428004)

except ImportError:
    pass


def fechar():
    _l_(428009)

    _c_(428007, _a_(428006, _n_(428005, "tela_principal", lambda: tela_principal), "destroy"))
    _l_(428008)


def tela_clientes():
    _l_(428021)

    _c_(428011, _n_(428010, "fechar", lambda: fechar))
    _l_(428012)
    _c_(428019, _n_(428013, "exec", lambda: exec), _c_(428017, _a_(428016, _c_(428015, _n_(428014, "open", lambda: open), 'cadastro_cliente.py'), "read")), {'c': _n_(428018, "tela_principal", lambda: tela_principal)})
    _l_(428020)


def tela_carros():
    _l_(428023)

    pass
    _l_(428022)


tela_principal = _c_(428025, _n_(428024, "Tk", lambda: Tk))
_l_(428026)
_c_(428029, _a_(428028, _n_(428027, "tela_principal", lambda: tela_principal), "title"), 'Principal')
_l_(428030)
_c_(428033, _a_(428032, _n_(428031, "tela_principal", lambda: tela_principal), "geometry"), '400x300+250+50')
_l_(428034)

fr_logo = _c_(428037, _n_(428035, "Frame", lambda: Frame), _n_(428036, "tela_principal", lambda: tela_principal), borderwidth=1, relief='solid')
_l_(428038)
_c_(428041, _a_(428040, _n_(428039, "fr_logo", lambda: fr_logo), "place"), x=10, y=10, width=380, height=180)
_l_(428042)

btn_cliente = _c_(428046, _n_(428043, "Button", lambda: Button), _n_(428044, "tela_principal", lambda: tela_principal), text='CADASTRO\nCLIENTE', command=_n_(428045, "tela_clientes", lambda: tela_clientes))
_l_(428047)
_c_(428050, _a_(428049, _n_(428048, "btn_cliente", lambda: btn_cliente), "place"), x=30, y=220, width=100, height=50)
_l_(428051)

btn_carros = _c_(428055, _n_(428052, "Button", lambda: Button), _n_(428053, "tela_principal", lambda: tela_principal), text='PESQUISA\nCARROS',
                    command=_n_(428054, "tela_carros", lambda: tela_carros))
_l_(428056)
_c_(428059, _a_(428058, _n_(428057, "btn_carros", lambda: btn_carros), "place"), x=150, y=220, width=100, heigh=50)
_l_(428060)

btn_sair = _c_(428064, _n_(428061, "Button", lambda: Button), _n_(428062, "tela_principal", lambda: tela_principal), text='SAIR', command=_n_(428063, "fechar", lambda: fechar))
_l_(428065)
_c_(428068, _a_(428067, _n_(428066, "btn_sair", lambda: btn_sair), "place"), x=270, y=220, width=100, height=50)
_l_(428069)


_c_(428072, _a_(428071, _n_(428070, "tela_principal", lambda: tela_principal), "mainloop"))
_l_(428073)
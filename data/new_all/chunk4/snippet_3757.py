# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68500183/class-in-python-3-9-4-gives-inconsistent-attribute-error-when-calling-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from src.agents import ForagerAgent
    _l_(634883)

except ImportError:
    pass

forager_A = _c_(634885, _n_(634884, "ForagerAgent", lambda: ForagerAgent))
_l_(634886)
_n_(634887, "forager_A", lambda: forager_A).heatmap = {'stock_1': 100.0, 'stock_2': 0}
_l_(634888)
_c_(634891, _a_(634890, _n_(634889, "forager_A", lambda: forager_A), "update_list_of_knowns"))
_l_(634892)

forager_B = _c_(634894, _n_(634893, "ForagerAgent", lambda: ForagerAgent))
_l_(634895)
_n_(634896, "forager_B", lambda: forager_B).heatmap = {'stock_1': 0, 'stock_2': 15}
_l_(634897)

data = _c_(634900, _a_(634899, _n_(634898, "forager_A", lambda: forager_A), "share_heatmap_knowledge")) # method that yields knowledge as (['stock_1'], [100.0])
_l_(634901) # method that yields knowledge as (['stock_1'], [100.0])
_c_(634905, _a_(634903, _n_(634902, "forager_B", lambda: forager_B), "receive_heatmap_knowledge"), _n_(634904, "data", lambda: data))
_l_(634906)
_c_(634910, _n_(634907, "print", lambda: print), _a_(634909, _n_(634908, "forager_B", lambda: forager_B), "heatmap"))
_l_(634911)
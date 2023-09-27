# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5214578/print-string-to-text-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(1542751)

except ImportError:
    pass

now = _c_(1542755, _a_(1542754, _a_(1542753, _n_(1542752, "datetime", lambda: datetime), "datetime"), "now"))
_l_(1542756)
price = 1200
_l_(1542757)
currency = "INR"
_l_(1542758)

with _c_(1542760, _n_(1542759, "open", lambda: open), "D:\\log.txt","a") as f:
    _l_(1542770)

    _c_(1542768, _a_(1542762, _n_(1542761, "f", lambda: f), "write"), f'Product sold at {_n_(1542763, "currency", lambda: currency)} {_n_(1542764, "price", lambda: price) } on {_c_(1542767, _n_(1542765, "str", lambda: str), _n_(1542766, "now", lambda: now))}\n')
    _l_(1542769)


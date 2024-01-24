# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53706451/attributeerror-module-pika-has-no-attribute-blockingconnection-error-in-rab
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pika
    _l_(395138)

except ImportError:
    pass

connection = _c_(395144, _a_(395140, _n_(395139, "pika", lambda: pika), "BlockingConnection"), _c_(395143, _a_(395142, _n_(395141, "pika", lambda: pika), "ConnectionParameters"), 'localhost'))
_l_(395145)
channel = _c_(395148, _a_(395147, _n_(395146, "connection", lambda: connection), "channel"))
_l_(395149)

_c_(395152, _a_(395151, _n_(395150, "channel", lambda: channel), "queue_declare"), queue='hello')
_l_(395153)

_c_(395156, _a_(395155, _n_(395154, "channel", lambda: channel), "basic_publish"), exchange='',
                  routing_key='hello',
                  body='Hello World!')
_l_(395157)
_c_(395159, _n_(395158, "print", lambda: print), " [x] Sent 'Hello World!'")
_l_(395160)

_c_(395163, _a_(395162, _n_(395161, "connection", lambda: connection), "close"))
_l_(395164)
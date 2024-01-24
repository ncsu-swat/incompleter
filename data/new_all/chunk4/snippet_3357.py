# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75403903/why-am-i-receiving-the-typeerror-str-object-cannot-be-interpreted-as-an-inte
# create the if loop for option 2, port listener.
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _n_(599366, "choice", lambda: choice)=='2':
    _l_(599406)

# take the target host ip as user input and store it in a variable
    host = _c_(599368, _n_(599367, "input", lambda: input), 'Please enter target host: ')
    _l_(599369)
# take the target port and store it in a variable
    port = _c_(599373, _n_(599370, "int", lambda: int), _c_(599372, _n_(599371, "input", lambda: input), 'Please enter target port'))
    _l_(599374)
# check the connection for errors
    try:
        _l_(599390)

        _c_(599379, _a_(599376, _n_(599375, "s", lambda: s), "bind"), (_n_(599377, "host", lambda: host), _n_(599378, "port", lambda: port)))
        _l_(599380)
# if the connection fails, display an error message.
    except _a_(599382, _n_(599381, "socket", lambda: socket), "error") as e:
        _l_(599389)

        _c_(599387, _n_(599383, "print", lambda: print), _c_(599386, _n_(599384, "str", lambda: str), _n_(599385, "e", lambda: e)))
        _l_(599388)
# listen for the connection with the maximum number of queued connections being five.
    _c_(599393, _a_(599392, _n_(599391, "s", lambda: s), "listen"), 5)
    _l_(599394)
# accept the connection from client
    conn, addr = _c_(599397, _a_(599396, _n_(599395, "s", lambda: s), "accept"))
    _l_(599398)
# display a message on the client machine.
    _c_(599404, _n_(599399, "print", lambda: print), 'pwned: '+_n_(599400, "addr", lambda: addr)[0]+':'+_c_(599403, _n_(599401, "str", lambda: str), _n_(599402, "addr", lambda: addr)[1]))
    _l_(599405)
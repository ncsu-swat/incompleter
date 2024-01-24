# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49465554/try-to-build-webserver-and-read-html-file-with-typeerror-must-be-str-not-byte
#coding=utf-8

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import socket
    _l_(667058)

except ImportError:
    pass
try:
    import re
    _l_(667060)

except ImportError:
    pass

HOST = ''
_l_(667061)
PORT = 8000
_l_(667062)

#Read index.html, put into HTTP response data
index_content = '''
    HTTP/1.x 200 ok
    Content-Type: text/html

    '''
_l_(667063)

file = _c_(667065, _n_(667064, "open", lambda: open), 'index.html', 'r')
_l_(667066)
index_content += _c_(667069, _a_(667068, _n_(667067, "file", lambda: file), "read"))
_l_(667070)
_c_(667073, _a_(667072, _n_(667071, "file", lambda: file), "close"))
_l_(667074)

#Read picture, put into HTTP response data
file = _c_(667076, _n_(667075, "open", lambda: open), 'Yoda.png', 'rb')
_l_(667077)
pic_content = '''
    HTTP/1.1 200 ok
    Content-Type: image/png

    '''
_l_(667078)
pic_content += _c_(667081, _a_(667080, _n_(667079, "file", lambda: file), "read"))
_l_(667082)
_c_(667085, _a_(667084, _n_(667083, "file", lambda: file), "close"))
_l_(667086)



#Configure socket
sock = _c_(667093, _a_(667088, _n_(667087, "socket", lambda: socket), "socket"), _a_(667090, _n_(667089, "socket", lambda: socket), "AF_INET"), _a_(667092, _n_(667091, "socket", lambda: socket), "SOCK_STREAM"))
_l_(667094)
_c_(667099, _a_(667096, _n_(667095, "sock", lambda: sock), "bind"), (_n_(667097, "HOST", lambda: HOST), _n_(667098, "PORT", lambda: PORT)))
_l_(667100)
_c_(667103, _a_(667102, _n_(667101, "sock", lambda: sock), "listen"), 100)
_l_(667104)

#infinite loop
while True:
    _l_(667175)

    # maximum number of requests waiting
    conn, addr = _c_(667107, _a_(667106, _n_(667105, "sock", lambda: sock), "accept"))
    _l_(667108)
    request = _c_(667111, _a_(667110, _n_(667109, "conn", lambda: conn), "recv"), 1024)
    _l_(667112)
    method = _c_(667115, _a_(667114, _n_(667113, "request", lambda: request), "split"), ' ')[0]
    _l_(667116)
    src  = _c_(667119, _a_(667118, _n_(667117, "request", lambda: request), "split"), ' ')[1]
    _l_(667120)

    _c_(667123, _n_(667121, "print", lambda: print), "Connect by: ", _n_(667122, "addr", lambda: addr))
    _l_(667124)
    _c_(667127, _n_(667125, "print", lambda: print), "Request is:\n", _n_(667126, "request", lambda: request))
    _l_(667128)

    #deal wiht GET method
    if _n_(667129, "method", lambda: method) == 'GET':
        _l_(667165)

        if _n_(667130, "src", lambda: src) == '/index.html':
            _l_(667151)

            content = _n_(667131, "index_content", lambda: index_content)
            _l_(667132)
        elif _n_(667133, "src", lambda: src) == '/Yoda.png':
            _l_(667150)

            content = _n_(667134, "pic_content", lambda: pic_content)
            _l_(667135)
        elif _c_(667139, _a_(667137, _n_(667136, "re", lambda: re), "match"), '^/\?.*$', _n_(667138, "src", lambda: src)):
            _l_(667149)

            entry = _c_(667142, _a_(667141, _n_(667140, "src", lambda: src), "split"), '?')[1]      # main content of the request
            _l_(667143)      # main content of the request
            content = 'HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\n'
            _l_(667144)
            content += _n_(667145, "entry", lambda: entry)
            _l_(667146)
            content += '<br /><font color="green" size="7">register successs!</p>'
            _l_(667147)
        else:
            continue
            _l_(667148)


    #deal with POST method
    elif _n_(667152, "method", lambda: method) == 'POST':
        _l_(667164)

        form = _c_(667155, _a_(667154, _n_(667153, "request", lambda: request), "split"), '\r\n')
        _l_(667156)
        entry = _n_(667157, "form", lambda: form)[-1]      # main content of the request
        _l_(667158)      # main content of the request
        content = '''HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\n'''
        _l_(667159)
        content += _n_(667160, "entry", lambda: entry)
        _l_(667161)
        content += '''<br /><font color="green" size="7">register successs!</p>'''
        _l_(667162)

    ######
    # More operations, such as put the form into database
    # ...
    ######

    else:
        continue
        _l_(667163)

    _c_(667169, _a_(667167, _n_(667166, "conn", lambda: conn), "sendall"), _n_(667168, "content", lambda: content))
    _l_(667170)

    #close connection
    _c_(667173, _a_(667172, _n_(667171, "conn", lambda: conn), "close"))
    _l_(667174)
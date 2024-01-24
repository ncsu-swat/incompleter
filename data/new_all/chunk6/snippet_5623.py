# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60200283/i-got-this-error-typeerror-can-only-concatenate-str-not-nonetype-to-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, request
    _l_(374674)

except ImportError:
    pass
try:
    import requests
    _l_(374676)

except ImportError:
    pass
try:
    from twilio.twiml.messaging_response import MessagingResponse
    _l_(374678)

except ImportError:
    pass


app = _c_(374681, _n_(374679, "Flask", lambda: Flask), _n_(374680, "__name__", lambda: __name__))
_l_(374682)


@_c_(374685, _a_(374684, _n_(374683, "app", lambda: app), "route"), '/sms', methods=['POST'])
def bot():
    _l_(374752)


    incoming_msg = _c_(374691, _a_(374690, _c_(374689, _a_(374688, _a_(374687, _n_(374686, "request", lambda: request), "values"), "get"), 'Body', ''), "lower"))
    _l_(374692)
    resp = _c_(374694, _n_(374693, "MessagingResponse", lambda: MessagingResponse))
    _l_(374695)
    msg = _c_(374698, _a_(374697, _n_(374696, "resp", lambda: resp), "message"))
    _l_(374699)

    if 'moneychanger' in _n_(374700, "incoming_msg", lambda: incoming_msg):
        _l_(374747)

        search1 = 'Please provide the location please'
        _l_(374701)
        _c_(374705, _a_(374703, _n_(374702, "msg", lambda: msg), "body"), _n_(374704, "search1", lambda: search1))
        _l_(374706)

        message_latitude = _c_(374710, _a_(374709, _a_(374708, _n_(374707, "request", lambda: request), "values"), "get"), 'Latitude', None)
        _l_(374711)
        message_longitude = _c_(374715, _a_(374714, _a_(374713, _n_(374712, "request", lambda: request), "values"), "get"), 'Longitude', None)
        _l_(374716)

        responded = True
        _l_(374717)

        if _n_(374718, "message_latitude", lambda: message_latitude) == None:
            _l_(374746)

            location = '%20' + _n_(374719, "message_latitude", lambda: message_latitude) + '%2C' + _n_(374720, "message_longitude", lambda: message_longitude) 
            _l_(374721) 
            responded = False
            _l_(374722)


            url = f'https://tih-api.stb.gov.sg/money-changer/v1?location={_n_(374723, "location", lambda: location)}&radius=2000'
            _l_(374724)

            r = _c_(374728, _a_(374726, _n_(374725, 'requests', lambda: requests), 'get'), _n_(374727, 'url', lambda: url))
            _l_(374729)
            if _a_(374731, _n_(374730, 'r', lambda: r), 'status_code') == 200:
                _l_(374739)

                data = _c_(374734, _a_(374733, _n_(374732, 'r', lambda: r), 'json'))
                _l_(374735)
                search = _n_(374736, 'data', lambda: data)['data'][0]['name']
                _l_(374737)
            else:
                search = 'I could not retrieve a quote at this time, sorry.'
                _l_(374738)
            _c_(374743, _a_(374741, _n_(374740, 'msg', lambda: msg), 'body'), _n_(374742, 'search', lambda: search))
            _l_(374744)
            responded = True
            _l_(374745)
    aux = _c_(374750, _n_(374748, 'str', lambda: str), _n_(374749, 'resp', lambda: resp))
    _l_(374751)

    return aux

if _n_(374753, '__name__', lambda: __name__) == "__main__":
    _l_(374758)

    _c_(374756, _a_(374755, _n_(374754, 'app', lambda: app), 'run'), debug=True)
    _l_(374757)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60200283/i-got-this-error-typeerror-can-only-concatenate-str-not-nonetype-to-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, request
    _l_(343464)

except ImportError:
    pass
try:
    import requests
    _l_(343466)

except ImportError:
    pass
try:
    from twilio.twiml.messaging_response import MessagingResponse
    _l_(343468)

except ImportError:
    pass


app = _c_(343471, _n_(343469, "Flask", lambda: Flask), _n_(343470, "__name__", lambda: __name__))
_l_(343472)


@_c_(343475, _a_(343474, _n_(343473, "app", lambda: app), "route"), '/sms', methods=['POST'])
def bot():
    _l_(343542)


    incoming_msg = _c_(343481, _a_(343480, _c_(343479, _a_(343478, _a_(343477, _n_(343476, "request", lambda: request), "values"), "get"), 'Body', ''), "lower"))
    _l_(343482)
    resp = _c_(343484, _n_(343483, "MessagingResponse", lambda: MessagingResponse))
    _l_(343485)
    msg = _c_(343488, _a_(343487, _n_(343486, "resp", lambda: resp), "message"))
    _l_(343489)

    if 'moneychanger' in _n_(343490, "incoming_msg", lambda: incoming_msg):
        _l_(343537)

        search1 = 'Please provide the location please'
        _l_(343491)
        _c_(343495, _a_(343493, _n_(343492, "msg", lambda: msg), "body"), _n_(343494, "search1", lambda: search1))
        _l_(343496)

        message_latitude = _c_(343500, _a_(343499, _a_(343498, _n_(343497, "request", lambda: request), "values"), "get"), 'Latitude', None)
        _l_(343501)
        message_longitude = _c_(343505, _a_(343504, _a_(343503, _n_(343502, "request", lambda: request), "values"), "get"), 'Longitude', None)
        _l_(343506)

        responded = True
        _l_(343507)

        if _n_(343508, "message_latitude", lambda: message_latitude) == None:
            _l_(343536)

            location = '%20' + _n_(343509, "message_latitude", lambda: message_latitude) + '%2C' + _n_(343510, "message_longitude", lambda: message_longitude) 
            _l_(343511) 
            responded = False
            _l_(343512)


            url = f'https://tih-api.stb.gov.sg/money-changer/v1?location={_n_(343513, "location", lambda: location)}&radius=2000'
            _l_(343514)

            r = _c_(343518, _a_(343516, _n_(343515, 'requests', lambda: requests), 'get'), _n_(343517, 'url', lambda: url))
            _l_(343519)
            if _a_(343521, _n_(343520, 'r', lambda: r), 'status_code') == 200:
                _l_(343529)

                data = _c_(343524, _a_(343523, _n_(343522, 'r', lambda: r), 'json'))
                _l_(343525)
                search = _n_(343526, 'data', lambda: data)['data'][0]['name']
                _l_(343527)
            else:
                search = 'I could not retrieve a quote at this time, sorry.'
                _l_(343528)
            _c_(343533, _a_(343531, _n_(343530, 'msg', lambda: msg), 'body'), _n_(343532, 'search', lambda: search))
            _l_(343534)
            responded = True
            _l_(343535)
    aux = _c_(343540, _n_(343538, 'str', lambda: str), _n_(343539, 'resp', lambda: resp))
    _l_(343541)

    return aux

if _n_(343543, '__name__', lambda: __name__) == "__main__":
    _l_(343548)

    _c_(343546, _a_(343545, _n_(343544, 'app', lambda: app), 'run'), debug=True)
    _l_(343547)
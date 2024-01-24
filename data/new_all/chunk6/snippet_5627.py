# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60200283/i-got-this-error-typeerror-can-only-concatenate-str-not-nonetype-to-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, request
    _l_(372803)

except ImportError:
    pass
try:
    import requests
    _l_(372805)

except ImportError:
    pass
try:
    from twilio.twiml.messaging_response import MessagingResponse
    _l_(372807)

except ImportError:
    pass


app = _c_(372810, _n_(372808, "Flask", lambda: Flask), _n_(372809, "__name__", lambda: __name__))
_l_(372811)


@_c_(372814, _a_(372813, _n_(372812, "app", lambda: app), "route"), '/sms', methods=['POST'])
def bot():
    _l_(372881)


    incoming_msg = _c_(372820, _a_(372819, _c_(372818, _a_(372817, _a_(372816, _n_(372815, "request", lambda: request), "values"), "get"), 'Body', ''), "lower"))
    _l_(372821)
    resp = _c_(372823, _n_(372822, "MessagingResponse", lambda: MessagingResponse))
    _l_(372824)
    msg = _c_(372827, _a_(372826, _n_(372825, "resp", lambda: resp), "message"))
    _l_(372828)

    if 'moneychanger' in _n_(372829, "incoming_msg", lambda: incoming_msg):
        _l_(372876)

        search1 = 'Please provide the location please'
        _l_(372830)
        _c_(372834, _a_(372832, _n_(372831, "msg", lambda: msg), "body"), _n_(372833, "search1", lambda: search1))
        _l_(372835)

        message_latitude = _c_(372839, _a_(372838, _a_(372837, _n_(372836, "request", lambda: request), "values"), "get"), 'Latitude', None)
        _l_(372840)
        message_longitude = _c_(372844, _a_(372843, _a_(372842, _n_(372841, "request", lambda: request), "values"), "get"), 'Longitude', None)
        _l_(372845)

        responded = True
        _l_(372846)

        if _n_(372847, "message_latitude", lambda: message_latitude) == None:
            _l_(372875)

            location = '%20' + _n_(372848, "message_latitude", lambda: message_latitude) + '%2C' + _n_(372849, "message_longitude", lambda: message_longitude) 
            _l_(372850) 
            responded = False
            _l_(372851)


            url = f'https://tih-api.stb.gov.sg/money-changer/v1?location={_n_(372852, "location", lambda: location)}&radius=2000'
            _l_(372853)

            r = _c_(372857, _a_(372855, _n_(372854, 'requests', lambda: requests), 'get'), _n_(372856, 'url', lambda: url))
            _l_(372858)
            if _a_(372860, _n_(372859, 'r', lambda: r), 'status_code') == 200:
                _l_(372868)

                data = _c_(372863, _a_(372862, _n_(372861, 'r', lambda: r), 'json'))
                _l_(372864)
                search = _n_(372865, 'data', lambda: data)['data'][0]['name']
                _l_(372866)
            else:
                search = 'I could not retrieve a quote at this time, sorry.'
                _l_(372867)
            _c_(372872, _a_(372870, _n_(372869, 'msg', lambda: msg), 'body'), _n_(372871, 'search', lambda: search))
            _l_(372873)
            responded = True
            _l_(372874)
    aux = _c_(372879, _n_(372877, 'str', lambda: str), _n_(372878, 'resp', lambda: resp))
    _l_(372880)

    return aux

if _n_(372882, '__name__', lambda: __name__) == "__main__":
    _l_(372887)

    _c_(372885, _a_(372884, _n_(372883, 'app', lambda: app), 'run'), debug=True)
    _l_(372886)
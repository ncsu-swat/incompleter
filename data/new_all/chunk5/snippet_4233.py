# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60990464/kivy-buildozer-attributeerror-nonetype-object-has-no-attribute-text
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(657330)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(657332)

except ImportError:
    pass
try:
    from kivy.uix.widget import Widget
    _l_(657334)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(657336)

except ImportError:
    pass
try:
    from kivy.uix.label import Label
    _l_(657338)

except ImportError:
    pass
try:
    from kivy.uix.gridlayout import GridLayout
    _l_(657340)

except ImportError:
    pass
try:
    from kivy.uix.textinput import TextInput
    _l_(657342)

except ImportError:
    pass
try:
    import random
    _l_(657344)

except ImportError:
    pass
try:
    from kivy.clock import Clock
    _l_(657346)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(657348)

except ImportError:
    pass
try:
    import requests
    _l_(657350)

except ImportError:
    pass
try:
    import json
    _l_(657352)

except ImportError:
    pass

def login (name,password):
    _l_(657372)

    url_login = 'URL'
    _l_(657353)
    payload = {'email': _n_(657354, "name", lambda: name), 'password': _n_(657355, "password", lambda: password)}
    _l_(657356)
    headers = {'content-type': 'application/json'}
    _l_(657357)
    r = _c_(657368, _a_(657367, _c_(657366, _a_(657359, _n_(657358, "requests", lambda: requests), "post"), _n_(657360, "url_login", lambda: url_login), data=_c_(657364, _a_(657362, _n_(657361, "json", lambda: json), "dumps"), _n_(657363, "payload", lambda: payload)), headers=_n_(657365, "headers", lambda: headers)), "json"))
    _l_(657369)
    aux = (_n_(657370, "r", lambda: r)['token'])
    _l_(657371)
    return aux
token =_c_(657374, _n_(657373, "login", lambda: login), "ID","PW")
_l_(657375)

class ConnectPage(_n_(657376, "GridLayout", lambda: GridLayout)):
    _l_(657507)

    oee = _c_(657378, _n_(657377, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(657379)
    performance = _c_(657381, _n_(657380, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(657382)
    quality = _c_(657384, _n_(657383, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(657385)
    availability = _c_(657387, _n_(657386, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(657388)
    sensorstandort = _c_(657390, _n_(657389, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(657391)
    schicht = _c_(657393, _n_(657392, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(657394)
    timestamp = _c_(657396, _n_(657395, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(657397)
    alert = _c_(657399, _n_(657398, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(657400)

    def oee_anzeige(self, *args):
        _l_(657498)

        #Anfrage an Server senden
        url_report = 'URL/'
        _l_(657401)
        payload_report = {}
        _l_(657402)
        headers_report = {'content-type': 'application/json', 'Authorization': _n_(657403, "token", lambda: token)}
        _l_(657404)
        r_report = _c_(657413, _a_(657406, _n_(657405, "requests", lambda: requests), "get"), _n_(657407, "url_report", lambda: url_report), data=_c_(657411, _a_(657409, _n_(657408, "json", lambda: json), "dumps"), _n_(657410, "payload_report", lambda: payload_report)), headers=_n_(657412, "headers_report", lambda: headers_report))
        _l_(657414)
        response = _c_(657417, _a_(657416, _n_(657415, "r_report", lambda: r_report), "json"))
        _l_(657418)

        #Schicht, Sensorstandort und ggfs. Störgrund raussuchen
        x = 0
        _l_(657419)
        for i in _n_(657420, "response", lambda: response)['included']:
            _l_(657457)

            if _n_(657421, "response", lambda: response)['included'][_n_(657422, "x", lambda: x)]['type'] == 'shift':
                _l_(657426)

                schicht = _n_(657423, "response", lambda: response)['included'][_n_(657424, "x", lambda: x)]['attributes']['name']
                _l_(657425)
            if _n_(657427, "response", lambda: response)['included'][_n_(657428, "x", lambda: x)]['type'] == 'location':
                _l_(657432)

                sensorstandort = _n_(657429, "response", lambda: response)['included'][_n_(657430, "x", lambda: x)]['attributes']['name']
                _l_(657431)
            if _n_(657433, "response", lambda: response)['included'][_n_(657434, "x", lambda: x)]['type'] == 'notification':
                _l_(657455)


                timestamp = _c_(657438, _n_(657435, "str", lambda: str), _n_(657436, "response", lambda: response)['included'][_n_(657437, "x", lambda: x)]['attributes']['inserted-at'])
                _l_(657439)
                timestamp = _n_(657440, "timestamp", lambda: timestamp)[11:16] + ' Uhr'
                _l_(657441)

                #self.timestamp.text = timestamp
                if _n_(657442, "response", lambda: response)['included'][_n_(657443, "x", lambda: x)]['attributes']['triggered-by'] == 'standstill':
                    _l_(657454)

                    _a_(657445, _n_(657444, "self", lambda: self), "alert").text = "Verfügbarkeitsverlust seit"
                    _l_(657446)
                elif _n_(657447, "sensorstandort", lambda: sensorstandort) == _n_(657448, "response", lambda: response)['included'][_n_(657449, "x", lambda: x)]['attributes']['triggered-by'] == 'slowdown':
                    _l_(657453)

                    _a_(657451, _n_(657450, "self", lambda: self), "alert").text = "Leistungsverlust seit"
                    _l_(657452)
            x +=1
            _l_(657456)






        #oee Werte aus API ziehen
        oee = _c_(657460, _n_(657458, "str", lambda: str), _n_(657459, "response", lambda: response)['data']['attributes']['oee']) + " %"
        _l_(657461)
        availability = _c_(657464, _n_(657462, "str", lambda: str), _n_(657463, "response", lambda: response)['data']['attributes']['availability']) + " %"
        _l_(657465)
        performance =_c_(657468, _n_(657466, "str", lambda: str), _n_(657467, "response", lambda: response)['data']['attributes']['performance']) + " %"
        _l_(657469)
        quality = _c_(657472, _n_(657470, "str", lambda: str), _n_(657471, "response", lambda: response)['data']['attributes']['quality']) + " %"
        _l_(657473)




        #Labels definieren
        _a_(657475, _n_(657474, "self", lambda: self), "oee").text = _n_(657476, "oee", lambda: oee)
        _l_(657477)
        _a_(657479, _n_(657478, "self", lambda: self), "availability").text = _n_(657480, "availability", lambda: availability)
        _l_(657481)
        _a_(657483, _n_(657482, "self", lambda: self), "performance").text = _n_(657484, "performance", lambda: performance)
        _l_(657485)
        _a_(657487, _n_(657486, "self", lambda: self), "quality").text = _n_(657488, "quality", lambda: quality)
        _l_(657489)
        _a_(657491, _n_(657490, "self", lambda: self), "sensorstandort").text = _n_(657492, "sensorstandort", lambda: sensorstandort)
        _l_(657493)
        _a_(657495, _n_(657494, "self", lambda: self), "schicht").text = _n_(657496, "schicht", lambda: schicht)
        _l_(657497)


    def __init__(self, **kwargs):
        _l_(657506)

        _c_(657502, _a_(657500, _n_(657499, "super", lambda: super)(), "__init__"), **_n_(657501, "kwargs", lambda: kwargs))
        _l_(657503)
        _n_(657504, "self", lambda: self).cols = 2  # used for our grid
        _l_(657505)  # used for our grid


class EpicApp(_n_(657508, "App", lambda: App)):
    _l_(657527)

    def build(self):
        _l_(657526)

        t = _c_(657510, _n_(657509, "ConnectPage", lambda: ConnectPage))
        _l_(657511)
        _c_(657516, _a_(657513, _n_(657512, "Clock", lambda: Clock), "schedule_once"), _a_(657515, _n_(657514, "t", lambda: t), "oee_anzeige"), 2)
        _l_(657517)
        _c_(657522, _a_(657519, _n_(657518, "Clock", lambda: Clock), "schedule_interval"), _a_(657521, _n_(657520, "t", lambda: t), "oee_anzeige"), 90)
        _l_(657523)
        aux = _n_(657524, "t", lambda: t)
        _l_(657525)
        return aux



if _n_(657528, "__name__", lambda: __name__) == "__main__":
    _l_(657534)

    _c_(657532, _a_(657531, _c_(657530, _n_(657529, "EpicApp", lambda: EpicApp)), "run"))
    _l_(657533)
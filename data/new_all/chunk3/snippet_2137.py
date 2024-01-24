# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62173029/receiving-typeerror-nonetype-object-is-not-subscriptable-at-random-in-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(579365)

except ImportError:
    pass
try:
    import json
    _l_(579367)

except ImportError:
    pass
try:
    import urllib.request as request
    _l_(579369)

except ImportError:
    pass
try:
    from urllib.request import Request, urlopen
    _l_(579371)

except ImportError:
    pass
try:
    import time
    _l_(579373)

except ImportError:
    pass

# THINGS
'''
international API: https://arsonwarehouse.com/api/v1/foreign-stock
domestic API: https://api.torn.com/market/  ?selections=itemmarket&key=KEY
personal API: https://api.torn.com/user/2519609?selections=money&key=KEY
'''
_l_(579374)

capacity = 21
_l_(579375)
moneyOverride = False
_l_(579376)
totalCost: _n_(579377, "int", lambda: int)
_l_(579378)
totalIncome: _n_(579379, "int", lambda: int)
_l_(579380)

#Takes in the cost per item, multiplies by capacity, returns true if it's affordable
def checkAfford(costPer):
    _l_(579390)

    global totalCost
    _l_(579381)
    totalCost = _n_(579382, "capacity", lambda: capacity) * _n_(579383, "costPer", lambda: costPer)
    _l_(579384)
    if _n_(579385, "totalCost", lambda: totalCost) < _n_(579386, "money", lambda: money):
        _l_(579389)

        aux = True
        _l_(579387)
        return aux
    else:
        aux = False
        _l_(579388)
        return aux

#Puts together the API link with the ID number and calls pullJSON()
def checkDomestic(id):
    _l_(579402)

    jsonPULL = _c_(579393, _n_(579391, "pullJSON", lambda: pullJSON), f"https://api.torn.com/market/{_n_(579392, 'id', lambda: id)}?selections=itemmarket&key=YET")
    _l_(579394)
    if _n_(579395, "jsonPULL", lambda: jsonPULL) == None:
        _l_(579401)

        _c_(579397, _n_(579396, "print", lambda: print), "error")
        _l_(579398)
    else:
        aux = _n_(579399, "jsonPULL", lambda: jsonPULL)
        _l_(579400)
        return aux

#Requests the JSON from the server
def pullJSON(url):
    _l_(579435)

    req = _c_(579405, _n_(579403, "Request", lambda: Request), _n_(579404, "url", lambda: url), headers={'User-Agent': 'Mozilla/5.0'})
    _l_(579406)
    webpage = _c_(579411, _a_(579410, _c_(579409, _n_(579407, "urlopen", lambda: urlopen), _n_(579408, "req", lambda: req)), "read"))
    _l_(579412)
    with _c_(579415, _n_(579413, "urlopen", lambda: urlopen), _n_(579414, "req", lambda: req)) as response:
        _l_(579434)

        if _c_(579418, _a_(579417, _n_(579416, "response", lambda: response), "getcode")) == 200:
            _l_(579433)

            source = _c_(579421, _a_(579420, _n_(579419, "response", lambda: response), "read"))
            _l_(579422)
            data = _c_(579426, _a_(579424, _n_(579423, "json", lambda: json), "loads"), _n_(579425, "source", lambda: source))
            _l_(579427)
            aux = _n_(579428, "data", lambda: data)
            _l_(579429)
            return aux
        else:
           _c_(579431, _n_(579430, "print", lambda: print), 'An error occurred while attempting to retrieve data from the API.')
           _l_(579432)

internationalData = _c_(579437, _n_(579436, "pullJSON", lambda: pullJSON), "https://arsonwarehouse.com/api/v1/foreign-stock")
_l_(579438)
personalData = _c_(579440, _n_(579439, "pullJSON", lambda: pullJSON), "https://api.torn.com/user/2519609?selections=money&key=YET")
_l_(579441)
domesticData = _c_(579443, _n_(579442, "checkDomestic", lambda: checkDomestic), 10)
_l_(579444)

#Money override
if _n_(579445, "moneyOverride", lambda: moneyOverride) == False:
    _l_(579451)

    money = _c_(579448, _a_(579447, _n_(579446, "personalData", lambda: personalData), "get"), "money_onhand")
    _l_(579449)
else: 
    money = 1000000000000000
    _l_(579450)

_c_(579454, _n_(579452, "print", lambda: print), "onhand:", _n_(579453, "money", lambda: money))
_l_(579455)

i = 0 
_l_(579456) 

length = _c_(579459, _n_(579457, "len", lambda: len), _n_(579458, "internationalData", lambda: internationalData)["items"])
_l_(579460)
_c_(579463, _n_(579461, "print", lambda: print), _n_(579462, "length", lambda: length))
_l_(579464)

for x in _n_(579465, "internationalData", lambda: internationalData)["items"]:
    _l_(579501)

    _c_(579468, _a_(579467, _n_(579466, "time", lambda: time), "sleep"), 0.5)
    _l_(579469)
    ident = _n_(579470, "x", lambda: x)["item_id"]
    _l_(579471)
    domPrice = _n_(579472, "x", lambda: x)["price"]
    _l_(579473)
    _c_(579477, _n_(579474, "print", lambda: print), "DOMESTIC:          ID:", _n_(579475, "ident", lambda: ident), " at price:", _n_(579476, "domPrice", lambda: domPrice))
    _l_(579478)
    domestic = _c_(579483, _a_(579482, _c_(579481, _n_(579479, "checkDomestic", lambda: checkDomestic), _n_(579480, "ident", lambda: ident)), "get"), "itemmarket")[1]
    _l_(579484)
    inPrice = _n_(579485, "domestic", lambda: domestic)["cost"]
    _l_(579486)
    if _n_(579487, "inPrice", lambda: inPrice) == None:
        _l_(579492)

        _c_(579490, _n_(579488, "print", lambda: print), "error", _n_(579489, "domestic", lambda: domestic)["ID"])
        _l_(579491)
    location = _n_(579493, "x", lambda: x)["country"]
    _l_(579494)
    _c_(579499, _n_(579495, "print", lambda: print), "INTERNATIONAL:     ID:", _n_(579496, "ident", lambda: ident), " at price:", _n_(579497, "inPrice", lambda: inPrice), "location: ", _n_(579498, "location", lambda: location))
    _l_(579500)

_c_(579503, _n_(579502, "print", lambda: print), "end")
_l_(579504)
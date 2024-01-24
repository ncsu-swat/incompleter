# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47298943/made-a-program-in-python-but-get-typeerror-method-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyowm
    _l_(367311)

except ImportError:
    pass
try:
    import datetime
    _l_(367313)

except ImportError:
    pass
try:
    import csv
    _l_(367315)

except ImportError:
    pass

W = _c_(367318, _a_(367317, _n_(367316, "pyowm", lambda: pyowm), "OWM"), "****************************")
_l_(367319)
myHouse = _c_(367322, _a_(367321, _n_(367320, "W", lambda: W), "weather_at_place"), "St. albert,Canada")
_l_(367323)
myWeather = _c_(367326, _a_(367325, _n_(367324, "myHouse", lambda: myHouse), "get_weather"))
_l_(367327)
wind = _c_(367330, _a_(367329, _n_(367328, "myWeather", lambda: myWeather), "get_wind"))
_l_(367331)
windspeed = _n_(367332, "wind", lambda: wind)["speed"]
_l_(367333)
windangle = _n_(367334, "wind", lambda: wind)["deg"]
_l_(367335)
humidity = _c_(367338, _a_(367337, _n_(367336, "myWeather", lambda: myWeather), "get_humidity"))
_l_(367339)
temperature = _c_(367342, _a_(367341, _n_(367340, "myWeather", lambda: myWeather), "get_temperature"), "celsius")
_l_(367343)
high = _n_(367344, "temperature", lambda: temperature)["temp_max"]
_l_(367345)
low = _n_(367346, "temperature", lambda: temperature)["temp_min"]
_l_(367347)
current = _n_(367348, "temperature", lambda: temperature)["temp"]
_l_(367349)
date = _c_(367355, _a_(367354, _c_(367353, _a_(367352, _a_(367351, _n_(367350, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%D")
_l_(367356)
time = _c_(367362, _a_(367361, _c_(367360, _a_(367359, _a_(367358, _n_(367357, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%H")
_l_(367363)

done=0
_l_(367364)

while True:
    _l_(367449)

    if _c_(367370, _a_(367369, _c_(367368, _a_(367367, _a_(367366, _n_(367365, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%S") == "00" and _n_(367371, "done", lambda: done) == 0:
        _l_(367439)

        done=1
        _l_(367372)
        csvfile = _c_(367374, _n_(367373, "open", lambda: open), "weatherCSV.csv", "w")
        _l_(367375)
        writeCSV = _c_(367379, _a_(367377, _n_(367376, "csv", lambda: csv), "writer"), _n_(367378, "csvfile", lambda: csvfile), delimiter=",")
        _l_(367380)

        myWeather = _c_(367383, _a_(367382, _n_(367381, "myHouse", lambda: myHouse), "get_weather"))
        _l_(367384)
        wind = _a_(367386, _n_(367385, "myWeather", lambda: myWeather), "get_wind")
        _l_(367387)
        windspeed = _n_(367388, "wind", lambda: wind)["speed"]
        _l_(367389)
        windangle = _n_(367390, "wind", lambda: wind)["deg"]
        _l_(367391)
        humidity = _c_(367394, _a_(367393, _n_(367392, "myWeather", lambda: myWeather), "get_humidity"))
        _l_(367395)
        temperature = _c_(367398, _a_(367397, _n_(367396, "myWeather", lambda: myWeather), "get_temperature"), "celsius")
        _l_(367399)
        high = _n_(367400, "temperature", lambda: temperature)["temp_max"]
        _l_(367401)
        low = _n_(367402, "temperature", lambda: temperature)["temp_min"]
        _l_(367403)
        current = _n_(367404, "temperature", lambda: temperature)["temp"]
        _l_(367405)
        date = _c_(367411, _a_(367410, _c_(367409, _a_(367408, _a_(367407, _n_(367406, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%D")
        _l_(367412)
        time = _c_(367418, _a_(367417, _c_(367416, _a_(367415, _a_(367414, _n_(367413, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%H")
        _l_(367419)


        _c_(367430, _a_(367421, _n_(367420, "writeCSV", lambda: writeCSV), "writerow"), [_n_(367422, "current", lambda: current),_n_(367423, "high", lambda: high),_n_(367424, "low", lambda: low),_n_(367425, "windspeed", lambda: windspeed),_n_(367426, "windangle", lambda: windangle),_n_(367427, "humidity", lambda: humidity),_n_(367428, "date", lambda: date),_n_(367429, "time", lambda: time)])
        _l_(367431)
        _c_(367434, _a_(367433, _n_(367432, "csvfile", lambda: csvfile), "close"))
        _l_(367435)
        _c_(367437, _n_(367436, "print", lambda: print), "Added to file")
        _l_(367438)

    if _c_(367445, _a_(367444, _c_(367443, _a_(367442, _a_(367441, _n_(367440, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%S") == "30" and _n_(367446, "done", lambda: done) == 1:
        _l_(367448)

        done=0
        _l_(367447)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47298943/made-a-program-in-python-but-get-typeerror-method-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyowm
    _l_(350127)

except ImportError:
    pass
try:
    import datetime
    _l_(350129)

except ImportError:
    pass
try:
    import csv
    _l_(350131)

except ImportError:
    pass

W = _c_(350134, _a_(350133, _n_(350132, "pyowm", lambda: pyowm), "OWM"), "****************************")
_l_(350135)
myHouse = _c_(350138, _a_(350137, _n_(350136, "W", lambda: W), "weather_at_place"), "St. albert,Canada")
_l_(350139)
myWeather = _c_(350142, _a_(350141, _n_(350140, "myHouse", lambda: myHouse), "get_weather"))
_l_(350143)
wind = _c_(350146, _a_(350145, _n_(350144, "myWeather", lambda: myWeather), "get_wind"))
_l_(350147)
windspeed = _n_(350148, "wind", lambda: wind)["speed"]
_l_(350149)
windangle = _n_(350150, "wind", lambda: wind)["deg"]
_l_(350151)
humidity = _c_(350154, _a_(350153, _n_(350152, "myWeather", lambda: myWeather), "get_humidity"))
_l_(350155)
temperature = _c_(350158, _a_(350157, _n_(350156, "myWeather", lambda: myWeather), "get_temperature"), "celsius")
_l_(350159)
high = _n_(350160, "temperature", lambda: temperature)["temp_max"]
_l_(350161)
low = _n_(350162, "temperature", lambda: temperature)["temp_min"]
_l_(350163)
current = _n_(350164, "temperature", lambda: temperature)["temp"]
_l_(350165)
date = _c_(350171, _a_(350170, _c_(350169, _a_(350168, _a_(350167, _n_(350166, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%D")
_l_(350172)
time = _c_(350178, _a_(350177, _c_(350176, _a_(350175, _a_(350174, _n_(350173, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%H")
_l_(350179)

done=0
_l_(350180)

while True:
    _l_(350265)

    if _c_(350186, _a_(350185, _c_(350184, _a_(350183, _a_(350182, _n_(350181, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%S") == "00" and _n_(350187, "done", lambda: done) == 0:
        _l_(350255)

        done=1
        _l_(350188)
        csvfile = _c_(350190, _n_(350189, "open", lambda: open), "weatherCSV.csv", "w")
        _l_(350191)
        writeCSV = _c_(350195, _a_(350193, _n_(350192, "csv", lambda: csv), "writer"), _n_(350194, "csvfile", lambda: csvfile), delimiter=",")
        _l_(350196)

        myWeather = _c_(350199, _a_(350198, _n_(350197, "myHouse", lambda: myHouse), "get_weather"))
        _l_(350200)
        wind = _a_(350202, _n_(350201, "myWeather", lambda: myWeather), "get_wind")
        _l_(350203)
        windspeed = _n_(350204, "wind", lambda: wind)["speed"]
        _l_(350205)
        windangle = _n_(350206, "wind", lambda: wind)["deg"]
        _l_(350207)
        humidity = _c_(350210, _a_(350209, _n_(350208, "myWeather", lambda: myWeather), "get_humidity"))
        _l_(350211)
        temperature = _c_(350214, _a_(350213, _n_(350212, "myWeather", lambda: myWeather), "get_temperature"), "celsius")
        _l_(350215)
        high = _n_(350216, "temperature", lambda: temperature)["temp_max"]
        _l_(350217)
        low = _n_(350218, "temperature", lambda: temperature)["temp_min"]
        _l_(350219)
        current = _n_(350220, "temperature", lambda: temperature)["temp"]
        _l_(350221)
        date = _c_(350227, _a_(350226, _c_(350225, _a_(350224, _a_(350223, _n_(350222, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%D")
        _l_(350228)
        time = _c_(350234, _a_(350233, _c_(350232, _a_(350231, _a_(350230, _n_(350229, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%H")
        _l_(350235)


        _c_(350246, _a_(350237, _n_(350236, "writeCSV", lambda: writeCSV), "writerow"), [_n_(350238, "current", lambda: current),_n_(350239, "high", lambda: high),_n_(350240, "low", lambda: low),_n_(350241, "windspeed", lambda: windspeed),_n_(350242, "windangle", lambda: windangle),_n_(350243, "humidity", lambda: humidity),_n_(350244, "date", lambda: date),_n_(350245, "time", lambda: time)])
        _l_(350247)
        _c_(350250, _a_(350249, _n_(350248, "csvfile", lambda: csvfile), "close"))
        _l_(350251)
        _c_(350253, _n_(350252, "print", lambda: print), "Added to file")
        _l_(350254)

    if _c_(350261, _a_(350260, _c_(350259, _a_(350258, _a_(350257, _n_(350256, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%S") == "30" and _n_(350262, "done", lambda: done) == 1:
        _l_(350264)

        done=0
        _l_(350263)
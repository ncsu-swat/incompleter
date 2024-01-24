# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43747198/typeerror-cant-convert-int-object-to-str-implicitly-sorting-array-issue
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def main ():
    _l_(441881)

    rainfall = _c_(441833, _n_(441832, "rainInput", lambda: rainInput))
    _l_(441834)
    totalRain = _c_(441837, _n_(441835, "totalRainfall", lambda: totalRainfall), _n_(441836, "rainfall", lambda: rainfall))
    _l_(441838)
    average_Rainfall = _c_(441841, _n_(441839, "averageRainfall", lambda: averageRainfall), _n_(441840, "totalRain", lambda: totalRain))
    _l_(441842)
    highestMonth, highestMonthly = _c_(441845, _n_(441843, "highestMonthNumber", lambda: highestMonthNumber), _n_(441844, "rainfall", lambda: rainfall))
    _l_(441846)
    lowestMonth, lowestMonthly = _c_(441849, _n_(441847, "lowestMonthNumber", lambda: lowestMonthNumber), _n_(441848, "rainfall", lambda: rainfall))
    _l_(441850)
    _n_(441851, "print", lambda: print) #this is for spacing output
    _l_(441852) #this is for spacing output
    _c_(441857, _n_(441853, "print", lambda: print), 'The total rainfall for the year was: ' +_c_(441856, _n_(441854, "str", lambda: str), _n_(441855, "totalRain", lambda: totalRain)) + ' inche(s)')
    _l_(441858)
    _n_(441859, "print", lambda: print) #this is for spacing output
    _l_(441860) #this is for spacing output
    _c_(441865, _n_(441861, "print", lambda: print), 'The average rainfall for the year was: ' +_c_(441864, _n_(441862, "str", lambda: str), _n_(441863, "average_Rainfall", lambda: average_Rainfall)) +\
          ' inche(s)') 
    _l_(441866) 
    _n_(441867, "print", lambda: print) #this is for spacing in output
    _l_(441868) #this is for spacing in output
    _c_(441872, _n_(441869, "print", lambda: print), 'The highest amount of rain was', _n_(441870, "highestMonthly", lambda: highestMonthly), 'in' , _n_(441871, "highestMonth", lambda: highestMonth))
    _l_(441873)
    _n_(441874, "print", lambda: print) #this is for spacing in output
    _l_(441875) #this is for spacing in output
    _c_(441879, _n_(441876, "print", lambda: print), 'The lowest amount of rain was', _n_(441877, "lowestMonthly", lambda: lowestMonthly), 'in' , _n_(441878, "lowestMonth", lambda: lowestMonth))
    _l_(441880)

def rainInput ():
    _l_(441900)

    rainfall = ['January','Febuary','March','April','May','June','July','August'\
    ,'September','October','November','December']
    _l_(441882)
    month = 0
    _l_(441883)
    while _n_(441884, "month", lambda: month) < _c_(441887, _n_(441885, "len", lambda: len), _n_(441886, "rainfall", lambda: rainfall)):
        _l_(441897)

        _n_(441888, "rainfall", lambda: rainfall)[_n_(441889, "month", lambda: month)] = _c_(441894, _n_(441890, "input", lambda: input), 'Please enter the amount for month ' + _c_(441893, _n_(441891, "str", lambda: str), _n_(441892, "month", lambda: month) + 1) + ': ')
        _l_(441895)
        month += 1
        _l_(441896)
    aux = _n_(441898, "rainfall", lambda: rainfall)
    _l_(441899)

    return aux

def totalRainfall (rainfall):
    _l_(441915)

    totalRain = 0
    _l_(441901)
    month = 0
    _l_(441902)
    while _n_(441903, "month", lambda: month) < _c_(441906, _n_(441904, "len", lambda: len), _n_(441905, "rainfall", lambda: rainfall)):
        _l_(441912)

        totalRain = _n_(441907, "rainfall", lambda: rainfall)[_n_(441908, "month", lambda: month)] + _n_(441909, "totalRain", lambda: totalRain)
        _l_(441910)
        month += 1
        _l_(441911)
    aux = _n_(441913, "totalRain", lambda: totalRain)
    _l_(441914)

    return aux

def averageRainfall (totalRain):
    _l_(441920)

    average_Rainfall = _n_(441916, "totalRain", lambda: totalRain) / 12
    _l_(441917)
    aux = _n_(441918, "average_Rainfall", lambda: average_Rainfall)
    _l_(441919)

    return aux

def highestMonthNumber (rainfall):
    _l_(441938)

    month = ['January','Febuary','March','April','May','June','July','August'\
                ,'September','October','November','December']
    _l_(441921)
    highestMonthly = 0
    _l_(441922)
    for m, n in _c_(441925, _n_(441923, "enumerate", lambda: enumerate), _n_(441924, "rainfall", lambda: rainfall)):
        _l_(441933)

        if _n_(441926, "n", lambda: n) > _n_(441927, "highestMonthly", lambda: highestMonthly):
            _l_(441932)

            highestMonthly = _n_(441928, "n", lambda: n)
            _l_(441929)
            highestMonth = _n_(441930, "m", lambda: m)
            _l_(441931)
    aux = _n_(441934, "month", lambda: month)[_n_(441935, "highestMonth", lambda: highestMonth)], _n_(441936, "highestMonthly", lambda: highestMonthly)
    _l_(441937)

    return aux

def lowestMonthNumber (rainfall):
    _l_(441956)

    month = ['January','Febuary','March','April','May','June','July','August'\
                ,'September','October','November','December']
    _l_(441939)
    lowestMonthly = 0
    _l_(441940)
    for m, n in _c_(441943, _n_(441941, "enumerate", lambda: enumerate), _n_(441942, "rainfall", lambda: rainfall)):
        _l_(441951)

        if _n_(441944, "n", lambda: n) < _n_(441945, "lowestMonthly", lambda: lowestMonthly):
            _l_(441950)

            lowestMonthly = _n_(441946, "n", lambda: n)
            _l_(441947)
            lowestMonth = _n_(441948, "m", lambda: m)
            _l_(441949)
    aux = _n_(441952, "month", lambda: month)[_n_(441953, "lowestMonth", lambda: lowestMonth)], _n_(441954, "lowestMonthly", lambda: lowestMonthly)
    _l_(441955)

    return aux

_c_(441958, _n_(441957, "main", lambda: main))
_l_(441959)
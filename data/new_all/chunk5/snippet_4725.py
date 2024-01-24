# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51320783/python-3-6-tkinter-not-finding-file-filenotfounderror-errno-2-no-such-fil
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.animation as animation
    _l_(665497)

except ImportError:
    pass

def animate(i):
    _l_(665543)

    pullData = _c_(665501, _a_(665500, _c_(665499, _n_(665498, "open", lambda: open), 'sampleData.csv', "r"), "read"))
    _l_(665502)
    dataList = _c_(665505, _a_(665504, _n_(665503, "pullData", lambda: pullData), "split"), '\n')
    _l_(665506)
    xList =[]
    _l_(665507)
    yList = []
    _l_(665508)
    for eachLine in _n_(665509, "dataList", lambda: dataList):
        _l_(665532)

        if _c_(665512, _n_(665510, "len", lambda: len), _n_(665511, "eachLine", lambda: eachLine))>1:
            _l_(665531)

            x, y = _c_(665515, _a_(665514, _n_(665513, "eachLine", lambda: eachLine), "split"), ',')
            _l_(665516)
            _c_(665522, _a_(665518, _n_(665517, "xList", lambda: xList), "append"), _c_(665521, _n_(665519, "int", lambda: int), _n_(665520, "x", lambda: x)))
            _l_(665523)
            _c_(665529, _a_(665525, _n_(665524, "yList", lambda: yList), "append"), _c_(665528, _n_(665526, "int", lambda: int), _n_(665527, "y", lambda: y)))
            _l_(665530)
    _c_(665535, _a_(665534, _n_(665533, "a", lambda: a), "clear"))
    _l_(665536)
    _c_(665541, _a_(665538, _n_(665537, "a", lambda: a), "plot"), _n_(665539, "xList", lambda: xList), _n_(665540, "yList", lambda: yList) )
    _l_(665542)
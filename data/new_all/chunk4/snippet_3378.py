# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75170132/typeerror-int-object-is-not-subscriptable-dbscan
#retrieving the length and the breadth of the image
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
length = _c_(597310, _n_(597308, "len", lambda: len), _n_(597309, "img", lambda: img))
_l_(597311)
breadth = _c_(597314, _n_(597312, "len", lambda: len), _n_(597313, "img", lambda: img)[0])
_l_(597315)
if _n_(597316, "isdbscan", lambda: (isdbscan)):
    _l_(597395)

    _c_(597319, _n_(597317, "print", lambda: print), "Number of clusters = ",_n_(597318, "maxclus", lambda: maxclus))
    _l_(597320)
    for a in _c_(597323, _n_(597321, "range", lambda: range), 0,_n_(597322, "length", lambda: length)):
        _l_(597344)

        for aa in _c_(597326, _n_(597324, "range", lambda: range), 0,_n_(597325, "breadth", lambda: breadth)):
            _l_(597343)

            #here we want to change all the outliners to black color  
            if (_n_(597327, "clusters", lambda: clusters)[_n_(597328, "a", lambda: a)][_n_(597329, "aa", lambda: aa)] == -1):
                _l_(597342)

                _n_(597330, "img", lambda: img)[_n_(597331, "a", lambda: a)][_n_(597332, "aa", lambda: aa)][0]= 0
                _l_(597333)
                _n_(597334, "img", lambda: img)[_n_(597335, "a", lambda: a)][_n_(597336, "aa", lambda: aa)][1]= 0
                _l_(597337)
                _n_(597338, "img", lambda: img)[_n_(597339, "a", lambda: a)][_n_(597340, "aa", lambda: aa)][2]= 0
                _l_(597341)
    for z in _c_(597347, _n_(597345, "range", lambda: range), 0,_n_(597346, "maxclus", lambda: maxclus)):
        _l_(597394)

        #we randomly try to select the colors for the clusters 
        b = _c_(597352, _a_(597349, _n_(597348, "random", lambda: random), "sample"), _c_(597351, _n_(597350, "range", lambda: range), 0,255),1)
        _l_(597353)
        bb = _c_(597358, _a_(597355, _n_(597354, "random", lambda: random), "sample"), _c_(597357, _n_(597356, "range", lambda: range), 0,255),1)
        _l_(597359)
        bbb = _c_(597364, _a_(597361, _n_(597360, "random", lambda: random), "sample"), _c_(597363, _n_(597362, "range", lambda: range), 0,255),1)
        _l_(597365)
        for a in _c_(597368, _n_(597366, "range", lambda: range), 0,_n_(597367, "length", lambda: length)):
            _l_(597393)

            for aa in _c_(597371, _n_(597369, "range", lambda: range), 0,_n_(597370, "breadth", lambda: breadth)):
                _l_(597392)

                if (_n_(597372, "clusters", lambda: clusters)[_n_(597373, "a", lambda: a)][_n_(597374, "aa", lambda: aa)] == _n_(597375, "z", lambda: z)+1):
                    _l_(597391)

                    _n_(597376, "img", lambda: img)[_n_(597377, "a", lambda: a)][_n_(597378, "aa", lambda: aa)][0]= _n_(597379, "b", lambda: b)[0]
                    _l_(597380)
                    _n_(597381, "img", lambda: img)[_n_(597382, "a", lambda: a)][_n_(597383, "aa", lambda: aa)][1]= _n_(597384, "bb", lambda: bb)[0]
                    _l_(597385)
                    _n_(597386, "img", lambda: img)[_n_(597387, "a", lambda: a)][_n_(597388, "aa", lambda: aa)][2]= _n_(597389, "bbb", lambda: bbb)[0]
                    _l_(597390)
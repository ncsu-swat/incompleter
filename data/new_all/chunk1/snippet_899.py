# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46158510/nameerror-on-line-8-if-button-a-is-pressed
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
start = 0
_l_(382315)
ind = 0
_l_(382316)
ind1 = 5
_l_(382317)
c = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': [], '12': [], '13': [], '14': [], '15': [], '16': [], '17': [], '18': [], '19': [], '20': []}
_l_(382318)
d  = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0}
_l_(382319)
#Registering#
if _a_(382321, _n_(382320, "button_a", lambda: button_a), "is_pressed"):
    _l_(382381)

    start=1
    _l_(382322)
    _c_(382325, _a_(382324, _n_(382323, "display", lambda: display), "scroll"), "Index No.")
    _l_(382326)
elif _a_(382328, _n_(382327, "button_b", lambda: button_b), "is_pressed"):
    _l_(382380)

    start=0
    _l_(382329)


    if _n_(382330, "start", lambda: start)==1:
        _l_(382379)

        rgs=''
        _l_(382331)
        ind=0
        _l_(382332)
        while True:
            _l_(382378)

            rgs=''
            _l_(382333)
            while _n_(382334, "rgs", lambda: rgs)=='':
                _l_(382377)

                _c_(382337, _a_(382336, _n_(382335, "display", lambda: display), "scroll"), "Password")
                _l_(382338)
                for i in _c_(382340, _n_(382339, "range", lambda: range), 8):
                    _l_(382349)

                    if _a_(382342, _n_(382341, "button_a", lambda: button_a), "is_pressed"):
                        _l_(382348)

                        rgs+='0'
                        _l_(382343)
                    elif _a_(382345, _n_(382344, "button_b", lambda: button_b), "is_pressed"):
                        _l_(382347)

                        rgs+='1'
                        _l_(382346)
                for j in _c_(382351, _n_(382350, "range", lambda: range), 20):
                    _l_(382376)

                    if _n_(382352, "c", lambda: c)[_n_(382353, "j", lambda: j)][1]==_n_(382354, "rgs", lambda: rgs):
                        _l_(382375)

                        rgs=''
                        _l_(382355)
                        _c_(382358, _a_(382357, _n_(382356, "display", lambda: display), "scroll"), "PASSWORD USED")
                        _l_(382359)
                    else:
                        for q in _c_(382361, _n_(382360, "range", lambda: range), 20):
                            _l_(382374)

                            if _n_(382362, "c", lambda: c)[_n_(382363, "q", lambda: q)]==_n_(382364, "ind", lambda: ind):
                                _l_(382369)

                                _n_(382365, "c", lambda: c)[_n_(382366, "q", lambda: q)][1]=_n_(382367, "rgs", lambda: rgs)
                                _l_(382368)
                            _c_(382372, _a_(382371, _n_(382370, "display", lambda: display), "show"), "OK")
                            _l_(382373)
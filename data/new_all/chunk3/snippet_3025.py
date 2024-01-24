# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53622257/attributeerror-nonetype-object-has-no-attribute-send-pigpiod
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(537203)

except ImportError:
    pass
try:
    import pigpio
    _l_(537205)

except ImportError:
    pass

START_DELAY=600
_l_(537206)
FINAL_DELAY=500
_l_(537207)
STEP=1
_l_(537208)

GPIO=20
_l_(537209)

pi = _c_(537212, _a_(537211, _n_(537210, "pigpio", lambda: pigpio), "pi"))
_l_(537213)

_c_(537219, _a_(537215, _n_(537214, "pi", lambda: pi), "set_mode"), _n_(537216, "GPIO", lambda: GPIO), _a_(537218, _n_(537217, "pigpio", lambda: pigpio), "OUTPUT"))
_l_(537220)
_c_(537225, _a_(537222, _n_(537221, "pi", lambda: pi), "set_mode"), 21, _a_(537224, _n_(537223, "pigpio", lambda: pigpio), "OUTPUT"))
_l_(537226)
_c_(537231, _a_(537228, _n_(537227, "pi", lambda: pi), "set_mode"), 26,_a_(537230, _n_(537229, "pigpio", lambda: pigpio), "INPUT"))
_l_(537232)
_c_(537237, _a_(537234, _n_(537233, "pi", lambda: pi), "set_mode"), 16,_a_(537236, _n_(537235, "pigpio", lambda: pigpio), "INPUT"))
_l_(537238)
#pi.write(21,1)
_c_(537241, _a_(537240, _n_(537239, "pi", lambda: pi), "wave_clear"))
_l_(537242)

statee = 0
_l_(537243)
try:
    _l_(537399)

    while True:
        _l_(537385)


        _c_(537247, _a_(537245, _n_(537244, "pi", lambda: pi), "write"), 21,_n_(537246, "statee", lambda: statee))
        _l_(537248)
        _c_(537251, _a_(537250, _n_(537249, "pi", lambda: pi), "wave_clear"))
        _l_(537252)

        wf=[]
        _l_(537253)
        offset = _c_(537256, _a_(537255, _n_(537254, "pi", lambda: pi), "wave_get_micros"))
        _l_(537257)
        for delay in _c_(537262, _n_(537258, "range", lambda: range), _n_(537259, "START_DELAY", lambda: START_DELAY), _n_(537260, "FINAL_DELAY", lambda: FINAL_DELAY), -_n_(537261, "STEP", lambda: STEP)):
            _l_(537281)

            _c_(537270, _a_(537264, _n_(537263, "wf", lambda: wf), "append"), _c_(537269, _a_(537266, _n_(537265, "pigpio", lambda: pigpio), "pulse"), 1<<_n_(537267, "GPIO", lambda: GPIO), 0,       _n_(537268, "delay", lambda: delay)))
            _l_(537271)
            _c_(537279, _a_(537273, _n_(537272, "wf", lambda: wf), "append"), _c_(537278, _a_(537275, _n_(537274, "pigpio", lambda: pigpio), "pulse"), 0,       1<<_n_(537276, "GPIO", lambda: GPIO), _n_(537277, "delay", lambda: delay)))
            _l_(537280)

        for i in _c_(537283, _n_(537282, "range", lambda: range), 500):
            _l_(537302)

            _c_(537291, _a_(537285, _n_(537284, "wf", lambda: wf), "append"), _c_(537290, _a_(537287, _n_(537286, "pigpio", lambda: pigpio), "pulse"), 1<<_n_(537288, "GPIO", lambda: GPIO), 0,       _n_(537289, "FINAL_DELAY", lambda: FINAL_DELAY)))
            _l_(537292)
            _c_(537300, _a_(537294, _n_(537293, "wf", lambda: wf), "append"), _c_(537299, _a_(537296, _n_(537295, "pigpio", lambda: pigpio), "pulse"), 0,       1<<_n_(537297, "GPIO", lambda: GPIO), _n_(537298, "FINAL_DELAY", lambda: FINAL_DELAY)))
            _l_(537301)
        _c_(537309, _a_(537304, _n_(537303, "wf", lambda: wf), "append"), _c_(537308, _a_(537306, _n_(537305, "pigpio", lambda: pigpio), "pulse"), 0, 0, _n_(537307, "offset", lambda: offset)))
        _l_(537310)

        for delay in _c_(537315, _n_(537311, "range", lambda: range), _n_(537312, "FINAL_DELAY", lambda: FINAL_DELAY), _n_(537313, "START_DELAY", lambda: START_DELAY), _n_(537314, "STEP", lambda: STEP)):
            _l_(537334)

            _c_(537323, _a_(537317, _n_(537316, "wf", lambda: wf), "append"), _c_(537322, _a_(537319, _n_(537318, "pigpio", lambda: pigpio), "pulse"), 1<<_n_(537320, "GPIO", lambda: GPIO), 0,       _n_(537321, "delay", lambda: delay)))
            _l_(537324)
            _c_(537332, _a_(537326, _n_(537325, "wf", lambda: wf), "append"), _c_(537331, _a_(537328, _n_(537327, "pigpio", lambda: pigpio), "pulse"), 0,       1<<_n_(537329, "GPIO", lambda: GPIO), _n_(537330, "delay", lambda: delay)))
            _l_(537333)

        _c_(537338, _a_(537336, _n_(537335, "pi", lambda: pi), "wave_add_generic"), _n_(537337, "wf", lambda: wf))
        _l_(537339)

        wid2 = _c_(537342, _a_(537341, _n_(537340, "pi", lambda: pi), "wave_create"))
        _l_(537343)

        #pi.wave_send_once(wid2)
        _c_(537349, _a_(537345, _n_(537344, "pi", lambda: pi), "wave_send_using_mode"), _n_(537346, "wid2", lambda: wid2), _a_(537348, _n_(537347, "pigpio", lambda: pigpio), "WAVE_MODE_ONE_SHOT_SYNC"))
        _l_(537350)

        if _c_(537353, _a_(537352, _n_(537351, "pi", lambda: pi), "read"), 26) == 0:
            _l_(537362)

            _c_(537356, _a_(537355, _n_(537354, "pi", lambda: pi), "wave_tx_stop"))
            _l_(537357)
            _c_(537360, _a_(537359, _n_(537358, "pi", lambda: pi), "stop"))
            _l_(537361)
        if _c_(537365, _a_(537364, _n_(537363, "pi", lambda: pi), "read"), 16) == 0:
            _l_(537374)

            _c_(537368, _a_(537367, _n_(537366, "pi", lambda: pi), "wave_tx_stop"))
            _l_(537369)
            _c_(537372, _a_(537371, _n_(537370, "pi", lambda: pi), "stop"))
            _l_(537373)

        _c_(537377, _a_(537376, _n_(537375, "time", lambda: time), "sleep"), 0.75)
        _l_(537378)
        if _n_(537379, "statee", lambda: statee) == 0:
            _l_(537384)

            statee = 1
            _l_(537380)
        elif _n_(537381, "statee", lambda: statee) == 1:
            _l_(537383)

            statee = 0
            _l_(537382)
except _n_(537386, "KeyboardInterrupt", lambda: KeyboardInterrupt):
    _l_(537398)

    _c_(537388, _n_(537387, "print", lambda: print), "\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
    _l_(537389)
    _c_(537392, _a_(537391, _n_(537390, "pi", lambda: pi), "wave_tx_stop"))
    _l_(537393)
    _c_(537396, _a_(537395, _n_(537394, "pi", lambda: pi), "stop"))
    _l_(537397)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62721117/continuous-typeerror-function-object-is-not-subscriptable-in-python-3-8
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = 0
_l_(533425)
df, mavg, start = _c_(533427, _n_(533426, "getStock", lambda: getStock), companyName='AAPL', month=24, plot=True)
_l_(533428)

dayslist = []
_l_(533429)
while _n_(533430, "x", lambda: x) != 7:
    _l_(533448)

    day = _n_(533431, "start", lambda: start) + _c_(533436, _a_(533434, _a_(533433, _n_(533432, "dateutil", lambda: dateutil), "relativedelta"), "relativedelta"), days=_n_(533435, "x", lambda: x))
    _l_(533437)
    _c_(533445, _a_(533439, _n_(533438, "dayslist", lambda: dayslist), "append"), _c_(533444, _n_(533440, "int", lambda: int), _c_(533443, _a_(533442, _n_(533441, "day", lambda: day), "strftime"), '%Y%m%d')))
    _l_(533446)
    x += 1
    _l_(533447)

dates = _c_(533452, _a_(533450, _n_(533449, "np", lambda: np), "array"), _n_(533451, "dayslist", lambda: dayslist))
_l_(533453)
prediction_out = 7
_l_(533454)

_n_(533455, "df", lambda: df)['Prediction'] = _c_(533459, _a_(533457, _n_(533456, "df", lambda: df), "shift"), -_n_(533458, "prediction_out", lambda: prediction_out))
_l_(533460)
_c_(533465, _n_(533461, "print", lambda: print), _c_(533464, _a_(533463, _n_(533462, "df", lambda: df), "tail")))
_l_(533466)

x = _c_(533472, _a_(533468, _n_(533467, "np", lambda: np), "array"), _c_(533471, _a_(533470, _n_(533469, "df", lambda: df), "drop"), ['Prediction']))
_l_(533473)
y = _c_(533477, _a_(533475, _n_(533474, "np", lambda: np), "array"), _n_(533476, "df", lambda: df)["Prediction"])
_l_(533478)
x = _n_(533479, "x", lambda: x)[:-_n_(533480, "prediction_out", lambda: prediction_out)]
_l_(533481)
y = _n_(533482, "y", lambda: y)[:-_n_(533483, "prediction_out", lambda: prediction_out)]
_l_(533484)

x = _c_(533487, _a_(533486, _n_(533485, "x", lambda: x), "reshape"), -1, 1)
_l_(533488)
y = _c_(533491, _a_(533490, _n_(533489, "y", lambda: y), "reshape"), -1, 1)
_l_(533492)

x_train, x_test, y_train, y_test = _c_(533496, _n_(533493, "train_test_split", lambda: train_test_split), _n_(533494, "x", lambda: x), _n_(533495, "y", lambda: y), test_size=0.2)
_l_(533497)

svm_rbf = _c_(533499, _n_(533498, "SVR", lambda: SVR), kernel='rbf', C=1e3, gamma=0.1)
_l_(533500)
_c_(533505, _a_(533502, _n_(533501, "svm_rbf", lambda: svm_rbf), "fit"), _n_(533503, "x_train", lambda: x_train), _n_(533504, "y_train", lambda: y_train))
_l_(533506)

svm_confidence = _c_(533511, _a_(533508, _n_(533507, "svm_rbf", lambda: svm_rbf), "score"), _n_(533509, "x_test", lambda: x_test), _n_(533510, "y_test", lambda: y_test))
_l_(533512)
_c_(533517, _n_(533513, "print", lambda: print), _c_(533516, _a_(533514, 'SVM confidence is {}.', "format"), _n_(533515, "svm_confidence", lambda: svm_confidence)))
_l_(533518)

x_forecast = _c_(533524, _a_(533520, _n_(533519, "np", lambda: np), "array"), _c_(533523, _a_(533522, _n_(533521, "df", lambda: df), "drop"), ['Prediction']))[-_n_(533525, "prediction_out", lambda: prediction_out):]
_l_(533526)
_c_(533529, _n_(533527, "print", lambda: print), _n_(533528, "x_forecast", lambda: x_forecast))
_l_(533530)

fPlotList = []
_l_(533531)
x = 0
_l_(533532)
while _n_(533533, "x", lambda: x) != 7:
    _l_(533541)

    _c_(533538, _a_(533535, _n_(533534, "fPlotList", lambda: fPlotList), "append"), _n_(533536, "x_forecast", lambda: x_forecast)[_n_(533537, "x", lambda: x)])
    _l_(533539)
    x += 1
    _l_(533540)

_a_(533543, _n_(533542, "plt", lambda: plt), "plot")[_n_(533544, "fPlotList", lambda: fPlotList), _n_(533545, "dayslist", lambda: dayslist)]
_l_(533546)
_c_(533549, _a_(533548, _n_(533547, "plt", lambda: plt), "show"))
_l_(533550)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60579185/typeerror-compositemodel-object-is-not-callable-when-trying-to-fit-a-compos
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
gausmodel = _c_(558048, _n_(558047, "GaussianModel", lambda: GaussianModel))
_l_(558049)
linemodel = _c_(558051, _n_(558050, "LinearModel", lambda: LinearModel))
_l_(558052)

params = _c_(558055, _a_(558054, _n_(558053, "linemodel", lambda: linemodel), "make_params"), intercept=40, slope=0)
_l_(558056)
params += _c_(558059, _a_(558058, _n_(558057, "gausmodel", lambda: gausmodel), "make_params"), cen=100, sigma=10, amplitude=100)
_l_(558060)

model = _n_(558061, "gausmodel", lambda: gausmodel) + _n_(558062, "linemodel", lambda: linemodel)
_l_(558063)

x = _c_(558069, _a_(558065, _n_(558064, "pd", lambda: pd), "DataFrame"), _c_(558068, _a_(558067, _n_(558066, "np", lambda: np), "arange"), 0, 351), columns=['Pixel Position'])
_l_(558070)
df = _c_(558075, _a_(558072, _n_(558071, "pd", lambda: pd), "concat"), [_n_(558073, "x", lambda: x), _n_(558074, "intens", lambda: intens)], axis=1)
_l_(558076)

# Create models for fitting
peak1 = _c_(558078, _n_(558077, "model", lambda: model), prefix='p1_')
_l_(558079)
peak2 = _c_(558081, _n_(558080, "model", lambda: model), prefix='p2_')
_l_(558082)
peak3 = _c_(558084, _n_(558083, "model", lambda: model), prefix='p3_')
_l_(558085)
peak4 = _c_(558087, _n_(558086, "model", lambda: model), prefix='p4_')
_l_(558088)

# Set hints for start parameters
params = _c_(558091, _a_(558090, _n_(558089, "peak1", lambda: peak1), "make_params"))
_l_(558092)

_c_(558095, _a_(558094, _n_(558093, "params", lambda: params)['p1_cen'], "set"), value=80, min=70, max=100)
_l_(558096)
_c_(558099, _a_(558098, _n_(558097, "params", lambda: params)['p1_sigma'], "set"), value=10, min=5, max=20)
_l_(558100)
_c_(558103, _a_(558102, _n_(558101, "params", lambda: params)['p1_amplitude'], "set"), value=80, min=50, max=100000)
_l_(558104)
_c_(558107, _a_(558106, _n_(558105, "params", lambda: params)['p1_intercept'], "set"), value=40, min=30, max=55)
_l_(558108)
_c_(558111, _a_(558110, _n_(558109, "params", lambda: params)['p1_slope'], "set"), value=1, min=0.00001, max=5)
_l_(558112)

_c_(558118, _a_(558114, _n_(558113, "params", lambda: params), "update"), _c_(558117, _a_(558116, _n_(558115, "peak2", lambda: peak2), "make_params")))
_l_(558119)

_c_(558122, _a_(558121, _n_(558120, "params", lambda: params)['p2_center'], "set"), value=150, min=140, max=160)
_l_(558123)
_c_(558126, _a_(558125, _n_(558124, "params", lambda: params)['p2_sigma'], "set"), value=10, min=5, max=20)
_l_(558127)
_c_(558130, _a_(558129, _n_(558128, "params", lambda: params)['p2_amplitude'], "set"), value=80, min=50, max=100000)
_l_(558131)
_c_(558134, _a_(558133, _n_(558132, "params", lambda: params)['p2_intercept'], "set"), value=40, min=30, max=55)
_l_(558135)
_c_(558138, _a_(558137, _n_(558136, "params", lambda: params)['p2_slope'], "set"), value=1, min=0.00001, max=5)
_l_(558139)

_c_(558145, _a_(558141, _n_(558140, "params", lambda: params), "update"), _c_(558144, _a_(558143, _n_(558142, "peak3", lambda: peak3), "make_params")))
_l_(558146)

_c_(558149, _a_(558148, _n_(558147, "params", lambda: params)['p3_center'], "set"), value=200, min=180, max=220)
_l_(558150)
_c_(558153, _a_(558152, _n_(558151, "params", lambda: params)['p3_sigma'], "set"), value=10, min=5, max=20)
_l_(558154)
_c_(558157, _a_(558156, _n_(558155, "params", lambda: params)['p3_amplitude'], "set"), value=100, min=50, max=100000)
_l_(558158)
_c_(558161, _a_(558160, _n_(558159, "params", lambda: params)['p3_intercept'], "set"), value=40, min=30, max=55)
_l_(558162)
_c_(558165, _a_(558164, _n_(558163, "params", lambda: params)['p3_slope'], "set"), value=1, min=0.00001, max=5)
_l_(558166)

_c_(558172, _a_(558168, _n_(558167, "params", lambda: params), "update"), _c_(558171, _a_(558170, _n_(558169, "peak4", lambda: peak4), "make_params")))
_l_(558173)

_c_(558176, _a_(558175, _n_(558174, "params", lambda: params)['p4_center'], "set"), value=250, min=230, max=300)
_l_(558177)
_c_(558180, _a_(558179, _n_(558178, "params", lambda: params)['p4_sigma'], "set"), value=10, min=5, max=20)
_l_(558181)
_c_(558184, _a_(558183, _n_(558182, "params", lambda: params)['p4_amplitude'], "set"), value=100, min=50, max=100000)
_l_(558185)
_c_(558188, _a_(558187, _n_(558186, "params", lambda: params)['p4_intercept'], "set"), value=40, min=30, max=55)
_l_(558189)
_c_(558192, _a_(558191, _n_(558190, "params", lambda: params)['p4_slope'], "set"), value=1, min=0.00001, max=5)
_l_(558193)

# Define peak model
fit_model = _n_(558194, "peak1", lambda: peak1) + _n_(558195, "peak2", lambda: peak2) + _n_(558196, "peak3", lambda: peak3)
_l_(558197)

# Start fitting
init = _c_(558202, _a_(558199, _n_(558198, "fit_model", lambda: fit_model), "eval"), _n_(558200, "params", lambda: params), x=_n_(558201, "df", lambda: df))
_l_(558203)
result = _c_(558209, _a_(558205, _n_(558204, "fit_model", lambda: fit_model), "fit"), _n_(558206, "df", lambda: df)['Intensity'], _n_(558207, "params", lambda: params), x=_n_(558208, "df", lambda: df)['Pixel Position'])
_l_(558210)

_c_(558215, _n_(558211, "print", lambda: print), _c_(558214, _a_(558213, _n_(558212, "result", lambda: result), "fit_report")))
_l_(558216)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70855311/why-am-i-getting-a-type-error-int-not-iterable-while-using-plot-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
filenameWPC = _n_(587919, "root_name_of_output_file", lambda: root_name_of_output_file)+'GenPwr'
_l_(587920)
figWPC = _c_(587922, _n_(587921, "figure", lambda: figure), 1, dpi = 152 )
_l_(587923)
_c_(587926, _a_(587925, _n_(587924, "figWPC", lambda: figWPC), "set_size_inches"), 6, 4.05 )
_l_(587927)
_c_(587929, _n_(587928, "subplots_adjust", lambda: subplots_adjust), left=.12, bottom=0.12,right=.95, top=.95, hspace=.02, wspace=.18 )
_l_(587930)

_c_(587942, _a_(587932, _n_(587931, "plt", lambda: plt), "errorbar"), _n_(587933, "Vel", lambda: Vel), _n_(587934, "Power_", lambda: Power_)[_c_(587936, _n_(587935, "str", lambda: str), 'mean')], yerr=_n_(587937, "Power_", lambda: Power_)[_c_(587939, _n_(587938, "str", lambda: str), 'std')], 
dashes=_n_(587940, "lnsty", lambda: lnsty)[0],color=_n_(587941, "mkclr", lambda: mkclr)[0], clip_on=True,marker='o')
_l_(587943)

_c_(587945, _n_(587944, "xlim", lambda: xlim), 3,25.)
_l_(587946)
_c_(587948, _n_(587947, "ylim", lambda: ylim), 0,5500)
_l_(587949)
_c_(587951, _n_(587950, "xlabel", lambda: xlabel), 'Wind speed [m/s]' )   #NOVO
_l_(587952)   #NOVO
_c_(587954, _n_(587953, "ylabel", lambda: ylabel), 'Turbine Power [kW] '  )   #NOVO
_l_(587955)   #NOVO
_c_(587960, _n_(587956, "yticks", lambda: yticks), _c_(587959, _a_(587958, _n_(587957, "np", lambda: np), "arange"), 0,5500.01,500))
_l_(587961)
_c_(587966, _n_(587962, "xticks", lambda: xticks), _c_(587965, _a_(587964, _n_(587963, "np", lambda: np), "arange"), 3,25.01,1.))
_l_(587967)
_c_(587969, _n_(587968, "grid", lambda: grid), True)
_l_(587970)
_c_(587974, _n_(587971, "savefig", lambda: savefig), _n_(587972, "ResFolder", lambda: ResFolder)+_n_(587973, "filenameWPC", lambda: filenameWPC) +'.pdf')
_l_(587975)
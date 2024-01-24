# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36295380/typeerror-improper-input-n-2-must-not-exceed-m-1
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math
    _l_(416152)

except ImportError:
    pass

#stolen sig-fig function <--trust but verify
def round_figures(x, n):
    _l_(416169)

    aux = _c_(416167, _n_(416153, "round", lambda: round), _n_(416154, "x", lambda: x), _c_(416166, _n_(416155, "int", lambda: int), _n_(416156, "n", lambda: n) - _c_(416165, _a_(416158, _n_(416157, "math", lambda: math), "ceil"), _c_(416164, _a_(416160, _n_(416159, "math", lambda: math), "log10"), _c_(416163, _n_(416161, "abs", lambda: abs), _n_(416162, "x", lambda: x)))))) 
    _l_(416168) 
    return aux 

def try_michaelis_menten_fit( df, pretty=False ):
    _l_(416237)


    # auto-guess
    p0 = ( _c_(416172, _a_(416171, _n_(416170, "df", lambda: df)['productFinal'], "max")), _c_(416175, _a_(416174, _n_(416173, "df", lambda: df)['substrateConcentration'], "mean")) )
    _l_(416176)

    popt, pcov = _c_(416182, _n_(416177, "curve_fit", lambda: curve_fit), _n_(416178, "v", lambda: v), _n_(416179, "df", lambda: df)['substrateConcentration'], _n_(416180, "df", lambda: df)['productFinal'], p0=_n_(416181, "p0", lambda: p0) )
    _l_(416183)
    perr = _c_(416188, _n_(416184, "sqrt", lambda: sqrt), _c_(416187, _n_(416185, "diag", lambda: diag), _n_(416186, "pcov", lambda: pcov) ) )
    _l_(416189)

    kcat_km = _n_(416190, "popt", lambda: popt)[0] / _n_(416191, "popt", lambda: popt)[1]
    _l_(416192)
    # error propegation
    kcat_km_err = _c_(416198, _n_(416193, "sqrt", lambda: sqrt), (( (_n_(416194, "perr", lambda: perr)[0])  / _n_(416195, "popt", lambda: popt)[0])**2) + ((  (_n_(416196, "perr", lambda: perr)[1])  / _n_(416197, "popt", lambda: popt)[1])**2) )
    _l_(416199)

    kcat = ( _n_(416200, "popt", lambda: popt)[0] )
    _l_(416201)
    kcat_std_err = ( _n_(416202, "perr", lambda: perr)[0] )
    _l_(416203)

    km_uM = ( _n_(416204, "popt", lambda: popt)[1] * 1000000 )
    _l_(416205)
    km_std_err = ( _n_(416206, "perr", lambda: perr)[1] *1000000)
    _l_(416207)


    if _n_(416208, "pretty", lambda: pretty):
        _l_(416236)




        results = { 

        'kcat': _c_(416211, _n_(416209, "round_figures", lambda: round_figures), _n_(416210, "kcat", lambda: kcat), 3),
        'kcat_std_err': _c_(416214, _n_(416212, "round_figures", lambda: round_figures), _n_(416213, "kcat_std_err", lambda: kcat_std_err), 3),

        'km_uM': _c_(416217, _n_(416215, "round_figures", lambda: round_figures), _n_(416216, "km_uM", lambda: km_uM), 5),
        'km_std_err': _c_(416220, _n_(416218, "round_figures", lambda: round_figures), _n_(416219, "km_std_err", lambda: km_std_err), 3),

        'kcat/km': _c_(416223, _n_(416221, "round_figures", lambda: round_figures), _n_(416222, "kcat_km", lambda: kcat_km), 2),
        'kcat/km_err': _c_(416226, _n_(416224, "round_figures", lambda: round_figures), _n_(416225, "kcat_km_err", lambda: kcat_km_err), 2),

        }
        _l_(416227)
        aux = _c_(416231, _a_(416229, _n_(416228, "pandas", lambda: pandas), "Series"), _n_(416230, "results", lambda: results) )
        _l_(416232)

        return aux
    else: 
        aux = _n_(416233, "popt", lambda: popt), _n_(416234, "perr", lambda: perr) 
        _l_(416235) 
        return aux 

df = _c_(416240, _a_(416239, _n_(416238, "pandas", lambda: pandas), "read_csv"), 'PNP_Raw2Fittr.csv' ) 
_l_(416241) 



fits = _c_(416247, _a_(416245, _c_(416244, _a_(416243, _n_(416242, "df", lambda: df), "groupby"), 'sample'), "apply"), _n_(416246, "try_michaelis_menten_fit", lambda: try_michaelis_menten_fit), pretty=True ) 
_l_(416248) 
_c_(416251, _a_(416250, _n_(416249, "fits", lambda: fits), "to_csv"), 'fits_pretty_output.csv' )
_l_(416252)
_c_(416255, _n_(416253, "print", lambda: print), _n_(416254, "fits", lambda: fits) ) 
_l_(416256) 
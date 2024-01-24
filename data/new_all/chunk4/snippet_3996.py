# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64090848/flask-and-wtforms-typeerror-unsupported-operand-types-for-nonetype-and
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, url_for, render_template, make_response, request, redirect, session
    _l_(629010)

except ImportError:
    pass
try:
    from forms import DecimalField, BooleanField
    _l_(629012)

except ImportError:
    pass
try:
    import body_calculator
    _l_(629014)

except ImportError:
    pass



app = _c_(629017, _n_(629015, "Flask", lambda: Flask), _n_(629016, "__name__", lambda: __name__), static_folder='static',template_folder='templates')
_l_(629018)

@_c_(629021, _a_(629020, _n_(629019, "app", lambda: app), "route"), '/', methods = ['GET','POST'])
def index():
    _l_(629090)

    
    form = _c_(629023, _n_(629022, "DecimalField", lambda: DecimalField))
    _l_(629024)
    
    sex = _c_(629028, _a_(629027, _a_(629026, _n_(629025, "request", lambda: request), "form"), "get"), 'sex')
    _l_(629029)
    age = _c_(629033, _a_(629032, _a_(629031, _n_(629030, "request", lambda: request), "form"), "get"), 'age')
    _l_(629034)
    height = _c_(629038, _a_(629037, _a_(629036, _n_(629035, "request", lambda: request), "form"), "get"), 'height')
    _l_(629039)
    weight = _c_(629043, _a_(629042, _a_(629041, _n_(629040, "request", lambda: request), "form"), "get"), 'weight')
    _l_(629044)
    waist = _c_(629048, _a_(629047, _a_(629046, _n_(629045, "request", lambda: request), "form"), "get"), 'waist')
    _l_(629049)
    
    body = _c_(629057, _a_(629051, _n_(629050, "body_calculator", lambda: body_calculator), "Parameters"), _n_(629052, "height", lambda: height), _n_(629053, "weight", lambda: weight), _n_(629054, "age", lambda: age), _n_(629055, "sex", lambda: sex), _n_(629056, "waist", lambda: waist))
    _l_(629058)

    LBM = _c_(629061, _a_(629060, _n_(629059, "body", lambda: body), "Body_Lean_Mass"))
    _l_(629062)
    BMR = _c_(629065, _a_(629064, _n_(629063, "body", lambda: body), "Basal_Metabolic_Rate"))
    _l_(629066)
    BFP = _c_(629069, _a_(629068, _n_(629067, "body", lambda: body), "Body_Fat_Percentage"))
    _l_(629070)
    BMI = _c_(629073, _a_(629072, _n_(629071, "body", lambda: body), "Body_Mass_Index"))
    _l_(629074)

        
    context = {
        'int_form' : _n_(629075, "form", lambda: form),
        'LBM' : _n_(629076, "LBM", lambda: LBM),
        'BMR' : _n_(629077, "BMR", lambda: BMR),
        'BMI' : _n_(629078, "BMI", lambda: BMI)
        }
    _l_(629079)
    
    if _a_(629081, _n_(629080, "request", lambda: request), "method") == 'POST' and _c_(629084, _a_(629083, _n_(629082, "form", lambda: form), "validate")):
        _l_(629089)

        aux = _c_(629087, _n_(629085, "render_template", lambda: render_template), 'index.html', **_n_(629086, "context", lambda: context))
        _l_(629088)
        return aux


if _n_(629091, "__name__", lambda: __name__) == "__main__":
    _l_(629096)

    _c_(629094, _a_(629093, _n_(629092, "app", lambda: app), "run"), debug=True) 
    _l_(629095) 
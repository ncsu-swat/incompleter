# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64090848/flask-and-wtforms-typeerror-unsupported-operand-types-for-nonetype-and
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, url_for, render_template, make_response, request, redirect, session
    _l_(590731)

except ImportError:
    pass
try:
    from forms import DecimalField, BooleanField
    _l_(590733)

except ImportError:
    pass
try:
    import body_calculator
    _l_(590735)

except ImportError:
    pass



app = _c_(590738, _n_(590736, "Flask", lambda: Flask), _n_(590737, "__name__", lambda: __name__), static_folder='static',template_folder='templates')
_l_(590739)

@_c_(590742, _a_(590741, _n_(590740, "app", lambda: app), "route"), '/', methods = ['GET','POST'])
def index():
    _l_(590811)

    
    form = _c_(590744, _n_(590743, "DecimalField", lambda: DecimalField))
    _l_(590745)
    
    sex = _c_(590749, _a_(590748, _a_(590747, _n_(590746, "request", lambda: request), "form"), "get"), 'sex')
    _l_(590750)
    age = _c_(590754, _a_(590753, _a_(590752, _n_(590751, "request", lambda: request), "form"), "get"), 'age')
    _l_(590755)
    height = _c_(590759, _a_(590758, _a_(590757, _n_(590756, "request", lambda: request), "form"), "get"), 'height')
    _l_(590760)
    weight = _c_(590764, _a_(590763, _a_(590762, _n_(590761, "request", lambda: request), "form"), "get"), 'weight')
    _l_(590765)
    waist = _c_(590769, _a_(590768, _a_(590767, _n_(590766, "request", lambda: request), "form"), "get"), 'waist')
    _l_(590770)
    
    body = _c_(590778, _a_(590772, _n_(590771, "body_calculator", lambda: body_calculator), "Parameters"), _n_(590773, "height", lambda: height), _n_(590774, "weight", lambda: weight), _n_(590775, "age", lambda: age), _n_(590776, "sex", lambda: sex), _n_(590777, "waist", lambda: waist))
    _l_(590779)

    LBM = _c_(590782, _a_(590781, _n_(590780, "body", lambda: body), "Body_Lean_Mass"))
    _l_(590783)
    BMR = _c_(590786, _a_(590785, _n_(590784, "body", lambda: body), "Basal_Metabolic_Rate"))
    _l_(590787)
    BFP = _c_(590790, _a_(590789, _n_(590788, "body", lambda: body), "Body_Fat_Percentage"))
    _l_(590791)
    BMI = _c_(590794, _a_(590793, _n_(590792, "body", lambda: body), "Body_Mass_Index"))
    _l_(590795)

        
    context = {
        'int_form' : _n_(590796, "form", lambda: form),
        'LBM' : _n_(590797, "LBM", lambda: LBM),
        'BMR' : _n_(590798, "BMR", lambda: BMR),
        'BMI' : _n_(590799, "BMI", lambda: BMI)
        }
    _l_(590800)
    
    if _a_(590802, _n_(590801, "request", lambda: request), "method") == 'POST' and _c_(590805, _a_(590804, _n_(590803, "form", lambda: form), "validate")):
        _l_(590810)

        aux = _c_(590808, _n_(590806, "render_template", lambda: render_template), 'index.html', **_n_(590807, "context", lambda: context))
        _l_(590809)
        return aux


if _n_(590812, "__name__", lambda: __name__) == "__main__":
    _l_(590817)

    _c_(590815, _a_(590814, _n_(590813, "app", lambda: app), "run"), debug=True) 
    _l_(590816) 
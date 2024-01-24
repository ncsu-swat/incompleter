# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45117616/newton-optimize-typeerror-float-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from scipy import optimize
    _l_(441604)

except ImportError:
    pass

#########################
# IR Fixed PV Valuation #
#########################

def IR_Fixed_Valuation_PV(ValDate, Notional_v, AccrualDays_v, rate, Df_v):
    _l_(441642)

    PV=[]  
    _l_(441605)  
    for i in _c_(441610, _n_(441606, "range", lambda: range), 0,_c_(441609, _n_(441607, "len", lambda: len), _n_(441608, "AccrualDays_v", lambda: AccrualDays_v))):
        _l_(441639)

        if _c_(441614, _n_(441611, "sum", lambda: sum), _n_(441612, "AccrualDays_v", lambda: AccrualDays_v)[0:_n_(441613, "i", lambda: i)+1])<_n_(441615, "ValDate", lambda: ValDate):
            _l_(441638)

            if _n_(441616, "i", lambda: i)==0:
                _l_(441626)

                _c_(441619, _a_(441618, _n_(441617, "PV", lambda: PV), "append"), 0)
                _l_(441620)
            else:
                _c_(441624, _a_(441622, _n_(441621, "PV", lambda: PV), "append"), _n_(441623, "PV", lambda: PV)[-1])
                _l_(441625)
        else:
            _c_(441636, _a_(441628, _n_(441627, "PV", lambda: PV), "append"), _n_(441629, "Notional_v", lambda: Notional_v)[_n_(441630, "i", lambda: i)]*((1+_n_(441631, "rate", lambda: rate))**_n_(441632, "AccrualDays_v", lambda: AccrualDays_v)[_n_(441633, "i", lambda: i)]-1)*_n_(441634, "Df_v", lambda: Df_v)[_n_(441635, "i", lambda: i)])
            _l_(441637)
    aux = _n_(441640, "PV", lambda: (PV))
    _l_(441641)
    return aux

#############################
# IR Float Leg Valuation PV #
#############################

def IR_Float_Valuation_PV(ValDate, Notional_v, AccrualDays_v, Fra_rate_v, rate1, rate2, Df_v):
    _l_(441683)


    PV=[]  
    _l_(441643)  
    for i in _c_(441648, _n_(441644, "range", lambda: range), 0,_c_(441647, _n_(441645, "len", lambda: len), _n_(441646, "Notional_v", lambda: Notional_v))):
        _l_(441680)

        if _c_(441652, _n_(441649, "sum", lambda: sum), _n_(441650, "AccrualDays_v", lambda: AccrualDays_v)[0:_n_(441651, "i", lambda: i)+1])<_n_(441653, "ValDate", lambda: ValDate):
            _l_(441679)

            if _n_(441654, "i", lambda: i)==0:
                _l_(441664)

                _c_(441657, _a_(441656, _n_(441655, "PV", lambda: PV), "append"), 0)
                _l_(441658)
            else:
                _c_(441662, _a_(441660, _n_(441659, "PV", lambda: PV), "append"), _n_(441661, "PV", lambda: PV)[-1])
                _l_(441663)
        else:
            _c_(441677, _a_(441666, _n_(441665, "PV", lambda: PV), "append"), _n_(441667, "Notional_v", lambda: Notional_v)[_n_(441668, "i", lambda: i)]*(((((1+_n_(441669, "Fra_rate_v", lambda: Fra_rate_v)[_n_(441670, "i", lambda: i)])**(1/252)-1)*_n_(441671, "rate1", lambda: rate1)+1)*(1+_n_(441672, "rate2", lambda: rate2))**(1/252))**(252*_n_(441673, "AccrualDays_v", lambda: AccrualDays_v)[_n_(441674, "i", lambda: i)])-1)*_n_(441675, "Df_v", lambda: Df_v)[_n_(441676, "i", lambda: i)])
            _l_(441678)
    aux = _n_(441681, "PV", lambda: (PV))
    _l_(441682)
    return aux


def fun(a, b, c, d, e, f, g, h, i, j):
    _l_(441703)

    aux = _c_(441691, _n_(441684, "sum", lambda: sum), _c_(441690, _n_(441685, "IR_Fixed_Valuation_PV", lambda: IR_Fixed_Valuation_PV), 0, _n_(441686, "a", lambda: a), _n_(441687, "b", lambda: b), _n_(441688, "c", lambda: c), _n_(441689, "d", lambda: d))) - _c_(441701, _n_(441692, "sum", lambda: sum), _c_(441700, _n_(441693, "IR_Float_Valuation_PV", lambda: IR_Float_Valuation_PV), 0, _n_(441694, "e", lambda: e), _n_(441695, "f", lambda: f), _n_(441696, "g", lambda: g), _n_(441697, "h", lambda: h),_n_(441698, "i", lambda: i),_n_(441699, "j", lambda: j)))
    _l_(441702)
    return aux

#def main():
a=[1e+06,1e+06,1e+06]
_l_(441704)
b=[0.33,0.33,0.33]
_l_(441705)
c=0.10
_l_(441706)
d=[0.97, 0.96, 0.92]
_l_(441707)

e=_n_(441708, "a", lambda: a)
_l_(441709)
f=_n_(441710, "b", lambda: b)
_l_(441711)
g=[0.09,0.11,0.12]
_l_(441712)
h=1
_l_(441713)
i=0
_l_(441714)
j=_n_(441715, "d", lambda: d)
_l_(441716)
res = _c_(441730, _a_(441718, _n_(441717, "optimize", lambda: optimize), "newton"), _n_(441719, "fun", lambda: fun), _n_(441720, "c", lambda: c), args=(_n_(441721, "a", lambda: a),_n_(441722, "b", lambda: b),_n_(441723, "d", lambda: d),_n_(441724, "e", lambda: e),_n_(441725, "f", lambda: f),_n_(441726, "g", lambda: g),_n_(441727, "h", lambda: h),_n_(441728, "i", lambda: i),_n_(441729, "j", lambda: j),),tol=10e1, maxiter=50)
_l_(441731)
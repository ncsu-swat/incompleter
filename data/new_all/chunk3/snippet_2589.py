# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70391782/solve-typeerror-must-be-real-number-not-gk-operators
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from gekko import GEKKO
    _l_(574951)

except ImportError:
    pass
try:
    import math
    _l_(574953)

except ImportError:
    pass

m = _c_(574955, _n_(574954, "GEKKO", lambda: GEKKO), remote=False)
_l_(574956)
x1,x2,lambda1_L,lambda2_L,lambda1_U,lambda2_U,mu1,mu2,mu3,mu4,mu5,mu6,mu7,mu8,W1=[_c_(574959, _a_(574958, _n_(574957, "m", lambda: m), "Var"), 1) for i in _c_(574961, _n_(574960, "range", lambda: range), 15)] 
_l_(574962) 
sigma_p = _c_(574971, _a_(574964, _n_(574963, "math", lambda: math), "sqrt"), 0.028573*_n_(574965, "x1", lambda: x1)*_n_(574966, "x1", lambda: x1)+0.03129*_n_(574967, "x2", lambda: x2)*_n_(574968, "x2", lambda: x2)+0.020231*_n_(574969, "x1", lambda: x1)*_n_(574970, "x2", lambda: x2))
_l_(574972)
A= (0.028573*_n_(574973, "x1", lambda: x1)+0.010115*_n_(574974, "x2", lambda: x2))/_n_(574975, "sigma_p", lambda: sigma_p)
_l_(574976)
B=(0.03129*_n_(574977, "x2", lambda: x2)+0.010115*_n_(574978, "x1", lambda: x1))/_n_(574979, "sigma_p", lambda: sigma_p)
_l_(574980)
_c_(575031, _a_(574982, _n_(574981, "m", lambda: m), "Equations"), [292.7182*_n_(574983, "lambda1_L", lambda: lambda1_L)+(2.25*_n_(574984, "A", lambda: A)-0.025926)*_n_(574985, "lambda2_L", lambda: lambda2_L) + 446.444*_n_(574986, "lambda1_U", lambda: lambda1_U)+(2.25*_n_(574987, "A", lambda: A)-0.040535)*_n_(574988, "lambda2_U", lambda: lambda2_U)-446.444*_n_(574989, "mu1", lambda: mu1)-0.405858*_n_(574990, "mu2", lambda: mu2)+(2*_n_(574991, "A", lambda: A)-0.057146*_n_(574992, "x1", lambda: x1)-0.020231*_n_(574993, "x2", lambda: x2))*_n_(574994, "mu3", lambda: mu3)+_n_(574995, "mu4", lambda: mu4)-_n_(574996, "mu5", lambda: mu5)+_n_(574997, "mu6", lambda: mu6)==0,\
            272.9655*_n_(574998, "lambda1_L", lambda: lambda1_L)+(2.25*_n_(574999, "B", lambda: B)-0.03633)*_n_(575000, "lambda2_L", lambda: lambda2_L)+513.4587*_n_(575001, "lambda1_U", lambda: lambda1_U)+(2.25*_n_(575002, "B", lambda: B)-0.051024)*_n_(575003, "lambda2_U", lambda: lambda2_U)-513.4587*_n_(575004, "mu1", lambda: mu1)-0.466781*_n_(575005, "mu2", lambda: mu2)+(2*_n_(575006, "B", lambda: B)-0.06258*_n_(575007, "x2", lambda: x2)-0.020231*_n_(575008, "x1", lambda: x1))*_n_(575009, "mu3", lambda: mu3)+_n_(575010, "mu4", lambda: mu4)-_n_(575011, "mu7", lambda: mu7)+_n_(575012, "mu8", lambda: mu8)==0,\
            _n_(575013, "mu1", lambda: mu1)*(_n_(575014, "W1", lambda: W1)-446.444*_n_(575015, "x1", lambda: x1)-513.4587*_n_(575016, "x2", lambda: x2)-33)==0,\
            _n_(575017, "mu2", lambda: mu2)*(0.13-0.405858*_n_(575018, "x1", lambda: x1)-0.466781*_n_(575019, "x2", lambda: x2))<=0,\
            _n_(575020, "mu3", lambda: mu3)*(_n_(575021, "x1", lambda: x1)+_n_(575022, "x2", lambda: x2)-1)==0,\
            _n_(575023, "mu5", lambda: mu5)*(0.03-_n_(575024, "x1", lambda: x1))<=0,\
            _n_(575025, "mu6", lambda: mu6)*(_n_(575026, "x1", lambda: x1)-0.38)<=0,\
            _n_(575027, "mu7", lambda: mu7)*(0.05-_n_(575028, "x2", lambda: x2))<=0,\
            _n_(575029, "mu8", lambda: mu8)*(_n_(575030, "x2", lambda: x2)-0.42)<=0])
_l_(575032)
_c_(575035, _a_(575034, _n_(575033, "m", lambda: m), "solve"), disp=False)
_l_(575036)
_c_(575068, _n_(575037, "print", lambda: print), _a_(575039, _n_(575038, "x1", lambda: x1), "value"),_a_(575041, _n_(575040, "x2", lambda: x2), "value"),_a_(575043, _n_(575042, "lambda1_L", lambda: lambda1_L), "value"),_a_(575045, _n_(575044, "lambda2_L", lambda: lambda2_L), "value"),_a_(575047, _n_(575046, "lambda1_U", lambda: lambda1_U), "value"),_a_(575049, _n_(575048, "lambda2_U", lambda: lambda2_U), "value"),_a_(575051, _n_(575050, "mu1", lambda: mu1), "value"),_a_(575053, _n_(575052, "mu2", lambda: mu2), "value"),_a_(575055, _n_(575054, "mu3", lambda: mu3), "value"),_a_(575057, _n_(575056, "mu4", lambda: mu4), "value"),_a_(575059, _n_(575058, "mu5", lambda: mu5), "value"),_a_(575061, _n_(575060, "mu6", lambda: mu6), "value"),_a_(575063, _n_(575062, "mu7", lambda: mu7), "value"),_a_(575065, _n_(575064, "mu8", lambda: mu8), "value"),_a_(575067, _n_(575066, "W1", lambda: W1), "value"))
_l_(575069)
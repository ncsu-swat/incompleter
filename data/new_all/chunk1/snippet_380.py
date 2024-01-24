# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39753260/sympy-to-numpy-causes-the-attributeerror-symbol-object-has-no-attribute-cos
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sympy as sp
    _l_(419252)

except ImportError:
    pass
try:
    import numpy as np
    _l_(419254)

except ImportError:
    pass
try:
    from sympy import init_printing
    _l_(419256)

except ImportError:
    pass
_c_(419258, _n_(419257, "init_printing", lambda: init_printing))
_l_(419259)
t_1,t_2,X_1,X_2,Y_1,Y_2,X_c1,X_c2,Y_c1,Y_c2,a_1,a_2,psi_1,psi_2,b_1,b_2= _c_(419262, _a_(419261, _n_(419260, "sp", lambda: sp), "symbols"), 't_1 t_2 X_1 X_2 Y_1 Y_2 X_c1 X_c2 Y_c1 Y_c2 a_1 a_2 psi_1 psi_2 b_1 b_2')
_l_(419263)

X_1=_n_(419264, "X_c1", lambda: X_c1) + (_n_(419265, "a_1", lambda: a_1) * _c_(419269, _a_(419267, _n_(419266, "sp", lambda: sp), "cos"), _n_(419268, "t_1", lambda: t_1)) * _c_(419273, _a_(419271, _n_(419270, "sp", lambda: sp), "cos"), _n_(419272, "psi_1", lambda: psi_1))) - (_n_(419274, "b_1", lambda: (b_1)) * _c_(419278, _a_(419276, _n_(419275, "sp", lambda: sp), "sin"), _n_(419277, "t_1", lambda: t_1))* _c_(419282, _a_(419280, _n_(419279, "sp", lambda: sp), "sin"), _n_(419281, "psi_1", lambda: psi_1)))
_l_(419283)

X_2=_n_(419284, "X_c2", lambda: X_c2) + (_n_(419285, "a_2", lambda: a_2) * _c_(419289, _a_(419287, _n_(419286, "sp", lambda: sp), "cos"), _n_(419288, "t_2", lambda: t_2)) * _c_(419293, _a_(419291, _n_(419290, "sp", lambda: sp), "cos"), _n_(419292, "psi_2", lambda: psi_2))) - (_n_(419294, "b_2", lambda: (b_2)) * _c_(419298, _a_(419296, _n_(419295, "sp", lambda: sp), "sin"), _n_(419297, "t_2", lambda: t_2))* _c_(419302, _a_(419300, _n_(419299, "sp", lambda: sp), "sin"), _n_(419301, "psi_2", lambda: psi_2)))
_l_(419303)

Y_1=_n_(419304, "Y_c1", lambda: Y_c1) + (_n_(419305, "a_1", lambda: a_1) * _c_(419309, _a_(419307, _n_(419306, "sp", lambda: sp), "cos"), _n_(419308, "t_1", lambda: t_1)) * _c_(419313, _a_(419311, _n_(419310, "sp", lambda: sp), "sin"), _n_(419312, "psi_1", lambda: psi_1))) + (_n_(419314, "b_1", lambda: (b_1)) * _c_(419318, _a_(419316, _n_(419315, "sp", lambda: sp), "sin"), _n_(419317, "t_1", lambda: t_1))* _c_(419322, _a_(419320, _n_(419319, "sp", lambda: sp), "cos"), _n_(419321, "psi_1", lambda: psi_1)))
_l_(419323)

Y_2=_n_(419324, "Y_c2", lambda: Y_c2) + (_n_(419325, "a_2", lambda: a_2) * _c_(419329, _a_(419327, _n_(419326, "sp", lambda: sp), "cos"), _n_(419328, "t_2", lambda: t_2)) * _c_(419333, _a_(419331, _n_(419330, "sp", lambda: sp), "sin"), _n_(419332, "psi_2", lambda: psi_2))) + (_n_(419334, "b_2", lambda: (b_2)) * _c_(419338, _a_(419336, _n_(419335, "sp", lambda: sp), "sin"), _n_(419337, "t_2", lambda: t_2))* _c_(419342, _a_(419340, _n_(419339, "sp", lambda: sp), "sin"), _n_(419341, "psi_2", lambda: psi_2)))
_l_(419343)

D=(((_n_(419344, "X_2", lambda: X_2)-_n_(419345, "X_1", lambda: X_1))**2) + ((_n_(419346, "Y_2", lambda: Y_2)-_n_(419347, "Y_1", lambda: Y_1))**2))**0.5
_l_(419348)

y_1=_c_(419353, _a_(419350, _n_(419349, "sp", lambda: sp), "diff"), _n_(419351, "D", lambda: D),_n_(419352, "t_1", lambda: t_1))
_l_(419354)

y_2=_c_(419359, _a_(419356, _n_(419355, "sp", lambda: sp), "diff"), _n_(419357, "D", lambda: D),_n_(419358, "t_2", lambda: t_2))
_l_(419360)

f=_c_(419365, _a_(419362, _n_(419361, "sp", lambda: sp), "lambdify"), _n_(419363, "t_1", lambda: t_1), _n_(419364, "y_1", lambda: y_1), "numpy")
_l_(419366)

g=_c_(419371, _a_(419368, _n_(419367, "sp", lambda: sp), "lambdify"), _n_(419369, "t_2", lambda: t_2), _n_(419370, "y_2", lambda: y_2), "numpy")
_l_(419372)
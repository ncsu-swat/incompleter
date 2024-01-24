# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61199368/typeerror-numpy-float64-object-is-not-callable-in-scipy-optimize-minimize-lib
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def c_func(theta):
    _l_(566949)


    data_pima = _c_(566706, _a_(566705, _n_(566704, "pd", lambda: pd), "read_csv"), '~/Documents/Uwaterloo_Study_Docs/ECE_602/Project_final/Dataset/PIMA/pima-indians-diabetes.csv')
    _l_(566707)
    _c_(566710, _a_(566709, _n_(566708, "data_pima", lambda: data_pima), "rename"), columns={'1':'Target', '6':'Pregnancies', '148':'Glucose', '72':'BloodPressure', '35':'SkinThickness', '0': 'Insulin',                                                    '33.6': 'BMI', '0.627':'DiabeticPedigreeFunction','50':'Age'},inplace=True)
    _l_(566711)
    X = _a_(566714, _a_(566713, _n_(566712, "data_pima", lambda: data_pima), "loc")[:,:'Age'], "values")
    _l_(566715)
    y = _a_(566717, _n_(566716, "data_pima", lambda: data_pima)['Target'], "values")
    _l_(566718)
    data_pima_positive = _a_(566720, _n_(566719, "data_pima", lambda: data_pima), "loc")[(_n_(566721, "data_pima", lambda: data_pima)['Target'] > 0)]
    _l_(566722)
    data_pima_negative = _a_(566724, _n_(566723, "data_pima", lambda: data_pima), "loc")[(_n_(566725, "data_pima", lambda: data_pima)['Target'] < 1)]
    _l_(566726)


    X_train, X_test, y_train, y_test = _c_(566730, _n_(566727, "train_test_split", lambda: train_test_split), _n_(566728, "X", lambda: X), _n_(566729, "y", lambda: y), test_size=0.30,random_state=42)
    _l_(566731)

    sq_dist = _c_(566734, _n_(566732, "pdist", lambda: pdist), _n_(566733, "X", lambda: X), 'sqeuclidean')
    _l_(566735)
    sigma = [10**(0.1), 10**(-0.7), 10**(-0.4), 10**(-0.1), 10**(0.2), 10**(0.5), 10**(0.8), 10**(1.1), 10**(1.4), 10**(1.7)]
    _l_(566736)

    G = 0
    _l_(566737)
    for value in _c_(566739, _n_(566738, "range", lambda: range), 10):
        _l_(566763)

        gamma = 1/(_n_(566740, "sigma", lambda: sigma)[_n_(566741, "value", lambda: value)]**2)
        _l_(566742)
        gamma = -_n_(566743, "gamma", lambda: gamma) * _n_(566744, "theta", lambda: theta)[_n_(566745, "value", lambda: value)] 
        _l_(566746) 
        mat_sqr_dist = _c_(566749, _n_(566747, "squareform", lambda: squareform), _n_(566748, "sq_dist", lambda: sq_dist))
        _l_(566750)
        g = _c_(566755, _a_(566752, _n_(566751, "np", lambda: np), "exp"), _n_(566753, "gamma", lambda: gamma) * _n_(566754, "mat_sqr_dist", lambda: mat_sqr_dist))
        _l_(566756)
        G = _c_(566761, _a_(566758, _n_(566757, "np", lambda: np), "add"), _n_(566759, "G", lambda: G), _n_(566760, "g", lambda: g))
        _l_(566762)

    # number of positive sample from the dataset
    m_plus = _c_(566767, _n_(566764, "len", lambda: len), _a_(566766, _n_(566765, "data_pima_positive", lambda: data_pima_positive), "index"))
    _l_(566768)
    data_pima_positive = _a_(566770, _n_(566769, "data_pima_positive", lambda: data_pima_positive), "values")
    _l_(566771)
    m_minus = _c_(566775, _n_(566772, "len", lambda: len), _a_(566774, _n_(566773, "data_pima_negative", lambda: data_pima_negative), "index"))
    _l_(566776)
    one_plus = _c_(566780, _a_(566778, _n_(566777, "np", lambda: np), "ones"), _n_(566779, "m_plus", lambda: m_plus))
    _l_(566781)
    one_minus = _c_(566785, _a_(566783, _n_(566782, "np", lambda: np), "ones"), _n_(566784, "m_minus", lambda: m_minus))
    _l_(566786)
    I_plus = _c_(566790, _a_(566788, _n_(566787, "np", lambda: np), "identity"), _n_(566789, "m_plus", lambda: m_plus))
    _l_(566791)
    J_plus_1value = _c_(566797, _a_(566793, _n_(566792, "np", lambda: np), "dot"), _n_(566794, "one_plus", lambda: one_plus), _a_(566796, _n_(566795, "one_plus", lambda: one_plus), "T"))
    _l_(566798)
    J_plus = (1/_c_(566802, _a_(566800, _n_(566799, "np", lambda: np), "sqrt"), _n_(566801, "m_plus", lambda: m_plus))) * (_n_(566803, "I_plus", lambda: I_plus) - (1/_n_(566804, "m_plus", lambda: m_plus)) * _n_(566805, "J_plus_1value", lambda: J_plus_1value))
    _l_(566806)
    I_minus = _c_(566810, _a_(566808, _n_(566807, "np", lambda: np), "identity"), _n_(566809, "m_minus", lambda: m_minus))
    _l_(566811)
    J_minus_1value = _c_(566817, _a_(566813, _n_(566812, "np", lambda: np), "dot"), _n_(566814, "one_minus", lambda: one_minus), _a_(566816, _n_(566815, "one_minus", lambda: one_minus), "T"))
    _l_(566818)
    J_minus = (1/_c_(566822, _a_(566820, _n_(566819, "np", lambda: np), "sqrt"), _n_(566821, "m_minus", lambda: m_minus))) * (_n_(566823, "I_minus", lambda: I_minus) - (1/_n_(566824, "m_minus", lambda: m_minus)) * _n_(566825, "J_minus_1value", lambda: J_minus_1value))
    _l_(566826)

    J = _c_(566831, _a_(566828, _n_(566827, "linalg", lambda: linalg), "block_diag"), _n_(566829, "J_plus", lambda: J_plus), _n_(566830, "J_minus", lambda: J_minus))
    _l_(566832)
    a_plus_1 = (1/_n_(566833, "m_plus", lambda: m_plus))* _n_(566834, "one_plus", lambda: one_plus)
    _l_(566835)
    a_minus_1  = (1/_n_(566836, "m_minus", lambda: m_minus))* _n_(566837, "one_minus", lambda: one_minus)
    _l_(566838)
    zeros_a_plus = _c_(566844, _a_(566840, _n_(566839, "np", lambda: np), "zeros"), _c_(566843, _n_(566841, "len", lambda: len), _n_(566842, "a_minus_1", lambda: a_minus_1)))
    _l_(566845)
    a_plus = _c_(566850, _a_(566847, _n_(566846, "np", lambda: np), "block"), [_n_(566848, "a_plus_1", lambda: a_plus_1), _n_(566849, "zeros_a_plus", lambda: zeros_a_plus)])
    _l_(566851)
    zeros_a_minus = _c_(566857, _a_(566853, _n_(566852, "np", lambda: np), "zeros"), _c_(566856, _n_(566854, "len", lambda: len), _n_(566855, "a_plus_1", lambda: a_plus_1)))
    _l_(566858)
    a_minus = _c_(566863, _a_(566860, _n_(566859, "np", lambda: np), "block"), [_n_(566861, "zeros_a_minus", lambda: zeros_a_minus), _n_(566862, "a_minus_1", lambda: a_minus_1)])
    _l_(566864)
    a = _n_(566865, "a_plus", lambda: a_plus) - _n_(566866, "a_minus", lambda: a_minus)
    _l_(566867)
    lambda_val = 10**(-8)
    _l_(566868)
    I = _c_(566874, _a_(566870, _n_(566869, "np", lambda: np), "identity"), _c_(566873, _n_(566871, "len", lambda: len), _n_(566872, "J", lambda: J)))
    _l_(566875)
    J_G = _c_(566880, _a_(566877, _n_(566876, "np", lambda: np), "matmul"), _n_(566878, "J", lambda: J),_n_(566879, "G", lambda: G))
    _l_(566881)
    lambda_I = _n_(566882, "lambda_val", lambda: lambda_val)*_n_(566883, "I", lambda: I)
    _l_(566884)
    J_G_J = _c_(566889, _a_(566886, _n_(566885, "np", lambda: np), "matmul"), _n_(566887, "J_G", lambda: J_G), _n_(566888, "J", lambda: J))
    _l_(566890)
    value_1 = (_n_(566891, "lambda_I", lambda: lambda_I) + _n_(566892, "J_G_J", lambda: J_G_J))
    _l_(566893)
    J_G_a = _c_(566898, _a_(566895, _n_(566894, "np", lambda: np), "matmul"), _n_(566896, "J_G", lambda: J_G),_n_(566897, "a", lambda: a))
    _l_(566899)
    G_J = _c_(566904, _a_(566901, _n_(566900, "np", lambda: np), "matmul"), _n_(566902, "G", lambda: G),_n_(566903, "J", lambda: J))
    _l_(566905)
    aT_G_J = _c_(566911, _a_(566907, _n_(566906, "np", lambda: np), "matmul"), _a_(566909, _n_(566908, "a", lambda: a), "T"),_n_(566910, "G_J", lambda: G_J))
    _l_(566912)
    G_a = _c_(566917, _a_(566914, _n_(566913, "np", lambda: np), "matmul"), _n_(566915, "G", lambda: G),_n_(566916, "a", lambda: a))
    _l_(566918)
    aT_G_a = _c_(566924, _a_(566920, _n_(566919, "np", lambda: np), "matmul"), _a_(566922, _n_(566921, "a", lambda: a), "T"), _n_(566923, "G_a", lambda: G_a))
    _l_(566925)
    value_1Inv = _c_(566929, _a_(566927, _n_(566926, "linalg", lambda: linalg), "inv"), _n_(566928, "value_1", lambda: value_1))
    _l_(566930)
    aT_G_J_value1Inv = _c_(566935, _a_(566932, _n_(566931, "np", lambda: np), "matmul"), _n_(566933, "aT_G_J", lambda: aT_G_J), _n_(566934, "value_1Inv", lambda: value_1Inv))
    _l_(566936)
    aT_G_J_value1Inv_J_G_a = _c_(566941, _a_(566938, _n_(566937, "np", lambda: np), "matmul"), _n_(566939, "aT_G_J_value1Inv", lambda: aT_G_J_value1Inv), _n_(566940, "J_G_a", lambda: J_G_a))
    _l_(566942)
    func_val = (1/_n_(566943, "lambda_val", lambda: lambda_val))*(_n_(566944, "aT_G_J_value1Inv_J_G_a", lambda: aT_G_J_value1Inv_J_G_a) - _n_(566945, "aT_G_a", lambda: aT_G_a))
    _l_(566946)
    aux = _n_(566947, "func_val", lambda: func_val)
    _l_(566948)
    return aux


if _n_(566950, "__name__", lambda: __name__) == "__main__":
    _l_(566983)

    try:
        import numpy as np
        _l_(566952)

    except ImportError:
        pass
    try:
        import pandas as pd
        _l_(566954)

    except ImportError:
        pass
    try:
        from sklearn.model_selection import train_test_split
        _l_(566956)

    except ImportError:
        pass
    try:
        from scipy.spatial.distance import pdist, squareform
        _l_(566958)

    except ImportError:
        pass
    try:
        from scipy import linalg
        _l_(566960)

    except ImportError:
        pass
    try:
        from scipy.optimize import linprog
        _l_(566962)

    except ImportError:
        pass
    try:
        from scipy import optimize as optimize
        _l_(566964)

    except ImportError:
        pass

    theta_val = _c_(566967, _a_(566966, _n_(566965, "np", lambda: np), "array"), [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
    _l_(566968)

    value = _c_(566971, _n_(566969, "c_func", lambda: c_func), _n_(566970, "theta_val", lambda: theta_val))
    _l_(566972)
    result = _c_(566977, _a_(566974, _n_(566973, "optimize", lambda: optimize), "minimize"), _n_(566975, "value", lambda: value), _n_(566976, "theta_val", lambda: theta_val), method='Newton-CG', jac=True, options={'disp':True})
    _l_(566978)
    _c_(566981, _n_(566979, "print", lambda: print), _n_(566980, "result", lambda: result))
    _l_(566982)
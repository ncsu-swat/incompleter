# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72127203/typeerror-unsupported-operand-types-for-float-and-float-pandas
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def que_fn(x,cols):
    _l_(619952)


    if (_n_(619898, "x", lambda: x)[(_n_(619899, "x", lambda: x)[_n_(619900, "cols", lambda: cols)[2]]==_n_(619901, "x", lambda: x)[_n_(619902, "cols", lambda: cols)[3]])]) & (_n_(619903, "x", lambda: x)[_c_(619907, _a_(619906, _n_(619904, "x", lambda: x)[_n_(619905, "cols", lambda: cols)[2]], "notna"))]) & (_n_(619908, "x", lambda: x)[_c_(619912, _a_(619911, _n_(619909, "x", lambda: x)[_n_(619910, "cols", lambda: cols)[3]], "notna"))]):
        _l_(619951)

        aux = "Test1"
        _l_(619913)
        return aux
    elif (_n_(619914, "x", lambda: x)[_c_(619918, _a_(619917, _n_(619915, "x", lambda: x)[_n_(619916, "cols", lambda: cols)[2]], "isnull"))]) & (_n_(619919, "x", lambda: x)[_c_(619923, _a_(619922, _n_(619920, "x", lambda: x)[_n_(619921, "cols", lambda: cols)[3]], "isnull"))]):
        _l_(619950)

        aux = "Test1"
        _l_(619924)
        return aux
    elif (_n_(619925, "x", lambda: x)[_c_(619929, _a_(619928, _n_(619926, "x", lambda: x)[_n_(619927, "cols", lambda: cols)[2]], "isnull"))]) & (_n_(619930, "x", lambda: x)[_c_(619934, _a_(619933, _n_(619931, "x", lambda: x)[_n_(619932, "cols", lambda: cols)[3]], "notna"))]):
        _l_(619949)

        aux = "Test2"
        _l_(619935)
        return aux
    elif (_n_(619936, "x", lambda: x)[_c_(619940, _a_(619939, _n_(619937, "x", lambda: x)[_n_(619938, "cols", lambda: cols)[2]], "notna"))]) & (_n_(619941, "x", lambda: x)[_c_(619945, _a_(619944, _n_(619942, "x", lambda: x)[_n_(619943, "cols", lambda: cols)[3]], "isnull"))]):
        _l_(619948)

        aux = "Test3"
        _l_(619946)
        return aux
    else:
        aux = "Test4"
        _l_(619947)
        return aux
        
        
check_cols = ['id_a','id_b','value_a','value_b']
_l_(619953)

_n_(619954, "new_df", lambda: new_df)['calc_value'] = _c_(619961, _a_(619956, _n_(619955, "test_df", lambda: test_df), "apply"), _c_(619960, _n_(619957, "que_fn", lambda: que_fn), _n_(619958, "test_df", lambda: test_df),_n_(619959, "check_cols", lambda: check_cols)),axis=1)
_l_(619962)
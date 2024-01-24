# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61365330/celery-running-signature-from-database-attributeerror-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def example_job_1(arg_1, arg_2, **kwargs):
    _l_(568784)

    example_task_1_s = _c_(568774, _a_(568772, _n_(568771, "task_1", lambda: task_1), "si"), _n_(568773, "arg_1", lambda: arg_1))
    _l_(568775)
    example_task_2_s = _c_(568779, _a_(568777, _n_(568776, "task_2", lambda: task_2), "s"), _n_(568778, "arg_2", lambda: arg_2))
    _l_(568780)
    aux = _n_(568781, "example_task_1_s", lambda: example_task_1_s) | _n_(568782, "example_task_2_s", lambda: example_task_2_s)
    _l_(568783)
    return aux

def example_job_2(arg_1, arg_2, **kwargs):
    _l_(568790)

    aux = _c_(568788, _a_(568786, _n_(568785, "task_1", lambda: task_1), "si"), _n_(568787, "arg_1", lambda: arg_1))
    _l_(568789)
    return aux


signature = _c_(568794, _n_(568791, "example_job_1", lambda: example_job_1), _n_(568792, "arg_1", lambda: arg_1), _n_(568793, "arg_2", lambda: arg_2)) | _c_(568797, _n_(568795, "example_job_2", lambda: example_job_2), _n_(568796, "arg_1", lambda: arg_1)) # _chain object
_l_(568798) # _chain object
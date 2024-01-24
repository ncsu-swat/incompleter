# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51445557/celery-workflow-error-typeerror-unsupported-operand-types-for-asyncresul
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(407881)

except ImportError:
    pass
try:
    from celery import Celery, group, chord, chain
    _l_(407883)

except ImportError:
    pass

class CeleryConfig:
    _l_(407909)

    """
    Configuration for Celery
    """
    broker_url = _c_(407887, _a_(407886, _a_(407885, _n_(407884, "os", lambda: os), "environ"), "get"), 'CELERY_BROKER_URL','mongodb://localhost:9001/jobs')
    _l_(407888)
    result_backend = _c_(407892, _a_(407891, _a_(407890, _n_(407889, "os", lambda: os), "environ"), "get"), 'CELERY_RESULT_BACKEND', 'mongodb://localhost:9001/')
    _l_(407893)
    celery_mongodb_backend_settings = {
        "database": "results", 
        "taskmeta_collection": "test",
    }
    _l_(407894)
    enable_utc = True
    _l_(407895)
    timezone = "UTC"
    _l_(407896)
    celery_imports = ('test',)
    _l_(407897)
    task_always_eager = _c_(407901, _a_(407900, _a_(407899, _n_(407898, "os", lambda: os), "environ"), "get"), 'CELERY_ALWAYS_EAGER', False)
    _l_(407902)
    task_eager_propagates = _c_(407906, _a_(407905, _a_(407904, _n_(407903, "os", lambda: os), "environ"), "get"), 'CELERY_EAGER_PROPAGATES',False)
    _l_(407907)
    task_serializer = 'json'
    _l_(407908)

celery_app = _c_(407911, _n_(407910, "Celery", lambda: Celery), "test")
_l_(407912)
_c_(407916, _a_(407914, _n_(407913, "celery_app", lambda: celery_app), "config_from_object"), _n_(407915, "CeleryConfig", lambda: CeleryConfig))
_l_(407917)

@_c_(407920, _a_(407919, _n_(407918, "celery_app", lambda: celery_app), "task"), bind=True)
def dummy_task(self, *args, **kwargs):
    _l_(407922)

    aux = True
    _l_(407921)
    return aux

@_c_(407925, _a_(407924, _n_(407923, "celery_app", lambda: celery_app), "task"), bind=True)
def a(self, pagination, *args, **kwargs):
    _l_(407929)

    aux = _n_(407926, "pagination", lambda: pagination)[0] + _n_(407927, "pagination", lambda: pagination)[1]
    _l_(407928)
    return aux

@_c_(407932, _a_(407931, _n_(407930, "celery_app", lambda: celery_app), "task"), bind=True)
def b(self, pagination, *args, **kwargs):
    _l_(407936)

    aux = _n_(407933, "pagination", lambda: pagination)[0] + _n_(407934, "pagination", lambda: pagination)[1]
    _l_(407935)
    return aux

@_c_(407939, _a_(407938, _n_(407937, "celery_app", lambda: celery_app), "task"), bind=True)
def workflow(self):
    _l_(407981)

    batch_size = 10
    _l_(407940)
    flow_a = _c_(407955, _c_(407954, _n_(407941, "chord", lambda: chord), _c_(407950, _n_(407942, "group", lambda: group), (_c_(407947, _a_(407944, _n_(407943, "a", lambda: a), "s"), (_n_(407945, "k", lambda: k),_n_(407946, "batch_size", lambda: batch_size)), max_retries=None) for k in _c_(407949, _n_(407948, "range", lambda: range), 5))), _c_(407953, _a_(407952, _n_(407951, "dummy_task", lambda: dummy_task), "s"))))
    _l_(407956)
    flow_b = _c_(407971, _c_(407970, _n_(407957, "chord", lambda: chord), _c_(407966, _n_(407958, "group", lambda: group), (_c_(407963, _a_(407960, _n_(407959, "b", lambda: b), "si"), (_n_(407961, "k", lambda: k),_n_(407962, "batch_size", lambda: batch_size)), immutable=True, max_retries=None) for k in _c_(407965, _n_(407964, "range", lambda: range), 5))), _c_(407969, _a_(407968, _n_(407967, "dummy_task", lambda: dummy_task), "s"))))
    _l_(407972)

    r = _c_(407977, _c_(407976, _n_(407973, "chain", lambda: chain), _n_(407974, "flow_a", lambda: flow_a), _n_(407975, "flow_b", lambda: flow_b)))
    _l_(407978)
    aux = _n_(407979, "r", lambda: r)
    _l_(407980)
    return aux

task = _c_(407984, _a_(407983, _n_(407982, "workflow", lambda: workflow), "apply_async"))
_l_(407985)
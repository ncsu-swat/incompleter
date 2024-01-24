# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75224761/multiprocess-package-baseprocess-typeerror-baseprocess-popen
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def __initialise_strat_class_obj(self, *, strat_name: _n_(593133, "str", lambda: str), strat_config: _n_(593134, "StratInput", lambda: StratInput)):
    _l_(593167)

    try:
        _l_(593157)

        strat_instance = _c_(593140, _n_(593135, "strat_class_dict", lambda: strat_class_dict)[_n_(593136, "strat_name", lambda: strat_name)], strat_args=_a_(593138, _n_(593137, "self", lambda: self), "strat_args"), strat_input=_n_(593139, "strat_config", lambda: strat_config))  # dynamically fetching & calling the class
        _l_(593141)  # dynamically fetching & calling the class
        _c_(593144, _a_(593143, _n_(593142, "strat_instance", lambda: strat_instance), "init"))
        _l_(593145)
    except _n_(593146, "Exception", lambda: Exception) as e:
        _l_(593156)

        _c_(593153, _a_(593149, _a_(593148, _n_(593147, "self", lambda: self), "_logger"), "error"), f"unable to init strategy `{_a_(593151, _n_(593150, 'strat_config', lambda: strat_config), 'id')}`: {_n_(593152, 'e', lambda: e)}")
        _l_(593154)
        aux = False 
        _l_(593155) 
        return aux 
    strat_process = _c_(593161, _n_(593158, "Process", lambda: Process), target=_a_(593160, _n_(593159, "strat_instance", lambda: strat_instance), "run"))
    _l_(593162)
    _c_(593165, _a_(593164, _n_(593163, "strat_process", lambda: strat_process), "start"))# starting the class method in a separate process
    _l_(593166)# starting the class method in a separate process
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72903946/attributeerror-forkawarelocal-object-has-no-attribute-connection-even-wit
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _n_(390180, "__name__", lambda: __name__) == "__main__":
    _l_(390229)

    start = _c_(390183, _a_(390182, _n_(390181, "time", lambda: time), "perf_counter"))
    _l_(390184)
    with _c_(390186, _n_(390185, "Manager", lambda: Manager)) as manager:
        _l_(390211)

        genome_score_avgs = _c_(390189, _a_(390188, _n_(390187, "manager", lambda: manager), "list"))
        _l_(390190)
        processes = [_c_(390195, _n_(390191, "Process", lambda: Process), target=_n_(390192, "compareGenomes", lambda: compareGenomes), args=(_n_(390193, "chunk", lambda: chunk), _n_(390194, "genome_score_avgs", lambda: genome_score_avgs),)) for chunk in _c_(390197, _n_(390196, "divideGenomes", lambda: divideGenomes), 'TEST_DIR')]
        _l_(390198)
        for p in _n_(390199, "processes", lambda: processes):
            _l_(390204)

            _c_(390202, _a_(390201, _n_(390200, "p", lambda: p), "start"))
            _l_(390203)
        for p in _n_(390205, "processes", lambda: processes):
            _l_(390210)

            _c_(390208, _a_(390207, _n_(390206, "p", lambda: p), "join"))
            _l_(390209)
    _c_(390214, _n_(390212, "print", lambda: print), _n_(390213, "genome_score_avgs", lambda: genome_score_avgs))
    _l_(390215)
    _c_(390220, _n_(390216, "print", lambda: print), *_c_(390219, _n_(390217, "createTimeline", lambda: createTimeline), _n_(390218, "genome_score_avgs", lambda: genome_score_avgs)), sep='\n')
    _l_(390221)
    _c_(390227, _n_(390222, "print", lambda: print), f'Finished in {_c_(390225, _a_(390224, _n_(390223, "time", lambda: time), "perf_counter")) - _n_(390226, "start", lambda: start)} seconds')
    _l_(390228)
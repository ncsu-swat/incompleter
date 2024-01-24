# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60049527/shutting-down-manager-error-attributeerror-forkawarelocal-object-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import multiprocessing
    _l_(379163)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(379165)

except ImportError:
    pass
try:
    import numpy as np
    _l_(379167)

except ImportError:
    pass


def add_empty_dfs_to_shared_dict(shared_dict, key):
    _l_(379174)

    _n_(379168, "shared_dict", lambda: shared_dict)[_n_(379169, "key", lambda: key)] = _c_(379172, _a_(379171, _n_(379170, "pd", lambda: pd), "DataFrame"))
    _l_(379173)


def edit_df_in_shared_dict(shared_dict, namespace, ind):
    _l_(379191)

    row_to_insert = _a_(379177, _a_(379176, _n_(379175, "namespace", lambda: namespace), "df"), "loc")[_n_(379178, "ind", lambda: ind)]
    _l_(379179)
    df = _n_(379180, "shared_dict", lambda: shared_dict)[_n_(379181, "ind", lambda: ind)]
    _l_(379182)
    _n_(379183, "df", lambda: df)[_n_(379184, "ind", lambda: ind)] = _n_(379185, "row_to_insert", lambda: row_to_insert)
    _l_(379186)
    _n_(379187, "shared_dict", lambda: shared_dict)[_n_(379188, "ind", lambda: ind)] = _n_(379189, "df", lambda: df)
    _l_(379190)


if _n_(379192, "__name__", lambda: __name__) == '__main__':
    _l_(379266)

    manager = _c_(379195, _a_(379194, _n_(379193, "multiprocessing", lambda: multiprocessing), "Manager"))
    _l_(379196)
    shared_dict = _c_(379199, _a_(379198, _n_(379197, "manager", lambda: manager), "dict"))
    _l_(379200)
    namespace = _c_(379203, _a_(379202, _n_(379201, "manager", lambda: manager), "Namespace"))
    _l_(379204)

    n = 100
    _l_(379205)
    dataframe_to_be_shared = _c_(379220, _a_(379219, _c_(379218, _a_(379207, _n_(379206, "pd", lambda: pd), "DataFrame"), {
        'player_id': _c_(379212, _n_(379208, "list", lambda: list), _c_(379211, _n_(379209, "range", lambda: range), _n_(379210, "n", lambda: n))),
        'data': _c_(379217, _a_(379215, _a_(379214, _n_(379213, "np", lambda: np), "random"), "random"), _n_(379216, "n", lambda: n)),
    }), "set_index"), 'player_id')
    _l_(379221)

    _n_(379222, "namespace", lambda: namespace).df = _n_(379223, "dataframe_to_be_shared", lambda: dataframe_to_be_shared)
    _l_(379224)

    for i in _c_(379227, _n_(379225, "range", lambda: range), _n_(379226, "n", lambda: n)):
        _l_(379233)

        _c_(379231, _n_(379228, "add_empty_dfs_to_shared_dict", lambda: add_empty_dfs_to_shared_dict), _n_(379229, "shared_dict", lambda: shared_dict), _n_(379230, "i", lambda: i))
        _l_(379232)

    jobs = []
    _l_(379234)
    for i in _c_(379237, _n_(379235, "range", lambda: range), _n_(379236, "n", lambda: n)):
        _l_(379255)

        p = _c_(379244, _a_(379239, _n_(379238, "multiprocessing", lambda: multiprocessing), "Process"), target=_n_(379240, "edit_df_in_shared_dict", lambda: edit_df_in_shared_dict),
            args=(_n_(379241, "shared_dict", lambda: shared_dict), _n_(379242, "namespace", lambda: namespace), _n_(379243, "i", lambda: i))
        )
        _l_(379245)
        _c_(379249, _a_(379247, _n_(379246, "jobs", lambda: jobs), "append"), _n_(379248, "p", lambda: p))
        _l_(379250)
        _c_(379253, _a_(379252, _n_(379251, "p", lambda: p), "start"))
        _l_(379254)

    for p in _n_(379256, "jobs", lambda: jobs):
        _l_(379261)

        _c_(379259, _a_(379258, _n_(379257, "p", lambda: p), "join"))
        _l_(379260)

    _c_(379264, _n_(379262, "print", lambda: print), _n_(379263, "shared_dict", lambda: shared_dict)[1])
    _l_(379265)
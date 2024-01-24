# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62703755/typeerror-init-got-multiple-values-for-argument-center
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import yt
    _l_(571819)

except ImportError:
    pass

ds = _c_(571822, _a_(571821, _n_(571820, "yt", lambda: yt), "load"), "puredef_hdf5_chk_000000")
_l_(571823)
p = _c_(571827, _a_(571825, _n_(571824, "yt", lambda: yt), "ProjectionPlot"), _n_(571826, "ds", lambda: ds),'particle_postion_x', 'particle_postion_y',['particle_dens'], center='m', width=(20, 'Mpc'))
_l_(571828)
_c_(571831, _a_(571830, _n_(571829, "p", lambda: p), "annotate_particles"), (20, 'Mpc'))
_l_(571832)
_c_(571835, _a_(571834, _n_(571833, "p", lambda: p), "save"))
_l_(571836)
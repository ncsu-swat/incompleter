# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46618669/i-am-using-gridsearchcv-and-fit-is-giving-me-a-typeerror-get-params-missing-1
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
k=['rbf', 'linear','poly','sigmoid']
_l_(418863)
c= [1,5,10,20,30,50,80,100]
_l_(418864)
g=[1e-7,1e-6,1e-5,1e-4,1e-2,0.0001]
_l_(418865)

param_grid=_c_(418870, _n_(418866, "dict", lambda: dict), kernel=_n_(418867, "k", lambda: k), C=_n_(418868, "c", lambda: c), gamma=_n_(418869, "g", lambda: g))
_l_(418871)
_c_(418874, _n_(418872, "print", lambda: print), _n_(418873, "param_grid", lambda: param_grid))
_l_(418875)
grid = _c_(418879, _n_(418876, "GridSearchCV", lambda: GridSearchCV), _n_(418877, "SVC", lambda: SVC), _n_(418878, "param_grid", lambda: param_grid),scoring='accuracy')
_l_(418880)
_c_(418885, _a_(418882, _n_(418881, "grid", lambda: grid), "fit"), _n_(418883, "X_t_train", lambda: X_t_train), _n_(418884, "y_t_train", lambda: y_t_train))  
_l_(418886)  

_c_(418888, _n_(418887, "print", lambda: print))
_l_(418889)
_c_(418891, _n_(418890, "print", lambda: print), "Grid scores on development set:")
_l_(418892)
_c_(418894, _n_(418893, "print", lambda: print))  
_l_(418895)  
_c_(418899, _n_(418896, "print", lambda: print), _a_(418898, _n_(418897, "grid", lambda: grid), "grid_scores_"))
_l_(418900)
_c_(418902, _n_(418901, "print", lambda: print), "Best parameters set found on development set:")
_l_(418903)
_c_(418905, _n_(418904, "print", lambda: print))
_l_(418906)
_c_(418910, _n_(418907, "print", lambda: print), _a_(418909, _n_(418908, "grid", lambda: grid), "best_params_"))
_l_(418911)
_c_(418913, _n_(418912, "print", lambda: print), "Grid best score:")
_l_(418914)
_c_(418916, _n_(418915, "print", lambda: print))
_l_(418917)
_c_(418921, _n_(418918, "print", lambda: print), _a_(418920, _n_(418919, "grid", lambda: grid), "best_score_"))
_l_(418922)
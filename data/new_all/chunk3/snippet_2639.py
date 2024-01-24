# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68146968/typeerror-tuple-indices-must-be-integers-or-slices-not-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
avgPetal_widthS = _c_(569135, _n_(569133, "Average", lambda: Average), _n_(569134, "petal_widthS", lambda: petal_widthS))
_l_(569136)
avgPetal_widthVe = _c_(569139, _n_(569137, "Average", lambda: Average), _n_(569138, "petal_widthVe", lambda: petal_widthVe))
_l_(569140)
avgPetal_widthVi = _c_(569143, _n_(569141, "Average", lambda: Average), _n_(569142, "petal_widthVi", lambda: petal_widthVi))
_l_(569144)
avgPetal_lengthS = _c_(569147, _n_(569145, "Average", lambda: Average), _n_(569146, "petal_lengthS", lambda: petal_lengthS))
_l_(569148)
avgPetal_lengthVe = _c_(569151, _n_(569149, "Average", lambda: Average), _n_(569150, "petal_lengthVe", lambda: petal_lengthVe))
_l_(569152)
avgPetal_lengthVi = _c_(569155, _n_(569153, "Average", lambda: Average), _n_(569154, "petal_lengthVi", lambda: petal_lengthVi))
_l_(569156)
avgSepal_widthS = _c_(569159, _n_(569157, "Average", lambda: Average), _n_(569158, "sepal_widthS", lambda: sepal_widthS))
_l_(569160)
avgSepal_widthVe = _c_(569163, _n_(569161, "Average", lambda: Average), _n_(569162, "sepal_widthVe", lambda: sepal_widthVe))
_l_(569164)
avgSepal_widthVi = _c_(569167, _n_(569165, "Average", lambda: Average), _n_(569166, "sepal_widthVi", lambda: sepal_widthVi))
_l_(569168)
avgSepal_lengthS = _c_(569171, _n_(569169, "Average", lambda: Average), _n_(569170, "sepal_lengthS", lambda: sepal_lengthS))
_l_(569172)
avgSepal_lengthVe = _c_(569175, _n_(569173, "Average", lambda: Average), _n_(569174, "sepal_lengthVe", lambda: sepal_lengthVe))
_l_(569176)
avgSepal_lengthVi = _c_(569179, _n_(569177, "Average", lambda: Average), _n_(569178, "sepal_lengthVi", lambda: sepal_lengthVi))
_l_(569180)

setosa = []
_l_(569181)
versicolor = []
_l_(569182)
virginica = []
_l_(569183)

_c_(569190, _a_(569185, _n_(569184, "setosa", lambda: setosa), "append"), ['Setsota',_n_(569186, "avgPetal_lengthS", lambda: avgPetal_lengthS),_n_(569187, "avgPetal_widthS", lambda: avgPetal_widthS),_n_(569188, "avgSepal_lengthS", lambda: avgSepal_lengthS),_n_(569189, "avgSepal_widthS", lambda: avgSepal_widthS)])
_l_(569191)
_c_(569198, _a_(569193, _n_(569192, "versicolor", lambda: versicolor), "append"), ['Versicolor',_n_(569194, "avgPetal_lengthVe", lambda: avgPetal_lengthVe),_n_(569195, "avgPetal_widthVe", lambda: avgPetal_widthVe),_n_(569196, "avgSepal_lengthVe", lambda: avgSepal_lengthVe),_n_(569197, "avgSepal_widthVe", lambda: avgSepal_widthVe)])
_l_(569199)
_c_(569206, _a_(569201, _n_(569200, "virginica", lambda: virginica), "append"), ['Virginica',_n_(569202, "avgPetal_lengthVi", lambda: avgPetal_lengthVi),_n_(569203, "avgPetal_widthVi", lambda: avgPetal_widthVi),_n_(569204, "avgSepal_lengthVi", lambda: avgSepal_lengthVi),_n_(569205, "avgSepal_widthVi", lambda: avgSepal_widthVi)])
_l_(569207)

avgIris = (
    ['Setsota',_n_(569208, "avgPetal_lengthS", lambda: avgPetal_lengthS),_n_(569209, "avgPetal_widthS", lambda: avgPetal_widthS),_n_(569210, "avgSepal_lengthS", lambda: avgSepal_lengthS),_n_(569211, "avgSepal_widthS", lambda: avgSepal_widthS)], 
    ['Versicolor',_n_(569212, "avgPetal_lengthVe", lambda: avgPetal_lengthVe),_n_(569213, "avgPetal_widthVe", lambda: avgPetal_widthVe),_n_(569214, "avgSepal_lengthVe", lambda: avgSepal_lengthVe),_n_(569215, "avgSepal_widthVe", lambda: avgSepal_widthVe)],
    ['Virginica',_n_(569216, "avgPetal_lengthVi", lambda: avgPetal_lengthVi),_n_(569217, "avgPetal_widthVi", lambda: avgPetal_widthVi),_n_(569218, "avgSepal_lengthVi", lambda: avgSepal_lengthVi),_n_(569219, "avgSepal_widthVi", lambda: avgSepal_widthVi)])
_l_(569220)

gap = ' '*3
_l_(569221)
heading = f"{'Species:':11s}{_n_(569222, 'gap', lambda: gap)}{'Petal Length':12s}{_n_(569223, 'gap', lambda: gap)}{'Petal Width':11s}{_n_(569224, 'gap', lambda: gap)}{'Sepal Length':12s}{_n_(569225, 'gap', lambda: gap)}{'Sepal Width':11s}"
_l_(569226)
_c_(569228, _n_(569227, "print", lambda: print), "\n")
_l_(569229)
_c_(569231, _n_(569230, "print", lambda: print), "="*69)
_l_(569232)
_c_(569235, _n_(569233, "print", lambda: print), _n_(569234, "heading", lambda: heading))
_l_(569236)
_c_(569238, _n_(569237, "print", lambda: print), "-"*69)
_l_(569239)
_c_(569241, _n_(569240, "print", lambda: print), "Attributes (cm):")
_l_(569242)
for i in _n_(569243, "avgIris", lambda: avgIris):
    _l_(569259)

    rec = f"{_n_(569244, 'avgIris', lambda: avgIris)[_n_(569245, 'i', lambda: i)][0]:11s}{_n_(569246, 'gap', lambda: gap)}{_n_(569247, 'avgIris', lambda: avgIris)[_n_(569248, 'i', lambda: i)][1]:12f}{_n_(569249, 'gap', lambda: gap)}{_n_(569250, 'avgIris', lambda: avgIris)[_n_(569251, 'i', lambda: i)][2]:11f}{_n_(569252, 'gap', lambda: gap)}{_n_(569253, 'avgIris', lambda: avgIris)[_n_(569254, 'i', lambda: i)][3]:12f}{_n_(569255, 'gap', lambda: gap)}{_n_(569256, 'avgIris', lambda: avgIris)[_n_(569257, 'i', lambda: i)][4]:11f}"
    _l_(569258)
_c_(569262, _n_(569260, "print", lambda: print), _n_(569261, "rec", lambda: rec))
_l_(569263)
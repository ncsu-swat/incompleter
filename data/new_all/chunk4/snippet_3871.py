# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66162440/typeerror-dict-object-is-not-callable-while-loading-and-testing-pytorch-model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
_l_(638288)

model = _c_(638291, _a_(638290, _n_(638289, "torch", lambda: torch), "load"), 'Final_model.pth.tar')
_l_(638292)

normalize = _c_(638295, _a_(638294, _n_(638293, "transforms", lambda: transforms), "Normalize"), mean=[0.4914, 0.4824, 0.4467],std=[0.2471, 0.2435, 0.2616])
_l_(638296)
transform = _c_(638303, _a_(638298, _n_(638297, "transforms", lambda: transforms), "Compose"), [_c_(638301, _a_(638300, _n_(638299, "transforms", lambda: transforms), "ToTensor")),_n_(638302, "normalize", lambda: normalize)])
_l_(638304)
val_set = _c_(638308, _a_(638306, _n_(638305, "datasets", lambda: datasets), "CIFAR10"), '../data', train=False,download=True,transform=_n_(638307, "transform", lambda: transform))
_l_(638309)

for i in _c_(638311, _n_(638310, "range", lambda: range), 48,64):
    _l_(638359)

    _c_(638315, _a_(638313, _n_(638312, "plt", lambda: plt), "subplot"), 4,4,_n_(638314, "i", lambda: i)+1-48)
    _l_(638316)
    _c_(638319, _a_(638318, _n_(638317, "plt", lambda: plt), "subplots_adjust"), hspace=1,wspace=1)
    _l_(638320)
    _c_(638323, _a_(638322, _n_(638321, "plt", lambda: plt), "xticks"), [])
    _l_(638324)
    _c_(638327, _a_(638326, _n_(638325, "plt", lambda: plt), "yticks"), [])
    _l_(638328)
    _c_(638334, _a_(638330, _n_(638329, "plt", lambda: plt), "imshow"), _a_(638332, _n_(638331, "val_set", lambda: val_set), "data")[_n_(638333, "i", lambda: i)])
    _l_(638335)
    out = _c_(638346, _a_(638345, _c_(638344, _n_(638336, "model", lambda: model), _c_(638343, _a_(638342, _c_(638341, _n_(638337, "transform", lambda: transform), _a_(638339, _n_(638338, "val_set", lambda: val_set), "data")[_n_(638340, "i", lambda: i)]), "view"), 1,3,32,32))[0], "tolist"))
    _l_(638347)
    _c_(638357, _a_(638349, _n_(638348, "plt", lambda: plt), "xlabel"), _n_(638350, "class_names", lambda: class_names)[_c_(638356, _a_(638352, _n_(638351, "out", lambda: out), "index"), _c_(638355, _n_(638353, "max", lambda: max), _n_(638354, "out", lambda: out)))])
    _l_(638358)
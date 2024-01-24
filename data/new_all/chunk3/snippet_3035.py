# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52688788/typeerror-only-size-1-arrays-can-be-converted-to-python-scalars-when-trying-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
train_labels_GT = _n_(536836, "y_train", lambda: y_train)[:,1] #Get Ground truth
_l_(536837) #Get Ground truth


_c_(536839, _n_(536838, "print", lambda: print), 'Writing train text file...')
_l_(536840)

data_dir = _c_(536847, _a_(536843, _a_(536842, _n_(536841, "os", lambda: os), "path"), "join"), _c_(536846, _a_(536845, _n_(536844, "os", lambda: os), "getcwd")), "Data/Out")
_l_(536848)


_c_(536857, _n_(536849, "savetxt", lambda: savetxt), _c_(536854, _a_(536852, _a_(536851, _n_(536850, "os", lambda: os), "path"), "join"), _n_(536853, "data_dir", lambda: data_dir), "train.txt"), _n_(536855, "x_train", lambda: x_train), True, _n_(536856, "y_train", lambda: y_train))
_l_(536858)
_c_(536867, _n_(536859, "savetxt", lambda: savetxt), _c_(536864, _a_(536862, _a_(536861, _n_(536860, "os", lambda: os), "path"), "join"), _n_(536863, "data_dir", lambda: data_dir), "test.txt"), _n_(536865, "x_test", lambda: x_test), True, _n_(536866, "y_test", lambda: y_test))
_l_(536868)


_c_(536870, _n_(536869, "print", lambda: print), "Done")
_l_(536871)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51870801/typeerror-fetch-argument-none-has-invalid-type-class-nonetype-in-tensorflow
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(388672)

except ImportError:
    pass
try:
    import numpy as np
    _l_(388674)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(388676)

except ImportError:
    pass
try:
    from sklearn.datasets import load_boston
    _l_(388678)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(388680)

except ImportError:
    pass

boston=_c_(388682, _n_(388681, "load_boston", lambda: load_boston))
_l_(388683)
_c_(388686, _n_(388684, "type", lambda: type), _n_(388685, "boston", lambda: boston))
_l_(388687)
_a_(388689, _n_(388688, "boston", lambda: boston), "feature_names")
_l_(388690)

bd=_c_(388697, _a_(388692, _n_(388691, "pd", lambda: pd), "DataFrame"), data=_a_(388694, _n_(388693, "boston", lambda: boston), "data"),columns=_a_(388696, _n_(388695, "boston", lambda: boston), "feature_names"))
_l_(388698)

_n_(388699, "bd", lambda: bd)['Price']=_c_(388704, _a_(388701, _n_(388700, "pd", lambda: pd), "DataFrame"), data=_a_(388703, _n_(388702, "boston", lambda: boston), "target"))
_l_(388705)
_c_(388711, _a_(388708, _a_(388707, _n_(388706, "np", lambda: np), "random"), "shuffle"), _a_(388710, _n_(388709, "bd", lambda: bd), "values"))
_l_(388712)


W0=_c_(388715, _a_(388714, _n_(388713, "tf", lambda: tf), "Variable"), 0.0000000003)
_l_(388716)
W1=_c_(388719, _a_(388718, _n_(388717, "tf", lambda: tf), "Variable"), 0.000000000002)
_l_(388720)
b=_c_(388723, _a_(388722, _n_(388721, "tf", lambda: tf), "Variable"), 0.0000000000001)
_l_(388724)
    #print(bd.shape[1])

    #tf.summary.histogram('Weights', W0)
    #tf.summary.histogram('Weights', W1)
    #tf.summary.histogram('Biases', b)



dataset_input=_a_(388726, _n_(388725, "bd", lambda: bd), "iloc")[:, 0 : _a_(388728, _n_(388727, "bd", lambda: bd), "shape")[1]-1];
_l_(388729)
    #dataset_input.head(2)

dataset_output=_a_(388731, _n_(388730, "bd", lambda: bd), "iloc")[:, _a_(388733, _n_(388732, "bd", lambda: bd), "shape")[1]-1]
_l_(388734)
dataset_output=_a_(388736, _n_(388735, "dataset_output", lambda: dataset_output), "values")
_l_(388737)
dataset_output=_c_(388742, _a_(388739, _n_(388738, "dataset_output", lambda: dataset_output), "reshape"), (_a_(388741, _n_(388740, "bd", lambda: bd), "shape")[0],1)) #converted (506,) to (506,1) because in pandas
_l_(388743) #converted (506,) to (506,1) because in pandas
    #the shape was not changing and it was needed later in feed_dict


dataset_input=_a_(388745, _n_(388744, "dataset_input", lambda: dataset_input), "values")  #only dataset_input is in DataFrame form and converting it into np.ndarray
_l_(388746)  #only dataset_input is in DataFrame form and converting it into np.ndarray

    # ADDED
dataset_input = _c_(388752, _a_(388748, _n_(388747, "np", lambda: np), "array"), _n_(388749, "dataset_input", lambda: dataset_input), dtype=_a_(388751, _n_(388750, "np", lambda: np), "float32"))
_l_(388753)
    # ADDED
dataset_output = _c_(388759, _a_(388755, _n_(388754, "np", lambda: np), "array"), _n_(388756, "dataset_output", lambda: dataset_output), dtype=_a_(388758, _n_(388757, "np", lambda: np), "float32"))
_l_(388760)

X=_c_(388767, _a_(388762, _n_(388761, "tf", lambda: tf), "placeholder"), _a_(388764, _n_(388763, "tf", lambda: tf), "float32"), shape=(None,_a_(388766, _n_(388765, "bd", lambda: bd), "shape")[1]-1))
_l_(388768)
Y=_c_(388773, _a_(388770, _n_(388769, "tf", lambda: tf), "placeholder"), _a_(388772, _n_(388771, "tf", lambda: tf), "float32"), shape=(None,1))
_l_(388774)

Y_=_n_(388775, "W0", lambda: W0)*_n_(388776, "X", lambda: X)*_n_(388777, "X", lambda: X) + _n_(388778, "W1", lambda: W1)*_n_(388779, "X", lambda: X) + _n_(388780, "b", lambda: b)
_l_(388781)
    #Y_pred = tf.add(tf.multiply(tf.pow(X, pow_i), W), Y_pred)
_c_(388785, _n_(388782, "print", lambda: print), _a_(388784, _n_(388783, "X", lambda: X), "shape"))
_l_(388786)
_c_(388790, _n_(388787, "print", lambda: print), _a_(388789, _n_(388788, "Y", lambda: Y), "shape"))
_l_(388791)


loss=_c_(388799, _a_(388793, _n_(388792, "tf", lambda: tf), "reduce_mean"), _c_(388798, _a_(388795, _n_(388794, "tf", lambda: tf), "square"), _n_(388796, "Y_", lambda: Y_)-_n_(388797, "Y", lambda: Y)))
_l_(388800)
    #tf.summary.scalar('loss',loss)

optimizer=_c_(388804, _a_(388803, _a_(388802, _n_(388801, "tf", lambda: tf), "train"), "GradientDescentOptimizer"), 0.0000000000001)
_l_(388805)
train=_c_(388809, _a_(388807, _n_(388806, "optimizer", lambda: optimizer), "minimize"), _n_(388808, "loss", lambda: loss))
_l_(388810)

init=_c_(388813, _a_(388812, _n_(388811, "tf", lambda: tf), "global_variables_initializer"))#tf.global_variables_initializer()#tf.initialize_all_variables()
_l_(388814)#tf.global_variables_initializer()#tf.initialize_all_variables()
sess=_c_(388817, _a_(388816, _n_(388815, "tf", lambda: tf), "Session"))
_l_(388818)
_c_(388822, _a_(388820, _n_(388819, "sess", lambda: sess), "run"), _n_(388821, "init", lambda: init))
_l_(388823)



wb_=[]
_l_(388824)
with _c_(388827, _a_(388826, _n_(388825, "tf", lambda: tf), "Session")) as sess:
    _l_(388919)

    summary_merge = _c_(388831, _a_(388830, _a_(388829, _n_(388828, "tf", lambda: tf), "summary"), "merge_all"))
    _l_(388832)

    writer=_c_(388838, _a_(388835, _a_(388834, _n_(388833, "tf", lambda: tf), "summary"), "FileWriter"), "Users/ajay/Documents",_a_(388837, _n_(388836, "sess", lambda: sess), "graph"))
    _l_(388839)

    epochs=10
    _l_(388840)
    _c_(388844, _a_(388842, _n_(388841, "sess", lambda: sess), "run"), _n_(388843, "init", lambda: init))
    _l_(388845)

    for i in _c_(388848, _n_(388846, "range", lambda: range), _n_(388847, "epochs", lambda: epochs)):
        _l_(388918)

        s_mer=_c_(388856, _a_(388850, _n_(388849, "sess", lambda: sess), "run"), _n_(388851, "summary_merge", lambda: summary_merge),feed_dict={_n_(388852, "X", lambda: X): _n_(388853, "dataset_input", lambda: dataset_input), _n_(388854, "Y", lambda: Y): _n_(388855, "dataset_output", lambda: dataset_output)})  #ERROR________ERROR
        _l_(388857)  #ERROR________ERROR
        _c_(388865, _a_(388859, _n_(388858, "sess", lambda: sess), "run"), _n_(388860, "train", lambda: train),feed_dict={_n_(388861, "X", lambda: X):_n_(388862, "dataset_input", lambda: dataset_input),_n_(388863, "Y", lambda: Y):_n_(388864, "dataset_output", lambda: dataset_output)})
        _l_(388866)

            #CHANGED
        _c_(388876, _n_(388867, "print", lambda: print), "loss",_c_(388875, _a_(388869, _n_(388868, "sess", lambda: sess), "run"), _n_(388870, "loss", lambda: loss), feed_dict={_n_(388871, "X", lambda: X):_n_(388872, "dataset_input", lambda: dataset_input),_n_(388873, "Y", lambda: Y):_n_(388874, "dataset_output", lambda: dataset_output)}))
        _l_(388877)
        #sess.run(loss, feed_dict={X:dataset_input,Y:dataset_output})
        _c_(388882, _a_(388879, _n_(388878, "writer", lambda: writer), "add_summary"), _n_(388880, "s_mer", lambda: s_mer),_n_(388881, "i", lambda: i))
        _l_(388883)

            #tf.summary.histogram(name="loss",values=loss)
        if(_n_(388884, "i", lambda: i)%5==0):
            _l_(388905)

            _c_(388893, _n_(388885, "print", lambda: print), _n_(388886, "i", lambda: i), _c_(388892, _a_(388888, _n_(388887, "sess", lambda: sess), "run"), [_n_(388889, "W0", lambda: W0),_n_(388890, "W1", lambda: W1),_n_(388891, "b", lambda: b)]))
            _l_(388894)
            _c_(388903, _a_(388896, _n_(388895, "wb__", lambda: wb__), "append"), _c_(388902, _a_(388898, _n_(388897, "sess", lambda: sess), "run"), [_n_(388899, "W0", lambda: W0),_n_(388900, "W1", lambda: W1),_n_(388901, "b", lambda: b)]))
            _l_(388904)

        _c_(388910, _n_(388906, "print", lambda: print), _c_(388909, _a_(388908, _n_(388907, "writer", lambda: writer), "get_logdir")))
        _l_(388911)
        _c_(388916, _n_(388912, "print", lambda: print), _c_(388915, _a_(388914, _n_(388913, "writer", lambda: writer), "close")))
        _l_(388917)
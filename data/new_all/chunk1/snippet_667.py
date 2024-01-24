# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63497874/typeerror-keyword-argument-not-understood-input
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
model = _c_(384846, _n_(384845, "Sequential", lambda: Sequential))
_l_(384847)
_c_(384850, _n_(384848, "print", lambda: print), _n_(384849, "nb_filters", lambda: nb_filters)[0], 'filters')
_l_(384851)
_c_(384856, _n_(384852, "print", lambda: print), 'input shape', _n_(384853, "img_rows", lambda: img_rows), 'rows', _n_(384854, "img_cols", lambda: img_cols), 'cols', _n_(384855, "patch_size", lambda: patch_size), 'patchsize')
_l_(384857)

_c_(384868, _a_(384859, _n_(384858, "model", lambda: model), "add"), _c_(384867, _n_(384860, "Convolution3D", lambda: Convolution3D), _n_(384861, "nb_filters", lambda: nb_filters)[0],
    kernel_dim1=1, # depth
    kernel_dim2=_n_(384862, "nb_conv", lambda: nb_conv)[0], # rows
    kernel_dim3=_n_(384863, "nb_conv", lambda: nb_conv)[1], # cols
    input_shape=(1, _n_(384864, "img_rows", lambda: img_rows), _n_(384865, "img_cols", lambda: img_cols), _n_(384866, "patch_size", lambda: patch_size)),
    activation='relu'
))
_l_(384869)

_c_(384876, _a_(384871, _n_(384870, "model", lambda: model), "add"), _c_(384875, _n_(384872, "MaxPooling3D", lambda: MaxPooling3D), pool_size=(1, _n_(384873, "nb_pool", lambda: nb_pool)[0], _n_(384874, "nb_pool", lambda: nb_pool)[0])))
_l_(384877)

_c_(384882, _a_(384879, _n_(384878, "model", lambda: model), "add"), _c_(384881, _n_(384880, "Dropout", lambda: Dropout), 0.2))
_l_(384883)

_c_(384888, _a_(384885, _n_(384884, "model", lambda: model), "add"), _c_(384887, _n_(384886, "Flatten", lambda: Flatten)))
_l_(384889)

_c_(384894, _a_(384891, _n_(384890, "model", lambda: model), "add"), _c_(384893, _n_(384892, "Dense", lambda: Dense), 128, init='normal', activation='relu'))
_l_(384895)

_c_(384900, _a_(384897, _n_(384896, "model", lambda: model), "add"), _c_(384899, _n_(384898, "Dropout", lambda: Dropout), 0.2))
_l_(384901)

_c_(384907, _a_(384903, _n_(384902, "model", lambda: model), "add"), _c_(384906, _n_(384904, "Dense", lambda: Dense), _n_(384905, "nb_classes", lambda: nb_classes),init='normal'))
_l_(384908)

_c_(384913, _a_(384910, _n_(384909, "model", lambda: model), "add"), _c_(384912, _n_(384911, "Activation", lambda: Activation), 'softmax'))
_l_(384914)
#optimizer adam,sgd,RMSprop,Adagrad,Adadelta,Nadam,
_c_(384917, _a_(384916, _n_(384915, "model", lambda: model), "compile"), loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
_l_(384918)
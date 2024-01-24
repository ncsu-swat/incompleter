# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63492634/typeerror-init-missing-1-required-positional-argument-kernel-size
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
model = _c_(567073, _n_(567072, "Sequential", lambda: Sequential))
_l_(567074)
_c_(567077, _n_(567075, "print", lambda: print), _n_(567076, "nb_filters", lambda: nb_filters)[0], 'filters')
_l_(567078)
_c_(567083, _n_(567079, "print", lambda: print), 'input shape', _n_(567080, "img_rows", lambda: img_rows), 'rows', _n_(567081, "img_cols", lambda: img_cols), 'cols', _n_(567082, "patch_size", lambda: patch_size), 'patchsize')
_l_(567084)

_c_(567095, _a_(567086, _n_(567085, "model", lambda: model), "add"), _c_(567094, _n_(567087, "Convolution3D", lambda: Convolution3D), _n_(567088, "nb_filters", lambda: nb_filters)[0],
    kernel_dim1=1, # depth
    kernel_dim2=_n_(567089, "nb_conv", lambda: nb_conv)[0], # rows
    kernel_dim3=_n_(567090, "nb_conv", lambda: nb_conv)[1], # cols
    input_shape=(1, _n_(567091, "img_rows", lambda: img_rows), _n_(567092, "img_cols", lambda: img_cols), _n_(567093, "patch_size", lambda: patch_size)),
    activation='relu'
))
_l_(567096)

_c_(567103, _a_(567098, _n_(567097, "model", lambda: model), "add"), _c_(567102, _n_(567099, "MaxPooling3D", lambda: MaxPooling3D), pool_size=(1, _n_(567100, "nb_pool", lambda: nb_pool)[0], _n_(567101, "nb_pool", lambda: nb_pool)[0])))
_l_(567104)

_c_(567109, _a_(567106, _n_(567105, "model", lambda: model), "add"), _c_(567108, _n_(567107, "Dropout", lambda: Dropout), 0.2))
_l_(567110)

_c_(567115, _a_(567112, _n_(567111, "model", lambda: model), "add"), _c_(567114, _n_(567113, "Flatten", lambda: Flatten)))
_l_(567116)

_c_(567121, _a_(567118, _n_(567117, "model", lambda: model), "add"), _c_(567120, _n_(567119, "Dense", lambda: Dense), 128, init='normal', activation='relu'))
_l_(567122)

_c_(567127, _a_(567124, _n_(567123, "model", lambda: model), "add"), _c_(567126, _n_(567125, "Dropout", lambda: Dropout), 0.2))
_l_(567128)

_c_(567134, _a_(567130, _n_(567129, "model", lambda: model), "add"), _c_(567133, _n_(567131, "Dense", lambda: Dense), _n_(567132, "nb_classes", lambda: nb_classes),init='normal'))
_l_(567135)

_c_(567140, _a_(567137, _n_(567136, "model", lambda: model), "add"), _c_(567139, _n_(567138, "Activation", lambda: Activation), 'softmax'))
_l_(567141)
#optimizer adam,sgd,RMSprop,Adagrad,Adadelta,Nadam,
_c_(567144, _a_(567143, _n_(567142, "model", lambda: model), "compile"), loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
_l_(567145)
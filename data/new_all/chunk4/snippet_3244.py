# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76790765/typeerror-exception-encountered-when-calling-layer-convtokenizer-type-convto
# Compile
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
opt = _c_(618823, _n_(618820, "AdamW", lambda: AdamW), learning_rate=_n_(618821, "Learning_Rate", lambda: Learning_Rate), weight_decay=_n_(618822, "Weight_Decay", lambda: Weight_Decay))
_l_(618824)
_c_(618832, _a_(618826, _n_(618825, "model", lambda: model), "compile"), loss='sparse_categorical_crossentropy',
    optimizer=_n_(618827, "opt", lambda: opt),
    metrics=[
        _c_(618829, _n_(618828, "Accuracy", lambda: Accuracy), name="Top1Accuracy"), _c_(618831, _n_(618830, "TopKAccuracy", lambda: TopKAccuracy), k=3, name="Top3Accuracy")
    ]
)
_l_(618833)

history = _c_(618838, _a_(618835, _n_(618834, "model", lambda: model), "fit"), _n_(618836, "train_ds", lambda: train_ds),
    validation_data=_n_(618837, "test_ds", lambda: test_ds), 
    epochs=5
)
_l_(618839)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61109095/typeerror-nonetype-object-is-not-subscriptable-when-i-train-a-cnn-model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Metrics(_n_(536377, "Callback", lambda: Callback)):
    _l_(536432)

    def on_train_begin(self, logs = {}):
        _l_(536380)

        _n_(536378, "self", lambda: self).val_kappas = []
        _l_(536379)

    def on_epoch_end(self, epoch, logs = {}):
        _l_(536431)

        X_val, y_val = _a_(536382, _n_(536381, "self", lambda: self), "validation_data")[:2]
        _l_(536383)
        y_val = _c_(536386, _a_(536385, _n_(536384, "y_val", lambda: y_val), "sum"), axis = 1) - 1
        _l_(536387)

        y_pred = _c_(536392, _a_(536390, _a_(536389, _n_(536388, "self", lambda: self), "model"), "predict"), _n_(536391, "X_val", lambda: X_val)) > 0.5
        _l_(536393)
        y_pred = _c_(536399, _a_(536398, _c_(536397, _a_(536395, _n_(536394, "y_pred", lambda: y_pred), "astype"), _n_(536396, "int", lambda: int)), "sum"), axis = 1) - 1
        _l_(536400)

        _val_kappa = _c_(536404, _n_(536401, "cohen_kappa_score", lambda: cohen_kappa_score), _n_(536402, "y_val", lambda: y_val),
            _n_(536403, "y_pred", lambda: y_pred), 
            weights = 'quadratic'
        )
        _l_(536405)

        _c_(536410, _a_(536408, _a_(536407, _n_(536406, "self", lambda: self), "val_kappas"), "append"), _n_(536409, "_val_kappa", lambda: _val_kappa))
        _l_(536411)

        _c_(536414, _n_(536412, "print", lambda: print), f"val_kappa: {_n_(536413, '_val_kappa', lambda: _val_kappa):.4f}")
        _l_(536415)

        if _n_(536416, "_val_kappa", lambda: _val_kappa) == _c_(536420, _n_(536417, "max", lambda: max), _a_(536419, _n_(536418, "self", lambda: self), "val_kappas")):
            _l_(536429)

            _c_(536422, _n_(536421, "print", lambda: print), "Validation Kappa has improved. Saving model.")
            _l_(536423)
            _c_(536427, _a_(536426, _a_(536425, _n_(536424, "self", lambda: self), "model"), "save"), '/path_to/model.h5')
            _l_(536428)
        aux = ""
        _l_(536430)

        return aux
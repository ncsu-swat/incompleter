# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53095195/typeerror-unsupported-operand-types-for-builtin-function-or-method-and
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
fout = _c_(544454, _n_(544452, "open", lambda: open), _n_(544453, "path", lambda: path) + "/log.txt", "w")
_l_(544455)
while (True):
    _l_(544576)

    mini_batch = _c_(544460, _a_(544457, _n_(544456, "train_graph_data", lambda: train_graph_data), "sample"), _a_(544459, _n_(544458, "config", lambda: config), "batch_size"))
    _l_(544461)
    loss = _c_(544465, _a_(544463, _n_(544462, "model", lambda: model), "fit"), _n_(544464, "mini_batch", lambda: mini_batch))
    _l_(544466)
    batch_n += 1
    _l_(544467)
    if _a_(544469, _n_(544468, "train_graph_data", lambda: train_graph_data), "is_epoch_end"):
        _l_(544575)

        epochs += 1
        _l_(544470)
        batch_n = 0
        _l_(544471)
        loss = 0
        _l_(544472)
        if _n_(544473, "epochs", lambda: epochs) % _a_(544475, _n_(544474, "config", lambda: config), "display") == 0:
            _l_(544566)

            embedding = None
            _l_(544476)
            while (True):
                _l_(544508)

                mini_batch = _c_(544481, _a_(544478, _n_(544477, "train_graph_data", lambda: train_graph_data), "sample"), _a_(544480, _n_(544479, "config", lambda: config), "batch_size"), do_shuffle=False)
                _l_(544482)
                loss += _c_(544486, _a_(544484, _n_(544483, "model", lambda: model), "get_loss"), _n_(544485, "mini_batch", lambda: mini_batch))
                _l_(544487)
                if _n_(544488, "embedding", lambda: embedding) is None:
                    _l_(544503)

                    embedding = _c_(544492, _a_(544490, _n_(544489, "model", lambda: model), "get_embedding"), _n_(544491, "mini_batch", lambda: mini_batch))
                    _l_(544493)
                else:
                    embedding = _c_(544501, _a_(544495, _n_(544494, "np", lambda: np), "vstack"), (_n_(544496, "embedding", lambda: embedding), _c_(544500, _a_(544498, _n_(544497, "model", lambda: model), "get_embedding"), _n_(544499, "mini_batch", lambda: mini_batch))))
                    _l_(544502)
                if _a_(544505, _n_(544504, "train_graph_data", lambda: train_graph_data), "is_epoch_end"):
                    _l_(544507)

                    break
                    _l_(544506)
            if _a_(544510, _n_(544509, "config", lambda: config), "check_reconstruction"):
                _l_(544521)

                _n_(544511, "print", lambda: print) >> _n_(544512, "fout", lambda: fout), _n_(544513, "epochs", lambda: epochs), "reconstruction:", _c_(544519, _n_(544514, "check_reconstruction", lambda: check_reconstruction), _n_(544515, "embedding", lambda: embedding), _n_(544516, "train_graph_data", lambda: train_graph_data),
                                                                               _a_(544518, _n_(544517, "config", lambda: config), "check_reconstruction"))
                _l_(544520)
            if _a_(544523, _n_(544522, "config", lambda: config), "check_link_prediction"):
                _l_(544535)

                _n_(544524, "print", lambda: print) >> _n_(544525, "fout", lambda: fout), _n_(544526, "epochs", lambda: epochs), "link_prediction:", _c_(544533, _n_(544527, "check_link_prediction", lambda: check_link_prediction), _n_(544528, "embedding", lambda: embedding), _n_(544529, "train_graph_data", lambda: train_graph_data),
                                                                                 _n_(544530, "origin_graph_data", lambda: origin_graph_data),
                                                                                 _a_(544532, _n_(544531, "config", lambda: config), "check_link_prediction"))
                _l_(544534)
            if _a_(544537, _n_(544536, "config", lambda: config), "check_classification"):
                _l_(544553)

                data = _c_(544542, _a_(544539, _n_(544538, "train_graph_data", lambda: train_graph_data), "sample"), _a_(544541, _n_(544540, "train_graph_data", lambda: train_graph_data), "N"), do_shuffle=False, with_label=True)
                _l_(544543)
                _n_(544544, "print", lambda: print) >> _n_(544545, "fout", lambda: fout), _n_(544546, "epochs", lambda: epochs), "classification", _c_(544551, _n_(544547, "check_multi_label_classification", lambda: check_multi_label_classification), _n_(544548, "embedding", lambda: embedding), _a_(544550, _n_(544549, "data", lambda: data), "label"))
                _l_(544552)
            _c_(544556, _a_(544555, _n_(544554, "fout", lambda: fout), "flush"))
            _l_(544557)
            _c_(544564, _a_(544559, _n_(544558, "model", lambda: model), "save_model"), _n_(544560, "path", lambda: path) + '/epoch' + _c_(544563, _n_(544561, "str", lambda: str), _n_(544562, "epochs", lambda: epochs)) + ".model")
            _l_(544565)
        if _n_(544567, "epochs", lambda: epochs) == _a_(544569, _n_(544568, "config", lambda: config), "epochs_limit"):
            _l_(544574)

            _c_(544571, _n_(544570, "print", lambda: print), "exceed epochs limit terminating")
            _l_(544572)
            break
            _l_(544573)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59590849/attributeerror-int-object-has-no-attribute-view1
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for epoch in _c_(451407, _n_(451405, "range", lambda: range), _n_(451406, "epochs", lambda: epochs)):
    _l_(451504)

    # Train for one epoch, then validate
    _c_(451414, _n_(451408, "train", lambda: train), _n_(451409, "train_loader", lambda: train_loader), _n_(451410, "model", lambda: model), _n_(451411, "criterion", lambda: criterion), _n_(451412, "optimizer", lambda: optimizer), _n_(451413, "epoch", lambda: epoch))
    _l_(451415)
    correct=0
    _l_(451416)
    total=0
    _l_(451417)

    with _c_(451420, _a_(451419, _n_(451418, "torch", lambda: torch), "no_grad")):
        _l_(451476)

        losses = _c_(451427, _n_(451421, "validate", lambda: validate), _n_(451422, "val_loader", lambda: val_loader), _n_(451423, "model", lambda: model), _n_(451424, "criterion", lambda: criterion), _n_(451425, "save_images", lambda: save_images), _n_(451426, "epoch", lambda: epoch))
        _l_(451428)
        for data in _c_(451431, _n_(451429, "enumerate", lambda: enumerate), _n_(451430, "train_loader", lambda: train_loader)):
            _l_(451443)

            input_gray, labels = _n_(451432, "data", lambda: data)
            _l_(451433)
            input_gray = _c_(451437, _a_(451435, _n_(451434, "input_gray", lambda: input_gray), "view"), _n_(451436, "batch_size", lambda: batch_size),1,64,32)
            _l_(451438)
            input_gray = _c_(451441, _a_(451440, _n_(451439, "input_gray", lambda: input_gray), "float"))
            _l_(451442)

        if _n_(451444, "use_gpu", lambda: use_gpu):
            _l_(451454)

            input_gray, labels = _c_(451448, _a_(451447, _a_(451446, _n_(451445, "input_gray", lambda: input_gray), "to"), "cuda")), _c_(451452, _a_(451451, _a_(451450, _n_(451449, "labels", lambda: labels), "to"), "cuda"))
            _l_(451453)

        output_ab = _c_(451457, _n_(451455, "model", lambda: model), _n_(451456, "input_gray", lambda: input_gray))
        _l_(451458)
        _, predicted = _c_(451463, _a_(451460, _n_(451459, "torch", lambda: torch), "max"), _a_(451462, _n_(451461, "output_ab", lambda: output_ab), "data"),1)
        _l_(451464)
        total+=_c_(451467, _a_(451466, _n_(451465, "labels", lambda: labels), "size"))
        _l_(451468)
        correct+=_c_(451474, _a_(451473, _c_(451472, _a_(451471, (_n_(451469, "predicted", lambda: predicted)==_n_(451470, "labels", lambda: labels)), "sum")), "item"))
        _l_(451475)

    _c_(451480, _n_(451477, "print", lambda: print), "Accuracy train %d %%"%(100*_n_(451478, "correct", lambda: correct)/_n_(451479, "total", lambda: total)))
    _l_(451481)
    _c_(451486, _a_(451483, _n_(451482, "train_acc", lambda: train_acc), "append"), 100*_n_(451484, "correct", lambda: correct)/_n_(451485, "total", lambda: total))    
    _l_(451487)    

    # Save checkpoint and replace old best model if current model is better   
    if _n_(451488, "losses", lambda: losses) < _n_(451489, "best_losses", lambda: best_losses):
        _l_(451503)

        best_losses = _n_(451490, "losses", lambda: losses)
        _l_(451491)
        _c_(451501, _a_(451493, _n_(451492, "torch", lambda: torch), "save"), _c_(451496, _a_(451495, _n_(451494, "model", lambda: model), "state_dict")), _c_(451500, _a_(451497, 'checkpoints/model-epoch-{}-losses-{:.3f}.pth', "format"), _n_(451498, "epoch", lambda: epoch)+1,_n_(451499, "losses", lambda: losses)))
        _l_(451502)
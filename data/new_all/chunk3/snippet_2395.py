# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46650275/not-run-the-model-with-test-data-typeerror-cannot-interpret-feed-dict-key-as
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(532861, _a_(532860, _n_(532859, "tf", lambda: tf), "Session")) as sess:
    _l_(532987)

    _c_(532867, _a_(532863, _n_(532862, "sess", lambda: sess), "run"), _c_(532866, _a_(532865, _n_(532864, "tf", lambda: tf), "global_variables_initializer")))
    _l_(532868)
    iteration=0
    _l_(532869)
    for e in _c_(532872, _n_(532870, "range", lambda: range), _n_(532871, "epochs", lambda: epochs)):
        _l_(532981)

        for batch_x,batch_y in _c_(532877, _n_(532873, "get_batch", lambda: get_batch), _n_(532874, "train_x", lambda: train_x),_n_(532875, "train_y", lambda: train_y),_n_(532876, "batch_size", lambda: batch_size)):
            _l_(532980)

            iteration+=1
            _l_(532878)
            feed = {_a_(532880, _n_(532879, "pred1", lambda: pred1), "inputs"): _n_(532881, "train_x", lambda: train_x),
                    _a_(532883, _n_(532882, "pred1", lambda: pred1), "y"): _n_(532884, "train_y", lambda: train_y),
                    _a_(532886, _n_(532885, "pred1", lambda: pred1), "learning_rate"): _n_(532887, "learning_rate_value", lambda: learning_rate_value),
                    _a_(532889, _n_(532888, "pred1", lambda: pred1), "is_training"):True
                   }
            _l_(532890)
            train_loss, _, train_acc = _c_(532900, _a_(532892, _n_(532891, "sess", lambda: sess), "run"), [_a_(532894, _n_(532893, "pred1", lambda: pred1), "cost"), _a_(532896, _n_(532895, "pred1", lambda: pred1), "optimizer"), _a_(532898, _n_(532897, "pred1", lambda: pred1), "accuracy")], feed_dict=_n_(532899, "feed", lambda: feed))
            _l_(532901)
            if _n_(532902, "iteration", lambda: iteration) % _n_(532903, "train_collect", lambda: train_collect) == 0:
                _l_(532979)

                _c_(532907, _a_(532905, _n_(532904, "x_collect", lambda: x_collect), "append"), _n_(532906, "e", lambda: e))
                _l_(532908)
                _c_(532912, _a_(532910, _n_(532909, "train_loss_collect", lambda: train_loss_collect), "append"), _n_(532911, "train_loss", lambda: train_loss))
                _l_(532913)
                _c_(532917, _a_(532915, _n_(532914, "train_acc_collect", lambda: train_acc_collect), "append"), _n_(532916, "train_acc", lambda: train_acc))
                _l_(532918)
                if _n_(532919, "iteration", lambda: iteration) % _n_(532920, "train_print", lambda: train_print)==0:
                    _l_(532934)

                    _c_(532932, _n_(532921, "print", lambda: print), _c_(532925, _a_(532922, "Epoch: {}/{}", "format"), _n_(532923, "e", lambda: e) + 1, _n_(532924, "epochs", lambda: epochs)),
                     _c_(532928, _a_(532926, "Train Loss: {:.4f}", "format"), _n_(532927, "train_loss", lambda: train_loss)),
                     _c_(532931, _a_(532929, "Train Acc: {:.4f}", "format"), _n_(532930, "train_acc", lambda: train_acc)))       
                    _l_(532933)       
                feed = {_a_(532936, _n_(532935, "pred1", lambda: pred1), "inputs"): _n_(532937, "valid_x", lambda: valid_x),
                        _a_(532939, _n_(532938, "pred1", lambda: pred1), "y"): _n_(532940, "valid_y", lambda: valid_y),
                        _a_(532942, _n_(532941, "pred1", lambda: pred1), "is_training"):False
                       }
                _l_(532943)
                val_loss, val_acc = _c_(532951, _a_(532945, _n_(532944, "sess", lambda: sess), "run"), [_a_(532947, _n_(532946, "pred1", lambda: pred1), "cost"), _a_(532949, _n_(532948, "pred1", lambda: pred1), "accuracy")], feed_dict=_n_(532950, "feed", lambda: feed))
                _l_(532952)
                _c_(532956, _a_(532954, _n_(532953, "valid_loss_collect", lambda: valid_loss_collect), "append"), _n_(532955, "val_loss", lambda: val_loss))
                _l_(532957)
                _c_(532961, _a_(532959, _n_(532958, "valid_acc_collect", lambda: valid_acc_collect), "append"), _n_(532960, "val_acc", lambda: val_acc)) 
                _l_(532962) 
                if _n_(532963, "iteration", lambda: iteration) % _n_(532964, "train_print", lambda: train_print)==0:
                    _l_(532978)

                    _c_(532976, _n_(532965, "print", lambda: print), _c_(532969, _a_(532966, "Epoch: {}/{}", "format"), _n_(532967, "e", lambda: e) + 1, _n_(532968, "epochs", lambda: epochs)),
                      _c_(532972, _a_(532970, "Validation Loss: {:.4f}", "format"), _n_(532971, "val_loss", lambda: val_loss)),
                      _c_(532975, _a_(532973, "Validation Acc: {:.4f}", "format"), _n_(532974, "val_acc", lambda: val_acc)))
                    _l_(532977)
    _c_(532985, _a_(532983, _n_(532982, "saver", lambda: saver), "save"), _n_(532984, "sess", lambda: sess), "./insurance2.ckpt")
    _l_(532986)
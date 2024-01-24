# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60296710/attributeerror-dataset-object-has-no-attribute-c-fastai
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
X = _c_(419107, _n_(419105, "list", lambda: list), _n_(419106, "df", lambda: df)['input_img'])
_l_(419108)
y = _c_(419111, _n_(419109, "list", lambda: list), _n_(419110, "df", lambda: df)['mask_img'])
_l_(419112)

X_train, X_valid, y_train, y_valid = _c_(419116, _n_(419113, "train_test_split", lambda: train_test_split), _n_(419114, "X", lambda: X), _n_(419115, "y", lambda: y), test_size=0.33, random_state=42)
_l_(419117)

class NumbersDataset():
    _l_(419163)

    def __init__(self, inputs, labels):
        _l_(419124)

        _n_(419118, "self", lambda: self).X = _n_(419119, "inputs", lambda: inputs)
        _l_(419120)
        _n_(419121, "self", lambda: self).y = _n_(419122, "labels", lambda: labels)
        _l_(419123)

    def __len__(self):
        _l_(419130)

        aux = _c_(419128, _n_(419125, "len", lambda: len), _a_(419127, _n_(419126, "self", lambda: self), "X"))
        _l_(419129)
        return aux

    def __getitem__(self, idx):
        _l_(419162)

        img_train = _c_(419136, _a_(419132, _n_(419131, "cv2", lambda: cv2), "imread"), _a_(419134, _n_(419133, "self", lambda: self), "X")[_n_(419135, "idx", lambda: idx)])
        _l_(419137)
        img_mask = _c_(419143, _a_(419139, _n_(419138, "cv2", lambda: cv2), "imread"), _a_(419141, _n_(419140, "self", lambda: self), "y")[_n_(419142, "idx", lambda: idx)])
        _l_(419144)
        img_train = _c_(419150, _a_(419146, _n_(419145, "cv2", lambda: cv2), "resize"), _n_(419147, "img_train", lambda: img_train), (427,240), interpolation = _a_(419149, _n_(419148, "cv2", lambda: cv2), "INTER_LANCZOS4")) 
        _l_(419151) 
        img_mask = _c_(419157, _a_(419153, _n_(419152, "cv2", lambda: cv2), "resize"), _n_(419154, "img_mask", lambda: img_mask), (427,240), interpolation = _a_(419156, _n_(419155, "cv2", lambda: cv2), "INTER_LANCZOS4")) 
        _l_(419158) 
        aux = _n_(419159, "img_train", lambda: img_train), _n_(419160, "img_mask", lambda: img_mask)
        _l_(419161)
        return aux
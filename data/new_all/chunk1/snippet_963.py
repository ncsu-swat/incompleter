# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64429461/typeerror-iteration-over-a-0-d-tensor
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
lr = 0.001
_l_(407436)

num_epochs = 10
_l_(407437)

model = _c_(407446, _n_(407438, "LSTMClassifier", lambda: LSTMClassifier), embed_size=_n_(407439, "embed_size", lambda: embed_size), 
                       hidden_size=_n_(407440, "hidden_size", lambda: hidden_size), 
                       vocab_size=_n_(407441, "vocab_size", lambda: vocab_size),
                       num_layers=_n_(407442, "num_layers", lambda: num_layers),
                       num_classes=_a_(407444, _n_(407443, "train_ds", lambda: train_ds), "num_classes"), 
                       batch_size=_n_(407445, "batch_size", lambda: batch_size))
_l_(407447)

if _n_(407448, "use_gpu", lambda: use_gpu):
    _l_(407453)

    model = _c_(407451, _a_(407450, _n_(407449, "model", lambda: model), "cuda"))
    _l_(407452)

criterion = _c_(407456, _a_(407455, _n_(407454, "nn", lambda: nn), "CrossEntropyLoss"))
_l_(407457)

if _n_(407458, "use_gpu", lambda: use_gpu):
    _l_(407477)

    criterion = _c_(407461, _a_(407460, _n_(407459, "criterion", lambda: criterion), "cuda"))
    _l_(407462)

    optimizer = _c_(407469, _a_(407464, _n_(407463, "optim", lambda: optim), "Adam"), _c_(407467, _a_(407466, _n_(407465, "model", lambda: model), "parameters")), lr=_n_(407468, "lr", lambda: lr), betas=(0.7, 0.99))
    _l_(407470)
    scheduler = _c_(407475, _a_(407473, _a_(407472, _n_(407471, "optim", lambda: optim), "lr_scheduler"), "StepLR"), _n_(407474, "optimizer", lambda: optimizer), step_size=1, gamma=0.975)
    _l_(407476)

hist = _c_(407486, _n_(407478, "train", lambda: train), _n_(407479, "model", lambda: model), _n_(407480, "train_dl", lambda: train_dl), _n_(407481, "valid_dl", lambda: valid_dl), _n_(407482, "criterion", lambda: criterion), _n_(407483, "optimizer", lambda: optimizer), _n_(407484, "scheduler", lambda: scheduler), _n_(407485, "num_epochs", lambda: num_epochs))
_l_(407487)
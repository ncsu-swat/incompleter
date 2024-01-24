# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66545871/attributeerror-dict-object-has-no-attribute-step
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(362543)

except ImportError:
    pass
try:
    import ast
    _l_(362545)

except ImportError:
    pass
try:
    import torch
    _l_(362547)

except ImportError:
    pass
try:
    import torchaudio
    _l_(362549)

except ImportError:
    pass
try:
    import torch.nn as nn
    _l_(362551)

except ImportError:
    pass
try:
    from torch.nn import functional as F
    _l_(362553)

except ImportError:
    pass
try:
    import torch.optim as optim
    _l_(362555)

except ImportError:
    pass
try:
    from torch.utils.data import DataLoader
    _l_(362557)

except ImportError:
    pass
try:
    from pytorch_lightning.core.lightning import LightningModule
    _l_(362559)

except ImportError:
    pass
try:
    from pytorch_lightning import Trainer
    _l_(362561)

except ImportError:
    pass
try:
    from argparse import ArgumentParser
    _l_(362563)

except ImportError:
    pass
try:
    from model import SpeechRecognition
    _l_(362565)

except ImportError:
    pass
try:
    from dataset import Data, collate_fn_padd
    _l_(362567)

except ImportError:
    pass
try:
    from pytorch_lightning.callbacks import ModelCheckpoint
    _l_(362569)

except ImportError:
    pass

nodes = _c_(362571, _n_(362570, "int", lambda: int), 1)
_l_(362572)
gpus = _c_(362574, _n_(362573, "int", lambda: int), 1)
_l_(362575)
data_workers = _c_(362577, _n_(362576, "int", lambda: int), 0)
_l_(362578)
train_file  = 'path/to/your/train.json'
_l_(362579)
valid_file = 'path/to/your/test.json'
_l_(362580)
valid_every = _c_(362582, _n_(362581, "int", lambda: int), 1000)
_l_(362583)
save_model_path = 'path/where/you/want/to/save/your/model'
_l_(362584)
logdir = 'path/where/you/want/to/save/your/logs'
_l_(362585)
epochs = _c_(362587, _n_(362586, "int", lambda: int), 10)
_l_(362588)
batch_size = _c_(362590, _n_(362589, "int", lambda: int), 64)
_l_(362591)
pct_start = _c_(362593, _n_(362592, "float", lambda: float), 0.3)
_l_(362594)
div_factor = _c_(362596, _n_(362595, "int", lambda: int), 100)
_l_(362597)
dparams_override = _c_(362599, _n_(362598, "str", lambda: str), "{}")
_l_(362600)
hparams_override = _c_(362602, _n_(362601, "str", lambda: str), "{}")
_l_(362603)
load_model_from = None
_l_(362604)
resume_from_checkpoint = None
_l_(362605)

class SpeechModule(_n_(362606, "LightningModule", lambda: LightningModule)):
    _l_(362789)

    def __init__(self, model, args):
        _l_(362624)

        _c_(362611, _a_(362610, _n_(362607, "super", lambda: super)(_n_(362608, "SpeechModule", lambda: SpeechModule), _n_(362609, "self", lambda: self)), "__init__"))
        _l_(362612)
        _n_(362613, "self", lambda: self).model = _n_(362614, "model", lambda: model)
        _l_(362615)
        _n_(362616, "self", lambda: self).criterion = _c_(362619, _a_(362618, _n_(362617, "nn", lambda: nn), "CTCLoss"), blank=28, zero_infinity=True)
        _l_(362620)
        _n_(362621, "self", lambda: self).args = _n_(362622, "args", lambda: args)
        _l_(362623)

    def forward(self, x, hidden):
        _l_(362631)

        aux = _c_(362629, _a_(362626, _n_(362625, "self", lambda: self), "model"), _n_(362627, "x", lambda: x), _n_(362628, "hidden", lambda: hidden))
        _l_(362630)
        return aux

    def configure_optimizers(self):
        _l_(362659)

        _n_(362632, "self", lambda: self).optimizer = _c_(362642, _a_(362634, _n_(362633, "optim", lambda: optim), "AdamW"), _c_(362638, _a_(362637, _a_(362636, _n_(362635, "self", lambda: self), "model"), "parameters")), _a_(362641, _a_(362640, _n_(362639, "self", lambda: self), "args"), "learning_rate"))
        _l_(362643)
        lr_scheduler = _c_(362649, _a_(362646, _a_(362645, _n_(362644, "optim", lambda: optim), "lr_scheduler"), "ReduceLROnPlateau"), _a_(362648, _n_(362647, "self", lambda: self), "optimizer"), mode='min',
            factor=0.50, patience=6
        )
        _l_(362650)
        _n_(362651, "self", lambda: self).scheduler = {
            'scheduler': _n_(362652, "lr_scheduler", lambda: lr_scheduler),
            'reduce_on_plateau': True,
            'monitor': 'val_checkpoint_on'
        }
        _l_(362653)
        aux = [_a_(362655, _n_(362654, "self", lambda: self), "optimizer")], [_a_(362657, _n_(362656, "self", lambda: self), "scheduler")]
        _l_(362658)

        return aux

    def step(self, batch):
        _l_(362703)

        spectrograms, labels, input_lengths, label_lengths = _n_(362660, "batch", lambda: batch) 
        _l_(362661) 
        bs = _a_(362663, _n_(362662, "spectrograms", lambda: spectrograms), "shape")[0]
        _l_(362664)
        hidden = _c_(362669, _a_(362667, _a_(362666, _n_(362665, "self", lambda: self), "model"), "_init_hidden"), _n_(362668, "bs", lambda: bs))
        _l_(362670)
        hn, c0 = _c_(362675, _a_(362672, _n_(362671, "hidden", lambda: hidden)[0], "to"), _a_(362674, _n_(362673, "self", lambda: self), "device")), _c_(362680, _a_(362677, _n_(362676, "hidden", lambda: hidden)[1], "to"), _a_(362679, _n_(362678, "self", lambda: self), "device"))
        _l_(362681)
        output, _ = _c_(362686, _n_(362682, "self", lambda: self), _n_(362683, "spectrograms", lambda: spectrograms), (_n_(362684, "hn", lambda: hn), _n_(362685, "c0", lambda: c0)))
        _l_(362687)
        output = _c_(362691, _a_(362689, _n_(362688, "F", lambda: F), "log_softmax"), _n_(362690, "output", lambda: output), dim=2)
        _l_(362692)
        loss = _c_(362699, _a_(362694, _n_(362693, "self", lambda: self), "criterion"), _n_(362695, "output", lambda: output), _n_(362696, "labels", lambda: labels), _n_(362697, "input_lengths", lambda: input_lengths), _n_(362698, "label_lengths", lambda: label_lengths))
        _l_(362700)
        aux = _n_(362701, "loss", lambda: loss)
        _l_(362702)
        return aux

    def training_step(self, batch, batch_idx):
        _l_(362717)

        loss = _c_(362707, _a_(362705, _n_(362704, "self", lambda: self), "step"), _n_(362706, "batch", lambda: batch))
        _l_(362708)
        logs = {'loss': _n_(362709, "loss", lambda: loss), 'lr': _a_(362712, _a_(362711, _n_(362710, "self", lambda: self), "optimizer"), "param_groups")[0]['lr'] }
        _l_(362713)
        aux = {'loss': _n_(362714, "loss", lambda: loss), 'log': _n_(362715, "logs", lambda: logs)}
        _l_(362716)
        return aux

    def train_dataloader(self):
        _l_(362739)

        d_params = _a_(362719, _n_(362718, "Data", lambda: Data), "parameters")
        _l_(362720)
        _c_(362724, _a_(362722, _n_(362721, "d_params", lambda: d_params), "update"), _n_(362723, "dparams_override", lambda: dparams_override))
        _l_(362725)
        train_dataset = _c_(362730, _n_(362726, "Data", lambda: Data), json_path=_a_(362728, _n_(362727, "self", lambda: self), "train_file"), **_n_(362729, "d_params", lambda: d_params))
        _l_(362731)
        aux = _c_(362737, _n_(362732, "DataLoader", lambda: DataLoader), dataset=_n_(362733, "train_dataset", lambda: train_dataset),
                            batch_size= _n_(362734, "batch_size", lambda: batch_size),
                            num_workers= _n_(362735, "data_workers", lambda: data_workers),
                            pin_memory=True,
                            collate_fn=_n_(362736, "collate_fn_padd", lambda: collate_fn_padd))
        _l_(362738)
        return aux

    def validation_step(self, batch, batch_idx):
        _l_(362747)

        loss = _c_(362743, _a_(362741, _n_(362740, "self", lambda: self), "step"), _n_(362742, "batch", lambda: batch))
        _l_(362744)
        aux = {'val_loss': _n_(362745, "loss", lambda: loss)}
        _l_(362746)
        return aux

    def validation_epoch_end(self, outputs):
        _l_(362767)

        avg_loss = _c_(362754, _a_(362753, _c_(362752, _a_(362749, _n_(362748, "torch", lambda: torch), "stack"), [_n_(362750, "x", lambda: x)['val_loss'] for x in _n_(362751, "outputs", lambda: outputs)]), "mean"))
        _l_(362755)
        _c_(362760, _a_(362758, _a_(362757, _n_(362756, "self", lambda: self), "scheduler"), "step"), _n_(362759, "avg_loss", lambda: avg_loss))
        _l_(362761)
        tensorboard_logs = {'val_loss': _n_(362762, "avg_loss", lambda: avg_loss)}
        _l_(362763)
        aux = {'val_loss': _n_(362764, "avg_loss", lambda: avg_loss), 'log': _n_(362765, "tensorboard_logs", lambda: tensorboard_logs)}
        _l_(362766)
        return aux

    def val_dataloader(self):
        _l_(362788)

        d_params = _a_(362769, _n_(362768, "Data", lambda: Data), "parameters")
        _l_(362770)
        _c_(362774, _a_(362772, _n_(362771, "d_params", lambda: d_params), "update"), _n_(362773, "dparams_override", lambda: dparams_override))
        _l_(362775)
        test_dataset = _c_(362779, _n_(362776, "Data", lambda: Data), json_path=_n_(362777, "valid_file", lambda: valid_file), **_n_(362778, "d_params", lambda: d_params), valid=True)
        _l_(362780)
        aux = _c_(362786, _n_(362781, "DataLoader", lambda: DataLoader), dataset=_n_(362782, "test_dataset", lambda: test_dataset),
                            batch_size= _n_(362783, "batch_size", lambda: batch_size),
                            num_workers= _n_(362784, "data_workers", lambda: data_workers),
                            collate_fn=_n_(362785, "collate_fn_padd", lambda: collate_fn_padd),
                            pin_memory=True)
        _l_(362787)
        return aux


def checkpoint_callback():
    _l_(362794)

    aux = _c_(362792, _n_(362790, "ModelCheckpoint", lambda: ModelCheckpoint), filepath= _n_(362791, "save_model_path", lambda: save_model_path),
        save_top_k=True,
        verbose=True,
        monitor='val_loss',
        mode='min',
        prefix=''
    )
    _l_(362793)
    return aux

def main(args):
    _l_(362837)

    h_params = _a_(362796, _n_(362795, "SpeechRecognition", lambda: SpeechRecognition), "hyper_parameters")
    _l_(362797)
    _c_(362801, _a_(362799, _n_(362798, "h_params", lambda: h_params), "update"), _n_(362800, "hparams_override", lambda: hparams_override))
    _l_(362802)
    model = _c_(362805, _n_(362803, "SpeechRecognition", lambda: SpeechRecognition), **_n_(362804, "h_params", lambda: h_params))
    _l_(362806)
    if _n_(362807, "load_model_from", lambda: load_model_from):
        _l_(362819)

        speech_module = _c_(362812, _a_(362809, _n_(362808, "SpeechModule", lambda: SpeechModule), "load_from_checkpoint"), _n_(362810, "load_model_from", lambda: load_model_from), model=_n_(362811, "model", lambda: model))
        _l_(362813)
    else:
        speech_module = _c_(362817, _n_(362814, "SpeechModule", lambda: SpeechModule), _n_(362815, "model", lambda: model), _n_(362816, "args", lambda: args))
        _l_(362818)
    trainer = _c_(362821, _n_(362820, "Trainer", lambda: Trainer))
    _l_(362822)

    trainer = _c_(362830, _n_(362823, "Trainer", lambda: Trainer), max_epochs= _n_(362824, "epochs", lambda: epochs), gpus= _n_(362825, "gpus", lambda: gpus),
        num_nodes= _n_(362826, "nodes", lambda: nodes), distributed_backend=None,
        gradient_clip_val=1.0,                     
        val_check_interval= _n_(362827, "valid_every", lambda: valid_every),
        checkpoint_callback=_n_(362828, "checkpoint_callback", lambda: checkpoint_callback),
        resume_from_checkpoint= _n_(362829, "resume_from_checkpoint", lambda: resume_from_checkpoint)
    )
    _l_(362831)
    _c_(362835, _a_(362833, _n_(362832, "trainer", lambda: trainer), "fit"), _n_(362834, "speech_module", lambda: speech_module))
    _l_(362836)

if _n_(362838, "__name__", lambda: __name__) == "__main__":
    _l_(362883)

    parser = _c_(362840, _n_(362839, "ArgumentParser", lambda: ArgumentParser))
    _l_(362841)
    _c_(362845, _a_(362843, _n_(362842, "parser", lambda: parser), "add_argument"), '--learning_rate', default=1e-3, type=_n_(362844, "float", lambda: float), help='learning rate')
    _l_(362846)

    args = _c_(362849, _a_(362848, _n_(362847, "parser", lambda: parser), "parse_args"))
    _l_(362850)
    hparams_override = _c_(362854, _a_(362852, _n_(362851, "ast", lambda: ast), "literal_eval"), _n_(362853, "hparams_override", lambda: hparams_override))
    _l_(362855)
    dparams_override = _c_(362859, _a_(362857, _n_(362856, "ast", lambda: ast), "literal_eval"), _n_(362858, "dparams_override", lambda: dparams_override))
    _l_(362860)
    if _n_(362861, "save_model_path", lambda: save_model_path):
        _l_(362878)

        if not _c_(362870, _a_(362864, _a_(362863, _n_(362862, "os", lambda: os), "path"), "isdir"), _c_(362869, _a_(362867, _a_(362866, _n_(362865, "os", lambda: os), "path"), "dirname"), _n_(362868, "save_model_path", lambda: save_model_path))):
            _l_(362877)

            raise _c_(362875, _n_(362871, "Exception", lambda: Exception), _c_(362874, _a_(362872, "the directory for path {} does not exist", "format"), _n_(362873, "save_model_path", lambda: save_model_path)))
            _l_(362876)

    _c_(362881, _n_(362879, "main", lambda: main), _n_(362880, "args", lambda: args))
    _l_(362882)
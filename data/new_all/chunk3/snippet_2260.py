# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55128842/attributeerror-module-torch-nn-functional-has-no-attribute-resize
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import models as m
    _l_(569856)

except ImportError:
    pass
try:
    import densenet as x
    _l_(569858)

except ImportError:
    pass
try:
    from torch.autograd import Variable
    _l_(569860)

except ImportError:
    pass
try:
    import torch.nn as nn
    _l_(569862)

except ImportError:
    pass
try:
    import torch.optim as optim
    _l_(569864)

except ImportError:
    pass
try:
    from torch.utils.data import DataLoader
    _l_(569866)

except ImportError:
    pass
try:
    from torchvision.datasets import ImageFolder
    _l_(569868)

except ImportError:
    pass
try:
    from torchvision.transforms import transforms
    _l_(569870)

except ImportError:
    pass
try:
    import torch
    _l_(569872)

except ImportError:
    pass
try:
    from sklearn.metrics import confusion_matrix
    _l_(569874)

except ImportError:
    pass
try:
    import numpy as np
    _l_(569876)

except ImportError:
    pass

tr1=  _c_(569882, _a_(569878, _n_(569877, "transforms", lambda: transforms), "Compose"), [_c_(569881, _a_(569880, _n_(569879, "transforms", lambda: transforms), "Resize"), (224,224))])
_l_(569883)

train_dataset = _c_(569886, _n_(569884, "ImageFolder", lambda: ImageFolder), '../../cat_dog_dataset /training_set',transform=_n_(569885, "tr1", lambda: tr1))
_l_(569887)
train_loader = _c_(569890, _n_(569888, "DataLoader", lambda: DataLoader), _n_(569889, "train_dataset", lambda: train_dataset), 
                      batch_size = 1, 
                      shuffle = True, 
                      num_workers = 1)
_l_(569891)

test_dataset = _c_(569894, _n_(569892, "ImageFolder", lambda: ImageFolder), '../../cat_dog_dataset/test_set',transform=_n_(569893, "tr1", lambda: tr1))
_l_(569895)
test_loader = _c_(569898, _n_(569896, "DataLoader", lambda: DataLoader), _n_(569897, "test_dataset", lambda: test_dataset), 
                      batch_size = 1, 
                      shuffle = False, 
                      num_workers = 1)
_l_(569899)

# GLOBAL VARIABLES
noe = 25
_l_(569900)
noc = 2
_l_(569901)

# MODEL INSTANCE 1
net = _c_(569904, _a_(569903, _n_(569902, "m", lambda: m), "resnet50"))
_l_(569905)
_n_(569906, "net", lambda: net).fc = _c_(569910, _a_(569908, _n_(569907, "nn", lambda: nn), "Linear"), 2048,_n_(569909, "noc", lambda: noc))
_l_(569911)
#net=net.cuda()

criterion = _c_(569914, _a_(569913, _n_(569912, "nn", lambda: nn), "CrossEntropyLoss"))
_l_(569915)
optimizer = _c_(569921, _a_(569917, _n_(569916, "optim", lambda: optim), "Adam"), _c_(569920, _a_(569919, _n_(569918, "net", lambda: net), "parameters")))
_l_(569922)

def train(epoch):
    _l_(569969)

    _c_(569925, _a_(569924, _n_(569923, "net", lambda: net), "train"))
    _l_(569926)

    train_loss_epoch=0.0
    _l_(569927)
    #    running_loss=0
    for batch in _n_(569928, "train_loader", lambda: train_loader):
        _l_(569963)


        inputs, labels = _n_(569929, "batch", lambda: batch)
        _l_(569930)
        inputs, labels = _c_(569933, _n_(569931, "Variable", lambda: Variable), _n_(569932, "inputs", lambda: inputs)), _c_(569936, _n_(569934, "Variable", lambda: Variable), _n_(569935, "labels", lambda: labels))
        _l_(569937)
        _c_(569940, _a_(569939, _n_(569938, "optimizer", lambda: optimizer), "zero_grad"))
        _l_(569941)
        #        print(inputs)
        # FORWARD PASS

        out = _c_(569944, _n_(569942, "net", lambda: net), _n_(569943, "inputs", lambda: inputs))
        _l_(569945)
        # CALCULATE LOSS
        loss = _c_(569949, _n_(569946, "criterion", lambda: criterion), _n_(569947, "out", lambda: out), _n_(569948, "labels", lambda: labels))
        _l_(569950)
        # BACK PROPAGATION
        _c_(569953, _a_(569952, _n_(569951, "loss", lambda: loss), "backward"))
        _l_(569954)
        # WEIGHT UPDATION
        _c_(569957, _a_(569956, _n_(569955, "optimizer", lambda: optimizer), "step"))
        _l_(569958)
#        print(loss.data[0])

        train_loss_epoch+=_c_(569961, _a_(569960, _n_(569959, "loss", lambda: loss), "item"))
        _l_(569962)
#    total_loss_epoch+=t
    _c_(569967, _n_(569964, "print", lambda: print), _n_(569965, "epoch", lambda: epoch),_n_(569966, "train_loss_epoch", lambda: train_loss_epoch))
    _l_(569968)

def test():
    _l_(570057)

    final_updated_cm=_c_(569973, _a_(569971, _n_(569970, "np", lambda: np), "zeros"), (2,2),dtype=_n_(569972, "int", lambda: int))
    _l_(569974)
#    confusion_matrix = meter.ConfusionMeter(3)
    _c_(569977, _a_(569976, _n_(569975, "net", lambda: net), "eval"))
    _l_(569978)
    test_loss=0.0
    _l_(569979)
    correct=0.0
    _l_(569980)
    for inputs,labels in _n_(569981, "test_loader", lambda: test_loader):
        _l_(570031)

 #           updated_cm=torch.zeros(23,23)
        inputs, labels = _c_(569984, _n_(569982, "Variable", lambda: Variable), _n_(569983, "inputs", lambda: inputs)), _c_(569987, _n_(569985, "Variable", lambda: Variable), _n_(569986, "labels", lambda: labels))
        _l_(569988)
        out = _c_(569991, _n_(569989, "net", lambda: net), _n_(569990, "inputs", lambda: inputs))
        _l_(569992)
        #print(out)
        loss=_c_(569996, _n_(569993, "criterion", lambda: criterion), _n_(569994, "out", lambda: out),_n_(569995, "labels", lambda: labels))
        _l_(569997)
        test_loss+=_c_(570000, _a_(569999, _n_(569998, "loss", lambda: loss), "item"))
        _l_(570001)

#        pred=out.data.max(1, keepdim=True)[1]
        pred=_c_(570006, _a_(570003, _n_(570002, "torch", lambda: torch), "max"), _a_(570005, _n_(570004, "out", lambda: out), "data"))
        _l_(570007)
        #print(pred)
#        pred=torch.max(out.data,1)[1]
        correct+=_c_(570019, _a_(570018, _c_(570017, _a_(570016, _c_(570015, _a_(570009, _n_(570008, "pred", lambda: pred), "eq"), _c_(570014, _a_(570012, _a_(570011, _n_(570010, "labels", lambda: labels), "data"), "view_as"), _n_(570013, "pred", lambda: pred))), "cpu")), "sum"))
        _l_(570020)
#        confusion_matrix.add(out.data.squeeze(), labels)
        cm=_c_(570026, _n_(570021, "confusion_matrix", lambda: confusion_matrix), _a_(570023, _n_(570022, "labels", lambda: labels), "data"),_a_(570025, _n_(570024, "pred", lambda: pred), "data"),labels=[0,1])
        _l_(570027)
        final_updated_cm=_n_(570028, "final_updated_cm", lambda: final_updated_cm)+_n_(570029, "cm", lambda: cm)
        _l_(570030)
    test_loss /=_c_(570035, _n_(570032, "len", lambda: len), _a_(570034, _n_(570033, "test_loader", lambda: test_loader), "dataset"))
    _l_(570036)
    _c_(570051, _n_(570037, "print", lambda: print), _c_(570050, _a_(570038, '\nTest Set: Average loss: {:.4f},Accuracy: {}/{}  ({:.0f}%)\n', "format"), _n_(570039, "test_loss", lambda: test_loss),_n_(570040, "correct", lambda: correct),_c_(570044, _n_(570041, "len", lambda: len), _a_(570043, _n_(570042, "test_loader", lambda: test_loader), "dataset")),
       100.0 * _n_(570045, "correct", lambda: correct) / _c_(570049, _n_(570046, "len", lambda: len), _a_(570048, _n_(570047, "test_loader", lambda: test_loader), "dataset"))))
    _l_(570052)

#    t=(100.0*correct/len(test_loader.dataset)).item()
#    f=open('2.txt','w')
#    f.write(str(t))
#    f.close()    
#    print(t)

    _c_(570055, _n_(570053, "print", lambda: print), _n_(570054, "final_updated_cm", lambda: final_updated_cm))
    _l_(570056)

for epoch in _c_(570060, _n_(570058, "range", lambda: range), _n_(570059, "noe", lambda: noe)):
    _l_(570065)

    _c_(570063, _n_(570061, "train", lambda: train), _n_(570062, "epoch", lambda: epoch))
    _l_(570064)
_c_(570067, _n_(570066, "test", lambda: test))
_l_(570068)
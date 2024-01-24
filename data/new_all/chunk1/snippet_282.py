# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60296710/attributeerror-dataset-object-has-no-attribute-c-fastai
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _n_(378924, "__name__", lambda: __name__) == '__main__':
    _l_(378954)

    dataset_train = _c_(378928, _n_(378925, "NumbersDataset", lambda: NumbersDataset), _n_(378926, "X_train", lambda: X_train), _n_(378927, "y_train", lambda: y_train))
    _l_(378929)
    dataloader_train = _c_(378932, _n_(378930, "DataLoader", lambda: DataLoader), _n_(378931, "dataset_train", lambda: dataset_train), batch_size=4, shuffle=True, num_workers=2)
    _l_(378933)

    dataset_valid = _c_(378937, _n_(378934, "NumbersDataset", lambda: NumbersDataset), _n_(378935, "X_valid", lambda: X_valid), _n_(378936, "y_valid", lambda: y_valid))
    _l_(378938)
    dataloader_valid = _c_(378941, _n_(378939, "DataLoader", lambda: DataLoader), _n_(378940, "dataset_valid", lambda: dataset_valid), batch_size=4, shuffle=True, num_workers=2)
    _l_(378942)

    datas = _c_(378946, _n_(378943, "DataBunch", lambda: DataBunch), train_dl = _n_(378944, "dataloader_train", lambda: dataloader_train), valid_dl = _n_(378945, "dataloader_valid", lambda: dataloader_valid))
    _l_(378947)
    leaner = _c_(378952, _n_(378948, "unet_learner", lambda: unet_learner), data = _n_(378949, "datas", lambda: datas), arch = _a_(378951, _n_(378950, "models", lambda: models), "resnet34"))
    _l_(378953)
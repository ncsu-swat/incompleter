# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63309484/typeerror-img-should-be-pil-image-got-class-numpy-ndarray
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(525843)

except ImportError:
    pass
try:
    import numpy as np
    _l_(525845)

except ImportError:
    pass
try:
    import torch
    _l_(525847)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(525849)

except ImportError:
    pass
try:
    from torch.utils.data import Dataset
    _l_(525851)

except ImportError:
    pass
try:
    from torchvision import transforms, utils
    _l_(525853)

except ImportError:
    pass
try:
    from torchvision.transforms import functional
    _l_(525855)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(525857)

except ImportError:
    pass
try:
    import pdb
    _l_(525859)

except ImportError:
    pass
try:
    import cv2
    _l_(525861)

except ImportError:
    pass
try:
    from cv2 import imread
    _l_(525863)

except ImportError:
    pass
try:
    from cv2 import resize
    _l_(525865)

except ImportError:
    pass

class CellsDataset(_n_(525866, "Dataset", lambda: Dataset)):
    _l_(526030)

    # a very simple dataset

    def __init__(self, root_dir, transform=None, return_filenames=False):
        _l_(525905)

        _n_(525867, "self", lambda: self).root = _n_(525868, "root_dir", lambda: root_dir)
        _l_(525869)
        _n_(525870, "self", lambda: self).transform = _n_(525871, "transform", lambda: transform)
        _l_(525872)
        _n_(525873, "self", lambda: self).return_filenames = _n_(525874, "return_filenames", lambda: return_filenames)
        _l_(525875)
        _n_(525876, "self", lambda: self).files = [_c_(525883, _a_(525879, _a_(525878, _n_(525877, "os", lambda: os), "path"), "join"), _a_(525881, _n_(525880, "self", lambda: self), "root"),_n_(525882, "filename", lambda: filename)) for filename in _c_(525888, _a_(525885, _n_(525884, "os", lambda: os), "listdir"), _a_(525887, _n_(525886, "self", lambda: self), "root"))]
        _l_(525889)
        _n_(525890, "self", lambda: self).files = [_n_(525891, "path", lambda: path) for path in _a_(525893, _n_(525892, "self", lambda: self), "files")
                      if _c_(525898, _a_(525896, _a_(525895, _n_(525894, "os", lambda: os), "path"), "isfile"), _n_(525897, "path", lambda: path)) and _c_(525903, _a_(525901, _a_(525900, _n_(525899, "os", lambda: os), "path"), "splitext"), _n_(525902, "path", lambda: path))[1]=='.png']
        _l_(525904)

    def __len__(self):
        _l_(525911)

        aux = _c_(525909, _n_(525906, "len", lambda: len), _a_(525908, _n_(525907, "self", lambda: self), "files"))
        _l_(525910)
        return aux

    def __getitem__(self, idx):
        _l_(525949)

        path = _a_(525913, _n_(525912, "self", lambda: self), "files")[_n_(525914, "idx", lambda: idx)]
        _l_(525915)
        #sample = Image.open(path)
        #sample = cv2.imread(path) 
        #sample = cv2.resize(sample, (512, 512))
        img = _c_(525918, _n_(525916, "imread", lambda: imread), filename=_n_(525917, "path", lambda: path))
        _l_(525919)
        sample = _c_(525922, _n_(525920, "resize", lambda: resize), src=_n_(525921, "img", lambda: img), dsize=(1024, 1024))
        _l_(525923)
        sample = _c_(525927, _a_(525925, _n_(525924, "functional", lambda: functional), "to_grayscale"), _n_(525926, "sample", lambda: sample), num_output_channels=3)
        _l_(525928)
        #image = cv2.imread(path)
         
        #sample = image.copy()
        # set blue and green channels to 0
        _n_(525929, "sample", lambda: sample)[:, :, 0] = 0
        _l_(525930)
        _n_(525931, "sample", lambda: sample)[:, :, 1] = 0
        _l_(525932)

        #transform3 = Grayscale(num_output_channels=3)
        #sample = transform3(sample) # convert to a 3 channel grayscale, as it needs to be 3 channel.
        if _a_(525934, _n_(525933, "self", lambda: self), "transform"):
            _l_(525940)

            sample = _c_(525938, _a_(525936, _n_(525935, "self", lambda: self), "transform"), _n_(525937, "sample", lambda: sample))
            _l_(525939)

        if _a_(525942, _n_(525941, "self", lambda: self), "return_filenames"):
            _l_(525948)

            aux = _n_(525943, "sample", lambda: sample), _n_(525944, "path", lambda: path)
            _l_(525945)
            return aux
        else:
            aux = _n_(525946, "sample", lambda: sample)
            _l_(525947)
            return aux

    def duplicate_and_transform(self,transforms):
        _l_(526029)

        currfilelen = _c_(525952, _a_(525951, _n_(525950, "self", lambda: self), "__len__"))
        _l_(525953)
        
        for pind in _c_(525956, _n_(525954, "range", lambda: range), 0,_n_(525955, "currfilelen", lambda: currfilelen)-1):
            _l_(526028)

            path = _a_(525958, _n_(525957, "self", lambda: self), "files")[_n_(525959, "pind", lambda: pind)]
            _l_(525960)
            sample = _c_(525964, _a_(525962, _n_(525961, "Image", lambda: Image), "open"), _n_(525963, "path", lambda: path))
            _l_(525965)
            samplet = _c_(525968, _n_(525966, "transforms", lambda: transforms), _n_(525967, "sample", lambda: sample))
            _l_(525969)
            # save the transformed images and save the associated counts:
            newpath = _n_(525970, "path", lambda: path)[:-4]+'trans.png' #path[:-4] is the path without the .png extension.
            _l_(525971) #path[:-4] is the path without the .png extension.
            _c_(525975, _a_(525973, _n_(525972, "samplet", lambda: samplet), "save"), _n_(525974, "newpath", lambda: newpath),"PNG")
            _l_(525976)
            metadata = _c_(525985, _a_(525978, _n_(525977, "pd", lambda: pd), "read_csv"), _c_(525984, _a_(525981, _a_(525980, _n_(525979, "os", lambda: os), "path"), "join"), _a_(525983, _n_(525982, "self", lambda: self), "root"),'gt.csv'))
            _l_(525986)
            _c_(525989, _a_(525988, _n_(525987, "metadata", lambda: metadata), "set_index"), 'filename',inplace=True)
            _l_(525990)
            count = _n_(525991, "metadata", lambda: metadata)['count'][_c_(525996, _a_(525994, _a_(525993, _n_(525992, "os", lambda: os), "path"), "split"), _n_(525995, "path", lambda: path))[-1]]
            _l_(525997)
            _c_(526001, _a_(525999, _n_(525998, "samplet", lambda: samplet), "save"), _n_(526000, "newpath", lambda: newpath),"PNG")
            _l_(526002)
            f = _c_(526006, _n_(526003, "open", lambda: open), _a_(526005, _n_(526004, "self", lambda: self), "root")+'gt_red.csv','a')
            _l_(526007)
            basepath = _c_(526012, _a_(526010, _a_(526009, _n_(526008, "os", lambda: os), "path"), "basename"), _n_(526011, "path", lambda: path)) # strip away the directory list and just get the filename
            _l_(526013) # strip away the directory list and just get the filename
            _c_(526020, _a_(526015, _n_(526014, "f", lambda: f), "write"), _n_(526016, "basepath", lambda: basepath)[:-4]+'trans.png,'+_c_(526019, _n_(526017, "str", lambda: str), _n_(526018, "count", lambda: count))+'\n')
            _l_(526021)
            # return the new file names and add to self.files.
            _c_(526026, _a_(526024, _a_(526023, _n_(526022, "self", lambda: self), "files"), "append"), _n_(526025, "newpath", lambda: newpath))
            _l_(526027)
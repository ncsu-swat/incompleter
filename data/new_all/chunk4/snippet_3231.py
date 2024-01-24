# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77073167/typeerror-expected-str-bytes-or-os-pathlike-object-not-dataframe-videoclass
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from torch.utils.data import DataLoader, Dataset,ConcatDataset,default_collate
    _l_(619472)

except ImportError:
    pass
try:
    from torch.utils.data import DistributedSampler
    _l_(619474)

except ImportError:
    pass
try:
    from pytorchvideo.data import labeled_video_dataset
    _l_(619476)

except ImportError:
    pass

# Create a training dataset
train_dataset = _c_(619484, _n_(619477, "labeled_video_dataset", lambda: labeled_video_dataset), _n_(619478, "df", lambda: df),  # Provide the DataFrame directly
    clip_sampler=_c_(619482, _n_(619479, "make_clip_sampler", lambda: make_clip_sampler), _n_(619480, "clipmode", lambda: clipmode), _n_(619481, "video_duration", lambda: video_duration)),
    transform=_n_(619483, "video_transform", lambda: video_transform),
    decode_audio=False
)
_l_(619485)

# Create a DataLoader for the training dataset
train_loader = _c_(619489, _n_(619486, "DataLoader", lambda: DataLoader), _n_(619487, "train_dataset", lambda: train_dataset),
    batch_size=_n_(619488, "batch_size", lambda: batch_size),
    num_workers=0,
    pin_memory=True
)
_l_(619490)
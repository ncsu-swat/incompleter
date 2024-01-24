# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77073167/typeerror-expected-str-bytes-or-os-pathlike-object-not-dataframe-videoclass
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from torch.utils.data import DataLoader
    _l_(580029)

except ImportError:
    pass
try:
    from pytorchvideo.data import labeled_video_dataset
    _l_(580031)

except ImportError:
    pass

# Create a training dataset
train_dataset = _c_(580039, _n_(580032, "labeled_video_dataset", lambda: labeled_video_dataset), _n_(580033, "df", lambda: df),  # Provide the DataFrame directly
    clip_sampler=_c_(580037, _n_(580034, "make_clip_sampler", lambda: make_clip_sampler), _n_(580035, "clipmode", lambda: clipmode), _n_(580036, "video_duration", lambda: video_duration)),
    transform=_n_(580038, "video_transform", lambda: video_transform),
    decode_audio=False
)
_l_(580040)

# Create a DataLoader for the training dataset
train_loader = _c_(580044, _n_(580041, "DataLoader", lambda: DataLoader), _n_(580042, "train_dataset", lambda: train_dataset),
    batch_size=_n_(580043, "batch_size", lambda: batch_size),
    num_workers=0,
    pin_memory=True
)
_l_(580045)
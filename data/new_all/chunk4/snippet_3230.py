# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77073167/typeerror-expected-str-bytes-or-os-pathlike-object-not-dataframe-videoclass
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(621614)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(621616)

except ImportError:
    pass

base_path = '/content/drive/MyDrive/Shoplifting Dataset (2022) - CV Laboratory MNNIT Allahabad/Shoplifting Dataset (2022) - CV Laboratory MNNIT Allahabad/Dataset/Dataset/'
_l_(621617)

normal_path = _c_(621622, _a_(621620, _a_(621619, _n_(621618, "os", lambda: os), "path"), "join"), _n_(621621, "base_path", lambda: base_path), 'Normal')
_l_(621623)
shoplifting_path = _c_(621628, _a_(621626, _a_(621625, _n_(621624, "os", lambda: os), "path"), "join"), _n_(621627, "base_path", lambda: base_path), 'Shoplifting')
_l_(621629)

if _c_(621634, _a_(621632, _a_(621631, _n_(621630, "os", lambda: os), "path"), "exists"), _n_(621633, "normal_path", lambda: normal_path)) and _c_(621639, _a_(621637, _a_(621636, _n_(621635, "os", lambda: os), "path"), "exists"), _n_(621638, "shoplifting_path", lambda: shoplifting_path)):
    _l_(621701)

    normal_files = [_c_(621645, _a_(621642, _a_(621641, _n_(621640, "os", lambda: os), "path"), "join"), _n_(621643, "normal_path", lambda: normal_path), _n_(621644, "filename", lambda: filename)) for filename in _c_(621649, _a_(621647, _n_(621646, "os", lambda: os), "listdir"), _n_(621648, "normal_path", lambda: normal_path)) if _c_(621652, _a_(621651, _n_(621650, "filename", lambda: filename), "endswith"), '.mp4')]
    _l_(621653)
    shoplifting_files = [_c_(621659, _a_(621656, _a_(621655, _n_(621654, "os", lambda: os), "path"), "join"), _n_(621657, "shoplifting_path", lambda: shoplifting_path), _n_(621658, "filename", lambda: filename)) for filename in _c_(621663, _a_(621661, _n_(621660, "os", lambda: os), "listdir"), _n_(621662, "shoplifting_path", lambda: shoplifting_path)) if _c_(621666, _a_(621665, _n_(621664, "filename", lambda: filename), "endswith"), '.mp4')]
    _l_(621667)

    # Create label lists
    normal_labels = [0] * _c_(621670, _n_(621668, "len", lambda: len), _n_(621669, "normal_files", lambda: normal_files))
    _l_(621671)
    shoplifting_labels = [1] * _c_(621674, _n_(621672, "len", lambda: len), _n_(621673, "shoplifting_files", lambda: shoplifting_files))
    _l_(621675)

    # Combine the lists of paths and labels
    all_files = _n_(621676, "normal_files", lambda: normal_files) + _n_(621677, "shoplifting_files", lambda: shoplifting_files)
    _l_(621678)
    all_labels = _n_(621679, "normal_labels", lambda: normal_labels) + _n_(621680, "shoplifting_labels", lambda: shoplifting_labels)
    _l_(621681)

    # Create a DataFrame
    data = {'Video_Path': _n_(621682, "all_files", lambda: all_files), 'Label': _n_(621683, "all_labels", lambda: all_labels)}
    _l_(621684)
    df = _c_(621688, _a_(621686, _n_(621685, "pd", lambda: pd), "DataFrame"), _n_(621687, "data", lambda: data))
    _l_(621689)

    # Print the first 5 rows
    _c_(621694, _n_(621690, "print", lambda: print), _c_(621693, _a_(621692, _n_(621691, "df", lambda: df), "head")))
    _l_(621695)
else:
    _c_(621699, _n_(621696, "print", lambda: print), f"One or both of the directories '{_n_(621697, 'normal_path', lambda: normal_path)}' and '{_n_(621698, 'shoplifting_path', lambda: shoplifting_path)}' do not exist.")
    _l_(621700)
try:
    from sklearn.model_selection import train_test_split
    _l_(621703)

except ImportError:
    pass
train_df, val_df = _c_(621706, _n_(621704, "train_test_split", lambda: train_test_split), _n_(621705, "df", lambda: df), test_size=0.25)
_l_(621707)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52920680/dataframe-append-generates-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import h5py
    _l_(427512)

except ImportError:
    pass
try:
    import numpy as np
    _l_(427514)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(427516)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(427518)

except ImportError:
    pass
try:
    from os import listdir
    _l_(427520)

except ImportError:
    pass
try:
    from pandas import HDFStore
    _l_(427522)

except ImportError:
    pass


def maintainLedger(mode, tick, lastBuyy = 0, lastSell = 0, quan = 0, prof = 0):
    _l_(427716)

    """THIS FUNCTION WRITES AND READS TRANSACTION DETAILS.
       mode = 0 - IF FILE EXITS, READ FILE
       mode = 1 - IF FILE EXITS, APPEND TO FILE"""

    # CHECK IF LEDGER FILE EXISTS, IF NOT CREATE A LEDGER FILE FOR THE FIRST TIME
    path = r'ledger'
    _l_(427523)
    suff = r'h5'
    _l_(427524)
    flie = _c_(427527, _n_(427525, "listdir", lambda: listdir), _n_(427526, "path", lambda: path))
    _l_(427528)
    flie = [_n_(427529, "item", lambda: item) for item in _n_(427530, "flie", lambda: flie) if _c_(427534, _a_(427532, _n_(427531, "item", lambda: item), "endswith"), _n_(427533, "suff", lambda: suff))]
    _l_(427535)

    if _c_(427538, _n_(427536, "len", lambda: len), _n_(427537, "flie", lambda: flie)) == 0:
        _l_(427715)

        HDF5Data = _c_(427540, _n_(427539, "HDFStore", lambda: HDFStore), 'ledger/ledger.h5')
        _l_(427541)

        # GENERATE NEW VALUES OF DATE/TIME
        mi = _c_(427547, _n_(427542, "int", lambda: int), _a_(427546, _c_(427545, _a_(427544, _n_(427543, "datetime", lambda: datetime), "now")), "minute"))
        _l_(427548)
        ho = _c_(427554, _n_(427549, "int", lambda: int), _a_(427553, _c_(427552, _a_(427551, _n_(427550, "datetime", lambda: datetime), "now")), "hour"))
        _l_(427555)
        da = _c_(427561, _n_(427556, "int", lambda: int), _a_(427560, _c_(427559, _a_(427558, _n_(427557, "datetime", lambda: datetime), "now")), "day"))
        _l_(427562)
        we = _c_(427569, _n_(427563, "int", lambda: int), _c_(427568, _a_(427567, _c_(427566, _a_(427565, _n_(427564, "datetime", lambda: datetime), "now")), "isocalendar"))[1])
        _l_(427570)
        mo = _c_(427576, _n_(427571, "int", lambda: int), _a_(427575, _c_(427574, _a_(427573, _n_(427572, "datetime", lambda: datetime), "now")), "month"))
        _l_(427577)
        ye = _c_(427583, _n_(427578, "int", lambda: int), _a_(427582, _c_(427581, _a_(427580, _n_(427579, "datetime", lambda: datetime), "now")), "year"))
        _l_(427584)

        newwData = _c_(427601, _a_(427600, _c_(427599, _a_(427586, _n_(427585, "np", lambda: np), "array"), [_n_(427587, "mode", lambda: mode), _n_(427588, "mi", lambda: mi), _n_(427589, "ho", lambda: ho), _n_(427590, "da", lambda: da), _n_(427591, "we", lambda: we), _n_(427592, "mo", lambda: mo), _n_(427593, "ye", lambda: ye), _n_(427594, "tick", lambda: tick), _n_(427595, "lastBuyy", lambda: lastBuyy), _n_(427596, "lastSell", lambda: lastSell), _n_(427597, "quan", lambda: quan), _n_(427598, "prof", lambda: prof)]), "reshape"), 1, 12)
        _l_(427602)
        newwData = _c_(427606, _a_(427604, _n_(427603, "pd", lambda: pd), "DataFrame"), _n_(427605, "newwData", lambda: newwData), columns = ['mode', 'mi', 'ho', 'da', 'we', 'mo', 'ye', 'tick', 'laBu', 'laSe', 'quan', 'prof'])
        _l_(427607)
        _c_(427611, _a_(427609, _n_(427608, "HDF5Data", lambda: HDF5Data), "put"), 'data', _n_(427610, "newwData", lambda: newwData), format = 'table', data_columns = True)
        _l_(427612)
        _c_(427615, _a_(427614, _n_(427613, "HDF5Data", lambda: HDF5Data), "close"))
        _l_(427616)

    elif _c_(427619, _n_(427617, "len", lambda: len), _n_(427618, "flie", lambda: flie)) == 1:
        _l_(427714)

        if _n_(427620, "mode", lambda: mode) == 0:
            _l_(427713)

            # READ PREVIOUSLY SAVED DATA AS PANDAS DATAFRAME
            readData = _c_(427623, _a_(427622, _n_(427621, "pd", lambda: pd), "read_hdf"), 'ledger/ledger.h5', mode = 'r')
            _l_(427624)

        elif _n_(427625, "mode", lambda: mode) == 1:
            _l_(427712)

            # GENERATE NEW VALUES OF DATE/TIME
            mi = _c_(427631, _n_(427626, "int", lambda: int), _a_(427630, _c_(427629, _a_(427628, _n_(427627, "datetime", lambda: datetime), "now")), "minute"))
            _l_(427632)
            ho = _c_(427638, _n_(427633, "int", lambda: int), _a_(427637, _c_(427636, _a_(427635, _n_(427634, "datetime", lambda: datetime), "now")), "hour"))
            _l_(427639)
            da = _c_(427645, _n_(427640, "int", lambda: int), _a_(427644, _c_(427643, _a_(427642, _n_(427641, "datetime", lambda: datetime), "now")), "day"))
            _l_(427646)
            we = _c_(427653, _n_(427647, "int", lambda: int), _c_(427652, _a_(427651, _c_(427650, _a_(427649, _n_(427648, "datetime", lambda: datetime), "now")), "isocalendar"))[1])
            _l_(427654)
            mo = _c_(427660, _n_(427655, "int", lambda: int), _a_(427659, _c_(427658, _a_(427657, _n_(427656, "datetime", lambda: datetime), "now")), "month"))
            _l_(427661)
            ye = _c_(427667, _n_(427662, "int", lambda: int), _a_(427666, _c_(427665, _a_(427664, _n_(427663, "datetime", lambda: datetime), "now")), "year"))
            _l_(427668)

            # GATHER NEW DATA INTO NUMPY ARRAY AND CONVERT TO PANDAS DATAFRAME
            newwData = _c_(427685, _a_(427684, _c_(427683, _a_(427670, _n_(427669, "np", lambda: np), "array"), [_n_(427671, "mode", lambda: mode), _n_(427672, "mi", lambda: mi), _n_(427673, "ho", lambda: ho), _n_(427674, "da", lambda: da), _n_(427675, "we", lambda: we), _n_(427676, "mo", lambda: mo), _n_(427677, "ye", lambda: ye), _n_(427678, "tick", lambda: tick), _n_(427679, "lastBuyy", lambda: lastBuyy), _n_(427680, "lastSell", lambda: lastSell), _n_(427681, "quan", lambda: quan), _n_(427682, "prof", lambda: prof)]), "reshape"), 1, 12)
            _l_(427686)
            newwData = _c_(427690, _a_(427688, _n_(427687, "pd", lambda: pd), "DataFrame"), _n_(427689, "newwData", lambda: newwData), columns = ['mode', 'mi', 'ho', 'da', 'we', 'mo', 'ye', 'tick', 'laBu', 'laSe', 'quan', 'prof'])
            _l_(427691)

            # READ PREVIOUSLY SAVED DATA AS PANDAS DATAFRAME AND APPEND NEW DATA
            readData = _c_(427694, _a_(427693, _n_(427692, "pd", lambda: pd), "read_hdf"), 'ledger/ledger.h5', mode = 'a')
            _l_(427695)
            _c_(427699, _a_(427697, _n_(427696, "readData", lambda: readData), "append"), 'data', _n_(427698, "newwData", lambda: newwData))
            _l_(427700)

            tempData = _c_(427703, _a_(427702, _n_(427701, "pd", lambda: pd), "read_hdf"), 'ledger/ledger.h5', mode = 'r')
            _l_(427704)
            _c_(427707, _n_(427705, "print", lambda: print), _n_(427706, "tempData", lambda: tempData))
            _l_(427708)

        else:
            _c_(427710, _n_(427709, "print", lambda: print), 'Please check input data for errors!')
            _l_(427711)



if _n_(427717, "__name__", lambda: __name__) == '__main__':
    _l_(427721)

    _c_(427719, _n_(427718, "maintainLedger", lambda: maintainLedger), 1, "AAPL")
    _l_(427720)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69696035/typeerror-object-of-type-mappingproxy-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import streamlit as st
    _l_(585329)

except ImportError:
    pass
try:
    import Controllers.ECGModel as ecgModel
    _l_(585331)

except ImportError:
    pass

def GetSourceProperty(filePath):
    _l_(585349)

    ecg = _a_(585333, _n_(585332, "ecgModel", lambda: ecgModel), "ECG")
    _l_(585334)
    _n_(585335, "ecg", lambda: ecg).Source = "MIT"
    _l_(585336)
    _n_(585337, "ecg", lambda: ecg).FileName = "100"
    _l_(585338)
    _n_(585339, "ecg", lambda: ecg).Channel = 2
    _l_(585340)
    _n_(585341, "ecg", lambda: ecg).Record = 11520000
    _l_(585342)
    _n_(585343, "ecg", lambda: ecg).Time = 1800
    _l_(585344)
    _n_(585345, "ecg", lambda: ecg).SampleRate = 500
    _l_(585346)
    aux = _n_(585347, "ecg", lambda: ecg)
    _l_(585348)
    return aux
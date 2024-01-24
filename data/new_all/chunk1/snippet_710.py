# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51895839/getting-typeerror-unsupported-operand-types-for-str-and-bool-message
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(403566)

except ImportError:
    pass
try:
    import json
    _l_(403568)

except ImportError:
    pass
try:
    import csv
    _l_(403570)

except ImportError:
    pass

path="C:/Users/bwerner/Documents/output/"
_l_(403571)


def vt_result_check(path):
    _l_(403619)

    vt_result = False
    _l_(403572)
    for filename in _c_(403576, _a_(403574, _n_(403573, "os", lambda: os), "listdir"), _n_(403575, "path", lambda: path)):
        _l_(403616)

        with _c_(403580, _n_(403577, "open", lambda: open), _n_(403578, "path", lambda: path) + _n_(403579, "filename", lambda: filename), 'r') as vt_result_file:
            _l_(403586)

            vt_data = _c_(403584, _a_(403582, _n_(403581, "json", lambda: json), "load"), _n_(403583, "vt_result_file", lambda: vt_result_file))
            _l_(403585)

        l = ()
        _l_(403587)

        # Look for any positive detected referrer samples
        # Look for any positive detected communicating samples
        # Look for any positive detected downloaded samples
        # Look for any positive detected URLs
        sample_types = ('detected_referrer_samples', 'detected_communicating_samples',
                        'detected_downloaded_samples', 'detected_urls')
        _l_(403588)
        vt_result |= _c_(403596, _n_(403589, "any", lambda: any), (_n_(403590, "sample", lambda: sample)['positives'] > 0 for sample_type in _n_(403591, "sample_types", lambda: sample_types)
                                                 for sample in _c_(403595, _a_(403593, _n_(403592, "vt_data", lambda: vt_data), "get"), _n_(403594, "sample_type", lambda: sample_type), [])))
        _l_(403597)

        # Look for a Dr. Web category of known infection source
        vt_result |= _c_(403600, _a_(403599, _n_(403598, "vt_data", lambda: vt_data), "get"), 'Dr.Web category') == "known infection source"
        _l_(403601)

        # Look for a Forecepoint ThreatSeeker category of elevated exposure
        # Look for a Forecepoint ThreatSeeker category of phishing and other frauds
        # Look for a Forecepoint ThreatSeeker category of suspicious content
        threats = ("elevated exposure", "phishing and other frauds", "suspicious content")
        _l_(403602)
        vt_result |= _c_(403605, _a_(403604, _n_(403603, "vt_data", lambda: vt_data), "get"), 'Forcepoint ThreatSeeker category') in _n_(403606, "threats", lambda: threats)
        _l_(403607)

        vt_result = _c_(403610, _n_(403608, "str", lambda: str), _n_(403609, "vt_result", lambda: vt_result))
        _l_(403611)
        _c_(403614, _n_(403612, "print", lambda: print), _n_(403613, "vt_result", lambda: vt_result))
        _l_(403615)
    aux = _n_(403617, "vt_result", lambda: vt_result)
    _l_(403618)

#        l.append(vt_result)

    return aux

if _n_(403620, "__name__", lambda: __name__) == '__main__':
    _l_(403625)

    _c_(403623, _n_(403621, "vt_result_check", lambda: vt_result_check), _n_(403622, "path", lambda: path))
    _l_(403624)
#    for i in range(vt_result_check(path)):
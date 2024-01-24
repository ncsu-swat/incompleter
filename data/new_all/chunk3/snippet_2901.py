# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59004021/typeerror-float-object-is-not-callable-issue
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from ROOT import TFile, TDirectory, TTree, TH1F, TCanvas
    _l_(560098)

except ImportError:
    pass
try:
    import math
    _l_(560100)

except ImportError:
    pass
try:
    import numpy as np
    _l_(560102)

except ImportError:
    pass

myfile = _c_(560104, _n_(560103, "TFile", lambda: TFile), "/home/hilary/root/compile/Research/angle_smearing.root")
_l_(560105)
hist = _c_(560108, _a_(560107, _n_(560106, "file", lambda: file), "Get"), "Zenith_Angles")
_l_(560109)
hgm = _c_(560111, _n_(560110, "TH1F", lambda: TH1F), 'Fvsx', 'Smearing_Test_1',100,0,90)
_l_(560112)

for i in _c_(560114, _n_(560113, "range", lambda: range), 1, 100,1):
    _l_(560153)

    for y in _c_(560116, _n_(560115, "range", lambda: range), 1, 100, 1):
        _l_(560152)

        u = _c_(560120, _a_(560118, _n_(560117, "hist", lambda: hist), "GetBinCenter"), _n_(560119, "i", lambda: i))
        _l_(560121)
        N = _c_(560125, _a_(560123, _n_(560122, "hist", lambda: hist), "GetBinContent"), _n_(560124, "i", lambda: i))
        _l_(560126)
        o = 1
        _l_(560127)
        x = _c_(560131, _a_(560129, _n_(560128, "hist", lambda: hist), "GetBinCenter"), _n_(560130, "y", lambda: y))
        _l_(560132)
        F = (_n_(560133, "N", lambda: N)/(_n_(560134, "o", lambda: o)*_c_(560139, _a_(560136, _n_(560135, "math", lambda: math), "sqrt"), 2*_a_(560138, _n_(560137, "math", lambda: math), "pi")))*_c_(560145, _a_(560141, _n_(560140, "math", lambda: math), "e"), (-(_n_(560142, "x", lambda: x)-_n_(560143, "u", lambda: u))**2)/(2*(_n_(560144, "o", lambda: o)**2)))) 
        _l_(560146) 
        _c_(560150, _a_(560148, _n_(560147, "hgm", lambda: hgm), "Fill"), _n_(560149, "F", lambda: F))
        _l_(560151)

c1 = _c_(560155, _n_(560154, "TCanvas", lambda: TCanvas))
_l_(560156)
_c_(560159, _a_(560158, _n_(560157, "hgm", lambda: hgm), "Draw"))
_l_(560160)
_c_(560163, _a_(560162, _n_(560161, "c1", lambda: c1), "SaveAs"), "/home/hilary/Desktop/Out_going_muons_etc/smearing_test_1.png")
_l_(560164)
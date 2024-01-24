# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58848048/attributeerror-class-object-has-no-attribute-outside-loop
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for region in _n_(539287, "regions", lambda: regions):
  _l_(539333)

  if _n_(539288, "region", lambda: region) == '1':
    _l_(539332)

    for region in _n_(539289, "regions", lambda: regions):
      _l_(539331)

      for col in _c_(539293, _n_(539290, "range", lambda: range), _a_(539292, _n_(539291, "prelim_sheet", lambda: prelim_sheet), "ncols")):
        _l_(539330)

        if (_c_(539297, _a_(539295, _n_(539294, "prelim_sheet", lambda: prelim_sheet), "cell_value"), 0, _n_(539296, "col", lambda: col)) == _a_(539299, _n_(539298, "r", lambda: r), "region_name")):
          _l_(539329)

          ...
          _l_(539300)
        else:
          for state in _n_(539301, "state_list", lambda: state_list):
            _l_(539328)

            if _c_(539304, _a_(539303, _n_(539302, "state", lambda: state), "strip")) == 'NewHampshire':
              _l_(539327)

              s = _c_(539307, _n_(539305, "state_class", lambda: state_class), _n_(539306, "state", lambda: state))
              _l_(539308)
              if (_c_(539314, _a_(539313, _c_(539312, _a_(539310, _n_(539309, "prelim_sheet", lambda: prelim_sheet), "cell_value"), 0, _n_(539311, "col", lambda: col)), "replace"), " ", "") == _a_(539316, _n_(539315, "s", lambda: s), "state_name")):
                _l_(539326)

                _n_(539317, "s", lambda: s).state_col = _n_(539318, "col", lambda: col)
                _l_(539319)
                _c_(539323, _n_(539320, "print", lambda: print), _a_(539322, _n_(539321, "s", lambda: s), "state_col"))
                _l_(539324)
                ...
                _l_(539325)
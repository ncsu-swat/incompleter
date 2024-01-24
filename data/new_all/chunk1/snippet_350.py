# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38918748/why-does-mocking-open-and-returning-a-filenotfounderror-raise-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import unittest
    _l_(377294)

except ImportError:
    pass
try:
    import unittest.mock as mock
    _l_(377296)

except ImportError:
    pass
try:
    import so_config
    _l_(377298)

except ImportError:
    pass
try:
    import so_main
    _l_(377300)

except ImportError:
    pass


class TestReadSaveLocation(_a_(377302, _n_(377301, "unittest", lambda: unittest), "TestCase")):
    _l_(377371)

    def setUp(self):
        _l_(377328)

        _n_(377303, "self", lambda: self).savelocation_path = _a_(377305, _n_(377304, "so_config", lambda: so_config), "SAVELOCATION_PATH")
        _l_(377306)
        _n_(377307, "self", lambda: self).root = _a_(377309, _n_(377308, "so_config", lambda: so_config), "ROOT")
        _l_(377310)
        _n_(377311, "so_config", lambda: so_config).ROOT = 'program root'
        _l_(377312)
        p = _c_(377315, _a_(377314, _n_(377313, "mock", lambda: mock), "patch"), 'so_main.open')
        _l_(377316)
        _n_(377317, "self", lambda: self).mock_open = _c_(377320, _a_(377319, _n_(377318, "p", lambda: p), "start"))
        _l_(377321)
        _c_(377326, _a_(377323, _n_(377322, "self", lambda: self), "addCleanup"), _a_(377325, _n_(377324, "p", lambda: p), "stop"))
        _l_(377327)

    def tearDown(self):
        _l_(377337)

        _n_(377329, "so_config", lambda: so_config).SAVELOCATION_PATH = _a_(377331, _n_(377330, "self", lambda: self), "savelocation_path")
        _l_(377332)
        _n_(377333, "so_config", lambda: so_config).ROOT = _a_(377335, _n_(377334, "self", lambda: self), "root")
        _l_(377336)

    def test_read_path_from_disk_file_into_config_py(self):
        _l_(377355)

        _a_(377343, _c_(377342, _a_(377341, _c_(377340, _a_(377339, _n_(377338, "self", lambda: self), "mock_open")), "__enter__")), "readline").return_value = 'data files location'
        _l_(377344)
        _c_(377347, _a_(377346, _n_(377345, "so_main", lambda: so_main), "load_savelocation"))
        _l_(377348)
        _c_(377353, _a_(377350, _n_(377349, "self", lambda: self), "assertEqual"), 'data files location', _a_(377352, _n_(377351, "so_config", lambda: so_config), "SAVELOCATION_PATH"))
        _l_(377354)

    def test_missing_file_defaults_savelocation_to_program_root(self):
        _l_(377370)

        _a_(377357, _n_(377356, "self", lambda: self), "mock_open").return_value = _n_(377358, "FileNotFoundError", lambda: FileNotFoundError)
        _l_(377359)
        _c_(377362, _a_(377361, _n_(377360, "so_main", lambda: so_main), "load_savelocation"))
        _l_(377363)
        _c_(377368, _a_(377365, _n_(377364, "self", lambda: self), "assertEqual"), 'program root', _a_(377367, _n_(377366, "so_config", lambda: so_config), "SAVELOCATION_PATH"))
        _l_(377369)
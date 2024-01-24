# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/27639305/typeerror-str-does-not-support-the-buffer-interface-configparser
# Load the configuration file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(427325, _n_(427323, "open", lambda: open), _n_(427324, "CONFIG_FILE", lambda: CONFIG_FILE),'r+') as f:
    _l_(427330)

    sample_config = _c_(427328, _a_(427327, _n_(427326, "f", lambda: f), "read"))
    _l_(427329)
#config = ConfigParser.RawConfigParser(allow_no_value=True)
config = _c_(427333, _a_(427332, _n_(427331, "configparser", lambda: configparser), "RawConfigParser"), allow_no_value=True)
_l_(427334)
_c_(427341, _a_(427336, _n_(427335, "config", lambda: config), "readfp"), _c_(427340, _a_(427338, _n_(427337, "io", lambda: io), "BytesIO"), _n_(427339, "sample_config", lambda: sample_config)))        
_l_(427342)        
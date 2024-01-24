# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68342294/what-is-the-cause-of-this-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(451284)

except ImportError:
    pass
try:
    import json
    _l_(451286)

except ImportError:
    pass
try:
    import sys
    _l_(451288)

except ImportError:
    pass
try:
    import utils
    _l_(451290)

except ImportError:
    pass
try:
    import error_handler
    _l_(451292)

except ImportError:
    pass
try:
    import get_helper
    _l_(451294)

except ImportError:
    pass
try:
    import os
    _l_(451296)

except ImportError:
    pass
try:
    import pvdata
    _l_(451298)

except ImportError:
    pass

def call_get():
    _l_(451399)

    try:
        _l_(451397)

        auth_tuple = _c_(451301, _a_(451300, _n_(451299, "utils", lambda: utils), "get_auth_details"), "get")
        _l_(451302)
        headers = _c_(451305, _a_(451304, _n_(451303, "utils", lambda: utils), "get_header"))
        _l_(451306)
        resource_types = _c_(451309, _a_(451308, _n_(451307, "utils", lambda: utils), "get_resource_types"))
        _l_(451310)
        namespaces = _c_(451313, _a_(451312, _n_(451311, "utils", lambda: utils), "get_namespaces"))
        _l_(451314)

        if _c_(451317, _a_(451316, _n_(451315, "resource_types", lambda: resource_types)[0], "lower")) == "all":
            _l_(451322)

            resource_types = _c_(451320, _a_(451319, _n_(451318, "utils", lambda: utils), "append_all_resources"))
            _l_(451321)

        _c_(451327, _a_(451324, _n_(451323, "get_helper", lambda: get_helper), "get_namespace_list"), _n_(451325, "auth_tuple", lambda: auth_tuple), _n_(451326, "headers", lambda: headers))
        _l_(451328)
        all_namespaces = _c_(451331, _a_(451330, _n_(451329, "utils", lambda: utils), "extract_namespaces_from_list"), "source")
        _l_(451332)

        if _c_(451335, _a_(451334, _n_(451333, "namespaces", lambda: namespaces)[0], "lower")) != "all":
            _l_(451342)

            _c_(451340, _a_(451337, _n_(451336, "error_handler", lambda: error_handler), "validate_source_namespaces"), _n_(451338, "namespaces", lambda: namespaces), _n_(451339, "all_namespaces", lambda: all_namespaces))
            _l_(451341)

        _c_(451348, _a_(451344, _n_(451343, "utils", lambda: utils), "create_file"), "Namespaces", "All_namespaces_at_source.txt", _c_(451347, _n_(451345, "str", lambda: str), _n_(451346, "all_namespaces", lambda: all_namespaces)))
        _l_(451349)

        _c_(451355, _a_(451351, _n_(451350, "get_helper", lambda: get_helper), "generate_json_for_all_namespaces"), _n_(451352, "all_namespaces", lambda: all_namespaces), _n_(451353, "auth_tuple", lambda: auth_tuple), _n_(451354, "headers", lambda: headers))
        _l_(451356)

        for resource_name in _n_(451357, "resource_types", lambda: resource_types):
            _l_(451382)

            if _c_(451360, _a_(451359, _n_(451358, "namespaces", lambda: namespaces)[0], "lower")) == "all":
                _l_(451381)

                for namespace in _n_(451361, "all_namespaces", lambda: all_namespaces):
                    _l_(451370)

                    _c_(451368, _a_(451363, _n_(451362, "get_helper", lambda: get_helper), "call_all_functions_for_get"), _n_(451364, "namespace", lambda: namespace), _n_(451365, "resource_name", lambda: resource_name), _n_(451366, "headers", lambda: headers), _n_(451367, "auth_tuple", lambda: auth_tuple))
                    _l_(451369)
            else:
                for namespace in _n_(451371, "namespaces", lambda: namespaces):
                    _l_(451380)

                    _c_(451378, _a_(451373, _n_(451372, "get_helper", lambda: get_helper), "call_all_functions_for_get"), _n_(451374, "namespace", lambda: namespace), _n_(451375, "resource_name", lambda: resource_name), _n_(451376, "headers", lambda: headers), _n_(451377, "auth_tuple", lambda: auth_tuple))
                    _l_(451379)
    except _n_(451383, "Exception", lambda: Exception) as error:
        _l_(451396)

        filename = _c_(451388, _a_(451386, _a_(451385, _n_(451384, "os", lambda: os), "path"), "basename"), _n_(451387, "__file__", lambda: __file__))
        _l_(451389)
        _c_(451394, _a_(451391, _n_(451390, "error_handler", lambda: error_handler), "print_exception_message"), _n_(451392, "error", lambda: error), _n_(451393, "filename", lambda: filename))
        _l_(451395)
    aux = ""
    _l_(451398)

    return aux

if _n_(451400, "__name__", lambda: __name__) == "__main__":
    _l_(451404)

    _c_(451402, _n_(451401, "call_get", lambda: call_get))
    _l_(451403)
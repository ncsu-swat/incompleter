# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76331642/python-typeerror-nonetype-object-not-iterable-whats-causing-it
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def get_input_data():
    _l_(623748)

    aux = _n_(623746, "input_data", lambda: input_data)
    _l_(623747)
    # Some code to retrieve input data
    return aux

def process_data(data):
    _l_(623761)

    processed_items = []
    _l_(623749)
    for item in _n_(623750, "data", lambda: data):
        _l_(623758)

        processed_item = _n_(623751, "item", lambda: item) * 2
        _l_(623752)
        _c_(623756, _a_(623754, _n_(623753, "processed_items", lambda: processed_items), "append"), _n_(623755, "processed_item", lambda: processed_item))
        _l_(623757)
    aux = _n_(623759, "processed_items", lambda: processed_items)
    _l_(623760)
    return aux

def main():
    _l_(623773)

    input_data = _c_(623763, _n_(623762, "get_input_data", lambda: get_input_data))
    _l_(623764)
    processed_data = _c_(623767, _n_(623765, "process_data", lambda: process_data), _n_(623766, "input_data", lambda: input_data))
    _l_(623768)
    _c_(623771, _n_(623769, "print", lambda: print), _n_(623770, "processed_data", lambda: processed_data))
    _l_(623772)

if _n_(623774, "__name__", lambda: __name__) == "__main__":
    _l_(623778)

    _c_(623776, _n_(623775, "main", lambda: main))
    _l_(623777)
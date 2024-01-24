# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66763769/import-soundfile-as-sf-but-on-jupyter-notebook-sf-gives-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import soundfile as sf
    _l_(357566)

except ImportError:
    pass
def speech_file_to_array_fn(batch):
    _l_(357583)

    speech_array, sampling_rate = _c_(357570, _a_(357568, _n_(357567, "sf", lambda: sf), "read"), _n_(357569, "batch", lambda: batch)["file"])
    _l_(357571)
    _n_(357572, "batch", lambda: batch)["speech"] = _n_(357573, "speech_array", lambda: speech_array)
    _l_(357574)
    _n_(357575, "batch", lambda: batch)["sampling_rate"] = _n_(357576, "sampling_rate", lambda: sampling_rate)
    _l_(357577)
    _n_(357578, "batch", lambda: batch)["target_text"] = _n_(357579, "batch", lambda: batch)["text"]
    _l_(357580)
    aux = _n_(357581, "batch", lambda: batch)
    _l_(357582)
    return aux

timit = _c_(357589, _a_(357585, _n_(357584, "timit", lambda: timit), "map"), _n_(357586, "speech_file_to_array_fn", lambda: speech_file_to_array_fn), remove_columns=_a_(357588, _n_(357587, "timit", lambda: timit), "column_names")["train"], num_proc=4)
_l_(357590)
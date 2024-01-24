# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51488228/attributeerror-str-object-has-no-attribute-id-using-biopython-parsing-fast
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
file_in ='lots_of_fasta_in_file.fasta'
_l_(395435)
file_out='new.fasta'
_l_(395436)

with _c_(395439, _n_(395437, "open", lambda: open), _n_(395438, "file_out", lambda: file_out), 'w') as f_out:
    _l_(395467)

    with _c_(395442, _n_(395440, "open", lambda: open), _n_(395441, "file_in", lambda: file_in), 'r') as f_in:
        _l_(395466)

        for seq_record in _c_(395446, _a_(395444, _n_(395443, "SeqIO", lambda: SeqIO), "parse"), _n_(395445, "f_in", lambda: f_in), 'fasta'):
            _l_(395465)

            name, sequence = _a_(395448, _n_(395447, "seq_record", lambda: seq_record), "id"), _c_(395452, _n_(395449, "str", lambda: str), _a_(395451, _n_(395450, "seq_record", lambda: seq_record), "seq"))
            _l_(395453)
            # remove .seq from ID and add features
            pair = [_c_(395456, _a_(395455, _n_(395454, "name", lambda: name), "replace"), '.seq',''), _n_(395457, "sequence", lambda: sequence)]
            _l_(395458)
            _c_(395463, _a_(395460, _n_(395459, "SeqIO", lambda: SeqIO), "write"), _n_(395461, "pair", lambda: pair), _n_(395462, "file_out", lambda: file_out), 'fasta')
            _l_(395464)
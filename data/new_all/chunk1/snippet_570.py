# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51488228/attributeerror-str-object-has-no-attribute-id-using-biopython-parsing-fast
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(386162, _n_(386161, "open", lambda: open), 'lots_of_fasta_in_file.fasta') as f:
    _l_(386185)

    for seq_record in _c_(386166, _a_(386164, _n_(386163, "SeqIO", lambda: SeqIO), "parse"), _n_(386165, "f", lambda: f), 'fasta'):
        _l_(386184)

        name, sequence = _a_(386168, _n_(386167, "seq_record", lambda: seq_record), "id"), _c_(386172, _n_(386169, "str", lambda: str), _a_(386171, _n_(386170, "seq_record", lambda: seq_record), "seq"))
        _l_(386173)
        pair = [_c_(386176, _a_(386175, _n_(386174, "name", lambda: name), "replace"), '.seq',''), _n_(386177, "sequence", lambda: sequence)]
        _l_(386178)
        _c_(386182, _a_(386180, _n_(386179, "SeqIO", lambda: SeqIO), "write"), _n_(386181, "pair", lambda: pair), "new.fasta", "fasta")
        _l_(386183)
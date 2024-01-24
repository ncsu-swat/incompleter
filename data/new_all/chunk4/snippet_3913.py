# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65377587/what-i-have-the-erroe-typeerror-string-indices-must-be-integers-how-can-i-sol
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
pep = 'MEGNCS'
_l_(591793)
newseqs = []
_l_(591794)
bt= {'I': ['ATA', 'ATC', 'ATT'], 'M': ['ATG'], 'T': ['ACA', 'ACC', 'ACG', 'ACT'], 'N': ['AAC', 'AAT'], 'K': ['AAA', 'AAG'], 'S': ['AGC', 'AGT', 'TCA', 'TCC', 'TCG', 'TCT'], 'R': ['AGA', 'AGG', 'CGA', 'CGC', 'CGG', 'CGT'], 'L': ['CTA', 'CTC', 'CTG', 'CTT', 'TTA', 'TTG'], 'P': ['CCA', 'CCC', 'CCG', 'CCT'], 'H': ['CAC', 'CAT'], 'Q': ['CAA', 'CAG'], 'V': ['GTA', 'GTC', 'GTG', 'GTT'], 'A': ['GCA', 'GCC', 'GCG', 'GCT'], 'D': ['GAC', 'GAT'], 'E': ['GAA', 'GAG'], 'G': ['GGA', 'GGC', 'GGG', 'GGT'], 'F': ['TTC', 'TTT'], 'Y': ['TAC', 'TAT'], '_': ['TAA', 'TAG', 'TGA'], 'C': ['TGC', 'TGT'], 'W': ['TGG']}
_l_(591795)
_c_(591800, _n_(591796, "back_trans", lambda: back_trans), _n_(591797, "pep", lambda: pep),_n_(591798, "bt", lambda: bt), 0, _n_(591799, "newseqs", lambda: newseqs))
_l_(591801)
_c_(591806, _n_(591802, "print", lambda: print), _c_(591805, _a_(591803, '\n', "join"), _n_(591804, "newseqs", lambda: newseqs)))
_l_(591807)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48244659/multiprocessing-cannot-write-list-to-csv-typeerror-applyresult-object-is-n
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from multiprocessing import Pool
    _l_(381221)

except ImportError:
    pass
try:
    import csv
    _l_(381223)

except ImportError:
    pass
pool = _c_(381225, _n_(381224, "Pool", lambda: Pool))
_l_(381226)

nodes = [['1001', '2008-01-06T02:12:13Z', ['']],
        ['1002', '2008-01-06T02:13:55Z', ['']],
        ['1003', '2008-01-06T02:13:00Z',  ['Lion', 'Rhinoceros', 'Leopard', 'Panda']],
        ['1004', '2008-01-06T02:15:20Z', ['Lion', 'Leopard', 'Eagle', 'Panda', 'Tiger']],
        ['1005', '2008-01-06T02:15:48Z', ['Lion', 'Panda', 'Cheetah', 'Goat', 'Tiger']],
        ['1006', '2008-01-06T02:13:30Z', ['']],
        ['1007', '2008-01-06T02:13:38Z', ['Cheetah', 'Tiger', 'Goat']]]
_l_(381227)

def nodes_to_links(nodes_list):
    _l_(381272)

    output_list = []
    _l_(381228)
    for ii, elem in _c_(381231, _n_(381229, "enumerate", lambda: enumerate), _n_(381230, "nodes_list", lambda: nodes_list)[:-1]):
        _l_(381269)

        for jj in _c_(381237, _n_(381232, "range", lambda: range), _n_(381233, "ii", lambda: ii) + 1, _c_(381236, _n_(381234, "len", lambda: len), _n_(381235, "nodes_list", lambda: nodes_list))):
            _l_(381268)

            common = _c_(381246, _a_(381241, _c_(381240, _n_(381238, "set", lambda: set), _n_(381239, "elem", lambda: elem)[-1]), "intersection"), _c_(381245, _n_(381242, "set", lambda: set), _n_(381243, "nodes_list", lambda: nodes_list)[_n_(381244, "jj", lambda: jj)][-1]))
            _l_(381247)
            if _c_(381250, _n_(381248, "len", lambda: len), _n_(381249, "common", lambda: common)) > 0 and _n_(381251, "common", lambda: common) != {''}:
                _l_(381267)

                _c_(381265, _a_(381253, _n_(381252, "output_list", lambda: output_list), "append"), [_n_(381254, "elem", lambda: elem)[0], _n_(381255, "nodes_list", lambda: nodes_list)[_n_(381256, "jj", lambda: jj)][0], _c_(381264, _a_(381257, ',', "join"), _c_(381263, _n_(381258, "map", lambda: map), _n_(381259, "str", lambda: str), _c_(381262, _n_(381260, "list", lambda: list), _n_(381261, "common", lambda: common))))])
                _l_(381266)
    aux = _n_(381270, "output_list", lambda: output_list)
    _l_(381271)
    return aux

#links = nodes_to_links(nodes) ###This works perfect without multiprocessing
links = _c_(381277, _a_(381274, _n_(381273, "pool", lambda: pool), "apply_async"), _n_(381275, "nodes_to_links", lambda: nodes_to_links), _n_(381276, "nodes", lambda: (nodes)))  ### This works if I don't write the list "links" to a csv, but not otherwise
_l_(381278)  ### This works if I don't write the list "links" to a csv, but not otherwise

# Write links to a csv file
def writeCSV(list_to_write, OutputFileName):
    _l_(381297)

    file = _c_(381281, _n_(381279, "open", lambda: open), _n_(381280, "OutputFileName", lambda: OutputFileName), 'w', newline='')
    _l_(381282)
    writer = _c_(381288, _a_(381284, _n_(381283, "csv", lambda: csv), "writer"), _n_(381285, "file", lambda: file), quotechar='"', delimiter=';',quoting=_a_(381287, _n_(381286, "csv", lambda: csv), "QUOTE_ALL"), skipinitialspace=True)
    _l_(381289)
    for row in _n_(381290, "list_to_write", lambda: list_to_write):
        _l_(381296)

        _c_(381294, _a_(381292, _n_(381291, "writer", lambda: writer), "writerow"), _n_(381293, "row", lambda: row))
        _l_(381295)

_c_(381300, _n_(381298, "writeCSV", lambda: writeCSV), _n_(381299, "links", lambda: links),'output_files/test.csv')
_l_(381301)
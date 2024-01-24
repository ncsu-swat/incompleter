# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66434835/attributeerror-tuple-object-has-no-attribute-convert
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(577251)

except ImportError:
    pass
try:
    import json
    _l_(577253)

except ImportError:
    pass
try:
    import random
    _l_(577255)

except ImportError:
    pass
try:
    import csv
    _l_(577257)

except ImportError:
    pass
try:
    from pydub import AudioSegment
    _l_(577259)

except ImportError:
    pass

file_path = '/path/to/file/.tsv '
_l_(577260)
save_json_path = '/path/where/you/want/the/jsons/saved' 
_l_(577261) 

def main(args):
    _l_(577433)

    data = []
    _l_(577262)
    directory = _c_(577265, _a_(577264, _n_(577263, "file_path", lambda: file_path), "rpartition"), '/')[0]
    _l_(577266)
    percent = _c_(577268, _n_(577267, "int", lambda: int), 100)
    _l_(577269)
    
    with _c_(577272, _n_(577270, "open", lambda: open), _n_(577271, "file_path", lambda: file_path), encoding="latin-1") as f:
        _l_(577277)

        lenght = _c_(577275, _n_(577273, "sum", lambda: sum), (1 for ine in _n_(577274, "f", lambda: f)))
        _l_(577276)
    with _c_(577280, _n_(577278, "open", lambda: open), _n_(577279, "file_path", lambda: file_path), newline='') as csvfile:
        _l_(577350)

        reader = _c_(577284, _a_(577282, _n_(577281, "csv", lambda: csv), "DictReader"), _n_(577283, "csvfile", lambda: csvfile), delimiter='\t')
        _l_(577285)
        index = 1
        _l_(577286)
        if_a_(577288, _n_(577287, "args", lambda: args), "convert"):
            _l_(577295)

            _c_(577293, _n_(577289, "print", lambda: print), _c_(577292, _n_(577290, "str", lambda: str), _n_(577291, "lenght", lambda: lenght)) + "files found")
            _l_(577294)
        for row in _n_(577296, "reader", lambda: reader):
            _l_(577349)

            file_name = _n_(577297, "row", lambda: row)['path']
            _l_(577298)
            filename = _c_(577301, _a_(577300, _n_(577299, "file_name", lambda: file_name), "rpartition"), '.')[0] + ".wav"
            _l_(577302)
            text = _n_(577303, "row", lambda: row)['sentence']
            _l_(577304)
            if_a_(577306, _n_(577305, "args", lambda: args), "convert"):
                _l_(577348)

                _c_(577312, _a_(577308, _n_(577307, "data", lambda: data), "append"), {
                "key": _n_(577309, "directory", lambda: directory) + "/clips/" + _n_(577310, "filename", lambda: filename),
                "text": _n_(577311, "text", lambda: text)
                })
                _l_(577313)
                _c_(577321, _n_(577314, "print", lambda: print), "converting file " + _c_(577317, _n_(577315, "str", lambda: str), _n_(577316, "index", lambda: index)) + "/" + _c_(577320, _n_(577318, "str", lambda: str), _n_(577319, "lenght", lambda: lenght)) + " to wav", end="\r")
                _l_(577322)
                src = _n_(577323, "directory", lambda: directory) + "/clips/" + _n_(577324, "file_name", lambda: file_name)
                _l_(577325)
                dst = _n_(577326, "directory", lambda: directory) + "/clips/" + _n_(577327, "filename", lambda: filename)
                _l_(577328)
                sound = _c_(577332, _a_(577330, _n_(577329, "AudioSegment", lambda: AudioSegment), "from_mp3"), _n_(577331, "src", lambda: src))
                _l_(577333)
                _c_(577337, _a_(577335, _n_(577334, "sound", lambda: sound), "export"), _n_(577336, "dst", lambda: dst), format="wav")
                _l_(577338)
                index = _n_(577339, "index", lambda: index) + 1
                _l_(577340)
            else:
                _c_(577346, _a_(577342, _n_(577341, "data", lambda: data), "append"), {
                "key": _n_(577343, "directory", lambda: directory) + "/clips/" + _n_(577344, "file_name", lambda: file_name),
                "text": _n_(577345, "text", lambda: text)
                })
                _l_(577347)
                
    _c_(577354, _a_(577352, _n_(577351, "random", lambda: random), "shuffle"), _n_(577353, "data", lambda: data))
    _l_(577355)

    _c_(577357, _n_(577356, "print", lambda: print), "creating JSON's")
    _l_(577358)
    f = _c_(577361, _n_(577359, "open", lambda: open), _n_(577360, "save_json_path", lambda: save_json_path) +"/"+ "train.json", "w")
    _l_(577362)
    
    with _c_(577365, _n_(577363, "open", lambda: open), _n_(577364, "save_json_path", lambda: save_json_path) +"/"+ 'train.json','w') as f:
        _l_(577393)

        d = _c_(577368, _n_(577366, "len", lambda: len), _n_(577367, "data", lambda: data))
        _l_(577369)
        i=0
        _l_(577370)
        while(_n_(577371, "i", lambda: i)<_c_(577376, _n_(577372, "int", lambda: int), _n_(577373, "d", lambda: d)-_n_(577374, "d", lambda: d)/_n_(577375, "percent", lambda: percent))):
            _l_(577392)

            r=_n_(577377, "data", lambda: data)[_n_(577378, "i", lambda: i)]
            _l_(577379)
            line = _c_(577383, _a_(577381, _n_(577380, "json", lambda: json), "dumps"), _n_(577382, "r", lambda: r))
            _l_(577384)
            _c_(577388, _a_(577386, _n_(577385, "f", lambda: f), "write"), _n_(577387, "line", lambda: line) + "\n")
            _l_(577389)
            i = _n_(577390, "i", lambda: i)+1
            _l_(577391)
    
    f = _c_(577396, _n_(577394, "open", lambda: open), _n_(577395, "save_json_path", lambda: save_json_path) +"/"+ "test.json", "w")
    _l_(577397)

    with _c_(577400, _n_(577398, "open", lambda: open), _n_(577399, "save_json_path", lambda: save_json_path) +"/"+ 'test.json','w') as f:
        _l_(577429)

        d = _c_(577403, _n_(577401, "len", lambda: len), _n_(577402, "data", lambda: data))
        _l_(577404)
        i=_c_(577409, _n_(577405, "int", lambda: int), _n_(577406, "d", lambda: d)-_n_(577407, "d", lambda: d)/_n_(577408, "percent", lambda: percent))
        _l_(577410)
        while(_n_(577411, "i", lambda: i)<_n_(577412, "d", lambda: d)):
            _l_(577428)

            r=_n_(577413, "data", lambda: data)[_n_(577414, "i", lambda: i)]
            _l_(577415)
            line = _c_(577419, _a_(577417, _n_(577416, "json", lambda: json), "dumps"), _n_(577418, "r", lambda: r))
            _l_(577420)
            _c_(577424, _a_(577422, _n_(577421, "f", lambda: f), "write"), _n_(577423, "line", lambda: line) + "\n")
            _l_(577425)
            i = _n_(577426, "i", lambda: i)+1
            _l_(577427)
    _c_(577431, _n_(577430, "print", lambda: print), "Done!")
    _l_(577432)

if _n_(577434, "__name__", lambda: __name__) == "__main__":
    _l_(577453)

    try:
        import argparse
        _l_(577436)

    except ImportError:
        pass

    parser = _c_(577439, _a_(577438, _n_(577437, "argparse", lambda: argparse), "ArgumentParser"), description="""
    Utility script to convert commonvoice into wav and create the training and test json files. """
    )
    _l_(577440)
    _c_(577443, _a_(577442, _n_(577441, "parser", lambda: parser), "add_argument"), '--convert', default=True, action='store_true',
                        help='says that the script should convert mp3 to wav')
    _l_(577444)

    
    args = _c_(577447, _a_(577446, _n_(577445, "parser", lambda: parser), "parse_known_args"))
    _l_(577448)
    _c_(577451, _n_(577449, "main", lambda: main), _n_(577450, "args", lambda: args))
    _l_(577452)
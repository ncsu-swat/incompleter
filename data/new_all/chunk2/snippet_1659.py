# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66422605/attributeerror-io-textiowrapper-object-has-no-attribute-rpartition
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(455115)

except ImportError:
    pass
try:
    import json
    _l_(455117)

except ImportError:
    pass
try:
    import random
    _l_(455119)

except ImportError:
    pass
try:
    import csv
    _l_(455121)

except ImportError:
    pass
try:
    from pydub import AudioSegment
    _l_(455123)

except ImportError:
    pass


file_path = _c_(455125, _n_(455124, "open", lambda: open), '/path/to/file/.tsv ', encoding='UTF-8')
_l_(455126)
save_json_path = '/path/where/you/want/the/jsons/saved' 
_l_(455127) 

def main(args):
    _l_(455299)

    data = []
    _l_(455128)
    directory = _c_(455131, _a_(455130, _n_(455129, "file_path", lambda: file_path), "rpartition"), '/')[0]
    _l_(455132)
    percent = _c_(455134, _n_(455133, "int", lambda: int), 100)
    _l_(455135)
    
    with _c_(455138, _n_(455136, "open", lambda: open), _n_(455137, "file_path", lambda: file_path)) as f:
        _l_(455143)

        lenght = _c_(455141, _n_(455139, "sum", lambda: sum), (1 for ine in _n_(455140, "f", lambda: f)))
        _l_(455142)
    
    
    
    
    with _c_(455146, _n_(455144, "open", lambda: open), _n_(455145, "file_path", lambda: file_path), newline='') as csvfile:
        _l_(455216)

        reader = _c_(455150, _a_(455148, _n_(455147, "csv", lambda: csv), "DictReader"), _n_(455149, "csvfile", lambda: csvfile), delimiter='\t')
        _l_(455151)
        index = 1
        _l_(455152)
        if_a_(455154, _n_(455153, "args", lambda: args), "convert"):
            _l_(455161)

            _c_(455159, _n_(455155, "print", lambda: print), _c_(455158, _n_(455156, "str", lambda: str), _n_(455157, "lenght", lambda: lenght)) + "files found")
            _l_(455160)
        for row in _n_(455162, "reader", lambda: reader):
            _l_(455215)

            file_name = _n_(455163, "row", lambda: row)['path']
            _l_(455164)
            filename = _c_(455167, _a_(455166, _n_(455165, "file_name", lambda: file_name), "rpartition"), '.')[0] + ".wav"
            _l_(455168)
            text = _n_(455169, "row", lambda: row)['sentence']
            _l_(455170)
            if_a_(455172, _n_(455171, "args", lambda: args), "convert"):
                _l_(455214)

                _c_(455178, _a_(455174, _n_(455173, "data", lambda: data), "append"), {
                "key": _n_(455175, "directory", lambda: directory) + "/clips/" + _n_(455176, "filename", lambda: filename),
                "text": _n_(455177, "text", lambda: text)
                })
                _l_(455179)
                _c_(455187, _n_(455180, "print", lambda: print), "converting file " + _c_(455183, _n_(455181, "str", lambda: str), _n_(455182, "index", lambda: index)) + "/" + _c_(455186, _n_(455184, "str", lambda: str), _n_(455185, "lenght", lambda: lenght)) + " to wav", end="\r")
                _l_(455188)
                src = _n_(455189, "directory", lambda: directory) + "/clips/" + _n_(455190, "file_name", lambda: file_name)
                _l_(455191)
                dst = _n_(455192, "directory", lambda: directory) + "/clips/" + _n_(455193, "filename", lambda: filename)
                _l_(455194)
                sound = _c_(455198, _a_(455196, _n_(455195, "AudioSegment", lambda: AudioSegment), "from_mp3"), _n_(455197, "src", lambda: src))
                _l_(455199)
                _c_(455203, _a_(455201, _n_(455200, "sound", lambda: sound), "export"), _n_(455202, "dst", lambda: dst), format="wav")
                _l_(455204)
                index = _n_(455205, "index", lambda: index) + 1
                _l_(455206)
            else:
                _c_(455212, _a_(455208, _n_(455207, "data", lambda: data), "append"), {
                "key": _n_(455209, "directory", lambda: directory) + "/clips/" + _n_(455210, "file_name", lambda: file_name),
                "text": _n_(455211, "text", lambda: text)
                })
                _l_(455213)
                
    _c_(455220, _a_(455218, _n_(455217, "random", lambda: random), "shuffle"), _n_(455219, "data", lambda: data))
    _l_(455221)

    _c_(455223, _n_(455222, "print", lambda: print), "creating JSON's")
    _l_(455224)
    f = _c_(455227, _n_(455225, "open", lambda: open), _n_(455226, "save_json_path", lambda: save_json_path) +"/"+ "train.json", "w")
    _l_(455228)
    
    with _c_(455231, _n_(455229, "open", lambda: open), _n_(455230, "save_json_path", lambda: save_json_path) +"/"+ 'train.json','w') as f:
        _l_(455259)

        d = _c_(455234, _n_(455232, "len", lambda: len), _n_(455233, "data", lambda: data))
        _l_(455235)
        i=0
        _l_(455236)
        while(_n_(455237, "i", lambda: i)<_c_(455242, _n_(455238, "int", lambda: int), _n_(455239, "d", lambda: d)-_n_(455240, "d", lambda: d)/_n_(455241, "percent", lambda: percent))):
            _l_(455258)

            r=_n_(455243, "data", lambda: data)[_n_(455244, "i", lambda: i)]
            _l_(455245)
            line = _c_(455249, _a_(455247, _n_(455246, "json", lambda: json), "dumps"), _n_(455248, "r", lambda: r))
            _l_(455250)
            _c_(455254, _a_(455252, _n_(455251, "f", lambda: f), "write"), _n_(455253, "line", lambda: line) + "\n")
            _l_(455255)
            i = _n_(455256, "i", lambda: i)+1
            _l_(455257)
    
    f = _c_(455262, _n_(455260, "open", lambda: open), _n_(455261, "save_json_path", lambda: save_json_path) +"/"+ "test.json", "w")
    _l_(455263)

    with _c_(455266, _n_(455264, "open", lambda: open), _n_(455265, "save_json_path", lambda: save_json_path) +"/"+ 'test.json','w') as f:
        _l_(455295)

        d = _c_(455269, _n_(455267, "len", lambda: len), _n_(455268, "data", lambda: data))
        _l_(455270)
        i=_c_(455275, _n_(455271, "int", lambda: int), _n_(455272, "d", lambda: d)-_n_(455273, "d", lambda: d)/_n_(455274, "percent", lambda: percent))
        _l_(455276)
        while(_n_(455277, "i", lambda: i)<_n_(455278, "d", lambda: d)):
            _l_(455294)

            r=_n_(455279, "data", lambda: data)[_n_(455280, "i", lambda: i)]
            _l_(455281)
            line = _c_(455285, _a_(455283, _n_(455282, "json", lambda: json), "dumps"), _n_(455284, "r", lambda: r))
            _l_(455286)
            _c_(455290, _a_(455288, _n_(455287, "f", lambda: f), "write"), _n_(455289, "line", lambda: line) + "\n")
            _l_(455291)
            i = _n_(455292, "i", lambda: i)+1
            _l_(455293)
    _c_(455297, _n_(455296, "print", lambda: print), "Done!")
    _l_(455298)

if _n_(455300, "__name__", lambda: __name__) == "__main__":
    _l_(455319)

    try:
        import argparse
        _l_(455302)

    except ImportError:
        pass

    parser = _c_(455305, _a_(455304, _n_(455303, "argparse", lambda: argparse), "ArgumentParser"), description="""
    Utility script to convert commonvoice into wav and create the training and test json files for speechrecognition. """
    )  
    _l_(455306)  
    _c_(455309, _a_(455308, _n_(455307, "parser", lambda: parser), "add_argument"), '--convert', default=True, action='store_true',
                        help='says that the script should convert mp3 to wav')
    _l_(455310)

    
    args = _c_(455313, _a_(455312, _n_(455311, "parser", lambda: parser), "parse_known_args"))
    _l_(455314)
    _c_(455317, _n_(455315, "main", lambda: main), _n_(455316, "args", lambda: args))
    _l_(455318)
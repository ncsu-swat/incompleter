# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66873968/filenotfounderror-errno-2-no-such-file-or-directory-corpus-or-ab-fmc-xlsx
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dir = "/home/geta/kelo/eXP/Test/corpus"
_l_(563239)
for root, subdirs, files in _c_(563243, _a_(563241, _n_(563240, "os", lambda: os), "walk"), _n_(563242, "dir", lambda: dir)):
    _l_(563288)

    _c_(563246, _n_(563244, "print", lambda: print), _n_(563245, "root", lambda: root))
    _l_(563247)
    for file in _n_(563248, "files", lambda: files):
        _l_(563287)

        #print(files)
        _c_(563251, _n_(563249, "print", lambda: print), "-----File in processed :", _n_(563250, "file", lambda: file))
        _l_(563252)
        # -----File in processed : corpus_or_AB_FMC.xlsx  # this file si located in the corpus directory
        sentences = _c_(563256, _a_(563254, _n_(563253, "pd", lambda: pd), "read_excel"), _n_(563255, "file", lambda: file), sheet_name= 0)
        _l_(563257)
        data_id = _a_(563259, _n_(563258, "sentences", lambda: sentences), "identifiant")
        _l_(563260)
        _c_(563265, _n_(563261, "print", lambda: print), "Total phrases: ", _c_(563264, _n_(563262, "len", lambda: len), _n_(563263, "data_id", lambda: data_id)))
        _l_(563266)
        data = _a_(563268, _n_(563267, "sentences", lambda: sentences), "verbatim")
        _l_(563269)

        data_label = _a_(563271, _n_(563270, "sentences", lambda: sentences), "etiquette")
        _l_(563272)
        #print(type(data_id))
        #print(type(data))
        #number = LabelEncoder()
        # 0 = C; 1= F; 2= M
        #data_label = number.fit_transform(sentences.etiquette.astype('str'))
        #print(data_label)
        
        _c_(563277, _n_(563273, "print", lambda: print), "etiquette  :" , _c_(563276, _a_(563275, _n_(563274, "sentences", lambda: sentences)['etiquette'], "unique")))
        _l_(563278)
        classes = _c_(563281, _a_(563280, _n_(563279, "sentences", lambda: sentences)['etiquette'], "unique"))
        _l_(563282)
        len_classes = _c_(563285, _n_(563283, "len", lambda: len), _n_(563284, "classes", lambda: classes))
        _l_(563286)
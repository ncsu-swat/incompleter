# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54155083/name-error-when-reading-files-recursively-in-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
top_dir_list= _c_(707260, _n_(707255, "next", lambda: next), _c_(707259, _a_(707257, _n_(707256, "os", lambda: os), "walk"), _n_(707258, "root", lambda: root)))[1]
_l_(707261)
for j in _c_(707266, _n_(707262, "range", lambda: range), 0,_c_(707265, _n_(707263, "len", lambda: len), _n_(707264, "top_dir_list", lambda: top_dir_list))):
    _l_(707366)

    sub_src=_n_(707267, "top_dir_list", lambda: top_dir_list)[_n_(707268, "j", lambda: j)]
    _l_(707269)
    sub_root=_c_(707275, _a_(707272, _a_(707271, _n_(707270, "os", lambda: os), "path"), "join"), _n_(707273, "root", lambda: root),_n_(707274, "sub_src", lambda: sub_src))
    _l_(707276)

    result_csv=_c_(707281, _a_(707279, _a_(707278, _n_(707277, "os", lambda: os), "path"), "join"), _n_(707280, "sub_root", lambda: sub_root),'metainfo.csv')
    _l_(707282)
    with _c_(707285, _n_(707283, "open", lambda: open), _n_(707284, "result_csv", lambda: result_csv), 'w',encoding='utf-8') as csvfile:
        _l_(707365)

        fieldnames=['filename','duration','filesize']  # keys.
        _l_(707286)  # keys.
        csv_writer = _c_(707291, _a_(707288, _n_(707287, "csv", lambda: csv), "DictWriter"), _n_(707289, "csvfile", lambda: csvfile), fieldnames=_n_(707290, "fieldnames", lambda: fieldnames)) 
        _l_(707292) 
        _c_(707295, _a_(707294, _n_(707293, "csv_writer", lambda: csv_writer), "writeheader"))
        _l_(707296)

        dirfiles=[]
        _l_(707297)
        for path, subdirs, files in _c_(707301, _a_(707299, _n_(707298, "os", lambda: os), "walk"), _n_(707300, "sub_root", lambda: sub_root)):
            _l_(707314)

            for item in _n_(707302, "files", lambda: files):
                _l_(707313)

                _c_(707311, _a_(707304, _n_(707303, "dirfiles", lambda: dirfiles), "append"), _c_(707310, _a_(707307, _a_(707306, _n_(707305, "os", lambda: os), "path"), "join"), _n_(707308, "path", lambda: path), _n_(707309, "item", lambda: item)))
                _l_(707312)
        length=_c_(707317, _n_(707315, "len", lambda: len), _n_(707316, "dirfiles", lambda: dirfiles))
        _l_(707318)
        for i in _c_(707321, _n_(707319, "range", lambda: range), 0,_n_(707320, "length", lambda: length)):
            _l_(707364)

            if _c_(707325, _a_(707324, _n_(707322, "dirfiles", lambda: dirfiles)[_n_(707323, "i", lambda: i)], "endswith"), '.rar'):
                _l_(707356)

                _c_(707329, _n_(707326, "print", lambda: print), 'this is a rar file:', _n_(707327, "dirfiles", lambda: dirfiles)[_n_(707328, "i", lambda: i)])
                _l_(707330)
            elif _c_(707334, _a_(707333, (_n_(707331, "dirfiles", lambda: dirfiles)[_n_(707332, "i", lambda: i)]), "endswith"), ('mp3', 'wav')):
                _l_(707355)

                #title=os.path.basename(dirfiles[i])
                title=_a_(707336, _n_(707335, "tag", lambda: tag), "filesize")
                _l_(707337)
                tag = _c_(707342, _a_(707339, _n_(707338, "TinyTag", lambda: TinyTag), "get"), _n_(707340, "dirfiles", lambda: dirfiles)[_n_(707341, "i", lambda: i)])
                _l_(707343)
                duration=_a_(707345, _n_(707344, "tag", lambda: tag), "duration")
                _l_(707346)
                filesize=_a_(707348, _n_(707347, "tag", lambda: tag), "filesize")
                _l_(707349)
            else:
                _c_(707353, _n_(707350, "print", lambda: print), "This file type is not supported:",_n_(707351, "dirfiles", lambda: dirfiles)[_n_(707352, "i", lambda: i)])
                _l_(707354)

            _c_(707362, _a_(707358, _n_(707357, "csv_writer", lambda: csv_writer), "writerow"), {'filename':_n_(707359, "title", lambda: title),'duration':_n_(707360, "duration", lambda: duration),'filesize':_n_(707361, "filesize", lambda: filesize)})
            _l_(707363)
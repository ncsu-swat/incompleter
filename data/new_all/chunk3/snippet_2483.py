# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76041886/filenotfounderror-errno-2-no-such-file-or-directory-file-name-py
########################################
#TREE
########################################
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
file_tree = _c_(556199, _n_(556197, "Frame", lambda: Frame), _n_(556198, "root", lambda: root))
_l_(556200)
_c_(556205, _a_(556202, _n_(556201, "file_tree", lambda: file_tree), "pack"), side='left', fill=_n_(556203, "Y", lambda: Y), expand=_n_(556204, "NO", lambda: NO))
_l_(556206)
def open_dir():
    _l_(556235)

    for i in _c_(556209, _a_(556208, _n_(556207, "tree", lambda: tree), "get_children")):
        _l_(556215)

        _c_(556213, _a_(556211, _n_(556210, "tree", lambda: tree), "delete"), _n_(556212, "i", lambda: i))
        _l_(556214)
    path = _c_(556217, _n_(556216, "askdirectory", lambda: askdirectory))
    _l_(556218)
    abspath = _c_(556223, _a_(556221, _a_(556220, _n_(556219, "os", lambda: os), "path"), "abspath"), _n_(556222, "path", lambda: path))
    _l_(556224)
    root_node = _c_(556228, _a_(556226, _n_(556225, "tree", lambda: tree), "insert"), '', 'end', text=_n_(556227, "abspath", lambda: abspath), open=True)
    _l_(556229)
    _c_(556233, _n_(556230, "process_directory", lambda: process_directory), _n_(556231, "root_node", lambda: root_node),_n_(556232, "abspath", lambda: abspath))
    _l_(556234)

def process_directory( parent, path):
    _l_(556267)


    for p in _c_(556239, _a_(556237, _n_(556236, "os", lambda: os), "listdir"), _n_(556238, "path", lambda: path)):
        _l_(556266)

        abspath = _c_(556245, _a_(556242, _a_(556241, _n_(556240, "os", lambda: os), "path"), "join"), _n_(556243, "path", lambda: path), _n_(556244, "p", lambda: p))
        _l_(556246)
        isdir = _c_(556251, _a_(556249, _a_(556248, _n_(556247, "os", lambda: os), "path"), "isdir"), _n_(556250, "abspath", lambda: abspath))
        _l_(556252)
        oid = _c_(556257, _a_(556254, _n_(556253, "tree", lambda: tree), "insert"), _n_(556255, "parent", lambda: parent), 'end', text=_n_(556256, "p", lambda: p), open=False)
        _l_(556258)
        if _n_(556259, "isdir", lambda: isdir):
            _l_(556265)

            _c_(556263, _n_(556260, "process_directory", lambda: process_directory), _n_(556261, "oid", lambda: oid), _n_(556262, "abspath", lambda: abspath))
            _l_(556264)

def Open_file_from_list_box(value):
    _l_(556301)

    global file
    _l_(556268)
    item_id = _c_(556271, _a_(556270, _n_(556269, "tree", lambda: tree), "selection"))
    _l_(556272)
    file = _c_(556276, _a_(556274, _n_(556273, "tree", lambda: tree), "item"), _n_(556275, "item_id", lambda: item_id), 'text') # get the filename from 'text' option
    _l_(556277) # get the filename from 'text' option
    filepath = _c_(556283, _a_(556280, _a_(556279, _n_(556278, "os", lambda: os), "path"), "join"), _n_(556281, "value", lambda: value),_n_(556282, "file", lambda: file))     
    _l_(556284)     
    _c_(556288, _a_(556286, _n_(556285, "editArea", lambda: editArea), "delete"), 1.0,_n_(556287, "END", lambda: END))
    _l_(556289)
    with _c_(556292, _n_(556290, "open", lambda: open), _n_(556291, "filepath", lambda: filepath),"r") as f:
        _l_(556300)

        _c_(556298, _a_(556294, _n_(556293, "editArea", lambda: editArea), "insert"), 1.0,_c_(556297, _a_(556296, _n_(556295, "f", lambda: f), "read")))
        _l_(556299)

tree = _c_(556305, _a_(556303, _n_(556302, "ttk", lambda: ttk), "Treeview"), _n_(556304, "file_tree", lambda: file_tree))
_l_(556306)
_c_(556311, _a_(556308, _n_(556307, "tree", lambda: tree), "pack"), expand=_n_(556309, "YES", lambda: YES),fill=_n_(556310, "BOTH", lambda: BOTH))
_l_(556312)
path = '.'
_l_(556313)
_c_(556317, _a_(556315, _n_(556314, "tree", lambda: tree), "heading"), '#0', text=_n_(556316, "path", lambda: path), anchor='w')
_l_(556318)
abspath = _c_(556323, _a_(556321, _a_(556320, _n_(556319, "os", lambda: os), "path"), "abspath"), _n_(556322, "path", lambda: path))
_l_(556324)
root_node = _c_(556328, _a_(556326, _n_(556325, "tree", lambda: tree), "insert"), '', 'end', text=_n_(556327, "abspath", lambda: abspath), open=True)
_l_(556329)
_c_(556333, _n_(556330, "process_directory", lambda: process_directory), _n_(556331, "root_node", lambda: root_node), _n_(556332, "abspath", lambda: abspath))
_l_(556334)

_c_(556340, _a_(556336, _n_(556335, "tree", lambda: tree), "bind"), "<<TreeviewSelect>>",lambda event=None:_c_(556339, _n_(556337, "Open_file_from_list_box", lambda: Open_file_from_list_box), _n_(556338, "path", lambda: path)))
_l_(556341)
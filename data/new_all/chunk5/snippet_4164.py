# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62135331/python-typeerror-cant-pickle-module-objects-multiprocessing-on-jupyter-notebo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(648168, _n_(648167, "open", lambda: open), 'file', 'r') as o:
    _l_(648178)

    vis_reader = _c_(648172, _a_(648170, _n_(648169, "csv", lambda: csv), "reader"), _n_(648171, "o", lambda: o),delimiter='|')
    _l_(648173)
    vis_items = _c_(648176, _n_(648174, "list", lambda: list), _n_(648175, "vis_reader", lambda: vis_reader))
    _l_(648177)

vis_data = _c_(648182, _a_(648180, _n_(648179, "pd", lambda: pd), "DataFrame"), _n_(648181, "vis_items", lambda: vis_items)) 
_l_(648183) 
all_other_vis_item_desc = _n_(648184, "vis_data", lambda: vis_data)[1]
_l_(648185)
vis_item_size = _n_(648186, "vis_data", lambda: vis_data)[2]
_l_(648187)

choice_mappings = {_n_(648188, "choice", lambda: choice): _c_(648192, _a_(648190, _n_(648189, "utils", lambda: utils), "default_process"), _n_(648191, "choice", lambda: choice)) for choice in _n_(648193, "all_vis_item_desc", lambda: all_vis_item_desc)}
_l_(648194)

def find_match(x):
    _l_(648291)

    match_description = _c_(648204, _a_(648196, _n_(648195, "process", lambda: process), "extractOne"), _c_(648200, _a_(648198, _n_(648197, "utils", lambda: utils), "default_process"), _n_(648199, "x", lambda: x)),
                                    _n_(648201, "choice_mappings", lambda: choice_mappings),
                                    processor=None,
                                    scorer=_a_(648203, _n_(648202, "fuzz", lambda: fuzz), "token_sort_ratio"),
                                    score_cutoff=65)
    _l_(648205)
    #check if the size match or no
    if _n_(648206, "match_description", lambda: match_description):
        _l_(648288)

        #check if the size match 
        eby_item_size = _c_(648210, _a_(648208, _n_(648207, "re", lambda: re), "sub"), r'(?<=\d)Z\b', r' oz ',_n_(648209, "x", lambda: x))
        _l_(648211)
        eby_item_size = _c_(648215, _a_(648213, _n_(648212, "re", lambda: re), "sub"), r'/(?=\d)', r' ct ',_n_(648214, "eby_item_size", lambda: eby_item_size))
        _l_(648216)
        eby_item_size = {_c_(648221, _a_(648220, _c_(648219, _a_(648218, _n_(648217, "x", lambda: x)[0], "replace"), " ", ""), "lower")) for x in _c_(648225, _n_(648222, "findall", lambda: findall), _n_(648223, "regex_size", lambda: regex_size), _n_(648224, "eby_item_size", lambda: eby_item_size))}
        _l_(648226)
        vis_item_desc = _n_(648227, "match_description", lambda: match_description)[0]
        _l_(648228)
        vis_item_size = _n_(648229, "vis_items", lambda: vis_items)[_c_(648233, _a_(648231, _n_(648230, "all_vis_item_desc", lambda: all_vis_item_desc), "index"), _n_(648232, "vis_item_desc", lambda: vis_item_desc))]
        _l_(648234)
        vis_item_size = _n_(648235, "vis_item_size", lambda: vis_item_size)[2]
        _l_(648236)
        if(_c_(648241, _a_(648240, _c_(648239, _a_(648238, _n_(648237, "vis_item_size", lambda: vis_item_size), "replace"), " ", ""), "lower")) in _n_(648242, "eby_item_size", lambda: eby_item_size)):
            _l_(648287)

            _c_(648244, _n_(648243, "print", lambda: print), "size match")
            _l_(648245)
            cross_reference_values = _n_(648246, "vis_items", lambda: vis_items)[_c_(648250, _a_(648248, _n_(648247, "all_vis_item_desc", lambda: all_vis_item_desc), "index"), _n_(648249, "vis_item_desc", lambda: vis_item_desc))]
            _l_(648251)
            _c_(648254, _n_(648252, "print", lambda: print), _n_(648253, "x", lambda: x))
            _l_(648255)
            _c_(648258, _n_(648256, "print", lambda: print), _n_(648257, "cross_reference_values", lambda: cross_reference_values))
            _l_(648259)
            message = "Decription match"
            _l_(648260)
            size_match = "size match"
            _l_(648261)
            ratio_matching = _n_(648262, "match_description", lambda: match_description)[1]
            _l_(648263)
        elif not _n_(648264, "eby_item_size", lambda: eby_item_size):
            _l_(648286)

            _c_(648266, _n_(648265, "print", lambda: print), "match")
            _l_(648267)
            cross_reference_values = _n_(648268, "vis_items", lambda: vis_items)[_c_(648272, _a_(648270, _n_(648269, "all_vis_item_desc", lambda: all_vis_item_desc), "index"), _n_(648271, "vis_item_desc", lambda: vis_item_desc))]
            _l_(648273)
            _c_(648276, _n_(648274, "print", lambda: print), _n_(648275, "x", lambda: x))
            _l_(648277)
            _c_(648280, _n_(648278, "print", lambda: print), _n_(648279, "cross_reference_values", lambda: cross_reference_values))
            _l_(648281)
            message = "Decription match"
            _l_(648282)
            size_match = "review size match"
            _l_(648283)
            ratio_matching = _n_(648284, "match_description", lambda: match_description)[1]
            _l_(648285)
    aux = _n_(648289, "match_description", lambda: match_description)
    _l_(648290)
    return aux
try:
    import numpy as np
    _l_(648293)

except ImportError:
    pass
try:
    from multiprocessing import Pool
    _l_(648295)

except ImportError:
    pass
try:
    import find_match
    _l_(648297)

except ImportError:
    pass

num_partitions = 10 #number of partitions to split dataframe
_l_(648298) #number of partitions to split dataframe
num_cores = 4 #number of cores on your machine
_l_(648299) #number of cores on your machine

def parallelize(df, func):
    _l_(648332)

    _c_(648301, _n_(648300, "print", lambda: print), "parallelizing")
    _l_(648302)
    df_split = _c_(648307, _a_(648304, _n_(648303, "np", lambda: np), "array_split"), _n_(648305, "df", lambda: df), _n_(648306, "num_partitions", lambda: num_partitions))
    _l_(648308)
    pool = _c_(648311, _n_(648309, "Pool", lambda: Pool), _n_(648310, "num_cores", lambda: num_cores))
    _l_(648312)
    df = _c_(648320, _a_(648314, _n_(648313, "pd", lambda: pd), "concat"), _c_(648319, _a_(648316, _n_(648315, "pool", lambda: pool), "map"), _n_(648317, "func", lambda: func), _n_(648318, "df_split", lambda: df_split)))
    _l_(648321)
    _c_(648324, _a_(648323, _n_(648322, "pool", lambda: pool), "close"))
    _l_(648325)
    _c_(648328, _a_(648327, _n_(648326, "pool", lambda: pool), "join"))
    _l_(648329)
    aux = _n_(648330, "df", lambda: df)
    _l_(648331)
    return aux

#read in the csv file of a list of items to pandas df
eby_data = _c_(648334, _n_(648333, "read_eby1", lambda: read_eby1))
_l_(648335)

data = _c_(648339, _n_(648336, "parallelize", lambda: parallelize), _n_(648337, "eby_data", lambda: eby_data), _n_(648338, "find_match", lambda: find_match))
_l_(648340)
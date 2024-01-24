# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62135331/python-typeerror-cant-pickle-module-objects-multiprocessing-on-jupyter-notebo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(652097, _n_(652096, "open", lambda: open), 'file', 'r') as o:
    _l_(652107)

    vis_reader = _c_(652101, _a_(652099, _n_(652098, "csv", lambda: csv), "reader"), _n_(652100, "o", lambda: o),delimiter='|')
    _l_(652102)
    vis_items = _c_(652105, _n_(652103, "list", lambda: list), _n_(652104, "vis_reader", lambda: vis_reader))
    _l_(652106)

vis_data = _c_(652111, _a_(652109, _n_(652108, "pd", lambda: pd), "DataFrame"), _n_(652110, "vis_items", lambda: vis_items)) 
_l_(652112) 
all_other_vis_item_desc = _n_(652113, "vis_data", lambda: vis_data)[1]
_l_(652114)
vis_item_size = _n_(652115, "vis_data", lambda: vis_data)[2]
_l_(652116)

choice_mappings = {_n_(652117, "choice", lambda: choice): _c_(652121, _a_(652119, _n_(652118, "utils", lambda: utils), "default_process"), _n_(652120, "choice", lambda: choice)) for choice in _n_(652122, "all_vis_item_desc", lambda: all_vis_item_desc)}
_l_(652123)

def find_match(x):
    _l_(652220)

    match_description = _c_(652133, _a_(652125, _n_(652124, "process", lambda: process), "extractOne"), _c_(652129, _a_(652127, _n_(652126, "utils", lambda: utils), "default_process"), _n_(652128, "x", lambda: x)),
                                    _n_(652130, "choice_mappings", lambda: choice_mappings),
                                    processor=None,
                                    scorer=_a_(652132, _n_(652131, "fuzz", lambda: fuzz), "token_sort_ratio"),
                                    score_cutoff=65)
    _l_(652134)
    #check if the size match or no
    if _n_(652135, "match_description", lambda: match_description):
        _l_(652217)

        #check if the size match 
        eby_item_size = _c_(652139, _a_(652137, _n_(652136, "re", lambda: re), "sub"), r'(?<=\d)Z\b', r' oz ',_n_(652138, "x", lambda: x))
        _l_(652140)
        eby_item_size = _c_(652144, _a_(652142, _n_(652141, "re", lambda: re), "sub"), r'/(?=\d)', r' ct ',_n_(652143, "eby_item_size", lambda: eby_item_size))
        _l_(652145)
        eby_item_size = {_c_(652150, _a_(652149, _c_(652148, _a_(652147, _n_(652146, "x", lambda: x)[0], "replace"), " ", ""), "lower")) for x in _c_(652154, _n_(652151, "findall", lambda: findall), _n_(652152, "regex_size", lambda: regex_size), _n_(652153, "eby_item_size", lambda: eby_item_size))}
        _l_(652155)
        vis_item_desc = _n_(652156, "match_description", lambda: match_description)[0]
        _l_(652157)
        vis_item_size = _n_(652158, "vis_items", lambda: vis_items)[_c_(652162, _a_(652160, _n_(652159, "all_vis_item_desc", lambda: all_vis_item_desc), "index"), _n_(652161, "vis_item_desc", lambda: vis_item_desc))]
        _l_(652163)
        vis_item_size = _n_(652164, "vis_item_size", lambda: vis_item_size)[2]
        _l_(652165)
        if(_c_(652170, _a_(652169, _c_(652168, _a_(652167, _n_(652166, "vis_item_size", lambda: vis_item_size), "replace"), " ", ""), "lower")) in _n_(652171, "eby_item_size", lambda: eby_item_size)):
            _l_(652216)

            _c_(652173, _n_(652172, "print", lambda: print), "size match")
            _l_(652174)
            cross_reference_values = _n_(652175, "vis_items", lambda: vis_items)[_c_(652179, _a_(652177, _n_(652176, "all_vis_item_desc", lambda: all_vis_item_desc), "index"), _n_(652178, "vis_item_desc", lambda: vis_item_desc))]
            _l_(652180)
            _c_(652183, _n_(652181, "print", lambda: print), _n_(652182, "x", lambda: x))
            _l_(652184)
            _c_(652187, _n_(652185, "print", lambda: print), _n_(652186, "cross_reference_values", lambda: cross_reference_values))
            _l_(652188)
            message = "Decription match"
            _l_(652189)
            size_match = "size match"
            _l_(652190)
            ratio_matching = _n_(652191, "match_description", lambda: match_description)[1]
            _l_(652192)
        elif not _n_(652193, "eby_item_size", lambda: eby_item_size):
            _l_(652215)

            _c_(652195, _n_(652194, "print", lambda: print), "match")
            _l_(652196)
            cross_reference_values = _n_(652197, "vis_items", lambda: vis_items)[_c_(652201, _a_(652199, _n_(652198, "all_vis_item_desc", lambda: all_vis_item_desc), "index"), _n_(652200, "vis_item_desc", lambda: vis_item_desc))]
            _l_(652202)
            _c_(652205, _n_(652203, "print", lambda: print), _n_(652204, "x", lambda: x))
            _l_(652206)
            _c_(652209, _n_(652207, "print", lambda: print), _n_(652208, "cross_reference_values", lambda: cross_reference_values))
            _l_(652210)
            message = "Decription match"
            _l_(652211)
            size_match = "review size match"
            _l_(652212)
            ratio_matching = _n_(652213, "match_description", lambda: match_description)[1]
            _l_(652214)
    aux = _n_(652218, "match_description", lambda: match_description)
    _l_(652219)
    return aux
try:
    import numpy as np
    _l_(652222)

except ImportError:
    pass
try:
    from multiprocessing import Pool
    _l_(652224)

except ImportError:
    pass
try:
    import find_match
    _l_(652226)

except ImportError:
    pass

num_partitions = 10 #number of partitions to split dataframe
_l_(652227) #number of partitions to split dataframe
num_cores = 4 #number of cores on your machine
_l_(652228) #number of cores on your machine

def parallelize(df, func):
    _l_(652261)

    _c_(652230, _n_(652229, "print", lambda: print), "parallelizing")
    _l_(652231)
    df_split = _c_(652236, _a_(652233, _n_(652232, "np", lambda: np), "array_split"), _n_(652234, "df", lambda: df), _n_(652235, "num_partitions", lambda: num_partitions))
    _l_(652237)
    pool = _c_(652240, _n_(652238, "Pool", lambda: Pool), _n_(652239, "num_cores", lambda: num_cores))
    _l_(652241)
    df = _c_(652249, _a_(652243, _n_(652242, "pd", lambda: pd), "concat"), _c_(652248, _a_(652245, _n_(652244, "pool", lambda: pool), "map"), _n_(652246, "func", lambda: func), _n_(652247, "df_split", lambda: df_split)))
    _l_(652250)
    _c_(652253, _a_(652252, _n_(652251, "pool", lambda: pool), "close"))
    _l_(652254)
    _c_(652257, _a_(652256, _n_(652255, "pool", lambda: pool), "join"))
    _l_(652258)
    aux = _n_(652259, "df", lambda: df)
    _l_(652260)
    return aux

#read in the csv file of a list of items to pandas df
eby_data = _c_(652263, _n_(652262, "read_eby1", lambda: read_eby1))
_l_(652264)

data = _c_(652268, _n_(652265, "parallelize", lambda: parallelize), _n_(652266, "eby_data", lambda: eby_data), _n_(652267, "find_match", lambda: find_match))
_l_(652269)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61056708/python-beginner-typeerror-nonetype-object-is-not-iterable-how-to-solve-it
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(549808)

except ImportError:
    pass
try:
    import numpy as np
    _l_(549810)

except ImportError:
    pass
try:
    import math
    _l_(549812)

except ImportError:
    pass
try:
    import random
    _l_(549814)

except ImportError:
    pass
try:
    import re
    _l_(549816)

except ImportError:
    pass
try:
    import csv
    _l_(549818)

except ImportError:
    pass
try:
    import argparse
    _l_(549820)

except ImportError:
    pass
try:
    import sys
    _l_(549822)

except ImportError:
    pass
try:
    from lxml import etree
    _l_(549824)

except ImportError:
    pass

_c_(549831, _a_(549827, _a_(549826, _n_(549825, "sys", lambda: sys), "path"), "append"), _c_(549830, _a_(549829, _n_(549828, "os", lambda: os), "getcwd")))
_l_(549832)
try:
    from tools.clean_text import cleaner
    _l_(549834)

except ImportError:
    pass
try:
    from xlm.utils import bool_flag
    _l_(549836)

except ImportError:
    pass


def review_extractor(text, category='verbatim', do_lower=False):
    _l_(549866)

    """
    Extract review and label
    """

    tree = _c_(549842, _a_(549838, _n_(549837, "etree", lambda: etree), "fromstring"), _c_(549841, _n_(549839, "bytes", lambda: bytes), _n_(549840, "text", lambda: text), encoding='utf-8'))
    _l_(549843)
    for e in _c_(549846, _a_(549845, _n_(549844, "tree", lambda: tree), "findall"), ".//*[@fmc]"):
        _l_(549865)

        label = _c_(549849, _a_(549848, _n_(549847, "e", lambda: e), "xpath"), "./@fmc")[0]
        _l_(549850)
        for c in _c_(549853, _a_(549852, _n_(549851, "e", lambda: e), "findall"), "./part"):
            _l_(549864)

            # print value of "fmc" attribute and text of child element
            _c_(549858, _n_(549854, "print", lambda: print), _a_(549856, _n_(549855, "c", lambda: c), "text"), _n_(549857, "label", lambda: label))
            _l_(549859)
            aux = _a_(549861, _n_(549860, "c", lambda: c), "text"), _n_(549862, "label", lambda: label)
            _l_(549863)
            #print(f"{label:15}{c.text}")
            return aux


def get_review_labels(text, category='verbatim', do_lower=False):
    _l_(549881)

    """
    Input: line
    Returns cleaned review and label
    """
    review_text, label = _c_(549871, _n_(549867, "review_extractor", lambda: review_extractor), _n_(549868, "text", lambda: text), category=_n_(549869, "category", lambda: category), do_lower=_n_(549870, "do_lower", lambda: do_lower))
    _l_(549872)
    #review_text = cleaner(review_text, rm_new_lines=True)
    _c_(549876, _n_(549873, "print", lambda: print), _n_(549874, "review_text", lambda: review_text), _n_(549875, "label", lambda: label))
    _l_(549877)
    aux = _n_(549878, "review_text", lambda: review_text), _n_(549879, "label", lambda: label)
    _l_(549880)
    return aux


def main():
    _l_(550022)

    parser = _c_(549884, _a_(549883, _n_(549882, "argparse", lambda: argparse), "ArgumentParser"))
    _l_(549885)

    _c_(549889, _a_(549887, _n_(549886, "parser", lambda: parser), "add_argument"), '--indir', type=_n_(549888, "str", lambda: str), help='Path to raw data directory.')
    _l_(549890)
    _c_(549894, _a_(549892, _n_(549891, "parser", lambda: parser), "add_argument"), '--outdir', type=_n_(549893, "str", lambda: str), help='Path to processed data directory.')
    _l_(549895)
    _c_(549899, _a_(549897, _n_(549896, "parser", lambda: parser), "add_argument"), '--do_lower', type=_n_(549898, "bool_flag", lambda: bool_flag), default='False', help='True if do lower case, False otherwise.')
    _l_(549900)
    _c_(549904, _a_(549902, _n_(549901, "parser", lambda: parser), "add_argument"), '--val_ratio', type=_n_(549903, "float", lambda: float), default=0.2, help='Ratio to split data for validation.')
    _l_(549905)
    _c_(549909, _a_(549907, _n_(549906, "parser", lambda: parser), "add_argument"), '--use_hugging_face', type=_n_(549908, "bool_flag", lambda: bool_flag), default='False', help='Prepare data to run fine-tuning using \
                                                                                    Hugging Face Transformer library')
    _l_(549910)

    args = _c_(549913, _a_(549912, _n_(549911, "parser", lambda: parser), "parse_args"))
    _l_(549914)

    indir = _c_(549920, _a_(549917, _a_(549916, _n_(549915, "os", lambda: os), "path"), "expanduser"), _a_(549919, _n_(549918, "args", lambda: args), "indir"))
    _l_(549921)
    outdir = _c_(549927, _a_(549924, _a_(549923, _n_(549922, "os", lambda: os), "path"), "expanduser"), _a_(549926, _n_(549925, "args", lambda: args), "outdir"))
    _l_(549928)

    category = 'verbatim'
    _l_(549929)
    lang = 'fr'
    _l_(549930)
    val_ratio = _a_(549932, _n_(549931, "args", lambda: args), "val_ratio")
    _l_(549933)

    train_fname = 'train.tsv' if _a_(549935, _n_(549934, "args", lambda: args), "use_hugging_face") else 'train_0.tsv' 
    _l_(549936) 
    val_fname = 'dev.tsv' if _a_(549938, _n_(549937, "args", lambda: args), "use_hugging_face") else 'valid_0.tsv' 
    _l_(549939) 
    test_fname = 'test.tsv' if _a_(549941, _n_(549940, "args", lambda: args), "use_hugging_face") else 'test_0.tsv'  
    _l_(549942)  

    #for category in categories:
    #print('-'*20)
    path = _c_(549949, _a_(549945, _a_(549944, _n_(549943, "os", lambda: os), "path"), "join"), _n_(549946, "indir", lambda: indir), _n_(549947, "lang", lambda: lang), _n_(549948, "category", lambda: category))
    _l_(549950)
    splts = ['train', 'test']
    _l_(549951)

    for s in _n_(549952, "splts", lambda: splts):
        _l_(550021)

        review_texts = []
        _l_(549953)
        labels = []
        _l_(549954)
        stats = []
        _l_(549955)


        with _c_(549963, _n_(549956, "open", lambda: open), _c_(549962, _a_(549959, _a_(549958, _n_(549957, "os", lambda: os), "path"), "join"), _n_(549960, "path", lambda: path), _n_(549961, "s", lambda: s)+'.review'), 'rt', encoding='utf-8') as f_in:
            _l_(550002)

            _c_(549966, _n_(549964, "next", lambda: next), _n_(549965, "f_in", lambda: f_in))
            _l_(549967)
            text = _c_(549970, _a_(549969, _n_(549968, "f_in", lambda: f_in), "read"))
            _l_(549971)
            _c_(549974, _n_(549972, "print", lambda: print), _n_(549973, "text", lambda: text)) # to display whole file
            _l_(549975) # to display whole file


            review_text, label = _c_(549981, _n_(549976, "get_review_labels", lambda: get_review_labels), _n_(549977, "text", lambda: text), category=_n_(549978, "category", lambda: category), do_lower=_a_(549980, _n_(549979, "args", lambda: args), "do_lower"))
            _l_(549982)
            #review_text, label = review_extractor(text, category=category, do_lower=args.do_lower) 
            _c_(549986, _a_(549984, _n_(549983, "review_texts", lambda: review_texts), "append"), _n_(549985, "review_text", lambda: review_text))
            _l_(549987)
            _c_(549991, _a_(549989, _n_(549988, "labels", lambda: labels), "append"), _n_(549990, "label", lambda: label))
            _l_(549992)
            _c_(550000, _a_(549994, _n_(549993, "stats", lambda: stats), "append"), _c_(549999, _n_(549995, "len", lambda: len), _c_(549998, _a_(549997, _n_(549996, "review_text", lambda: review_text), "split"))))
            _l_(550001)



        #assert len(review_texts) == len(labels) == i


        out_path = _c_(550008, _a_(550005, _a_(550004, _n_(550003, "os", lambda: os), "path"), "join"), _n_(550006, "outdir", lambda: outdir), _n_(550007, "category", lambda: category))
        _l_(550009)
        if not _c_(550014, _a_(550012, _a_(550011, _n_(550010, "os", lambda: os), "path"), "exists"), _n_(550013, "out_path", lambda: out_path)):
            _l_(550020)

            _c_(550018, _a_(550016, _n_(550015, "os", lambda: os), "makedirs"), _n_(550017, "out_path", lambda: out_path))
            _l_(550019)




if _n_(550023, "__name__", lambda: __name__) == "__main__":
    _l_(550027)

    _c_(550025, _n_(550024, "main", lambda: main))
    _l_(550026)
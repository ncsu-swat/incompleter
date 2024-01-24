# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72380052/how-solved-python-text-processing-attributeerror-list-object-has-no-attribut
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
selct = _c_(551937, _n_(551936, "StringVar", lambda: StringVar))
_l_(551938)
categorychoosen = _c_(551943, _a_(551940, _n_(551939, "ttk", lambda: ttk), "Combobox"), _n_(551941, "top", lambda: top), width = 27, textvariable = _n_(551942, "selct", lambda: selct))
_l_(551944)
_n_(551945, "categorychoosen", lambda: categorychoosen)['values'] = (' Computer Science', 
                          ' computer engineering',
                          ' Information Technology',
                          ' artificial intelligence',
                          ' cyber security',
                          ' computer networks',
                          ' Information Security',
                          ' Management Information Systems',
                          ' Software engineering',
                          ' data analysis',
                          ' Data Science')
_l_(551946)
  
_c_(551949, _a_(551948, _n_(551947, "categorychoosen", lambda: categorychoosen), "grid"), row=1, column=2)
_l_(551950)
_c_(551953, _a_(551952, _n_(551951, "categorychoosen", lambda: categorychoosen), "current"))
_l_(551954)

s = _c_(551956, _n_(551955, "StringVar", lambda: StringVar))
_l_(551957)
choosen = _c_(551962, _a_(551959, _n_(551958, "ttk", lambda: ttk), "Combobox"), _n_(551960, "top", lambda: top), width = 27, textvariable = _n_(551961, "s", lambda: s))
_l_(551963)
_n_(551964, "choosen", lambda: choosen)['values'] = (' Computer Science', 
                          ' computer engineering',
                          ' Information Technology',
                          ' artificial intelligence',
                          ' cyber security',
                          ' computer networks',
                          ' Information Security',
                          ' Management Information Systems',
                          ' Software engineering',
                          ' data analysis',
                          ' Data Science')
_l_(551965)
  
_c_(551968, _a_(551967, _n_(551966, "choosen", lambda: choosen), "grid"), row=1, column=3)
_l_(551969)
_c_(551972, _a_(551971, _n_(551970, "choosen", lambda: choosen), "current"))
_l_(551973)

def model():
    _l_(552064)

    try:
        from sklearn.model_selection import train_test_split
        _l_(551975)

    except ImportError:
        pass
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        _l_(551977)

    except ImportError:
        pass
    try:
        from scipy.sparse import hstack
        _l_(551979)

    except ImportError:
        pass
    try:
        from sklearn.multiclass import OneVsRestClassifier
        _l_(551981)

    except ImportError:
        pass
    try:
        from sklearn.neighbors import KNeighborsClassifier
        _l_(551983)

    except ImportError:
        pass

    resume = _c_(551986, _a_(551985, _n_(551984, "pd", lambda: pd), "read_csv"), r'/Users/asma/Desktop/UpdatedResumeDataSet.csv')
    _l_(551987)

    #DATA
    x = _a_(551989, _n_(551988, "resume", lambda: resume)['Resume'], "values")
    _l_(551990)
    y = _a_(551992, _n_(551991, "resume", lambda: resume)['Category'], "values")
    _l_(551993)
    v = [[_c_(551996, _a_(551995, _n_(551994, "selct", lambda: selct), "get")),_c_(551999, _a_(551998, _n_(551997, "s", lambda: s), "get"))]]
    _l_(552000)

    #transform
    word = _c_(552002, _n_(552001, "TfidfVectorizer", lambda: TfidfVectorizer), sublinear_tf=True, stop_words='english')
    _l_(552003)
    _c_(552007, _a_(552005, _n_(552004, "word", lambda: word), "fit"), _n_(552006, "x", lambda: x))
    _l_(552008)
    wordFeatures = _c_(552012, _a_(552010, _n_(552009, "word", lambda: word), "transform"), _n_(552011, "x", lambda: x))
    _l_(552013)
    
    w = _c_(552015, _n_(552014, "TfidfVectorizer", lambda: TfidfVectorizer), sublinear_tf=True, stop_words='english')
    _l_(552016)
    _c_(552020, _a_(552018, _n_(552017, "w", lambda: w), "fit"), _n_(552019, "v", lambda: v))
    _l_(552021)
    wx = _c_(552025, _a_(552023, _n_(552022, "word", lambda: word), "transform"), _n_(552024, "v", lambda: v))
    _l_(552026)

    # to 2D Array
    _c_(552029, _a_(552028, _n_(552027, "wx", lambda: wx), "reshape"), -1, 1)
    _l_(552030)
    _c_(552033, _a_(552032, _n_(552031, "wordFeatures", lambda: wordFeatures), "reshape"), -1, 1)
    _l_(552034)
    _c_(552037, _a_(552036, _n_(552035, "x", lambda: x), "reshape"), -1, 1)
    _l_(552038)

    #KNN 
    model = _c_(552040, _n_(552039, "KNeighborsClassifier", lambda: KNeighborsClassifier), n_neighbors=5, metric= 'euclidean')
    _l_(552041)
    _c_(552046, _a_(552043, _n_(552042, "model", lambda: model), "fit"), _n_(552044, "wordFeatures", lambda: wordFeatures),_n_(552045, "y", lambda: y))
    _l_(552047)
    x_test = _n_(552048, "wx", lambda: wx)
    _l_(552049)
    y_pred = _c_(552053, _a_(552051, _n_(552050, "model", lambda: model), "predict"), [_n_(552052, "x_test", lambda: x_test)])
    _l_(552054)
    jobR = _c_(552062, _a_(552061, _c_(552060, _n_(552055, "Label", lambda: Label), _n_(552056, "top", lambda: top),text=_c_(552059, _n_(552057, "str", lambda: str), [_n_(552058, "y_pred", lambda: y_pred)]) ,bg='light gray'), "grid"), row=4,column=2)
    _l_(552063)

but= _c_(552070, _a_(552069, _c_(552068, _n_(552065, "Button", lambda: Button), _n_(552066, "top", lambda: top),text="Start",bg='gray', command=_n_(552067, "model", lambda: model)), "grid"), row=3,column=0)
_l_(552071)
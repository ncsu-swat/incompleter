# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46232832/error-typeerror-xi-should-be-a-dictionary-list-or-tuple-using-python-3-5
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
__author__ = "Armin"
_l_(563445)
try:
    import csv
    _l_(563447)

except ImportError:
    pass
try:
    import svm
    _l_(563449)

except ImportError:
    pass
try:
    from svmutil import *
    _l_(563451)

except ImportError:
    pass
try:
    import pickle
    _l_(563453)

except ImportError:
    pass
try:
    import re
    _l_(563455)

except ImportError:
    pass

learningSet = _c_(563460, _a_(563457, _n_(563456, "csv", lambda: csv), "reader"), _c_(563459, _n_(563458, "open", lambda: open), "train.csv"))
_l_(563461)

# we have 5 class so, 5 classifier (opn, agr, ext, neu, con)
Features_con = []
_l_(563462)
Features_opn = []
_l_(563463)
Features_agr = []
_l_(563464)
Features_ext = []
_l_(563465)
Features_neu = []
_l_(563466)

users = []
_l_(563467)
allFeatures = []
_l_(563468)

pattern = _c_(563473, _a_(563470, _n_(563469, "re", lambda: re), "compile"), r"(.)\1{1,}", _a_(563472, _n_(563471, "re", lambda: re), "DOTALL"))
_l_(563474)

def preProcess(status):
    _l_(563487)

    _c_(563478, _a_(563476, _n_(563475, "re", lambda: re), "sub"), '((www\.[^\s]+)|(https?://[^\s]+))', '__LINK__', _n_(563477, "status", lambda: status))
    _l_(563479)
    _c_(563483, _a_(563481, _n_(563480, "re", lambda: re), "sub"), r'\d+', '', _n_(563482, "status", lambda: status))
    _l_(563484)
    aux = _n_(563485, "status", lambda: status)
    _l_(563486)
    return aux

def FeaturesVector(status):
    _l_(563502)

    words = _c_(563490, _n_(563488, "set", lambda: set), _n_(563489, "status", lambda: status))
    _l_(563491)
    features = {}
    _l_(563492)
    for word in _n_(563493, "allFeatures", lambda: allFeatures):
        _l_(563499)

        _n_(563494, "features", lambda: features)[_n_(563495, "word", lambda: word)] = (_n_(563496, "word", lambda: word) in _n_(563497, "status", lambda: status))
        _l_(563498)
    aux = _n_(563500, "features", lambda: features)
    _l_(563501)
    return aux

def getFeatures(status):
    _l_(563526)

    fv = []
    _l_(563503)
    bagsOfWord = _c_(563506, _a_(563505, _n_(563504, "status", lambda: status), "split"))
    _l_(563507)
    for word in _n_(563508, "bagsOfWord", lambda: bagsOfWord):
        _l_(563523)

        word = _c_(563511, _a_(563510, _n_(563509, "word", lambda: word), "strip"), '...?!')
        _l_(563512)
        word = _c_(563516, _a_(563514, _n_(563513, "pattern", lambda: pattern), "sub"), r"\1\1\1", _n_(563515, "word", lambda: word))
        _l_(563517)
        _c_(563521, _a_(563519, _n_(563518, "fv", lambda: fv), "append"), _n_(563520, "word", lambda: word))
        _l_(563522)
    aux = _n_(563524, "fv", lambda: fv)
    _l_(563525)
    return aux

def save_classifier(classifier, name):
    _l_(563541)

    f = _c_(563529, _n_(563527, "open", lambda: open), _n_(563528, "name", lambda: name)+'.pickle', 'wb')
    _l_(563530)
    _c_(563535, _a_(563532, _n_(563531, "pickle", lambda: pickle), "dump"), _n_(563533, "classifier", lambda: classifier), _n_(563534, "f", lambda: f))
    _l_(563536)
    _c_(563539, _a_(563538, _n_(563537, "f", lambda: f), "close"))
    _l_(563540)

def load_classifier(name):
    _l_(563557)

    f = _c_(563544, _n_(563542, "open", lambda: open), _n_(563543, "name", lambda: name) + '.pickle', 'rb')
    _l_(563545)
    classifier = _c_(563549, _a_(563547, _n_(563546, "pickle", lambda: pickle), "load"), _n_(563548, "f", lambda: f))
    _l_(563550)
    _c_(563553, _a_(563552, _n_(563551, "f", lambda: f), "close"))
    _l_(563554)
    aux = _n_(563555, "classifier", lambda: classifier)
    _l_(563556)
    return aux

def makeDict(features, featureList):
    _l_(563608)

    sortedFeatures = _c_(563560, _n_(563558, "sorted", lambda: sorted), _n_(563559, "featureList", lambda: featureList))
    _l_(563561)
    feature_vector = []
    _l_(563562)
    labels = []
    _l_(563563)
    for t in _n_(563564, "features", lambda: features):
        _l_(563604)

        label = 0
        _l_(563565)
        Map = {}
        _l_(563566)
        for w in _n_(563567, "sortedFeatures", lambda: sortedFeatures):
            _l_(563571)

            _n_(563568, "Map", lambda: Map)[_n_(563569, "w", lambda: w)] = 0
            _l_(563570)

        words = _n_(563572, "t", lambda: t)[0]
        _l_(563573)
        c = _n_(563574, "t", lambda: t)[1]
        _l_(563575)
        for word in _n_(563576, "words", lambda: words):
            _l_(563583)

            if _n_(563577, "word", lambda: word) in _n_(563578, "Map", lambda: Map):
                _l_(563582)

                _n_(563579, "Map", lambda: Map)[_n_(563580, "word", lambda: word)] = 1
                _l_(563581)

        values = _c_(563586, _a_(563585, _n_(563584, "Map", lambda: Map), "values"))
        _l_(563587)
        _c_(563591, _a_(563589, _n_(563588, "feature_vector", lambda: feature_vector), "append"), _n_(563590, "values", lambda: values))
        _l_(563592)
        if(_n_(563593, "c", lambda: c) == 'y'):
            _l_(563598)

            label = 1
            _l_(563594)
        elif(_n_(563595, "c", lambda: c) == 'n'):
            _l_(563597)

            label = 0
            _l_(563596)
        _c_(563602, _a_(563600, _n_(563599, "labels", lambda: labels), "append"), _n_(563601, "label", lambda: label))
        _l_(563603)
    aux = {'feature_vector' : _n_(563605, "feature_vector", lambda: feature_vector), 'labels': _n_(563606, "labels", lambda: labels)}
    _l_(563607)
    return aux

def makeDictTest(features, featuresList):
    _l_(563643)

    sortedFeatures = _c_(563611, _n_(563609, "sorted", lambda: sorted), _n_(563610, "featuresList", lambda: featuresList))
    _l_(563612)
    feature_vector = []
    _l_(563613)
    for t in _n_(563614, "features", lambda: features):
        _l_(563640)

        Map = {}
        _l_(563615)
        for w in _n_(563616, "sortedFeatures", lambda: sortedFeatures):
            _l_(563620)

            _n_(563617, "Map", lambda: Map)[_n_(563618, "w", lambda: w)] = 0
            _l_(563619)

        words = _n_(563621, "t", lambda: t)
        _l_(563622)
        for word in _n_(563623, "words", lambda: words):
            _l_(563630)

            if _n_(563624, "word", lambda: word) in _n_(563625, "Map", lambda: Map):
                _l_(563629)

                _n_(563626, "Map", lambda: Map)[_n_(563627, "word", lambda: word)] = 1
                _l_(563628)

        values = _c_(563633, _a_(563632, _n_(563631, "Map", lambda: Map), "values"))
        _l_(563634)
        _c_(563638, _a_(563636, _n_(563635, "feature_vector", lambda: feature_vector), "append"), _n_(563637, "values", lambda: values))
        _l_(563639)
    aux = _n_(563641, "feature_vector", lambda: feature_vector)
    _l_(563642)

    return aux


def svm(features, allFeatures):
    _l_(563667)

    res = _c_(563647, _n_(563644, "makeDict", lambda: makeDict), _n_(563645, "features", lambda: features), _n_(563646, "allFeatures", lambda: allFeatures))
    _l_(563648)
    problem = _c_(563652, _n_(563649, "svm_problem", lambda: svm_problem), _n_(563650, "res", lambda: res)['labels'], _n_(563651, "res", lambda: res)['feature_vector'])
    _l_(563653)
    param = _c_(563655, _n_(563654, "svm_parameter", lambda: svm_parameter), '-q')
    _l_(563656)
    _n_(563657, "param", lambda: param).kernel_type = _n_(563658, "LINEAR", lambda: LINEAR)
    _l_(563659)
    classifier = _c_(563663, _n_(563660, "svm_train", lambda: svm_train), _n_(563661, "problem", lambda: problem), _n_(563662, "param", lambda: param))
    _l_(563664)
    aux = _n_(563665, "classifier", lambda: classifier)
    _l_(563666)
    return aux

def yesOrNo(resList):
    _l_(563681)

    counter = 0;
    _l_(563668)
    for i in _n_(563669, "resList", lambda: resList):
        _l_(563673)

        if _n_(563670, "i", lambda: i) == 0.0:
            _l_(563672)

            counter += 1
            _l_(563671)
    if(_n_(563674, "counter", lambda: counter) > _c_(563677, _n_(563675, "len", lambda: len), _n_(563676, "resList", lambda: resList))/2):
        _l_(563679)

        aux = 'n'
        _l_(563678)
        return aux
    aux = 'y'
    _l_(563680)
    return aux

again = True
_l_(563682)
#mess = input("Do you want to load classifier? (y/n) ")
#if(mess == 'n'):
    #again = True

if_n_(563683, "again", lambda: (again)):
    _l_(564028)

    # extracting ans saving features
    for line in _n_(563684, "learningSet", lambda: learningSet):
        _l_(563972)

        userId = _n_(563685, "line", lambda: line)[0]
        _l_(563686)
        status = _n_(563687, "line", lambda: line)[1]
        _l_(563688)
        ext = _n_(563689, "line", lambda: line)[7]
        _l_(563690)
        neu = _n_(563691, "line", lambda: line)[8]
        _l_(563692)
        agr = _n_(563693, "line", lambda: line)[9]
        _l_(563694)
        con = _n_(563695, "line", lambda: line)[10]
        _l_(563696)
        opn = _n_(563697, "line", lambda: line)[11]
        _l_(563698)
        # date
        date = _n_(563699, "line", lambda: line)[12]
        _l_(563700)

        # network features
        networkSize = _n_(563701, "line", lambda: line)[13]
        _l_(563702)
        nBetweenness = _n_(563703, "line", lambda: line)[15]
        _l_(563704)
        density = _n_(563705, "line", lambda: line)[16]
        _l_(563706)
        nBrokerage = _n_(563707, "line", lambda: line)[18]
        _l_(563708)
        transitivity = _n_(563709, "line", lambda: line)[19]
        _l_(563710)
        if _n_(563711, "userId", lambda: userId) not in _n_(563712, "users", lambda: users):
            _l_(563893)

            _c_(563716, _a_(563714, _n_(563713, "users", lambda: users), "append"), _n_(563715, "userId", lambda: userId))
            _l_(563717)
            # network size
            _c_(563722, _a_(563719, _n_(563718, "Features_con", lambda: Features_con), "append"), (_n_(563720, "networkSize", lambda: networkSize), _n_(563721, "con", lambda: con)))
            _l_(563723)
            _c_(563728, _a_(563725, _n_(563724, "Features_ext", lambda: Features_ext), "append"), (_n_(563726, "networkSize", lambda: networkSize), _n_(563727, "ext", lambda: ext)))
            _l_(563729)
            _c_(563734, _a_(563731, _n_(563730, "Features_agr", lambda: Features_agr), "append"), (_n_(563732, "networkSize", lambda: networkSize), _n_(563733, "agr", lambda: agr)))
            _l_(563735)
            _c_(563740, _a_(563737, _n_(563736, "Features_neu", lambda: Features_neu), "append"), (_n_(563738, "networkSize", lambda: networkSize), _n_(563739, "neu", lambda: neu)))
            _l_(563741)
            _c_(563746, _a_(563743, _n_(563742, "Features_opn", lambda: Features_opn), "append"), (_n_(563744, "networkSize", lambda: networkSize), _n_(563745, "opn", lambda: opn)))
            _l_(563747)
            # normal betweenness
            _c_(563752, _a_(563749, _n_(563748, "Features_con", lambda: Features_con), "append"), (_n_(563750, "nBetweenness", lambda: nBetweenness), _n_(563751, "con", lambda: con)))
            _l_(563753)
            _c_(563758, _a_(563755, _n_(563754, "Features_ext", lambda: Features_ext), "append"), (_n_(563756, "nBetweenness", lambda: nBetweenness), _n_(563757, "ext", lambda: ext)))
            _l_(563759)
            _c_(563764, _a_(563761, _n_(563760, "Features_agr", lambda: Features_agr), "append"), (_n_(563762, "nBetweenness", lambda: nBetweenness), _n_(563763, "agr", lambda: agr)))
            _l_(563765)
            _c_(563770, _a_(563767, _n_(563766, "Features_neu", lambda: Features_neu), "append"), (_n_(563768, "nBetweenness", lambda: nBetweenness), _n_(563769, "neu", lambda: neu)))
            _l_(563771)
            _c_(563776, _a_(563773, _n_(563772, "Features_opn", lambda: Features_opn), "append"), (_n_(563774, "nBetweenness", lambda: nBetweenness), _n_(563775, "opn", lambda: opn)))
            _l_(563777)
            # density
            _c_(563782, _a_(563779, _n_(563778, "Features_con", lambda: Features_con), "append"), (_n_(563780, "density", lambda: density), _n_(563781, "con", lambda: con)))
            _l_(563783)
            _c_(563788, _a_(563785, _n_(563784, "Features_ext", lambda: Features_ext), "append"), (_n_(563786, "density", lambda: density), _n_(563787, "ext", lambda: ext)))
            _l_(563789)
            _c_(563794, _a_(563791, _n_(563790, "Features_agr", lambda: Features_agr), "append"), (_n_(563792, "density", lambda: density), _n_(563793, "agr", lambda: agr)))
            _l_(563795)
            _c_(563800, _a_(563797, _n_(563796, "Features_neu", lambda: Features_neu), "append"), (_n_(563798, "density", lambda: density), _n_(563799, "neu", lambda: neu)))
            _l_(563801)
            _c_(563806, _a_(563803, _n_(563802, "Features_opn", lambda: Features_opn), "append"), (_n_(563804, "density", lambda: density), _n_(563805, "opn", lambda: opn)))
            _l_(563807)
            # normal brokerage
            _c_(563812, _a_(563809, _n_(563808, "Features_con", lambda: Features_con), "append"), (_n_(563810, "nBrokerage", lambda: nBrokerage), _n_(563811, "con", lambda: con)))
            _l_(563813)
            _c_(563818, _a_(563815, _n_(563814, "Features_ext", lambda: Features_ext), "append"), (_n_(563816, "nBrokerage", lambda: nBrokerage), _n_(563817, "ext", lambda: ext)))
            _l_(563819)
            _c_(563824, _a_(563821, _n_(563820, "Features_agr", lambda: Features_agr), "append"), (_n_(563822, "nBrokerage", lambda: nBrokerage), _n_(563823, "agr", lambda: agr)))
            _l_(563825)
            _c_(563830, _a_(563827, _n_(563826, "Features_neu", lambda: Features_neu), "append"), (_n_(563828, "nBrokerage", lambda: nBrokerage), _n_(563829, "neu", lambda: neu)))
            _l_(563831)
            _c_(563836, _a_(563833, _n_(563832, "Features_opn", lambda: Features_opn), "append"), (_n_(563834, "nBrokerage", lambda: nBrokerage), _n_(563835, "opn", lambda: opn)))
            _l_(563837)
            # transitivity
            _c_(563842, _a_(563839, _n_(563838, "Features_con", lambda: Features_con), "append"), (_n_(563840, "transitivity", lambda: transitivity), _n_(563841, "con", lambda: con)))
            _l_(563843)
            _c_(563848, _a_(563845, _n_(563844, "Features_ext", lambda: Features_ext), "append"), (_n_(563846, "transitivity", lambda: transitivity), _n_(563847, "ext", lambda: ext)))
            _l_(563849)
            _c_(563854, _a_(563851, _n_(563850, "Features_agr", lambda: Features_agr), "append"), (_n_(563852, "transitivity", lambda: transitivity), _n_(563853, "agr", lambda: agr)))
            _l_(563855)
            _c_(563860, _a_(563857, _n_(563856, "Features_neu", lambda: Features_neu), "append"), (_n_(563858, "transitivity", lambda: transitivity), _n_(563859, "neu", lambda: neu)))
            _l_(563861)
            _c_(563866, _a_(563863, _n_(563862, "Features_opn", lambda: Features_opn), "append"), (_n_(563864, "transitivity", lambda: transitivity), _n_(563865, "opn", lambda: opn)))
            _l_(563867)
            # add to all
            _c_(563871, _a_(563869, _n_(563868, "allFeatures", lambda: allFeatures), "append"), _n_(563870, "networkSize", lambda: networkSize))
            _l_(563872)
            _c_(563876, _a_(563874, _n_(563873, "allFeatures", lambda: allFeatures), "append"), _n_(563875, "nBetweenness", lambda: nBetweenness))
            _l_(563877)
            _c_(563881, _a_(563879, _n_(563878, "allFeatures", lambda: allFeatures), "append"), _n_(563880, "nBrokerage", lambda: nBrokerage))
            _l_(563882)
            _c_(563886, _a_(563884, _n_(563883, "allFeatures", lambda: allFeatures), "append"), _n_(563885, "transitivity", lambda: transitivity))
            _l_(563887)
            _c_(563891, _a_(563889, _n_(563888, "allFeatures", lambda: allFeatures), "append"), _n_(563890, "density", lambda: density))
            _l_(563892)

        # date feature
        _c_(563898, _a_(563895, _n_(563894, "Features_con", lambda: Features_con), "append"), (_n_(563896, "date", lambda: date), _n_(563897, "con", lambda: con)))
        _l_(563899)
        _c_(563904, _a_(563901, _n_(563900, "Features_neu", lambda: Features_neu), "append"), (_n_(563902, "date", lambda: date), _n_(563903, "neu", lambda: neu)))
        _l_(563905)
        _c_(563910, _a_(563907, _n_(563906, "Features_agr", lambda: Features_agr), "append"), (_n_(563908, "date", lambda: date), _n_(563909, "agr", lambda: agr)))
        _l_(563911)
        _c_(563916, _a_(563913, _n_(563912, "Features_opn", lambda: Features_opn), "append"), (_n_(563914, "date", lambda: date), _n_(563915, "opn", lambda: opn)))
        _l_(563917)
        _c_(563922, _a_(563919, _n_(563918, "Features_ext", lambda: Features_ext), "append"), (_n_(563920, "date", lambda: date), _n_(563921, "ext", lambda: ext)))
        _l_(563923)
        _c_(563927, _a_(563925, _n_(563924, "allFeatures", lambda: allFeatures), "append"), _n_(563926, "date", lambda: date))
        _l_(563928)

        # linguestic features
        status = _c_(563931, _n_(563929, "preProcess", lambda: preProcess), _n_(563930, "status", lambda: status))
        _l_(563932)
        statusFeatures = _c_(563935, _n_(563933, "getFeatures", lambda: getFeatures), _n_(563934, "status", lambda: status))
        _l_(563936)
        _c_(563940, _a_(563938, _n_(563937, "allFeatures", lambda: allFeatures), "extend"), _n_(563939, "statusFeatures", lambda: statusFeatures))
        _l_(563941)
        _c_(563946, _a_(563943, _n_(563942, "Features_con", lambda: Features_con), "append"), (_n_(563944, "statusFeatures", lambda: statusFeatures), _n_(563945, "con", lambda: con)))
        _l_(563947)
        _c_(563952, _a_(563949, _n_(563948, "Features_neu", lambda: Features_neu), "append"), (_n_(563950, "statusFeatures", lambda: statusFeatures), _n_(563951, "neu", lambda: neu)))
        _l_(563953)
        _c_(563958, _a_(563955, _n_(563954, "Features_agr", lambda: Features_agr), "append"), (_n_(563956, "statusFeatures", lambda: statusFeatures), _n_(563957, "agr", lambda: agr)))
        _l_(563959)
        _c_(563964, _a_(563961, _n_(563960, "Features_opn", lambda: Features_opn), "append"), (_n_(563962, "statusFeatures", lambda: statusFeatures), _n_(563963, "opn", lambda: opn)))
        _l_(563965)
        _c_(563970, _a_(563967, _n_(563966, "Features_ext", lambda: Features_ext), "append"), (_n_(563968, "statusFeatures", lambda: statusFeatures), _n_(563969, "ext", lambda: ext)))
        _l_(563971)
    allFeatures = _c_(563977, _n_(563973, "list", lambda: list), _c_(563976, _n_(563974, "set", lambda: set), _n_(563975, "allFeatures", lambda: allFeatures)))
    _l_(563978)


    _c_(563980, _n_(563979, "print", lambda: print), "Training classifiers...")
    _l_(563981)
    # training classifiers
    SVM_CON = _c_(563985, _n_(563982, "svm", lambda: svm), _n_(563983, "Features_con", lambda: Features_con), _n_(563984, "allFeatures", lambda: allFeatures))
    _l_(563986)
    _c_(563988, _n_(563987, "print", lambda: print), "Done 1 from 5.")
    _l_(563989)
    SVM_AGR = _c_(563993, _n_(563990, "svm", lambda: svm), _n_(563991, "Features_agr", lambda: Features_agr), _n_(563992, "allFeatures", lambda: allFeatures))
    _l_(563994)
    _c_(563996, _n_(563995, "print", lambda: print), "Done 2 from 5.")
    _l_(563997)
    SVM_NEU = _c_(564001, _n_(563998, "svm", lambda: svm), _n_(563999, "Features_neu", lambda: Features_neu), _n_(564000, "allFeatures", lambda: allFeatures))
    _l_(564002)
    _c_(564004, _n_(564003, "print", lambda: print), "Done 3 from 5.")
    _l_(564005)
    SVM_EXT = _c_(564009, _n_(564006, "svm", lambda: svm), _n_(564007, "Features_ext", lambda: Features_ext), _n_(564008, "allFeatures", lambda: allFeatures))
    _l_(564010)
    _c_(564012, _n_(564011, "print", lambda: print), "Done 4 from 5.")
    _l_(564013)
    SVM_OPN = _c_(564017, _n_(564014, "svm", lambda: svm), _n_(564015, "Features_opn", lambda: Features_opn), _n_(564016, "allFeatures", lambda: allFeatures))
    _l_(564018)
    _c_(564020, _n_(564019, "print", lambda: print), "Done 5 from 5.")
    _l_(564021)
    _c_(564023, _n_(564022, "print", lambda: print), "Training classifiers done.")
    _l_(564024)

else:
    _c_(564026, _n_(564025, "print", lambda: print), "loading classifiers ...")
    _l_(564027)



Done = False
_l_(564029)

while(not _n_(564030, "Done", lambda: Done)):
    _l_(564181)

    testIn = _c_(564032, _n_(564031, "input", lambda: input), "Status: ")
    _l_(564033)
    nB = _c_(564035, _n_(564034, "input", lambda: input), "Normal Betweenness: ")
    _l_(564036)
    nBr = _c_(564038, _n_(564037, "input", lambda: input), "Normal Brokerage: ")
    _l_(564039)
    size = _c_(564041, _n_(564040, "input", lambda: input), "Normal Network Size: ")
    _l_(564042)
    tr = _c_(564044, _n_(564043, "input", lambda: input), "Normal Transitivity: ")
    _l_(564045)
    den = _c_(564047, _n_(564046, "input", lambda: input), "Normal Density: ")
    _l_(564048)
    dt = _c_(564050, _n_(564049, "input", lambda: input), "Date :")
    _l_(564051)
    FV = _c_(564054, _n_(564052, "getFeatures", lambda: getFeatures), _n_(564053, "testIn", lambda: testIn));
    _l_(564055)
    _c_(564059, _a_(564057, _n_(564056, "FV", lambda: FV), "append"), _n_(564058, "nBr", lambda: nBr))
    _l_(564060)
    _c_(564064, _a_(564062, _n_(564061, "FV", lambda: FV), "append"), _n_(564063, "nB", lambda: nB))
    _l_(564065)
    _c_(564069, _a_(564067, _n_(564066, "FV", lambda: FV), "append"), _n_(564068, "size", lambda: size))
    _l_(564070)
    _c_(564074, _a_(564072, _n_(564071, "FV", lambda: FV), "append"), _n_(564073, "tr", lambda: tr))
    _l_(564075)
    _c_(564079, _a_(564077, _n_(564076, "FV", lambda: FV), "append"), _n_(564078, "den", lambda: den))
    _l_(564080)
    _c_(564084, _a_(564082, _n_(564081, "FV", lambda: FV), "append"), _n_(564083, "dt", lambda: dt))
    _l_(564085)
    fv = _c_(564089, _n_(564086, "makeDictTest", lambda: makeDictTest), _n_(564087, "FV", lambda: FV), _n_(564088, "allFeatures", lambda: allFeatures))
    _l_(564090)
    con_label, con_acc, con_val = _c_(564097, _n_(564091, "svm_predict", lambda: svm_predict), [0] * _c_(564094, _n_(564092, "len", lambda: len), _n_(564093, "fv", lambda: fv)),_n_(564095, "fv", lambda: fv), _n_(564096, "SVM_CON", lambda: SVM_CON))
    _l_(564098)
    ext_label, ext_acc, ext_val =  _c_(564105, _n_(564099, "svm_predict", lambda: svm_predict), [0] * _c_(564102, _n_(564100, "len", lambda: len), _n_(564101, "fv", lambda: fv)),_n_(564103, "fv", lambda: fv), _n_(564104, "SVM_EXT", lambda: SVM_EXT))
    _l_(564106)
    agr_label, agr_acc, agr_val = _c_(564113, _n_(564107, "svm_predict", lambda: svm_predict), [0] * _c_(564110, _n_(564108, "len", lambda: len), _n_(564109, "fv", lambda: fv)),_n_(564111, "fv", lambda: fv), _n_(564112, "SVM_AGR", lambda: SVM_AGR))
    _l_(564114)
    neu_label, neu_acc, neu_val = _c_(564121, _n_(564115, "svm_predict", lambda: svm_predict), [0] * _c_(564118, _n_(564116, "len", lambda: len), _n_(564117, "fv", lambda: fv)),_n_(564119, "fv", lambda: fv), _n_(564120, "SVM_NEU", lambda: SVM_NEU))
    _l_(564122)
    opn_label, opn_acc, opn_val = _c_(564129, _n_(564123, "svm_predict", lambda: svm_predict), [0] * _c_(564126, _n_(564124, "len", lambda: len), _n_(564125, "fv", lambda: fv)),_n_(564127, "fv", lambda: fv), _n_(564128, "SVM_OPN", lambda: SVM_OPN))
    _l_(564130)
    _c_(564133, _n_(564131, "print", lambda: print), _n_(564132, "con_label", lambda: con_label))
    _l_(564134)
    _c_(564141, _n_(564135, "print", lambda: print), "Extraversion : " + _c_(564140, _n_(564136, "str", lambda: str), _c_(564139, _n_(564137, "yesOrNo", lambda: yesOrNo), _n_(564138, "ext_label", lambda: ext_label))))
    _l_(564142)
    _c_(564149, _n_(564143, "print", lambda: print), "Neuroticism : " + _c_(564148, _n_(564144, "str", lambda: str), _c_(564147, _n_(564145, "yesOrNo", lambda: yesOrNo), _n_(564146, "neu_label", lambda: neu_label))))
    _l_(564150)
    _c_(564157, _n_(564151, "print", lambda: print), "Agreeableness : " + _c_(564156, _n_(564152, "str", lambda: str), _c_(564155, _n_(564153, "yesOrNo", lambda: yesOrNo), _n_(564154, "agr_label", lambda: agr_label))))
    _l_(564158)
    _c_(564165, _n_(564159, "print", lambda: print), "Conscientiousness : " + _c_(564164, _n_(564160, "str", lambda: str), _c_(564163, _n_(564161, "yesOrNo", lambda: yesOrNo), _n_(564162, "con_label", lambda: con_label))))
    _l_(564166)
    _c_(564173, _n_(564167, "print", lambda: print), "Openness : " + _c_(564172, _n_(564168, "str", lambda: str), _c_(564171, _n_(564169, "yesOrNo", lambda: yesOrNo), _n_(564170, "opn_label", lambda: opn_label))))
    _l_(564174)
    mess = _c_(564176, _n_(564175, "input", lambda: input), "Do you want to countinue? (y/n) ")
    _l_(564177)
    if _n_(564178, "mess", lambda: mess) == "n":
        _l_(564180)

        Done = True
        _l_(564179)

testingSet = _c_(564186, _a_(564183, _n_(564182, "csv", lambda: csv), "reader"), _c_(564185, _n_(564184, "open", lambda: open), "test.csv"))
_l_(564187)

_c_(564189, _n_(564188, "print", lambda: print), "Evaluating ...")
_l_(564190)

tp_con = 0
_l_(564191)
tn_con = 0
_l_(564192)
fn_con = 0
_l_(564193)
fp_con = 0
_l_(564194)

tp_ext = 0
_l_(564195)
tn_ext = 0
_l_(564196)
fn_ext = 0
_l_(564197)
fp_ext = 0
_l_(564198)

tp_agr = 0
_l_(564199)
tn_agr = 0
_l_(564200)
fn_agr = 0
_l_(564201)
fp_agr = 0
_l_(564202)

tp_opn = 0
_l_(564203)
tn_opn = 0
_l_(564204)
fn_opn = 0
_l_(564205)
fp_opn = 0
_l_(564206)

tp_neu = 0
_l_(564207)
tn_neu = 0
_l_(564208)
fn_neu = 0
_l_(564209)
fp_neu = 0
_l_(564210)

for line in _n_(564211, "testingSet", lambda: testingSet):
    _l_(564405)

    testStatus = _n_(564212, "line", lambda: line)[1]
    _l_(564213)
    testExt = _n_(564214, "line", lambda: line)[7]
    _l_(564215)
    testNeu = _n_(564216, "line", lambda: line)[8]
    _l_(564217)
    testAgr = _n_(564218, "line", lambda: line)[9]
    _l_(564219)
    testCon = _n_(564220, "line", lambda: line)[10]
    _l_(564221)
    testOpn = _n_(564222, "line", lambda: line)[11]
    _l_(564223)
    testDate = _n_(564224, "line", lambda: line)[12]
    _l_(564225)
    testNetworkSize = _n_(564226, "line", lambda: line)[13]
    _l_(564227)
    testNBetweenness = _n_(564228, "line", lambda: line)[15]
    _l_(564229)
    testDensity = _n_(564230, "line", lambda: line)[16]
    _l_(564231)
    testNBrokerage = _n_(564232, "line", lambda: line)[18]
    _l_(564233)
    testTransitivity = _n_(564234, "line", lambda: line)[19]
    _l_(564235)
    FV = _c_(564238, _n_(564236, "getFeatures", lambda: getFeatures), _n_(564237, "testStatus", lambda: testStatus))
    _l_(564239)
    _c_(564243, _a_(564241, _n_(564240, "FV", lambda: FV), "append"), _n_(564242, "testNetworkSize", lambda: testNetworkSize))
    _l_(564244)
    _c_(564248, _a_(564246, _n_(564245, "FV", lambda: FV), "append"), _n_(564247, "testNBetweenness", lambda: testNBetweenness))
    _l_(564249)
    _c_(564253, _a_(564251, _n_(564250, "FV", lambda: FV), "append"), _n_(564252, "testDensity", lambda: testDensity))
    _l_(564254)
    _c_(564258, _a_(564256, _n_(564255, "FV", lambda: FV), "append"), _n_(564257, "testNBrokerage", lambda: testNBrokerage))
    _l_(564259)
    _c_(564263, _a_(564261, _n_(564260, "FV", lambda: FV), "append"), _n_(564262, "testDate", lambda: testDate))
    _l_(564264)
    _c_(564268, _a_(564266, _n_(564265, "FV", lambda: FV), "append"), _n_(564267, "testTransitivity", lambda: testTransitivity))
    _l_(564269)

    classCon = _c_(564275, _a_(564271, _n_(564270, "NBC_con", lambda: NBC_con), "classify"), _c_(564274, _n_(564272, "FeaturesVector", lambda: FeaturesVector), _n_(564273, "FV", lambda: FV)))
    _l_(564276)
    classExt = _c_(564282, _a_(564278, _n_(564277, "NBC_ext", lambda: NBC_ext), "classify"), _c_(564281, _n_(564279, "FeaturesVector", lambda: FeaturesVector), _n_(564280, "FV", lambda: FV)))
    _l_(564283)
    classAgr = _c_(564289, _a_(564285, _n_(564284, "NBC_agr", lambda: NBC_agr), "classify"), _c_(564288, _n_(564286, "FeaturesVector", lambda: FeaturesVector), _n_(564287, "FV", lambda: FV)))
    _l_(564290)
    classNeu = _c_(564296, _a_(564292, _n_(564291, "NBC_neu", lambda: NBC_neu), "classify"), _c_(564295, _n_(564293, "FeaturesVector", lambda: FeaturesVector), _n_(564294, "FV", lambda: FV)))
    _l_(564297)
    classOpn = _c_(564303, _a_(564299, _n_(564298, "NBC_opn", lambda: NBC_opn), "classify"), _c_(564302, _n_(564300, "FeaturesVector", lambda: FeaturesVector), _n_(564301, "FV", lambda: FV)))
    _l_(564304)

    if _n_(564305, "classCon", lambda: classCon) == _n_(564306, "testCon", lambda: testCon) and _n_(564307, "testCon", lambda: testCon) == 'y':
        _l_(564309)

        tp_con += 1
        _l_(564308)
    if _n_(564310, "classCon", lambda: classCon) == _n_(564311, "testCon", lambda: testCon) and _n_(564312, "testCon", lambda: testCon) == 'n':
        _l_(564314)

        tn_con += 1
        _l_(564313)
    if _n_(564315, "classCon", lambda: classCon) != _n_(564316, "testCon", lambda: testCon) and _n_(564317, "testCon", lambda: testCon) == 'y':
        _l_(564319)

        fp_con += 1
        _l_(564318)
    if _n_(564320, "classCon", lambda: classCon) != _n_(564321, "testCon", lambda: testCon) and _n_(564322, "testCon", lambda: testCon) == 'n':
        _l_(564324)

        fn_con += 1
        _l_(564323)

    if _n_(564325, "classExt", lambda: classExt) == _n_(564326, "testExt", lambda: testExt) and _n_(564327, "testExt", lambda: testExt) == 'y':
        _l_(564329)

        tp_ext += 1
        _l_(564328)
    if _n_(564330, "classExt", lambda: classExt) == _n_(564331, "testExt", lambda: testExt) and _n_(564332, "testExt", lambda: testExt) == 'n':
        _l_(564334)

        tn_ext += 1
        _l_(564333)
    if _n_(564335, "classExt", lambda: classExt) == _n_(564336, "testExt", lambda: testExt) and _n_(564337, "testExt", lambda: testExt) == 'y':
        _l_(564339)

        fp_ext += 1
        _l_(564338)
    if _n_(564340, "classExt", lambda: classExt) == _n_(564341, "testExt", lambda: testExt) and _n_(564342, "testExt", lambda: testExt) == 'n':
        _l_(564344)

        fn_ext += 1
        _l_(564343)

    if _n_(564345, "classOpn", lambda: classOpn) == _n_(564346, "testOpn", lambda: testOpn) and _n_(564347, "testOpn", lambda: testOpn) == 'y':
        _l_(564349)

        tp_opn += 1
        _l_(564348)
    if _n_(564350, "classOpn", lambda: classOpn) == _n_(564351, "testOpn", lambda: testOpn) and _n_(564352, "testOpn", lambda: testOpn) == 'n':
        _l_(564354)

        tn_opn += 1
        _l_(564353)
    if _n_(564355, "classOpn", lambda: classOpn) == _n_(564356, "testOpn", lambda: testOpn) and _n_(564357, "testOpn", lambda: testOpn) == 'y':
        _l_(564359)

        fp_opn += 1
        _l_(564358)
    if _n_(564360, "classOpn", lambda: classOpn) == _n_(564361, "testOpn", lambda: testOpn) and _n_(564362, "testOpn", lambda: testOpn) == 'n':
        _l_(564364)

        fn_opn += 1
        _l_(564363)

    if _n_(564365, "classAgr", lambda: classAgr) == _n_(564366, "testAgr", lambda: testAgr) and _n_(564367, "testAgr", lambda: testAgr) == 'y':
        _l_(564369)

        tp_agr += 1
        _l_(564368)
    if _n_(564370, "classAgr", lambda: classAgr) == _n_(564371, "testAgr", lambda: testAgr) and _n_(564372, "testAgr", lambda: testAgr) == 'n':
        _l_(564374)

        tn_agr += 1
        _l_(564373)
    if _n_(564375, "classAgr", lambda: classAgr) == _n_(564376, "testAgr", lambda: testAgr) and _n_(564377, "testAgr", lambda: testAgr) == 'y':
        _l_(564379)

        fp_agr += 1
        _l_(564378)
    if _n_(564380, "classAgr", lambda: classAgr) == _n_(564381, "testAgr", lambda: testAgr) and _n_(564382, "testAgr", lambda: testAgr) == 'n':
        _l_(564384)

        fn_agr += 1
        _l_(564383)

    if _n_(564385, "classNeu", lambda: classNeu) == _n_(564386, "testNeu", lambda: testNeu) and _n_(564387, "testNeu", lambda: testNeu) == 'y':
        _l_(564389)

        tp_neu += 1
        _l_(564388)
    if _n_(564390, "classNeu", lambda: classNeu) == _n_(564391, "testNeu", lambda: testNeu) and _n_(564392, "testNeu", lambda: testNeu) == 'n':
        _l_(564394)

        tn_neu += 1
        _l_(564393)
    if _n_(564395, "classNeu", lambda: classNeu) == _n_(564396, "testNeu", lambda: testNeu) and _n_(564397, "testNeu", lambda: testNeu) == 'y':
        _l_(564399)

        fp_neu += 1
        _l_(564398)
    if _n_(564400, "classNeu", lambda: classNeu) == _n_(564401, "testNeu", lambda: testNeu) and _n_(564402, "testNeu", lambda: testNeu) == 'n':
        _l_(564404)

        fn_neu += 1
        _l_(564403)

def precision(tp, tn, fp, fn):
    _l_(564413)

    aux = 0.5 * (_n_(564406, "tp", lambda: tp)/(_n_(564407, "tp", lambda: tp)+_n_(564408, "fp", lambda: fp)) + _n_(564409, "tn", lambda: tn)/(_n_(564410, "tn", lambda: tn)+_n_(564411, "fn", lambda: fn)))
    _l_(564412)
    return aux

def recall(tp, tn, fp, fn):
    _l_(564421)

    aux = 0.5 * (_n_(564414, "tp", lambda: tp)/(_n_(564415, "tp", lambda: tp)+_n_(564416, "fn", lambda: fn)) + _n_(564417, "tn", lambda: tn)/(_n_(564418, "tn", lambda: tn)+_n_(564419, "fp", lambda: fp)))
    _l_(564420)
    return aux

def F1(tp, tn, fp, fn):
    _l_(564441)

    pre = _c_(564427, _n_(564422, "precision", lambda: precision), _n_(564423, "tp", lambda: tp), _n_(564424, "tn", lambda: tn), _n_(564425, "fp", lambda: fp), _n_(564426, "fn", lambda: fn))
    _l_(564428)
    re = _c_(564434, _n_(564429, "recall", lambda: recall), _n_(564430, "tp", lambda: tp), _n_(564431, "tn", lambda: tn), _n_(564432, "fp", lambda: fp), _n_(564433, "fn", lambda: fn))
    _l_(564435)
    aux = 2 * (_n_(564436, "pre", lambda: pre) * _n_(564437, "re", lambda: re) / (_n_(564438, "pre", lambda: pre) + _n_(564439, "re", lambda: re)))
    _l_(564440)
    return aux


_c_(564451, _n_(564442, "print", lambda: print), "Con Pre(avg) = " + _c_(564450, _n_(564443, "str", lambda: str), _c_(564449, _n_(564444, "precision", lambda: precision), _n_(564445, "tp_con", lambda: tp_con), _n_(564446, "tn_con", lambda: tn_con), _n_(564447, "fp_con", lambda: fp_con), _n_(564448, "fn_con", lambda: fn_con))))
_l_(564452)
_c_(564462, _n_(564453, "print", lambda: print), "Con Re(avg) = " + _c_(564461, _n_(564454, "str", lambda: str), _c_(564460, _n_(564455, "recall", lambda: recall), _n_(564456, "tp_con", lambda: tp_con), _n_(564457, "tn_con", lambda: tn_con), _n_(564458, "fp_con", lambda: fp_con), _n_(564459, "fn_con", lambda: fn_con)))    )
_l_(564463)
_c_(564473, _n_(564464, "print", lambda: print), "Con F1(avg) = " + _c_(564472, _n_(564465, "str", lambda: str), _c_(564471, _n_(564466, "F1", lambda: F1), _n_(564467, "tp_con", lambda: tp_con), _n_(564468, "tn_con", lambda: tn_con), _n_(564469, "fp_con", lambda: fp_con), _n_(564470, "fn_con", lambda: fn_con)))        )
_l_(564474)
_c_(564484, _n_(564475, "print", lambda: print), "Agr Pre(avg) = " + _c_(564483, _n_(564476, "str", lambda: str), _c_(564482, _n_(564477, "precision", lambda: precision), _n_(564478, "tp_agr", lambda: tp_agr), _n_(564479, "tn_agr", lambda: tn_agr), _n_(564480, "fp_agr", lambda: fp_agr), _n_(564481, "fn_agr", lambda: fn_agr))))
_l_(564485)
_c_(564495, _n_(564486, "print", lambda: print), "Agr Re(avg) = " + _c_(564494, _n_(564487, "str", lambda: str), _c_(564493, _n_(564488, "recall", lambda: recall), _n_(564489, "tp_agr", lambda: tp_agr), _n_(564490, "tn_agr", lambda: tn_agr), _n_(564491, "fp_agr", lambda: fp_agr), _n_(564492, "fn_agr", lambda: fn_agr)))    )
_l_(564496)
_c_(564506, _n_(564497, "print", lambda: print), "Agr F1(avg) = " + _c_(564505, _n_(564498, "str", lambda: str), _c_(564504, _n_(564499, "F1", lambda: F1), _n_(564500, "tp_agr", lambda: tp_agr), _n_(564501, "tn_agr", lambda: tn_agr), _n_(564502, "fp_agr", lambda: fp_agr), _n_(564503, "fn_agr", lambda: fn_agr)))        )
_l_(564507)
_c_(564517, _n_(564508, "print", lambda: print), "Ext Pre(avg) = " + _c_(564516, _n_(564509, "str", lambda: str), _c_(564515, _n_(564510, "precision", lambda: precision), _n_(564511, "tp_ext", lambda: tp_ext), _n_(564512, "tn_ext", lambda: tn_ext), _n_(564513, "fp_ext", lambda: fp_ext), _n_(564514, "fn_ext", lambda: fn_ext))))
_l_(564518)
_c_(564528, _n_(564519, "print", lambda: print), "Ext Re(avg) = " + _c_(564527, _n_(564520, "str", lambda: str), _c_(564526, _n_(564521, "recall", lambda: recall), _n_(564522, "tp_ext", lambda: tp_ext), _n_(564523, "tn_ext", lambda: tn_ext), _n_(564524, "fp_ext", lambda: fp_ext), _n_(564525, "fn_ext", lambda: fn_ext)))    )
_l_(564529)
_c_(564539, _n_(564530, "print", lambda: print), "Ext F1(avg) = " + _c_(564538, _n_(564531, "str", lambda: str), _c_(564537, _n_(564532, "F1", lambda: F1), _n_(564533, "tp_ext", lambda: tp_ext), _n_(564534, "tn_ext", lambda: tn_ext), _n_(564535, "fp_ext", lambda: fp_ext), _n_(564536, "fn_ext", lambda: fn_ext)))        )
_l_(564540)
_c_(564550, _n_(564541, "print", lambda: print), "Neu Pre(avg) = " + _c_(564549, _n_(564542, "str", lambda: str), _c_(564548, _n_(564543, "precision", lambda: precision), _n_(564544, "tp_neu", lambda: tp_neu), _n_(564545, "tn_neu", lambda: tn_neu), _n_(564546, "fp_neu", lambda: fp_neu), _n_(564547, "fn_neu", lambda: fn_neu))))
_l_(564551)
_c_(564561, _n_(564552, "print", lambda: print), "Neu Re(avg) = " + _c_(564560, _n_(564553, "str", lambda: str), _c_(564559, _n_(564554, "recall", lambda: recall), _n_(564555, "tp_neu", lambda: tp_neu), _n_(564556, "tn_neu", lambda: tn_neu), _n_(564557, "fp_neu", lambda: fp_neu), _n_(564558, "fn_neu", lambda: fn_neu)))    )
_l_(564562)
_c_(564572, _n_(564563, "print", lambda: print), "Neu F1(avg) = " + _c_(564571, _n_(564564, "str", lambda: str), _c_(564570, _n_(564565, "F1", lambda: F1), _n_(564566, "tp_neu", lambda: tp_neu), _n_(564567, "tn_neu", lambda: tn_neu), _n_(564568, "fp_neu", lambda: fp_neu), _n_(564569, "fn_neu", lambda: fn_neu)))        )
_l_(564573)
_c_(564583, _n_(564574, "print", lambda: print), "Opn Pre(avg) = " + _c_(564582, _n_(564575, "str", lambda: str), _c_(564581, _n_(564576, "precision", lambda: precision), _n_(564577, "tp_opn", lambda: tp_opn), _n_(564578, "tn_opn", lambda: tn_opn), _n_(564579, "fp_opn", lambda: fp_opn), _n_(564580, "fn_opn", lambda: fn_opn))))
_l_(564584)
_c_(564594, _n_(564585, "print", lambda: print), "Opn Re(avg) = " + _c_(564593, _n_(564586, "str", lambda: str), _c_(564592, _n_(564587, "recall", lambda: recall), _n_(564588, "tp_opn", lambda: tp_opn), _n_(564589, "tn_opn", lambda: tn_opn), _n_(564590, "fp_opn", lambda: fp_opn), _n_(564591, "fn_opn", lambda: fn_opn)))    )
_l_(564595)
_c_(564605, _n_(564596, "print", lambda: print), "Opn F1(avg) = " + _c_(564604, _n_(564597, "str", lambda: str), _c_(564603, _n_(564598, "F1", lambda: F1), _n_(564599, "tp_opn", lambda: tp_opn), _n_(564600, "tn_opn", lambda: tn_opn), _n_(564601, "fp_opn", lambda: fp_opn), _n_(564602, "fn_opn", lambda: fn_opn)))        )
_l_(564606)
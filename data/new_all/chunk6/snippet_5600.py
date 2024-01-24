# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65100753/typeerror-supertype-obj-obj-must-be-an-instance-or-subtype-of-type-only-whe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(335641)

except ImportError:
    pass
try:
    from inspect import Parameter
    _l_(335643)

except ImportError:
    pass
def get_args(f):
    _l_(335683)

    args = _c_(335645, _n_(335644, "list", lambda: list))
    _l_(335646)
    kwargs = _c_(335648, _n_(335647, "dict", lambda: dict))
    _l_(335649)
    for param in _c_(335656, _a_(335655, _a_(335654, _c_(335653, _a_(335651, _n_(335650, "inspect", lambda: inspect), "signature"), _n_(335652, "f", lambda: f)), "parameters"), "values")):
        _l_(335679)

        if (_a_(335658, _n_(335657, "param", lambda: param), "kind") == _a_(335660, _n_(335659, "param", lambda: param), "POSITIONAL_OR_KEYWORD")):
            _l_(335678)

            if _a_(335662, _n_(335661, "param", lambda: param), "default") ==_a_(335664, _n_(335663, "Parameter", lambda: Parameter), "empty"):
                _l_(335677)

                _c_(335669, _a_(335666, _n_(335665, "args", lambda: args), "append"), _a_(335668, _n_(335667, "param", lambda: param), "name"))
                _l_(335670)
            else:
                _n_(335671, "kwargs", lambda: kwargs)[_a_(335673, _n_(335672, "param", lambda: param), "name")]= _a_(335675, _n_(335674, "param", lambda: param), "default") 
                _l_(335676) 
    aux = _n_(335680, "args", lambda: args), _n_(335681, "kwargs", lambda: kwargs) 
    _l_(335682) 
    return aux 

def  compileKwargs(dct):
    _l_(335705)

    string =""
    _l_(335684)
    poke = False
    _l_(335685)
    for k, o  in _c_(335688, _a_(335687, _n_(335686, "dct", lambda: dct), "items")):
        _l_(335702)

        if _c_(335691, _n_(335689, "type", lambda: type), _n_(335690, "o", lambda: o)) == _n_(335692, "str", lambda: str):
            _l_(335701)

            string+= _n_(335693, "k", lambda: k)+"='"+_n_(335694, "o", lambda: o)+"', "
            _l_(335695)
        else:           
            string+= _n_(335696, "k", lambda: k)+"="+_c_(335699, _n_(335697, "str", lambda: str), _n_(335698, "o", lambda: o))+", "
            _l_(335700)
    aux = _n_(335703, "string", lambda: string)
    _l_(335704)

    return aux

def  compileKwargs2(dct):
    _l_(335725)

    string =""
    _l_(335706)
    poke = False
    _l_(335707)
    for k, o  in _c_(335710, _a_(335709, _n_(335708, "dct", lambda: dct), "items")):
        _l_(335722)

        if _c_(335713, _n_(335711, "type", lambda: type), _n_(335712, "o", lambda: o)) == _n_(335714, "str", lambda: str):
            _l_(335721)

            string+= _n_(335715, "k", lambda: k)+"='"+_n_(335716, "k", lambda: k)+"', "
            _l_(335717)
        else:           
            string+= _n_(335718, "k", lambda: k)+"="+_n_(335719, "k", lambda: k)+", "
            _l_(335720)
    aux = _n_(335723, "string", lambda: string)
    _l_(335724)

    return aux

def stringArgs(liste):
    _l_(335731)

    aux = _c_(335729, _a_(335726, " ", "join"), [_n_(335727, "e", lambda: e)+"," for e in _n_(335728, "liste", lambda: liste)])
    _l_(335730)
    return aux

def compileArgs(liste1,liste2):
    _l_(335742)

    _c_(335738, _a_(335733, _n_(335732, "liste1", lambda: liste1), "extend"), [_n_(335734, "e", lambda: e) for e in _n_(335735, "liste2", lambda: liste2) if _n_(335736, "e", lambda: e) not in _n_(335737, "liste1", lambda: liste1)])
    _l_(335739)
    aux = _n_(335740, "liste1", lambda: liste1)
    _l_(335741)
    return aux

def editFuncName(actual: _n_(335743, "str", lambda: str), replace:_n_(335744, "str", lambda: str)):
    _l_(335753)

    #print('EDITFUNCNAME')
    #print(actual)
    string = _c_(335749, _a_(335746, _n_(335745, "re", lambda: re), "sub"), '(?<=def ).*?(?=\()',_n_(335747, "replace", lambda: replace), _n_(335748, "actual", lambda: actual))
    _l_(335750)
    aux = _n_(335751, "string", lambda: string)
    _l_(335752)
    #print('string', string)
    return aux
try:
    import inspect
    _l_(335755)

except ImportError:
    pass
try:
    from textwrap import dedent, indent
    _l_(335757)

except ImportError:
    pass
def processCode(code : _n_(335758, "list", lambda: list)):
    _l_(335778)

    string=""
    _l_(335759)
    #print('processcode')
    for i,e  in _c_(335762, _n_(335760, "enumerate", lambda: enumerate), _n_(335761, "code", lambda: code)):
        _l_(335775)

        #print('row', e)
        #print('dedent', e)
        if _n_(335763, "i", lambda: i) != 0:
            _l_(335774)

            string+=_c_(335768, _n_(335764, "indent", lambda: indent), _c_(335767, _n_(335765, "dedent", lambda: dedent), _n_(335766, "e", lambda: e)),'\t')
            _l_(335769)
        else :
            string+=_c_(335772, _n_(335770, "dedent", lambda: dedent), _n_(335771, "e", lambda: e))
            _l_(335773)
    aux = _n_(335776, "string", lambda: string)
    _l_(335777)
    return aux
try:
    import types
    _l_(335780)

except ImportError:
    pass
class MagicMeta(_n_(335781, "type", lambda: type)):
    _l_(335949)

    def __init__(cls, name, bases, dct):
        _l_(335948)

        #print(bases,dct)
        _c_(335786, _n_(335782, "setattr", lambda: setattr), _n_(335783, "cls", lambda: cls),'_CODE_', _c_(335785, _n_(335784, "dict", lambda: dict)))
        _l_(335787)

        #GET THE __init__ code function and its arg and kwargs
        # for the class and the inherited class
        func = _a_(335789, _n_(335788, "cls", lambda: cls), "__init__")
        _l_(335790)
        _a_(335792, _n_(335791, "cls", lambda: cls), "_CODE_")[_a_(335794, _n_(335793, "func", lambda: func), "__name__")]= _c_(335798, _a_(335796, _n_(335795, "inspect", lambda: inspect), "getsourcelines"), _n_(335797, "func", lambda: func))
        _l_(335799)
        args2 =_c_(335804, _n_(335800, "get_args", lambda: get_args), _a_(335803, _a_(335802, _n_(335801, "cls", lambda: cls), "__bases__")[0], "__init__"))
        _l_(335805)
        
        _c_(335810, _n_(335806, "setattr", lambda: setattr), _n_(335807, "cls", lambda: cls),'_ARGS_', _c_(335809, _n_(335808, "dict", lambda: dict)))
        _l_(335811)
        _a_(335813, _n_(335812, "cls", lambda: cls), "_ARGS_")[_a_(335815, _n_(335814, "func", lambda: func), "__name__")]=[_c_(335818, _n_(335816, "get_args", lambda: get_args), _n_(335817, "func", lambda: func)), _n_(335819, "args2", lambda: args2)]
        _l_(335820)

        lines = _a_(335822, _n_(335821, "cls", lambda: cls), "_CODE_")['__init__']
        _l_(335823)
        string= _n_(335824, "lines", lambda: lines)[0][0]
        _l_(335825)
        arg, kwarg = _a_(335827, _n_(335826, "cls", lambda: cls), "_ARGS_")['__init__'][0]
        _l_(335828)
        arg2, kwarg2 = _a_(335830, _n_(335829, "cls", lambda: cls), "_ARGS_")['__init__'][1]
        _l_(335831)

        comparg = _c_(335837, _n_(335832, "stringArgs", lambda: stringArgs), _c_(335836, _n_(335833, "compileArgs", lambda: compileArgs), _n_(335834, "arg", lambda: arg), _n_(335835, "arg2", lambda: arg2)))
        _l_(335838)
        #------------------------------------------------------

        #PROCESS arg and kwargs to manage it as string
        dct = {**_n_(335839, "kwarg", lambda: kwarg) ,**_n_(335840, "kwarg2", lambda: kwarg2)}
        _l_(335841)
        #print(dct)
        newargs = _n_(335842, "comparg", lambda: comparg) + _c_(335845, _n_(335843, "compileKwargs", lambda: compileKwargs), _n_(335844, "dct", lambda: dct))
        _l_(335846)
        string = _c_(335851, _a_(335848, _n_(335847, "re", lambda: re), "sub"), '(?<=\().*?(?=\))',_n_(335849, "newargs", lambda: newargs), _n_(335850, "string", lambda: string))
        _l_(335852)
        _c_(335857, _n_(335853, "print", lambda: print), _c_(335856, _n_(335854, "type", lambda: type), _n_(335855, "arg2", lambda: arg2)))
        _l_(335858)
        _c_(335861, _n_(335859, "print", lambda: print), _n_(335860, "arg2", lambda: arg2))
        _l_(335862)
        superarg =_c_(335867, _n_(335863, "stringArgs", lambda: stringArgs), [_n_(335864, "a", lambda: a) for a in _n_(335865, "arg2", lambda: arg2) if _n_(335866, "a", lambda: a) != 'self']) + _c_(335870, _n_(335868, "compileKwargs2", lambda: compileKwargs2), _n_(335869, "kwarg2", lambda: kwarg2))
        _l_(335871)
        arg =_c_(335876, _n_(335872, "stringArgs", lambda: stringArgs), [_n_(335873, "a", lambda: a) for a in _n_(335874, "arg2", lambda: arg2) if _n_(335875, "a", lambda: a) != 'self'])
        _l_(335877)
        printt = _c_(335880, _a_(335878, "print({})\n", "format"), _n_(335879, "arg", lambda: arg))
        _l_(335881)
        printtt = "print(locals())\n"
        _l_(335882)
        _c_(335885, _n_(335883, "print", lambda: print), _n_(335884, "superarg", lambda: superarg))
        _l_(335886)
        #--------------------------------------------------------

        #ADD the super().__init__ in the __init__ function
        superx = _c_(335893, _a_(335887, "super({},self).{}({})\n", "format"), _a_(335889, _n_(335888, "cls", lambda: cls), "__name__"), _a_(335891, _n_(335890, "func", lambda: func), "__name__"), _n_(335892, "superarg", lambda: superarg))
        _l_(335894)
        #superx = "super().{}({})\n".format( func.__name__, superarg)
        _c_(335897, _n_(335895, "print", lambda: print), _n_(335896, "superx", lambda: superx))
        _l_(335898)
        code = _n_(335899, "lines", lambda: lines)[0]
        _l_(335900)
        #print('LINE DEF', code[0])
        #--------------------------------------------------------

        #BUILD the code of the new __init__ function
        _n_(335901, "code", lambda: code)[0]= _c_(335904, _n_(335902, "editFuncName", lambda: editFuncName), _n_(335903, "string", lambda: string), 'tempo')
        _l_(335905)
        _c_(335909, _a_(335907, _n_(335906, "code", lambda: code), "insert"), 1, _n_(335908, "printt", lambda: printt))
        _l_(335910)
        _c_(335913, _a_(335912, _n_(335911, "code", lambda: code), "insert"), 2, "print(self, type(self))\n")
        _l_(335914)
        if _c_(335917, _n_(335915, "len", lambda: len), _n_(335916, "bases", lambda: bases))>0:
            _l_(335923)

            _c_(335921, _a_(335919, _n_(335918, "code", lambda: code), "insert"), 3, _n_(335920, "superx", lambda: superx))
            _l_(335922)
 
        _c_(335926, _n_(335924, "print", lambda: print), 'code:',_n_(335925, "code", lambda: code))
        _l_(335927)
        codestr  = _c_(335930, _n_(335928, "processCode", lambda: processCode), _n_(335929, "code", lambda: code))
        _l_(335931)
        #print('précompile', codestr)
        #--------------------------------------------------------

        #REPLACE the __init__ function code
        comp = _c_(335934, _n_(335932, "compile", lambda: compile), _n_(335933, "codestr", lambda: codestr), '<string>','exec')
        _l_(335935)
        #print(comp)
        _c_(335938, _n_(335936, "exec", lambda: exec), _n_(335937, "comp", lambda: comp))
        _l_(335939)
        _n_(335940, "cls", lambda: cls).__init__ = _c_(335946, _a_(335942, _n_(335941, "types", lambda: types), "MethodType"), _c_(335944, _n_(335943, "eval", lambda: eval), 'tempo'), _n_(335945, "cls", lambda: cls))
        _l_(335947)
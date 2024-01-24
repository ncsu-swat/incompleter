# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65100753/typeerror-supertype-obj-obj-must-be-an-instance-or-subtype-of-type-only-whe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(371295)

except ImportError:
    pass
try:
    from inspect import Parameter
    _l_(371297)

except ImportError:
    pass
def get_args(f):
    _l_(371337)

    args = _c_(371299, _n_(371298, "list", lambda: list))
    _l_(371300)
    kwargs = _c_(371302, _n_(371301, "dict", lambda: dict))
    _l_(371303)
    for param in _c_(371310, _a_(371309, _a_(371308, _c_(371307, _a_(371305, _n_(371304, "inspect", lambda: inspect), "signature"), _n_(371306, "f", lambda: f)), "parameters"), "values")):
        _l_(371333)

        if (_a_(371312, _n_(371311, "param", lambda: param), "kind") == _a_(371314, _n_(371313, "param", lambda: param), "POSITIONAL_OR_KEYWORD")):
            _l_(371332)

            if _a_(371316, _n_(371315, "param", lambda: param), "default") ==_a_(371318, _n_(371317, "Parameter", lambda: Parameter), "empty"):
                _l_(371331)

                _c_(371323, _a_(371320, _n_(371319, "args", lambda: args), "append"), _a_(371322, _n_(371321, "param", lambda: param), "name"))
                _l_(371324)
            else:
                _n_(371325, "kwargs", lambda: kwargs)[_a_(371327, _n_(371326, "param", lambda: param), "name")]= _a_(371329, _n_(371328, "param", lambda: param), "default") 
                _l_(371330) 
    aux = _n_(371334, "args", lambda: args), _n_(371335, "kwargs", lambda: kwargs) 
    _l_(371336) 
    return aux 

def  compileKwargs(dct):
    _l_(371359)

    string =""
    _l_(371338)
    poke = False
    _l_(371339)
    for k, o  in _c_(371342, _a_(371341, _n_(371340, "dct", lambda: dct), "items")):
        _l_(371356)

        if _c_(371345, _n_(371343, "type", lambda: type), _n_(371344, "o", lambda: o)) == _n_(371346, "str", lambda: str):
            _l_(371355)

            string+= _n_(371347, "k", lambda: k)+"='"+_n_(371348, "o", lambda: o)+"', "
            _l_(371349)
        else:           
            string+= _n_(371350, "k", lambda: k)+"="+_c_(371353, _n_(371351, "str", lambda: str), _n_(371352, "o", lambda: o))+", "
            _l_(371354)
    aux = _n_(371357, "string", lambda: string)
    _l_(371358)

    return aux

def  compileKwargs2(dct):
    _l_(371379)

    string =""
    _l_(371360)
    poke = False
    _l_(371361)
    for k, o  in _c_(371364, _a_(371363, _n_(371362, "dct", lambda: dct), "items")):
        _l_(371376)

        if _c_(371367, _n_(371365, "type", lambda: type), _n_(371366, "o", lambda: o)) == _n_(371368, "str", lambda: str):
            _l_(371375)

            string+= _n_(371369, "k", lambda: k)+"='"+_n_(371370, "k", lambda: k)+"', "
            _l_(371371)
        else:           
            string+= _n_(371372, "k", lambda: k)+"="+_n_(371373, "k", lambda: k)+", "
            _l_(371374)
    aux = _n_(371377, "string", lambda: string)
    _l_(371378)

    return aux

def stringArgs(liste):
    _l_(371385)

    aux = _c_(371383, _a_(371380, " ", "join"), [_n_(371381, "e", lambda: e)+"," for e in _n_(371382, "liste", lambda: liste)])
    _l_(371384)
    return aux

def compileArgs(liste1,liste2):
    _l_(371396)

    _c_(371392, _a_(371387, _n_(371386, "liste1", lambda: liste1), "extend"), [_n_(371388, "e", lambda: e) for e in _n_(371389, "liste2", lambda: liste2) if _n_(371390, "e", lambda: e) not in _n_(371391, "liste1", lambda: liste1)])
    _l_(371393)
    aux = _n_(371394, "liste1", lambda: liste1)
    _l_(371395)
    return aux

def editFuncName(actual: _n_(371397, "str", lambda: str), replace:_n_(371398, "str", lambda: str)):
    _l_(371407)

    #print('EDITFUNCNAME')
    #print(actual)
    string = _c_(371403, _a_(371400, _n_(371399, "re", lambda: re), "sub"), '(?<=def ).*?(?=\()',_n_(371401, "replace", lambda: replace), _n_(371402, "actual", lambda: actual))
    _l_(371404)
    aux = _n_(371405, "string", lambda: string)
    _l_(371406)
    #print('string', string)
    return aux
try:
    import inspect
    _l_(371409)

except ImportError:
    pass
try:
    from textwrap import dedent, indent
    _l_(371411)

except ImportError:
    pass
def processCode(code : _n_(371412, "list", lambda: list)):
    _l_(371432)

    string=""
    _l_(371413)
    #print('processcode')
    for i,e  in _c_(371416, _n_(371414, "enumerate", lambda: enumerate), _n_(371415, "code", lambda: code)):
        _l_(371429)

        #print('row', e)
        #print('dedent', e)
        if _n_(371417, "i", lambda: i) != 0:
            _l_(371428)

            string+=_c_(371422, _n_(371418, "indent", lambda: indent), _c_(371421, _n_(371419, "dedent", lambda: dedent), _n_(371420, "e", lambda: e)),'\t')
            _l_(371423)
        else :
            string+=_c_(371426, _n_(371424, "dedent", lambda: dedent), _n_(371425, "e", lambda: e))
            _l_(371427)
    aux = _n_(371430, "string", lambda: string)
    _l_(371431)
    return aux
try:
    import types
    _l_(371434)

except ImportError:
    pass
class MagicMeta(_n_(371435, "type", lambda: type)):
    _l_(371603)

    def __init__(cls, name, bases, dct):
        _l_(371602)

        #print(bases,dct)
        _c_(371440, _n_(371436, "setattr", lambda: setattr), _n_(371437, "cls", lambda: cls),'_CODE_', _c_(371439, _n_(371438, "dict", lambda: dict)))
        _l_(371441)

        #GET THE __init__ code function and its arg and kwargs
        # for the class and the inherited class
        func = _a_(371443, _n_(371442, "cls", lambda: cls), "__init__")
        _l_(371444)
        _a_(371446, _n_(371445, "cls", lambda: cls), "_CODE_")[_a_(371448, _n_(371447, "func", lambda: func), "__name__")]= _c_(371452, _a_(371450, _n_(371449, "inspect", lambda: inspect), "getsourcelines"), _n_(371451, "func", lambda: func))
        _l_(371453)
        args2 =_c_(371458, _n_(371454, "get_args", lambda: get_args), _a_(371457, _a_(371456, _n_(371455, "cls", lambda: cls), "__bases__")[0], "__init__"))
        _l_(371459)
        
        _c_(371464, _n_(371460, "setattr", lambda: setattr), _n_(371461, "cls", lambda: cls),'_ARGS_', _c_(371463, _n_(371462, "dict", lambda: dict)))
        _l_(371465)
        _a_(371467, _n_(371466, "cls", lambda: cls), "_ARGS_")[_a_(371469, _n_(371468, "func", lambda: func), "__name__")]=[_c_(371472, _n_(371470, "get_args", lambda: get_args), _n_(371471, "func", lambda: func)), _n_(371473, "args2", lambda: args2)]
        _l_(371474)

        lines = _a_(371476, _n_(371475, "cls", lambda: cls), "_CODE_")['__init__']
        _l_(371477)
        string= _n_(371478, "lines", lambda: lines)[0][0]
        _l_(371479)
        arg, kwarg = _a_(371481, _n_(371480, "cls", lambda: cls), "_ARGS_")['__init__'][0]
        _l_(371482)
        arg2, kwarg2 = _a_(371484, _n_(371483, "cls", lambda: cls), "_ARGS_")['__init__'][1]
        _l_(371485)

        comparg = _c_(371491, _n_(371486, "stringArgs", lambda: stringArgs), _c_(371490, _n_(371487, "compileArgs", lambda: compileArgs), _n_(371488, "arg", lambda: arg), _n_(371489, "arg2", lambda: arg2)))
        _l_(371492)
        #------------------------------------------------------

        #PROCESS arg and kwargs to manage it as string
        dct = {**_n_(371493, "kwarg", lambda: kwarg) ,**_n_(371494, "kwarg2", lambda: kwarg2)}
        _l_(371495)
        #print(dct)
        newargs = _n_(371496, "comparg", lambda: comparg) + _c_(371499, _n_(371497, "compileKwargs", lambda: compileKwargs), _n_(371498, "dct", lambda: dct))
        _l_(371500)
        string = _c_(371505, _a_(371502, _n_(371501, "re", lambda: re), "sub"), '(?<=\().*?(?=\))',_n_(371503, "newargs", lambda: newargs), _n_(371504, "string", lambda: string))
        _l_(371506)
        _c_(371511, _n_(371507, "print", lambda: print), _c_(371510, _n_(371508, "type", lambda: type), _n_(371509, "arg2", lambda: arg2)))
        _l_(371512)
        _c_(371515, _n_(371513, "print", lambda: print), _n_(371514, "arg2", lambda: arg2))
        _l_(371516)
        superarg =_c_(371521, _n_(371517, "stringArgs", lambda: stringArgs), [_n_(371518, "a", lambda: a) for a in _n_(371519, "arg2", lambda: arg2) if _n_(371520, "a", lambda: a) != 'self']) + _c_(371524, _n_(371522, "compileKwargs2", lambda: compileKwargs2), _n_(371523, "kwarg2", lambda: kwarg2))
        _l_(371525)
        arg =_c_(371530, _n_(371526, "stringArgs", lambda: stringArgs), [_n_(371527, "a", lambda: a) for a in _n_(371528, "arg2", lambda: arg2) if _n_(371529, "a", lambda: a) != 'self'])
        _l_(371531)
        printt = _c_(371534, _a_(371532, "print({})\n", "format"), _n_(371533, "arg", lambda: arg))
        _l_(371535)
        printtt = "print(locals())\n"
        _l_(371536)
        _c_(371539, _n_(371537, "print", lambda: print), _n_(371538, "superarg", lambda: superarg))
        _l_(371540)
        #--------------------------------------------------------

        #ADD the super().__init__ in the __init__ function
        superx = _c_(371547, _a_(371541, "super({},self).{}({})\n", "format"), _a_(371543, _n_(371542, "cls", lambda: cls), "__name__"), _a_(371545, _n_(371544, "func", lambda: func), "__name__"), _n_(371546, "superarg", lambda: superarg))
        _l_(371548)
        #superx = "super().{}({})\n".format( func.__name__, superarg)
        _c_(371551, _n_(371549, "print", lambda: print), _n_(371550, "superx", lambda: superx))
        _l_(371552)
        code = _n_(371553, "lines", lambda: lines)[0]
        _l_(371554)
        #print('LINE DEF', code[0])
        #--------------------------------------------------------

        #BUILD the code of the new __init__ function
        _n_(371555, "code", lambda: code)[0]= _c_(371558, _n_(371556, "editFuncName", lambda: editFuncName), _n_(371557, "string", lambda: string), 'tempo')
        _l_(371559)
        _c_(371563, _a_(371561, _n_(371560, "code", lambda: code), "insert"), 1, _n_(371562, "printt", lambda: printt))
        _l_(371564)
        _c_(371567, _a_(371566, _n_(371565, "code", lambda: code), "insert"), 2, "print(self, type(self))\n")
        _l_(371568)
        if _c_(371571, _n_(371569, "len", lambda: len), _n_(371570, "bases", lambda: bases))>0:
            _l_(371577)

            _c_(371575, _a_(371573, _n_(371572, "code", lambda: code), "insert"), 3, _n_(371574, "superx", lambda: superx))
            _l_(371576)
 
        _c_(371580, _n_(371578, "print", lambda: print), 'code:',_n_(371579, "code", lambda: code))
        _l_(371581)
        codestr  = _c_(371584, _n_(371582, "processCode", lambda: processCode), _n_(371583, "code", lambda: code))
        _l_(371585)
        #print('précompile', codestr)
        #--------------------------------------------------------

        #REPLACE the __init__ function code
        comp = _c_(371588, _n_(371586, "compile", lambda: compile), _n_(371587, "codestr", lambda: codestr), '<string>','exec')
        _l_(371589)
        #print(comp)
        _c_(371592, _n_(371590, "exec", lambda: exec), _n_(371591, "comp", lambda: comp))
        _l_(371593)
        _n_(371594, "cls", lambda: cls).__init__ = _c_(371600, _a_(371596, _n_(371595, "types", lambda: types), "MethodType"), _c_(371598, _n_(371597, "eval", lambda: eval), 'tempo'), _n_(371599, "cls", lambda: cls))
        _l_(371601)
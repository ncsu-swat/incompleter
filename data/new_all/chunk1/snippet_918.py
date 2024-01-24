# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39702882/glsl-parser-using-pyparsing-giving-attributeerrors
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyparsing
    _l_(417128)

except ImportError:
    pass

keywords = ("attribute const uniform varying break continue do for while"
            "if else"
            "in out inout"
            "float int void bool true false"
            "lowp mediump highp precision invariant"
            "discard return"
            "mat2 mat3 mat4"
            "vec2 vec3 vec4 ivec2 ivec3 ivec4 bvec2 bvec3 bvec4 sampler2D samplerCube"
            "struct")
_l_(417129)
reserved = ("asm"
            "class union enum typedef template this packed"
            "goto switch default"
            "inline noinline volatile public static extern external"
            "interface flat long short double half fixed unsigned superp"
            "input output"
            "hvec2 hvec3 hvec4 dvec2 dvec3 dvec4 fvec2 fvec3 fvec4 sampler1D sampler3D"
            "sampler1DShadow sampler2DShadow"
            "sampler2DRect sampler3DRect sampler2DRectShadow"
            "sizeof cast"
            "namespace using")
_l_(417130)
precision = "lowp mediump high"
_l_(417131)
storage = "const uniform attribute varying"
_l_(417132)


# Tokens
# ----------------------------------
LPAREN = _c_(417137, _a_(417136, _c_(417135, _a_(417134, _n_(417133, "pyparsing", lambda: pyparsing), "Literal"), "("), "suppress"))
_l_(417138)
RPAREN = _c_(417143, _a_(417142, _c_(417141, _a_(417140, _n_(417139, "pyparsing", lambda: pyparsing), "Literal"), ")"), "suppress"))
_l_(417144)
LBRACK = _c_(417149, _a_(417148, _c_(417147, _a_(417146, _n_(417145, "pyparsing", lambda: pyparsing), "Literal"), "["), "suppress"))
_l_(417150)
RBRACK = _c_(417155, _a_(417154, _c_(417153, _a_(417152, _n_(417151, "pyparsing", lambda: pyparsing), "Literal"), "]"), "suppress"))
_l_(417156)
LBRACE = _c_(417161, _a_(417160, _c_(417159, _a_(417158, _n_(417157, "pyparsing", lambda: pyparsing), "Literal"), "{"), "suppress"))
_l_(417162)
RBRACE = _c_(417167, _a_(417166, _c_(417165, _a_(417164, _n_(417163, "pyparsing", lambda: pyparsing), "Literal"), "}"), "suppress"))
_l_(417168)
IDENTIFIER = _c_(417175, _a_(417170, _n_(417169, "pyparsing", lambda: pyparsing), "Word"), _a_(417172, _n_(417171, "pyparsing", lambda: pyparsing), "alphas") + '_', _a_(417174, _n_(417173, "pyparsing", lambda: pyparsing), "alphanums") + '_')
_l_(417176)
TYPE = _c_(417183, _a_(417178, _n_(417177, "pyparsing", lambda: pyparsing), "Word"), _a_(417180, _n_(417179, "pyparsing", lambda: pyparsing), "alphas") + '_', _a_(417182, _n_(417181, "pyparsing", lambda: pyparsing), "alphanums") + "_")
_l_(417184)
END = _c_(417189, _a_(417188, _c_(417187, _a_(417186, _n_(417185, "pyparsing", lambda: pyparsing), "Literal"), ";"), "suppress"))
_l_(417190)
INT = _c_(417195, _a_(417192, _n_(417191, "pyparsing", lambda: pyparsing), "Word"), _a_(417194, _n_(417193, "pyparsing", lambda: pyparsing), "nums"))
_l_(417196)
FLOAT = _c_(417199, _a_(417198, _n_(417197, "pyparsing", lambda: pyparsing), "Regex"), '[+-]?(((\d+\.\d*)|(\d*\.\d+))([eE][-+]?\d+)?)|(\d*[eE][+-]?\d+)')
_l_(417200)
STORAGE = _c_(417208, _a_(417202, _n_(417201, "pyparsing", lambda: pyparsing), "Regex"), _c_(417207, _a_(417203, '|', "join"), _c_(417206, _a_(417205, _n_(417204, "storage", lambda: storage), "split"), ' ')))
_l_(417209)
PRECISION = _c_(417217, _a_(417211, _n_(417210, "pyparsing", lambda: pyparsing), "Regex"), _c_(417216, _a_(417212, '|', "join"), _c_(417215, _a_(417214, _n_(417213, "precision", lambda: precision), "split"), ' ')))
_l_(417218)
STRUCT = _c_(417223, _a_(417222, _c_(417221, _a_(417220, _n_(417219, "pyparsing", lambda: pyparsing), "Literal"), "struct"), "suppress"))
_l_(417224)


# ------------------------
def get_prototypes(code):
    _l_(417308)

    """
    Get all function declarations

    Code example
    ------------

    mediump vec3 function_1(vec4);
    vec3 function_2(float a, float b);
    """

    PARAMETER = _c_(417242, _a_(417226, _n_(417225, "pyparsing", lambda: pyparsing), "Group"), _c_(417232, _a_(417231, _c_(417230, _a_(417228, _n_(417227, "pyparsing", lambda: pyparsing), "Optional"), _n_(417229, "PRECISION", lambda: PRECISION)), "setResultsName"), "precision") +
                                _c_(417235, _a_(417234, _n_(417233, "TYPE", lambda: TYPE), "setResultsName"), "type") +
                                _c_(417241, _a_(417240, _c_(417239, _a_(417237, _n_(417236, "pyparsing", lambda: pyparsing), "Optional"), _n_(417238, "IDENTIFIER", lambda: IDENTIFIER)), "setResultsName"), "name"))
    _l_(417243)
    PARAMETERS = _c_(417249, _a_(417248, _c_(417247, _a_(417245, _n_(417244, "pyparsing", lambda: pyparsing), "delimitedList"), _n_(417246, "PARAMETER", lambda: PARAMETER)), "setResultsName"), "arg", listAllMatches=True)
    _l_(417250)
    PROTOTYPE = (_c_(417256, _a_(417255, _c_(417254, _a_(417252, _n_(417251, "pyparsing", lambda: pyparsing), "Optional"), _n_(417253, "PRECISION", lambda: PRECISION)), "setResultsName"), "precision") +
                 _c_(417259, _a_(417258, _n_(417257, "TYPE", lambda: TYPE), "setResultsName"), "type") +
                 _c_(417262, _a_(417261, _n_(417260, "IDENTIFIER", lambda: IDENTIFIER), "setResultsName"), "name") +
                 _n_(417263, "LPAREN", lambda: LPAREN) + _c_(417269, _a_(417268, _c_(417267, _a_(417265, _n_(417264, "pyparsing", lambda: pyparsing), "Optional"), _n_(417266, "PARAMETERS", lambda: PARAMETERS)), "setResultsName"), "args") + _n_(417270, "RPAREN", lambda: RPAREN) +
                 _n_(417271, "END", lambda: END))
    _l_(417272)
    _c_(417277, _a_(417274, _n_(417273, "PROTOTYPE", lambda: PROTOTYPE), "ignore"), _a_(417276, _n_(417275, "pyparsing", lambda: pyparsing), "cStyleComment"))
    _l_(417278)

    for (token, start, end) in _c_(417282, _a_(417280, _n_(417279, "PROTOTYPE", lambda: PROTOTYPE), "scanString"), _n_(417281, "code", lambda: code)):
        _l_(417307)

        _c_(417290, _n_(417283, "print", lambda: print), _a_(417285, _n_(417284, "token", lambda: token), "precision"), _a_(417287, _n_(417286, "token", lambda: token), "type"), _a_(417289, _n_(417288, "token", lambda: token), "name"), '(',)
        _l_(417291)
        for arg in _a_(417293, _n_(417292, "token", lambda: token), "args"):
            _l_(417303)

            _c_(417301, _n_(417294, "print", lambda: print), _a_(417296, _n_(417295, "arg", lambda: arg), "precision"), _a_(417298, _n_(417297, "arg", lambda: arg), "type"), _a_(417300, _n_(417299, "arg", lambda: arg), "name"), ',',)
            _l_(417302)
        _c_(417305, _n_(417304, "print", lambda: print), ')')
        _l_(417306)


# ------------------------
def get_functions(code):
    _l_(417400)

    """
    Get all function definitions

    Code example
    ------------

    mediump vec3 compute_normal(vec4);
    """

    PARAMETER = _c_(417326, _a_(417310, _n_(417309, "pyparsing", lambda: pyparsing), "Group"), _c_(417316, _a_(417315, _c_(417314, _a_(417312, _n_(417311, "pyparsing", lambda: pyparsing), "Optional"), _n_(417313, "PRECISION", lambda: PRECISION)), "setResultsName"), "precision") +
                                _c_(417319, _a_(417318, _n_(417317, "TYPE", lambda: TYPE), "setResultsName"), "type") +
                                _c_(417325, _a_(417324, _c_(417323, _a_(417321, _n_(417320, "pyparsing", lambda: pyparsing), "Optional"), _n_(417322, "IDENTIFIER", lambda: IDENTIFIER)), "setResultsName"), "name"))
    _l_(417327)
    PARAMETERS = _c_(417333, _a_(417332, _c_(417331, _a_(417329, _n_(417328, "pyparsing", lambda: pyparsing), "delimitedList"), _n_(417330, "PARAMETER", lambda: PARAMETER)), "setResultsName"), "arg", listAllMatches=True)
    _l_(417334)
    FUNCTION = (_c_(417340, _a_(417339, _c_(417338, _a_(417336, _n_(417335, "pyparsing", lambda: pyparsing), "Optional"), _n_(417337, "PRECISION", lambda: PRECISION)), "setResultsName"), "precision") +
                _c_(417343, _a_(417342, _n_(417341, "TYPE", lambda: TYPE), "setResultsName"), "type") +
                _c_(417346, _a_(417345, _n_(417344, "IDENTIFIER", lambda: IDENTIFIER), "setResultsName"), "name") +
                _n_(417347, "LPAREN", lambda: LPAREN) + _c_(417353, _a_(417352, _c_(417351, _a_(417349, _n_(417348, "pyparsing", lambda: pyparsing), "Optional"), _n_(417350, "PARAMETERS", lambda: PARAMETERS)), "setResultsName"), "args") + _n_(417354, "RPAREN", lambda: RPAREN) +
                _c_(417363, _a_(417362, _c_(417361, _a_(417358, _c_(417357, _a_(417356, _n_(417355, "pyparsing", lambda: pyparsing), "nestedExpr"), "{", "}"), "setParseAction"), _a_(417360, _n_(417359, "pyparsing", lambda: pyparsing), "originalTextFor")), "setResultsName"), "code"))
    _l_(417364)
    _c_(417369, _a_(417366, _n_(417365, "FUNCTION", lambda: FUNCTION), "ignore"), _a_(417368, _n_(417367, "pyparsing", lambda: pyparsing), "cStyleComment"))
    _l_(417370)

    for (token, start, end) in _c_(417374, _a_(417372, _n_(417371, "FUNCTION", lambda: FUNCTION), "scanString"), _n_(417373, "code", lambda: code)):
        _l_(417399)

        _c_(417382, _n_(417375, "print", lambda: print), _a_(417377, _n_(417376, "token", lambda: token), "precision"), _a_(417379, _n_(417378, "token", lambda: token), "type"), _a_(417381, _n_(417380, "token", lambda: token), "name"), '(',)
        _l_(417383)
        for arg in _a_(417385, _n_(417384, "token", lambda: token), "args"):
            _l_(417395)

            _c_(417393, _n_(417386, "print", lambda: print), _a_(417388, _n_(417387, "arg", lambda: arg), "precision"), _a_(417390, _n_(417389, "arg", lambda: arg), "type"), _a_(417392, _n_(417391, "arg", lambda: arg), "name"), ',',)
            _l_(417394)
        _c_(417397, _n_(417396, "print", lambda: print), ') { ... }')
        _l_(417398)


# ------------------------
def get_version(code):
    _l_(417420)

    """
    Get shader version (if specified)

    Code example
    ------------

    #version 120
    """

    VERSION = _c_(417408, _a_(417407, (
        _c_(417403, _a_(417402, _n_(417401, "pyparsing", lambda: pyparsing), "Literal"), "#") + _c_(417406, _a_(417405, _n_(417404, "pyparsing", lambda: pyparsing), "Keyword"), "version")), "suppress")) + _n_(417409, "INT", lambda: INT)
    _l_(417410)
    for (token, start, end) in _c_(417414, _a_(417412, _n_(417411, "VERSION", lambda: VERSION), "scanString"), _n_(417413, "code", lambda: code)):
        _l_(417417)

        version = _n_(417415, "token", lambda: token)[0]
        _l_(417416)
    aux = _n_(417418, "version", lambda: version)
    _l_(417419)
    return aux

# ------------------------


def get_declarations(code):
    _l_(417535)

    """
    Get all declarations prefixed with a storage qualifier.

    Code example
    ------------

    uniform lowp vec4 fg_color = vec4(1),
                      bg_color = vec4(vec3(0),1);
    """

    # Callable expression
    EXPRESSION = _c_(417423, _a_(417422, _n_(417421, "pyparsing", lambda: pyparsing), "Forward"))
    _l_(417424)
    ARG = _c_(417428, _a_(417426, _n_(417425, "pyparsing", lambda: pyparsing), "Group"), _n_(417427, "EXPRESSION", lambda: EXPRESSION)) | _n_(417429, "IDENTIFIER", lambda: IDENTIFIER) | _n_(417430, "FLOAT", lambda: FLOAT) | _n_(417431, "INT", lambda: INT)
    _l_(417432)
    ARGS = _c_(417436, _a_(417434, _n_(417433, "pyparsing", lambda: pyparsing), "delimitedList"), _n_(417435, "ARG", lambda: ARG))
    _l_(417437)
    _n_(417438, "EXPRESSION", lambda: EXPRESSION) << _n_(417439, "IDENTIFIER", lambda: IDENTIFIER) + \
        _c_(417448, _a_(417441, _n_(417440, "pyparsing", lambda: pyparsing), "Group"), _n_(417442, "LPAREN", lambda: LPAREN) + _c_(417446, _a_(417444, _n_(417443, "pyparsing", lambda: pyparsing), "Optional"), _n_(417445, "ARGS", lambda: ARGS)) + _n_(417447, "RPAREN", lambda: RPAREN))
    _l_(417449)

    # Value
    VALUE = _c_(417459, _a_(417456, (_n_(417450, "EXPRESSION", lambda: EXPRESSION) | _c_(417455, _a_(417452, _n_(417451, "pyparsing", lambda: pyparsing), "Word"), _a_(417454, _n_(417453, "pyparsing", lambda: pyparsing), "alphanums") + "_()+-/*")
             ), "setParseAction"), _a_(417458, _n_(417457, "pyparsing", lambda: pyparsing), "originalTextFor"))
    _l_(417460)

    # Single declaration
    VARIABLE = (_c_(417463, _a_(417462, _n_(417461, "IDENTIFIER", lambda: IDENTIFIER), "setResultsName"), "name") +
                _c_(417472, _a_(417465, _n_(417464, "pyparsing", lambda: pyparsing), "Optional"), _n_(417466, "LBRACK", lambda: LBRACK) +
                                   _c_(417470, _a_(417469, (_n_(417467, "INT", lambda: INT) | _n_(417468, "IDENTIFIER", lambda: IDENTIFIER)), "setResultsName"), "size")
                                   + _n_(417471, "RBRACK", lambda: RBRACK)) +
                _c_(417483, _a_(417474, _n_(417473, "pyparsing", lambda: pyparsing), "Optional"), _c_(417479, _a_(417478, _c_(417477, _a_(417476, _n_(417475, "pyparsing", lambda: pyparsing), "Literal"), "="), "suppress")) + _c_(417482, _a_(417481, _n_(417480, "VALUE", lambda: VALUE), "setResultsName"), "value")))
    _l_(417484)

    # Several declarations at once
    DECLARATION = (_c_(417487, _a_(417486, _n_(417485, "STORAGE", lambda: STORAGE), "setResultsName"), "storage") +
                   _c_(417493, _a_(417492, _c_(417491, _a_(417489, _n_(417488, "pyparsing", lambda: pyparsing), "Optional"), _n_(417490, "PRECISION", lambda: PRECISION)), "setResultsName"), "precision") +
                   _c_(417496, _a_(417495, _n_(417494, "TYPE", lambda: TYPE), "setResultsName"), "type") +
                   _c_(417502, _a_(417498, _n_(417497, "pyparsing", lambda: pyparsing), "delimitedList"), _c_(417501, _a_(417500, _n_(417499, "VARIABLE", lambda: VARIABLE), "setResultsName"), "variable", listAllMatches=True)) +
                   _n_(417503, "END", lambda: END))
    _l_(417504)
    _c_(417509, _a_(417506, _n_(417505, "DECLARATION", lambda: DECLARATION), "ignore"), _a_(417508, _n_(417507, "pyparsing", lambda: pyparsing), "cStyleComment"))
    _l_(417510)

    for (tokens, start, end) in _c_(417514, _a_(417512, _n_(417511, "DECLARATION", lambda: DECLARATION), "scanString"), _n_(417513, "code", lambda: code)):
        _l_(417534)

        for token in _a_(417516, _n_(417515, "tokens", lambda: tokens), "variable"):
            _l_(417533)

            _c_(417524, _n_(417517, "print", lambda: print), _a_(417519, _n_(417518, "tokens", lambda: tokens), "storage"), _a_(417521, _n_(417520, "tokens", lambda: tokens), "precision"), _a_(417523, _n_(417522, "tokens", lambda: tokens), "type"),)
            _l_(417525)
            _c_(417531, _n_(417526, "print", lambda: print), _a_(417528, _n_(417527, "token", lambda: token), "name"), _a_(417530, _n_(417529, "token", lambda: token), "size"))
            _l_(417532)


# ------------------------
def get_definitions(code):
    _l_(417607)

    """
    Get all structure definitions and associated declarations.

    Code example
    ------------

    uniform struct Light {
        vec4 position;
        vec3 color;
    } light0, light1;
    """

    # Single declaration
    DECLARATION = _c_(417550, _a_(417537, _n_(417536, "pyparsing", lambda: pyparsing), "Group"), _c_(417540, _a_(417539, _n_(417538, "IDENTIFIER", lambda: IDENTIFIER), "setResultsName"), "name") +
                                  _c_(417549, _a_(417542, _n_(417541, "pyparsing", lambda: pyparsing), "Optional"), _n_(417543, "LBRACK", lambda: LBRACK) +
                                                     _c_(417547, _a_(417546, (_n_(417544, "INT", lambda: INT) | _n_(417545, "IDENTIFIER", lambda: IDENTIFIER)), "setResultsName"), "size") +
                                                     _n_(417548, "RBRACK", lambda: RBRACK)))
    _l_(417551)
    # Several declarations at once
    DECLARATIONS = (_c_(417555, _a_(417553, _n_(417552, "pyparsing", lambda: pyparsing), "Optional"), _n_(417554, "PRECISION", lambda: PRECISION)) +
                    _n_(417556, "TYPE", lambda: TYPE) +
                    _c_(417560, _a_(417558, _n_(417557, "pyparsing", lambda: pyparsing), "delimitedList"), _n_(417559, "DECLARATION", lambda: DECLARATION)) +
                    _n_(417561, "END", lambda: END))
    _l_(417562)

    # Definition + declarations
    DEFINITION = (_n_(417563, "STRUCT", lambda: STRUCT) +
                  _c_(417566, _a_(417565, _n_(417564, "IDENTIFIER", lambda: IDENTIFIER), "setResultsName"), "name") +
                  _n_(417567, "LBRACE", lambda: LBRACE) + _c_(417573, _a_(417572, _c_(417571, _a_(417569, _n_(417568, "pyparsing", lambda: pyparsing), "OneOrMore"), _n_(417570, "DECLARATIONS", lambda: DECLARATIONS)), "setResultsName"), 'content') + _n_(417574, "RBRACE", lambda: RBRACE) +
                  _c_(417583, _a_(417576, _n_(417575, "pyparsing", lambda: pyparsing), "Optional"), _c_(417582, _a_(417578, _n_(417577, "pyparsing", lambda: pyparsing), "delimitedList"), _c_(417581, _a_(417580, _n_(417579, "DECLARATION", lambda: DECLARATION), "setResultsName"), "declarations", listAllMatches=True))) +
                  _n_(417584, "END", lambda: END))
    _l_(417585)
    _c_(417590, _a_(417587, _n_(417586, "DEFINITION", lambda: DEFINITION), "ignore"), _a_(417589, _n_(417588, "pyparsing", lambda: pyparsing), "cStyleComment"))
    _l_(417591)

    for (tokens, start, end) in _c_(417595, _a_(417593, _n_(417592, "DEFINITION", lambda: DEFINITION), "scanString"), _n_(417594, "code", lambda: code)):
        _l_(417606)

        for token in _a_(417597, _n_(417596, "tokens", lambda: tokens), "declarations"):
            _l_(417605)

            _c_(417603, _n_(417598, "print", lambda: print), _a_(417600, _n_(417599, "tokens", lambda: tokens), "name"), _a_(417602, _n_(417601, "token", lambda: token), "name"))
            _l_(417604)


# ----------------
def resolve(code):
    _l_(417751)

    """
    Expand const and preprocessor definitions in order to get constant values.

    Return the transformed code
    """

    constants = {}
    _l_(417608)

    DEFINITION = (_c_(417611, _a_(417610, _n_(417609, "pyparsing", lambda: pyparsing), "Literal"), "#") + _c_(417614, _a_(417613, _n_(417612, "pyparsing", lambda: pyparsing), "Literal"), "define") +
                  _c_(417617, _a_(417616, _n_(417615, "IDENTIFIER", lambda: IDENTIFIER), "setResultsName"), "name") +
                  _c_(417621, _a_(417620, _a_(417619, _n_(417618, "pyparsing", lambda: pyparsing), "restOfLine"), "setResultsName"), "value"))
    _l_(417622)

    VALUE = _c_(417627, _a_(417624, _n_(417623, "pyparsing", lambda: pyparsing), "Word"), _a_(417626, _n_(417625, "pyparsing", lambda: pyparsing), "alphanums") + "_()+-/*")
    _l_(417628)
    DECLARATION = (_c_(417631, _a_(417630, _n_(417629, "pyparsing", lambda: pyparsing), "Literal"), "const") +
                   _c_(417634, _a_(417633, _n_(417632, "TYPE", lambda: TYPE), "setResultsName"), "type") +
                   _c_(417637, _a_(417636, _n_(417635, "IDENTIFIER", lambda: IDENTIFIER), "setResultsName"), "name") +
                   _c_(417640, _a_(417639, _n_(417638, "pyparsing", lambda: pyparsing), "Literal"), "=") +
                   _c_(417643, _a_(417642, _n_(417641, "VALUE", lambda: VALUE), "setResultsName"), "value") +
                   _c_(417646, _a_(417645, _n_(417644, "pyparsing", lambda: pyparsing), "Literal"), ";"))
    _l_(417647)
    REFERENCE = _c_(417650, _a_(417649, _n_(417648, "pyparsing", lambda: pyparsing), "Forward"))
    _l_(417651)

    def process_definition(s, l, t):
        _l_(417679)

        value = _c_(417656, _a_(417653, _n_(417652, "REFERENCE", lambda: REFERENCE), "transformString"), _a_(417655, _n_(417654, "t", lambda: t), "value"))
        _l_(417657)
        _n_(417658, "constants", lambda: constants)[_a_(417660, _n_(417659, "t", lambda: t), "name")] = _n_(417661, "value", lambda: value)
        _l_(417662)
        _n_(417663, "REFERENCE", lambda: REFERENCE) << _c_(417673, _a_(417665, _n_(417664, "pyparsing", lambda: pyparsing), "MatchFirst"), _c_(417672, _n_(417666, "map", lambda: map), _a_(417668, _n_(417667, "pyparsing", lambda: pyparsing), "Keyword"), _c_(417671, _a_(417670, _n_(417669, "constants", lambda: constants), "keys"))))
        _l_(417674)
        aux = "#define " + _a_(417676, _n_(417675, "t", lambda: t), "name") + " " + _n_(417677, "value", lambda: value)
        _l_(417678)
        return aux

    def process_declaration(s, l, t):
        _l_(417709)

        value = _c_(417684, _a_(417681, _n_(417680, "REFERENCE", lambda: REFERENCE), "transformString"), _a_(417683, _n_(417682, "t", lambda: t), "value"))
        _l_(417685)
        _n_(417686, "constants", lambda: constants)[_a_(417688, _n_(417687, "t", lambda: t), "name")] = _n_(417689, "value", lambda: value)
        _l_(417690)
        _n_(417691, "REFERENCE", lambda: REFERENCE) << _c_(417701, _a_(417693, _n_(417692, "pyparsing", lambda: pyparsing), "MatchFirst"), _c_(417700, _n_(417694, "map", lambda: map), _a_(417696, _n_(417695, "pyparsing", lambda: pyparsing), "Keyword"), _c_(417699, _a_(417698, _n_(417697, "constants", lambda: constants), "keys"))))
        _l_(417702)
        aux = "const " + _a_(417704, _n_(417703, "t", lambda: t), "type") + " " + _a_(417706, _n_(417705, "t", lambda: t), "name") + "=" + _n_(417707, "value", lambda: value) + ";"
        _l_(417708)
        return aux

    def process_reference(s, l, t):
        _l_(417713)

        aux = _n_(417710, "constants", lambda: constants)[_n_(417711, "t", lambda: t)[0]]
        _l_(417712)
        return aux

    _c_(417717, _a_(417715, _n_(417714, "REFERENCE", lambda: REFERENCE), "setParseAction"), _n_(417716, "process_reference", lambda: process_reference))
    _l_(417718)
    _c_(417722, _a_(417720, _n_(417719, "DEFINITION", lambda: DEFINITION), "setParseAction"), _n_(417721, "process_definition", lambda: process_definition))
    _l_(417723)
    _c_(417727, _a_(417725, _n_(417724, "DECLARATION", lambda: DECLARATION), "setParseAction"), _n_(417726, "process_declaration", lambda: process_declaration))
    _l_(417728)
    EXPANDER = _n_(417729, "REFERENCE", lambda: REFERENCE) | _n_(417730, "DEFINITION", lambda: DEFINITION) | _n_(417731, "DECLARATION", lambda: DECLARATION)
    _l_(417732)

    code = _c_(417736, _a_(417734, _n_(417733, "EXPANDER", lambda: EXPANDER), "transformString"), _n_(417735, "code", lambda: code))
    _l_(417737)
    for key, val in _c_(417740, _a_(417739, _n_(417738, "constants", lambda: constants), "items")):
        _l_(417747)

        _n_(417741, "constants", lambda: constants)[_n_(417742, "key", lambda: key)] = _c_(417745, _n_(417743, "eval", lambda: eval), _n_(417744, "val", lambda: val))
        _l_(417746)
    aux = _n_(417748, "code", lambda: code), _n_(417749, "constants", lambda: constants)
    _l_(417750)

    return aux


# -----------------------------------------------------------------------------
if _n_(417752, "__name__", lambda: __name__) == '__main__':
    _l_(417754)


    code = """
#version 120

#define A (1)
const int B=(A+2);
#define C (B+3)
const int D=C+4;

uniform float array[D];

struct Point {
    vec4 position;
    float size;
};

uniform struct Light {
    vec4 position;
    vec3 color;
} light0, light1;

const float PI = 3.14159265358979323846264;
const float SQRT_2 = 1.4142135623730951;

uniform vec4 fg_color = vec4(1),
             bg_color = vec4(vec3(0),1);

mediump vec3 compute_normal(vec4 position, vec3 orientation);
vec3 /* */ compute_light(vec4, vec3, float intensity)
{
   vec3 hello;
   vec3 hello;
}

"""
    _l_(417753)
code, _ = _c_(417757, _n_(417755, "resolve", lambda: resolve), _n_(417756, "code", lambda: code))
_l_(417758)
_c_(417763, _n_(417759, "print", lambda: print), "GLSL version: %s\n" % _c_(417762, _n_(417760, "get_version", lambda: get_version), _n_(417761, "code", lambda: code)))
_l_(417764)

_c_(417767, _n_(417765, "get_definitions", lambda: get_definitions), _n_(417766, "code", lambda: code))
_l_(417768)
_c_(417771, _n_(417769, "get_declarations", lambda: get_declarations), _n_(417770, "code", lambda: code))
_l_(417772)
_c_(417775, _n_(417773, "get_prototypes", lambda: get_prototypes), _n_(417774, "code", lambda: code))
_l_(417776)
_c_(417779, _n_(417777, "get_functions", lambda: get_functions), _n_(417778, "code", lambda: code))
_l_(417780)

# code = """
# #if A
# #if B
# #if C
# #endif
# #endif
# #endif
# """

# IF = (pyparsing.Literal('#') + (pyparsing.Keyword('if') | pyparsing.Keyword('ifdef') | pyparsing.Keyword('ifndef')))
# ENDIF = (pyparsing.Literal('#') + pyparsing.Keyword('endif'))
# MACRO = (IF + pyparsing.restOfLine() +
#          SkipTo(ENDIF, include=True)).setParseAction(pyparsing.originalTextFor)
# for (tokens, start, end) in MACRO.scanString(code):
#     print tokens
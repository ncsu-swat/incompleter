# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/21367320/searching-for-equivalent-of-filenotfounderror-in-python-2
#!/usr/bin/python
#-*-coding:utf-8*

#option_controller.py

#Walle Cyril
#25/01/2014

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(377030)

except ImportError:
    pass
try:
    import os
    _l_(377032)

except ImportError:
    pass

class Options():
    _l_(377198)

    """Options is a class designed to read, add and change informations in a JSON file with a dictionnary in it.

    The entire object works even if the file is missing since it re-creates it.
    If present it must respect the JSON format: e.g. keys must be strings and so on.
    If something corrupted the file, just destroy the file or call read_file method to remake it."""

    def __init__(self,directory_name="Cache",file_name="options.json",imported_default_values=None):
        _l_(377056)

        #json file
        _n_(377033, "self", lambda: self).option_file_path=_c_(377039, _a_(377036, _a_(377035, _n_(377034, "os", lambda: os), "path"), "join"), _n_(377037, "directory_name", lambda: directory_name),_n_(377038, "file_name", lambda: file_name))
        _l_(377040)
        _n_(377041, "self", lambda: self).directory_name=_n_(377042, "directory_name", lambda: directory_name)
        _l_(377043)
        _n_(377044, "self", lambda: self).file_name=_n_(377045, "file_name", lambda: file_name)
        _l_(377046)
        #self.parameters_json_file={'sort_keys':True, 'indent':4, 'separators':(',',':')}
        #the default data
        if _n_(377047, "imported_default_values", lambda: imported_default_values) is None:
            _l_(377055)

            DEFAULT_INDENT = 2
            _l_(377048)
            _n_(377049, "self", lambda: self).default_values={\
                "translate_html_level": 1,\
                "indent_size":_n_(377050, "DEFAULT_INDENT", lambda: DEFAULT_INDENT),\
                "document_title":"Titre"}
            _l_(377051)
        else:
            _n_(377052, "self", lambda: self).default_values=_n_(377053, "imported_default_values", lambda: imported_default_values)
            _l_(377054)


    def read_file(self,read_this_key_only=False):
        _l_(377132)

        """returns the value for the given key or a dictionary if the key is not given.

        returns None if it s impossible"""
        try:
            _l_(377067)

            text_in_file=_c_(377062, _a_(377061, _c_(377060, _n_(377057, "open", lambda: open), _a_(377059, _n_(377058, "self", lambda: self), "option_file_path"),'r'), "read"))
            _l_(377063)
        except _n_(377064, "FileNotFoundError", lambda: FileNotFoundError):
            _l_(377066)

            text_in_file=""#if the file is not there we re-make one with default values
            _l_(377065)#if the file is not there we re-make one with default values
        if _n_(377068, "text_in_file", lambda: text_in_file)=="":
            _l_(377080)

            _c_(377071, _a_(377070, _n_(377069, "self", lambda: self), "__insert_all_default_values"))
            _l_(377072)
            text_in_file=_c_(377078, _a_(377077, _c_(377076, _n_(377073, "open", lambda: open), _a_(377075, _n_(377074, "self", lambda: self), "option_file_path"),'r'), "read"))
            _l_(377079)

        try:
            _l_(377104)

            option_dict=_c_(377084, _a_(377082, _n_(377081, "json", lambda: json), "loads"), _n_(377083, "text_in_file", lambda: text_in_file))
            _l_(377085)
        except _n_(377086, "ValueError", lambda: ValueError):
            _l_(377103)

            #if the json file is broken we re-make one with default values
            _c_(377089, _a_(377088, _n_(377087, "self", lambda: self), "__insert_all_default_values"))
            _l_(377090)
            text_in_file=_c_(377096, _a_(377095, _c_(377094, _n_(377091, "open", lambda: open), _a_(377093, _n_(377092, "self", lambda: self), "option_file_path"),'r'), "read"))
            _l_(377097)
            option_dict=_c_(377101, _a_(377099, _n_(377098, "json", lambda: json), "loads"), _n_(377100, "text_in_file", lambda: text_in_file))
            _l_(377102)

        if _n_(377105, "read_this_key_only", lambda: read_this_key_only):
            _l_(377131)

            if _n_(377106, "read_this_key_only", lambda: read_this_key_only) in _n_(377107, "option_dict", lambda: option_dict):
                _l_(377128)

                aux = _n_(377108, "option_dict", lambda: option_dict)[_n_(377109, "read_this_key_only", lambda: read_this_key_only)]#
                _l_(377110)#
                return aux#
            else:
                #if the value is not there it should be written for the next time
                if _n_(377111, "read_this_key_only", lambda: read_this_key_only) in _a_(377113, _n_(377112, "self", lambda: self), "default_values"):
                    _l_(377127)

                    _c_(377120, _a_(377115, _n_(377114, "self", lambda: self), "add_option_to_file"), _n_(377116, "read_this_key_only", lambda: read_this_key_only),_a_(377118, _n_(377117, "self", lambda: self), "default_values")[_n_(377119, "read_this_key_only", lambda: read_this_key_only)])
                    _l_(377121)
                    aux = _a_(377123, _n_(377122, "self", lambda: self), "default_values")[_n_(377124, "read_this_key_only", lambda: read_this_key_only)]
                    _l_(377125)
                    return aux
                else:
                    aux = None
                    _l_(377126)
                    #impossible because there is not default value so the value isn t meant to be here
                    return aux
        else:
            aux = _n_(377129, "option_dict", lambda: option_dict)
            _l_(377130)
            return aux

    def add_option_to_file(self,key,value):
        _l_(377156)

        """Adds or updates an option(key and value) to the json file if the option exists in the default_values of the object."""

        option_dict=_c_(377135, _a_(377134, _n_(377133, "self", lambda: self), "read_file"))
        _l_(377136)
        if _n_(377137, "key", lambda: key) in _a_(377139, _n_(377138, "self", lambda: self), "default_values"):
            _l_(377144)

            _n_(377140, "option_dict", lambda: option_dict)[_n_(377141, "key", lambda: key)]=_n_(377142, "value", lambda: value)
            _l_(377143)
        _c_(377154, _a_(377149, _c_(377148, _n_(377145, "open", lambda: open), _a_(377147, _n_(377146, "self", lambda: self), "option_file_path"),'w'), "write"), _c_(377153, _a_(377151, _n_(377150, "json", lambda: json), "dumps"), _n_(377152, "option_dict", lambda: option_dict),sort_keys=True, indent=4, separators=(',',':')))
        _l_(377155)


    def __insert_all_default_values(self):
        _l_(377197)

        """Recreate json file with default values.

    called if the document is empty or non-existing or corrupted."""
        try:
            _l_(377196)

            _c_(377167, _a_(377161, _c_(377160, _n_(377157, "open", lambda: open), _a_(377159, _n_(377158, "self", lambda: self), "option_file_path"),'w'), "write"), _c_(377166, _a_(377163, _n_(377162, "json", lambda: json), "dumps"), _a_(377165, _n_(377164, "self", lambda: self), "default_values"),sort_keys=True, indent=4, separators=(',',':')))
            _l_(377168)
        except _n_(377169, "FileNotFoundError", lambda: FileNotFoundError):
            _l_(377195)

            _c_(377174, _a_(377171, _n_(377170, "os", lambda: os), "mkdir"), _a_(377173, _n_(377172, "self", lambda: self), "directory_name"))#Create the directory
            _l_(377175)#Create the directory
            if _c_(377181, _a_(377178, _a_(377177, _n_(377176, "os", lambda: os), "path"), "isdir"), _a_(377180, _n_(377179, "self", lambda: self), "directory_name")):
                _l_(377194)

                _c_(377184, _a_(377183, _n_(377182, "self", lambda: self), "__insert_all_default_values"))
                _l_(377185)
            else:
                _c_(377192, _n_(377186, "print", lambda: print), "Impossible to write in %s and file %s not found" % (_c_(377189, _a_(377188, _n_(377187, "os", lambda: os), "getcwd")),_a_(377191, _n_(377190, "self", lambda: self), "option_file_path")))
                _l_(377193)


#demo
if _n_(377199, "__name__", lambda: __name__) == '__main__':
    _l_(377234)


    option_file_object=_c_(377201, _n_(377200, "Options", lambda: Options))
    _l_(377202)
    _c_(377206, _n_(377203, "print", lambda: print), _a_(377205, _n_(377204, "option_file_object", lambda: option_file_object), "__doc__"))
    _l_(377207)
    _c_(377212, _n_(377208, "print", lambda: print), _c_(377211, _a_(377210, _n_(377209, "option_file_object", lambda: option_file_object), "read_file")))
    _l_(377213)
    _c_(377216, _a_(377215, _n_(377214, "option_file_object", lambda: option_file_object), "add_option_to_file"), "","test")#this should have no effect
    _l_(377217)#this should have no effect

    _c_(377220, _a_(377219, _n_(377218, "option_file_object", lambda: option_file_object), "add_option_to_file"), "translate_html_level","0")#this should have an effect
    _l_(377221)#this should have an effect
    _c_(377226, _n_(377222, "print", lambda: print), "value of translate_html_level:",_c_(377225, _a_(377224, _n_(377223, "option_file_object", lambda: option_file_object), "read_file"), "translate_html_level"))
    _l_(377227)
    _c_(377232, _n_(377228, "print", lambda: print), _c_(377231, _a_(377230, _n_(377229, "option_file_object", lambda: option_file_object), "read_file")))
    _l_(377233)
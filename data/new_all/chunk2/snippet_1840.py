# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51153553/not-returning-updates-to-yaml-file-and-returning-typeerror-on-string-update
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class YAML_Config:
    _l_(466622)

    '''
    Class used to interact with .YAML filetypes. Allows the creation of objects \
    that can be manipulated and save certain YAML files and configuration settings.
    '''
    _l_(466445)

    def __init__(self, filename):
        _l_(466485)

        '''
        Initial defintion. Defines the location for saving a new .YAML file or for loading \
        a previous one. The dictionary corresponding to the .YAML file is saved to self.dict. \
        If this is a new .YAML file, an empty dictionary is created.

        Input Arguments:
            -filename: (string) The name of the file where the current .YAML file is \
            located or the new .YAML will be saved.
        '''
        _l_(466446)
        #Get the filename and save it to the class as a property.
        _n_(466447, "self", lambda: self).file = _n_(466448, "filename", lambda: filename)
        _l_(466449)

        #Check if the file exists...
        if _c_(466455, _a_(466452, _a_(466451, _n_(466450, "os", lambda: os), "path"), "isfile"), _a_(466454, _n_(466453, "self", lambda: self), "file")):
            _l_(466481)


            #Prepare to open the file with reading capabilities
            with _c_(466459, _n_(466456, "open", lambda: open), _a_(466458, _n_(466457, "self", lambda: self), "file"),'r') as infile:
                _l_(466465)


                #Get a dictionary with all of the YAML informatin.
                yaml_dict = _c_(466463, _a_(466461, _n_(466460, "yaml", lambda: yaml), "load"), _n_(466462, "infile", lambda: infile))
                _l_(466464)

        #If the file does not exist...
        else:

            #Create an empty dictionary to save all YAML data.
            yaml_dict = {}
            _l_(466466)

            #Create an empty .yaml file with the dictionary.
            with _c_(466470, _n_(466467, "open", lambda: open), _a_(466469, _n_(466468, "self", lambda: self), "file"), 'w') as infile:
                _l_(466477)


                #Save updated dictionary to YAML file.
                _c_(466475, _a_(466472, _n_(466471, "yaml", lambda: yaml), "dump"), _n_(466473, "yaml_dict", lambda: yaml_dict), _n_(466474, "infile", lambda: infile), default_flow_style=False)
                _l_(466476)

            _c_(466479, _n_(466478, "print", lambda: print), 'YAML configuration file not found. New, empty dictionary, and .yaml file created.')
            _l_(466480)

        _n_(466482, "self", lambda: self).dict=_n_(466483, "yaml_dict", lambda: yaml_dict)
        _l_(466484)




    def update_value(self, kwargs):
        _l_(466621)

        '''
        Used to update YAML files, and checks that the files were updated properly.
        '''
        _l_(466486)
        #If these are not keyword arguments, then throw an error.
        assert _n_(466487, "kwargs", lambda: kwargs), 'Input Error'
        _l_(466488)

        #Get the YAML dictionary before it is updated.
        yaml_dict = _a_(466490, _n_(466489, "self", lambda: self), "dict")
        _l_(466491)


        #Make a copy of the dictionary to compare against later.
        yaml_dict_original = _c_(466496, _a_(466493, _n_(466492, "copy", lambda: copy), "deepcopy"), _a_(466495, _n_(466494, "self", lambda: self), "dict"))
        _l_(466497)

        #Check if the dictionary is nonetype. This happens if the file is new as the file is empty.
        if _n_(466498, "yaml_dict_original", lambda: yaml_dict_original) is None:
            _l_(466507)


            #Redefine orginal dictionary as an empty dictionary.
            yaml_dict_original={}
            _l_(466499)

            #The new dictionary will simply be what is passed to the function.
            yaml_dict=_n_(466500, "kwargs", lambda: kwargs)
            _l_(466501)

        else:

            #Update the original dictionary and update it with the arguments passed.
            #This also updates self.dict as yaml_dict is simply a reference to
            #that dictionary, not a copy of it.
            _c_(466505, _a_(466503, _n_(466502, "yaml_dict", lambda: yaml_dict), "update"), _n_(466504, "kwargs", lambda: kwargs))
            _l_(466506)


        #Check if changes were made
        if (_n_(466508, "yaml_dict", lambda: yaml_dict)==_n_(466509, "yaml_dict_original", lambda: yaml_dict_original)) is False:
            _l_(466620)


            #Open the YAML file to write to it.
            with _c_(466513, _n_(466510, "open", lambda: open), _a_(466512, _n_(466511, "self", lambda: self), "file"), 'w') as outfile:
                _l_(466521)


                #Save updated dictionary to YAML file.
                _c_(466519, _a_(466515, _n_(466514, "yaml", lambda: yaml), "dump"), _a_(466517, _n_(466516, "self", lambda: self), "dict"), _n_(466518, "outfile", lambda: outfile), default_flow_style=False)
                _l_(466520)


    #Check that the file actually updated properly:

            #Double-check the file that it actually updated.
            with _c_(466525, _n_(466522, "open", lambda: open), _a_(466524, _n_(466523, "self", lambda: self), "file"), 'r') as infile:
                _l_(466531)


                lastupdate = _c_(466529, _a_(466527, _n_(466526, "yaml", lambda: yaml), "load"), _n_(466528, "infile", lambda: infile))
                _l_(466530)

            #Get any nonmatching values between what should be in the YAML file and what actually is.
            errors = { _n_(466532, "k", lambda: k) : _n_(466533, "yaml_dict", lambda: yaml_dict)[_n_(466534, "k", lambda: k)] for k in _c_(466537, _n_(466535, "set", lambda: set), _n_(466536, "yaml_dict", lambda: yaml_dict)) - _c_(466540, _n_(466538, "set", lambda: set), _n_(466539, "lastupdate", lambda: lastupdate)) }
            _l_(466541)

            #Find out what changed in the YAML file.
            edits = { _n_(466542, "k", lambda: k) : _n_(466543, "yaml_dict_original", lambda: yaml_dict_original)[_n_(466544, "k", lambda: k)] for k in _c_(466547, _n_(466545, "set", lambda: set), _n_(466546, "yaml_dict_original", lambda: yaml_dict_original)) - _c_(466550, _n_(466548, "set", lambda: set), _n_(466549, "lastupdate", lambda: lastupdate)) }
            _l_(466551)

            #Check if errors is not empty. Evaluating dictionaries as boolean either returns True (not empty)
            #or False (empty).
            if _c_(466554, _n_(466552, "bool", lambda: bool), _n_(466553, "errors", lambda: errors)) is True:
                _l_(466610)


                #First line of return print statement.
                _c_(466556, _n_(466555, "print", lambda: print), 'The following entries did not update successfully:')
                _l_(466557)

                #Loop through keys in errors
                for n in _n_(466558, "errors", lambda: errors):
                    _l_(466573)


                    #Print the current key
                    _c_(466561, _n_(466559, "print", lambda: print), _n_(466560, "n", lambda: n))
                    _l_(466562)

                    #Loop through entries of current key
                    for m in _n_(466563, "errors", lambda: errors)[_n_(466564, "n", lambda: n)]:
                        _l_(466572)


                        #Print current entry of current key
                        _c_(466570, _n_(466565, "print", lambda: print), _n_(466566, "m", lambda: m),':',_n_(466567, "errors", lambda: errors)[_n_(466568, "n", lambda: n)][_n_(466569, "m", lambda: m)])
                        _l_(466571)

            #Saved properly, check for edits and display to user.
            else:

                #Find where any edits were made.
                edits = {_n_(466574, "k", lambda: k): _n_(466575, "yaml_dict_original", lambda: yaml_dict_original)[_n_(466576, "k", lambda: k)] for k in _n_(466577, "yaml_dict_original", lambda: yaml_dict_original) if _n_(466578, "k", lambda: k) in _n_(466579, "lastupdate", lambda: lastupdate) and _n_(466580, "yaml_dict_original", lambda: yaml_dict_original)[_n_(466581, "k", lambda: k)] != _n_(466582, "lastupdate", lambda: lastupdate)[_n_(466583, "k", lambda: k)]}
                _l_(466584)

                #Show user what edits were successfuly made.
                _c_(466592, _n_(466585, "print", lambda: print), '%s was successfully updated with the following changes:' %  _c_(466591, _a_(466588, _a_(466587, _n_(466586, "os", lambda: os), "path"), "basename"), _a_(466590, _n_(466589, "self", lambda: self), "file")))
                _l_(466593)

                #Loop through keys in edits
                for n in _n_(466594, "edits", lambda: edits):
                    _l_(466609)


                    #Print the current key
                    _c_(466597, _n_(466595, "print", lambda: print), _n_(466596, "n", lambda: n))
                    _l_(466598)

                    #Loop through entries of current key
                    for m in _n_(466599, "edits", lambda: edits)[_n_(466600, "n", lambda: n)]:
                        _l_(466608)


                        #Print current entry of current key
                        _c_(466606, _n_(466601, "print", lambda: print), _n_(466602, "m", lambda: m),':',_n_(466603, "edits", lambda: edits)[_n_(466604, "n", lambda: n)][_n_(466605, "m", lambda: m)])
                        _l_(466607)

        #If no changes were made...        
        else:

            #Show user what edits were successfuly made.
            _c_(466618, _n_(466611, "print", lambda: print), 'No changes to %s were passed. File not updated.' %  

    _c_(466617, _a_(466614, _a_(466613, _n_(466612, "os", lambda: os), "path"), "basename"), _a_(466616, _n_(466615, "self", lambda: self), "file")))
            _l_(466619)



test=_c_(466624, _n_(466623, "YAML_Config", lambda: YAML_Config), r'...Path\Python Work\yaml_test.yaml')
_l_(466625)

d = {'A': 7, 'B':{'C':'D', 'D':False, 'E':'Julio'},\
     'The Real C': {'J?':'Yes, this is J.', 'K' : 241},'Q' : 'PQ'}
_l_(466626)

_c_(466630, _a_(466628, _n_(466627, "test", lambda: test), "update_value"), _n_(466629, "d", lambda: d))
_l_(466631)
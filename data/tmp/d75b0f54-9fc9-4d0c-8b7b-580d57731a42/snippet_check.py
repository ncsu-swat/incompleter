class TBD0: # pragma: no cover
 # pragma: no cover
    def __init__(self): # pragma: no cover
        self.container = {0: 1, 1: 2, 2: 3} # pragma: no cover
        self.keys = list(self.container.keys()) # pragma: no cover
        self.iter_current = 0 # pragma: no cover
 # pragma: no cover
    def __refresh_keys(self): # pragma: no cover
        self.keys = list(self.container.keys()) # pragma: no cover
        for key in self.keys: # pragma: no cover
            if not isinstance(key, int): # pragma: no cover
                return # pragma: no cover
        sorted(self.keys) # pragma: no cover
 # pragma: no cover
    def __str__(self): # pragma: no cover
        self.__refresh_keys() # pragma: no cover
        ret_str = '' # pragma: no cover
        ret_str += '[ ' # pragma: no cover
        for (idx, (key, val)) in enumerate(self.container.items()): # pragma: no cover
            ret_str += str(val) # pragma: no cover
            if idx < len(self.keys) - 1: # pragma: no cover
                ret_str += ', ' # pragma: no cover
        ret_str += ' ]' # pragma: no cover
        return ret_str # pragma: no cover
 # pragma: no cover
    def __getitem__(self, key): # pragma: no cover
        self.__refresh_keys() # pragma: no cover
        ret_val = None # pragma: no cover
        if isinstance(key, slice): # pragma: no cover
            list_to_return = [] # pragma: no cover
            start = key.start or 0 # pragma: no cover
            stop = key.stop or len(self.container) # pragma: no cover
            step = key.step or 1 # pragma: no cover
            if start < 0: # pragma: no cover
                if start * -1 > len(self.keys): # pragma: no cover
                    diff = start * -1 - len(self.keys) # pragma: no cover
                    if len(self.keys) > 0: # pragma: no cover
                        for i in range(max(self.keys), max(self.keys) + diff + 1): # pragma: no cover
                            self.container[i] = 0 # pragma: no cover
                    else: # pragma: no cover
                        for i in range(0, diff + 1): # pragma: no cover
                            self.container[i] = 0 # pragma: no cover
                self.__refresh_keys() # pragma: no cover
                start = self.keys[start] # pragma: no cover
            if stop < 0: # pragma: no cover
                if stop * -1 > len(self.keys): # pragma: no cover
                    diff = stop * -1 - len(self.keys) # pragma: no cover
                    if len(self.keys) > 0: # pragma: no cover
                        for i in range(max(self.keys), max(self.keys) + diff + 1): # pragma: no cover
                            self.container[i] = 0 # pragma: no cover
                    else: # pragma: no cover
                        for i in range(0, diff + 1): # pragma: no cover
                            self.container[i] = 0 # pragma: no cover
                self.__refresh_keys() # pragma: no cover
                stop = self.keys[stop] # pragma: no cover
            for i in range(start, stop, step): # pragma: no cover
                list_to_return.append(self.container[i]) # pragma: no cover
            ret_val = list_to_return # pragma: no cover
        elif isinstance(key, int): # pragma: no cover
            if key < 0: # pragma: no cover
                key = self.keys[key] # pragma: no cover
            ret_val = self.container[key] # pragma: no cover
        elif isinstance(key, str): # pragma: no cover
            ret_val = self.container[key] # pragma: no cover
        return ret_val # pragma: no cover
 # pragma: no cover
    def __setitem__(self, key, val): # pragma: no cover
        self.__refresh_keys() # pragma: no cover
        if isinstance(key, slice): # pragma: no cover
            start = key.start or 0 # pragma: no cover
            stop = key.stop or len(self.container) # pragma: no cover
            step = key.step or 1 # pragma: no cover
            if start < 0: # pragma: no cover
                start = self.keys[start] # pragma: no cover
            if stop < 0: # pragma: no cover
                stop = self.keys[stop] # pragma: no cover
            for i in range(0, stop, step): # pragma: no cover
                if i not in self.keys: # pragma: no cover
                    self.container[i] = 0 # pragma: no cover
            for i in range(start, stop, step): # pragma: no cover
                self.container[i] = val # pragma: no cover
            return True # pragma: no cover
        elif isinstance(key, int): # pragma: no cover
            if key < 0: # pragma: no cover
                key = self.keys[key] # pragma: no cover
            for i in range(0, key): # pragma: no cover
                if i not in self.keys: # pragma: no cover
                    self.container[i] = 0 # pragma: no cover
            self.container[key] = val # pragma: no cover
            return True # pragma: no cover
        elif isinstance(key, str): # pragma: no cover
            self.container[key] = val # pragma: no cover
            return True # pragma: no cover
        self.__refresh_keys() # pragma: no cover
        return False # pragma: no cover
 # pragma: no cover
    def __iter__(self): # pragma: no cover
        return iter(self.container) # pragma: no cover
 # pragma: no cover
    def __len__(self): # pragma: no cover
        return len(self.keys) # pragma: no cover
__original_start_marker = None # pragma: no cover
index = input('Enter an index: ')
my_list = TBD0()
print(my_list[index])
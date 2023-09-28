# Extracted from https://stackoverflow.com/questions/11277432/how-can-i-remove-a-key-from-a-python-dictionary

run_step = 1

# Original (run_step == 0)
# Error 1 ~ NameError: name 'key' is not defined
# Executes: false
if run_step == 0:
    try: 
        del dict[key]
    except KeyError: 
        pass

    my_dict.pop('key', None)
    if 'key' in dict: 
        del myDict['key']

# Step 1 (run_step == 1)
# Action: Error was in line 9 where "key" item is being accessed but "key" is not defined. I am defining "key" as an integer.
# Error 1 ~ TypeError: 'type' object does not support item deletion
# Executes: false
if run_step == 1:
    key = 1
    try: 
        del dict[key]
    except KeyError: 
        pass

    my_dict.pop('key', None)
    if 'key' in dict: 
        del myDict['key']


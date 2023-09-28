# Extracted from https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python

run_step = 5

# Original (run_step == 0)
# Error 1 ~ ModuleNotFoundError: No module named 'typeguard'
# Executes: false
if run_step == 0:
    from typeguard import check_type
    from typing import List

    try:
        check_type('mylist', [1, 2], List[int])
    except TypeError as e:
        print(e)

    check_type('foo', [1, 3.14], List[Union[int, float]])
    # vs
    isinstance(foo, list) and all(isinstance(a, (int, float)) for a in foo) 

# Step 1 (run_step == 1)
# Action: Since 'typeguard' module could not be found, I am installing 'typeguard' module.
# Error 1 ~ NameError: name 'Union' is not defined
# Executes: false
if run_step == 1:
    # Action steps: installing required modules
    import sys
    import subprocess
    import pkg_resources

    required = {'typeguard'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    not_installed = required - installed

    for pkg in not_installed:
        proc = subprocess.Popen([sys.executable, '-m', 'pip', 'install', pkg])
        proc.wait()
    # Action ends

    from typeguard import check_type
    from typing import List

    try:
        check_type('mylist', [1, 2], List[int])
    except TypeError as e:
        print(e)

    check_type('foo', [1, 3.14], List[Union[int, float]])
    # vs
    isinstance(foo, list) and all(isinstance(a, (int, float)) for a in foo) 

    # Action cleanup: uninstall typeguard
    for pkg in not_installed:
        proc = subprocess.Popen([sys.executable, '-m', 'pip', 'uninstall', '-y', pkg], stdout=subprocess.DEVNULL)
        proc.wait()
    # Action cleanup ends

# Step 2 (run_step == 2)
# Action: import Union from typing module
# Error 1 ~ TypeError: check_type() takes 2 positional arguments but 3 were given
# Executes: false
if run_step == 2:
    # Action steps: importing Union from type module
    import sys
    import subprocess
    import pkg_resources
    from typing import List, Union
    
    required = {'typeguard'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    not_installed = required - installed

    for pkg in not_installed:
        proc = subprocess.Popen([sys.executable, '-m', 'pip', 'install', pkg])
        proc.wait()
    # Action ends

    from typeguard import check_type

    try:
        check_type('mylist', [1, 2], List[int])
    except TypeError as e:
        print(e)

    check_type('foo', [1, 3.14], List[Union[int, float]])
    # vs
    isinstance(foo, list) and all(isinstance(a, (int, float)) for a in foo) 

    # Action cleanup: uninstall typeguard
    for pkg in not_installed:
        proc = subprocess.Popen([sys.executable, '-m', 'pip', 'uninstall', '-y', pkg], stdout=subprocess.DEVNULL)
        proc.wait()
    # Action cleanup ends

# Step 3 (run_step == 3)
# Action: Since "check_type" is a function from a third-party library "typeguard", we fuzz the version of the module "typeguard" when installing. I found "typeguard==2.5.0" to have compatible function signature with three arguments.
# Error 1 ~ 
# Executes: 
if run_step == 3:
    # Action steps: changing "typeguard" version to "2.5.0"
    import sys
    import subprocess
    import pkg_resources
    from typing import List, Union
    
    required = {'typeguard==2.5.0'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    not_installed = required - installed

    for pkg in not_installed:
        proc = subprocess.Popen([sys.executable, '-m', 'pip', 'install', pkg])
        proc.wait()
    # Action ends

    from typeguard import check_type

    try:
        check_type('mylist', [1, 2], List[int])
    except TypeError as e:
        print(e)

    check_type('foo', [1, 3.14], List[Union[int, float]])
    # vs
    isinstance(foo, list) and all(isinstance(a, (int, float)) for a in foo) 

    # Action cleanup: uninstall typeguard
    for pkg in not_installed:
        proc = subprocess.Popen([sys.executable, '-m', 'pip', 'uninstall', '-y', pkg], stdout=subprocess.DEVNULL)
        proc.wait()
    # Action cleanup ends

# Step 4 (run_step == 4)
# Action: Since "check_type" is a function from a third-party library "typeguard", we fuzz the version of the module "typeguard" when installing. I found "typeguard==2.5.0" to have compatible function signature with three arguments.
# Error 1 ~ NameError: name 'foo' is not defined
# Executes: false
if run_step == 4:
    # Action steps: changing "typeguard" version to "2.5.0"
    import sys
    import subprocess
    import pkg_resources
    from typing import List, Union
    
    required = {'typeguard==2.5.0'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    not_installed = required - installed

    for pkg in not_installed:
        proc = subprocess.Popen([sys.executable, '-m', 'pip', 'install', pkg])
        proc.wait()
    # Action ends

    from typeguard import check_type

    try:
        check_type('mylist', [1, 2], List[int])
    except TypeError as e:
        print(e)

    check_type('foo', [1, 3.14], List[Union[int, float]])
    # vs
    isinstance(foo, list) and all(isinstance(a, (int, float)) for a in foo) 

    # Action cleanup: uninstall typeguard
    for pkg in not_installed:
        proc = subprocess.Popen([sys.executable, '-m', 'pip', 'uninstall', '-y', pkg], stdout=subprocess.DEVNULL)
        proc.wait()
    # Action cleanup ends

# Step 5 (run_step == 5)
# Action: Define a variable called "foo" as integer and assign it a value "1". But, if "foo" is an integer, we are unable to cover the second predicate of the following clause
# Executes: true
if run_step == 5:
    # Action steps: changing "typeguard" version to "2.5.0"
    import sys
    import subprocess
    import pkg_resources
    from typing import List, Union
    
    required = {'typeguard==2.5.0'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    not_installed = required - installed

    for pkg in not_installed:
        proc = subprocess.Popen([sys.executable, '-m', 'pip', 'install', '-q', pkg])
        proc.wait()
    # Action ends

    from typeguard import check_type

    try:
        check_type('mylist', [1, 2], List[int])
    except TypeError as e:
        print(e)

    check_type('foo', [1, 3.14], List[Union[int, float]])
    
    # Define variable "foo" as an integer with value 1. But, if "foo" is an integer, we are unable to cover the second predicate of the following clause
    foo = 1
    isinstance(foo, list) and all(isinstance(a, (int, float)) for a in foo)

    # Action cleanup: uninstall typeguard
    for pkg in not_installed:
        proc = subprocess.Popen([sys.executable, '-m', 'pip', 'uninstall', '-y', pkg], stdout=subprocess.DEVNULL)
        proc.wait()
    # Action cleanup ends 


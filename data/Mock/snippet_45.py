# Extracted from https://stackoverflow.com/questions/30081275/why-is-1000000000000000-in-range1000000000000001-so-fast-in-python-3

run_step = 2

# Original (run_step == 0)
# Error 1 ~ In line 15, NameError: name 'my_crappy_range' is not defined
# Executes: false
if run_step == 0:
    a = range(5)
    print(list(a))
    [0, 1, 2, 3, 4]
    print(list(a))
    [0, 1, 2, 3, 4]

    b = my_crappy_range(5)
    print(list(b))
    [0, 1, 2, 3, 4]
    print(list(b))
    []

    import collections.abc
    isinstance(a, collections.abc.Sequence)
    True

    a[3]         # indexable
    3
    len(a)       # sized
    5
    3 in a       # membership
    True
    reversed(a)  # reversible
    a.index(3)   # implements 'index'
    3
    a.count(3)   # implements 'count'
    1

# Step 1 (run_step == 1)
# Action: Since the usage of "my_crappy_range(5)" looks like a standard way to call a function, I am inferring that "my_crappy_range" is an undefined function that takes a single integer argument. So, I define "my_crappy_range" function that takes a single integer argument and returns None.
# Error 1 ~ In line 52, TypeError: 'NoneType' object is not iterable
# Executes: false
elif run_step == 1:
    def my_crappy_range(val):
        return None

    a = range(5)
    print(list(a))
    [0, 1, 2, 3, 4]
    print(list(a))
    [0, 1, 2, 3, 4]

    b = my_crappy_range(5)
    print(list(b))
    [0, 1, 2, 3, 4]
    print(list(b))
    []

    import collections.abc
    isinstance(a, collections.abc.Sequence)
    True

    a[3]         # indexable
    3
    len(a)       # sized
    5
    3 in a       # membership
    True
    reversed(a)  # reversible
    a.index(3)   # implements 'index'
    3
    a.count(3)   # implements 'count'
    1

# Step 2 (run_step == 2)
# Action: The error occurs at line 52 where the function call list(...) is expecting an iterable, but the value "b" returned by the function "my_crappy_range" is None type. So, I am having "my_crappy_range" return an iterable "list" type object 
# Executes: true
elif run_step == 2:
    def my_crappy_range(val):
        return list()

    a = range(5)
    print(list(a))
    [0, 1, 2, 3, 4]
    print(list(a))
    [0, 1, 2, 3, 4]

    b = my_crappy_range(5)
    print(list(b))
    [0, 1, 2, 3, 4]
    print(list(b))
    []

    import collections.abc
    isinstance(a, collections.abc.Sequence)
    True

    a[3]         # indexable
    3
    len(a)       # sized
    5
    3 in a       # membership
    True
    reversed(a)  # reversible
    a.index(3)   # implements 'index'
    3
    a.count(3)   # implements 'count'
    1
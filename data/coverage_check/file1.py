with open('file2.py', 'w+') as file2_file:
    file2_file.write('def foo():\n\ta = 1\n\tif a == 1:\n\t\ta = 1')

from file2 import foo
foo()
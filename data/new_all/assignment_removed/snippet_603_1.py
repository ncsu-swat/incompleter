import os
import sys
arguments = ['hello.py']
print(os.execvp(program, (program,) + tuple(arguments)))
print('Goodbye')
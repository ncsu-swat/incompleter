import os, sys
from subprocess import Popen, PIPE

count = 0
for file in os.listdir('../../../data/lexecutor_success'):
    if file.endswith('.py.orig'):
        count += 1
        out, err = Popen([sys.executable, file], stdout=PIPE, stderr=PIPE).communicate()

        if not len(err):
            print(file)
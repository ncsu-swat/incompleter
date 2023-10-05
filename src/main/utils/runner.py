import sys
from subprocess import Popen, PIPE

class Runner:
    def __init__(self, path: str) -> None:
        self.path = path

    def run(self) -> list[str]:
        try:
            print('\nRunning: {}\n'.format(self.path))
            proc = Popen([sys.executable, self.path], stdout=PIPE, stderr=PIPE)
            proc.wait()
            out, err = proc.communicate()
            out = out.decode('utf-8')
            err = err.decode('utf-8')
            return out, err
        except Exception as e:
            print(e)
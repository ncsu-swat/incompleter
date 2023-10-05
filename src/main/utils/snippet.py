import sys

from typing import List
from pathlib import Path
from subprocess import Popen, PIPE

class Snippet:
    def __init__(self, snippet_path: str) -> None:
        self.snippet_path   : str       = snippet_path
        self.code           : List[str] = []
        
        self.code.append(self.__read_snippet())

    def __read_snippet(self) -> str:
        if not Path(self.snippet_path).exists(): raise FileNotFoundError('Snippet path does not exist\nSnippet path: {}\n'.format(self.snippet_path))
        snippet_file = open(self.snippet_path, 'r')
        return snippet_file.read()

    def run(self, idx: int) -> List[str]:
        try:
            print('\nRunning: {}\n'.format(self.snippet_path))
            proc = Popen([sys.executable, self.snippet_path], stdout=PIPE, stderr=PIPE)
            proc.wait()
            out, err = proc.communicate()
            out = out.decode('utf-8')
            err = err.decode('utf-8')
            
            return out, err
        except Exception as e:
            print(e)
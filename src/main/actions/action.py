from abc import ABC, abstractmethod
from pathlib import Path

class Action(ABC):
    def __init__(self, snippet_path: str, lineno: int) -> None:
        self.snippet_path = snippet_path
        self.lineno = lineno

        self.snippet = self.__read_snippet()

        print(self.snippet)

    def __str__(self) -> str:
        desc = 'Original Snippet Path: {}\nException Causing Line No.: {}\n'.format(self.snippet_path, str(self.lineno))
        return desc

    def __read_snippet(self) -> str:
        if not Path(self.snippet_path).exists(): raise FileNotFoundError('Snippet path does not exist\nSnippet path: {}\n'.format(self.snippet_path))
        snippet_file = open(self.snippet_path, 'r')
        return snippet_file.read()

    @abstractmethod
    def apply_pattern(self) -> bool:
        pass
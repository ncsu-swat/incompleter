from abc import ABC, abstractmethod
from pathlib import Path

from main.utils.snippet import Snippet

class Action(ABC):
    def __init__(self, snippet: Snippet, lineno: int) -> None:
        self.snippet = snippet
        self.lineno: int = lineno

    def __str__(self) -> str:
        desc = 'Exception Causing Line No.: {}\n'.format(str(self.lineno))
        return desc

    @abstractmethod
    def apply_pattern(self) -> bool:
        pass
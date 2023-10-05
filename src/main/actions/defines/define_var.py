from main.actions.action import Action
from typing import Any
import ast

class Def_Var(Action):
    def __init__(self, snippet_path: str, lineno: int, **kwargs: Any) -> None:
        super().__init__(snippet_path, lineno)

        self.var_name = kwargs['var_name']
        self.var_val = kwargs['var_val']

    def __str__(self) -> str:
        desc = super().__str__()
        desc += 'Variable name: {}\nVariable value: {}\n'.format(self.var_name, self.var_val)

        return desc

    def apply_pattern(self):
        pass

if __name__ == "__main__":
    def_var = Def_Var(snippet_path='data/LExecutorFails/snippet_45.py.orig', lineno=1, var_name='a', var_val=2)
    print(def_var)

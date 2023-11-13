from main.utils.snippet import Snippet
from main.actions.action_base_class import ActionBaseClass
from typing import Any
import os
import ast

from pathlib import Path

class CreateFile(ActionBaseClass):
    def __init__(self, snippet: Snippet=None, lineno: int=0, **kwargs: dict) -> None:
        super().__init__(snippet, lineno)

        self.file_name = kwargs['file_name']
        self.file_content = kwargs['file_content']

    def __str__(self) -> str:
        desc = super().__str__()
        desc += 'File name: {}\nFile content: {}'.format(self.file_name, self.file_content)

        return desc

    def check_criteria(self) -> bool:
        return True

    def apply_pattern(self) -> str:
        try:
            # Create file with all intermediate directories
            file_to_create = Path(os.path.join(self.snippet.tmp_dir, self.file_name))
            file_to_create.parent.mkdir(exist_ok=True, parents=True)
            
            # Write to file
            with open(os.path.join(self.snippet.tmp_dir, self.file_name), 'wb') as file_to_write:
                file_to_write.write(self.file_content)

        except OSError as e:
            pass

        tree = ast.parse(self.snippet.get_latest())
        return ast.unparse(ast.fix_missing_locations(tree))


from path_config import DATA_DIR
from main.utils.snippet import Snippet
from main.actions.action_base_class import ActionBaseClass
from typing import Any
import ast
import os
import pickle

class AddImport(ActionBaseClass):
    def __init__(self, snippet: Snippet=None, lineno: int=0, **kwargs: dict) -> None:
        super().__init__(snippet, lineno)

        self.module_name = kwargs['module_name']
        self.import_dict = self.__get_local_package_index()

    def __str__(self) -> str:
        desc = super().__str__()
        desc += 'Module name: {}\n'.format(self.module_name)

        return desc

    def __get_local_package_index(self) -> dict:
        with open(os.path.join(DATA_DIR, 'package_meta/import_dict.pickle'), 'rb') as import_dict_pickle:
            if import_dict := pickle.load(import_dict_pickle):
                return import_dict
        return None

    def check_criteria(self) -> bool:
        if self.import_dict is None:
            return False

        if self.module_name in self.import_dict.keys():
            return True

        for module, import_ast in self.import_dict.items():
            if 'names' in dir(import_ast):
                for alias in import_ast.names:
                    if alias.name == self.module_name:
                        self.import_dict[self.module_name] = ast.Import(
                                                                names = [
                                                                    ast.alias(name=self.module_name)
                                                                ]
                                                            )
                        return True

        return False

    def apply_pattern(self) -> str:
        class AddImportTransformer(ast.NodeTransformer):
            def __init__(self, **kwargs: Any) -> None:
                self.snippet: Snippet = kwargs['snippet']
                self.lineno: int = kwargs['lineno']
                self.module_name: str = kwargs['module_name']
                self.import_dict: dict = kwargs['import_dict']

            @ActionBaseClass.add_to_history
            def visit_Body(self, node: ast.Module) -> ast.Module:
                node.body.insert(0, self.import_dict[self.module_name])

                return node

        tree = ast.parse(self.snippet.get_latest())
        AddImportTransformer(snippet=self.snippet, lineno=self.lineno, module_name=self.module_name, import_dict=self.import_dict).visit_Body(tree)

        
from path_config import DATA_DIR
from main.utils.snippet import Snippet
from main.actions.action import Action
from typing import Any
import ast
import os
import pickle

class AddImport(Action):
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

        return False

    def apply_pattern(self) -> str:
        class AddImportTransformer(ast.NodeTransformer):
            def __init__(self, **kwargs: Any) -> None:
                self.lineno: int = kwargs['lineno']
                self.module_name: str = kwargs['module_name']
                self.import_dict: dict = kwargs['import_dict']

            def visit_Body(self, node: ast.Module) -> ast.Module:
                # to_visit = []
                # visited = set()
                # node_found = False
                # line_count = 0

                # to_visit.append(node)
                # while(not (node_found or len(to_visit) == 0)):
                #     parent_node = to_visit[-1]
                #     if parent_node not in visited: 
                #         print(str(line_count), parent_node)
                #     visited.add(parent_node)
                    
                #     unvisited_child_exists = False
                #     for child_node in ast.iter_child_nodes(parent_node):
                #         if child_node not in visited:
                #             if len(list(ast.iter_child_nodes(child_node))) > 0:
                #                 line_count += 1

                #             unvisited_child_exists = True
                #             to_visit.append(child_node)
                #             break
                #     if not unvisited_child_exists:
                #         to_visit.pop()
                
                node.body.insert(0, self.import_dict[self.module_name])

                # node.body.insert(self.lineno-1, ast.Assign(
                #     targets = [
                #         ast.Name(id=self.var_name, ctx=ast.Store())
                #     ],
                #     value=ast.Constant(value=self.var_val)
                # ))

                return node

        tree = ast.parse(self.snippet.get_latest())
        # print(ast.dump(tree, indent=4))

        AddImportTransformer(lineno=self.lineno, module_name=self.module_name, import_dict=self.import_dict).visit_Body(tree)

        # print(ast.unparse(ast.fix_missing_locations(tree)))
        
        return ast.unparse(ast.fix_missing_locations(tree))


        
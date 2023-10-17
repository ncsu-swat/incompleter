from main.utils.snippet import Snippet
from main.actions.action import Action
from typing import Any
import ast

class DefineVar(Action):
    def __init__(self, snippet: Snippet=None, lineno: int=0, **kwargs: dict) -> None:
        super().__init__(snippet, lineno)

        self.var_name = kwargs['var_name']
        self.var_val = kwargs['var_val']

    def __str__(self) -> str:
        desc = super().__str__()
        desc += 'Variable name: {}\nVariable value: {}\n'.format(self.var_name, self.var_val)

        return desc

    def check_criteria(self) -> bool:
        return True

    def apply_pattern(self) -> str:
        class AddNameTransformer(ast.NodeTransformer):
            def __init__(self, **kwargs: Any) -> None:
                self.lineno: int = kwargs['lineno']
                self.var_name: str = kwargs['var_name']
                self.var_val: Any = kwargs['var_val']

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
                
                node.body.insert(0, ast.Assign(
                    targets = [
                        ast.Name(id=self.var_name, ctx=ast.Store())
                    ],
                    value=ast.Constant(value=self.var_val)
                ))

                # node.body.insert(self.lineno-1, ast.Assign(
                #     targets = [
                #         ast.Name(id=self.var_name, ctx=ast.Store())
                #     ],
                #     value=ast.Constant(value=self.var_val)
                # ))

                return node

        tree = ast.parse(self.snippet.get_latest())
        # print(ast.dump(tree, indent=4))

        AddNameTransformer(lineno=self.lineno, var_name=self.var_name, var_val=self.var_val).visit_Body(tree)

        # print(ast.unparse(ast.fix_missing_locations(tree)))
        
        return ast.unparse(ast.fix_missing_locations(tree))


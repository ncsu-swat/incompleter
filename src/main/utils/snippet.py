from path_config import DATA_DIR

import sys
import os
import re
import shutil
import ast

from typing import List, Dict, Tuple, Any
from pathlib import Path
from subprocess import Popen, PIPE

class Snippet:
    def __init__(self, snippet_path: str) -> None:
        self.LIFETIME = 2
        self.current_iter = 0

        self.snippet_path: str = snippet_path
        self.tmp_path: str = self.__create_tmp_path()
        self.tmp_dir: str = '/'.join(self.tmp_path.split('/')[:-1])
        self.code: List[str] = [ self.__clean_snippet(self.__read_snippet()) ]
        self.latest: int = 0

        self.temp_identifier_counter: int = 0

        self.mocked_values: Dict[str, Any] = {}
        self.def_history: Dict[int, str] = {} # e.g. { iteration_number: defined_identifier }
        self.identifier_dependency: Dict[str, str] = {}

    def __read_snippet(self) -> str:
        if not Path(self.snippet_path).exists(): raise FileNotFoundError('Snippet path does not exist\nSnippet path: {}\n'.format(self.snippet_path))
        snippet_file = open(self.snippet_path, 'r')
        return snippet_file.read()

    def __clean_snippet(self, code: str) -> str:
        lines = code.split('\n')
        cleaned_lines = []

        for line in lines:
            line = re.sub(r'(?m)^ *#.*\n?', '', line) # removing lines that only have comments
            if len(line) > 0 and not line.isspace():
                cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)

    # def __normalize_snippet(self) -> str:

    def __create_tmp_path(self) -> str:
        tmp_path = os.path.join(DATA_DIR, 'tmp', self.snippet_path.split('/')[-1])
        tmp_file = Path(tmp_path)
        tmp_file.parent.mkdir(parents=True, exist_ok=True)

        return tmp_path

    def __create_tmp_file(self) -> str:
        with open(self.tmp_path, 'w+') as tmp_file:
            try:
                tmp_file.write(self.get_latest())
            except Exception as e:
                print('__create_tmp_file Exception: ' + e)

    def __delete_tmp_file(self) -> None:
        try:
            os.remove(self.tmp_path)
        except Exception as e:
            print('__delete_tmp_file Exception: ' + e)

    def cleanup(self) -> None:
        for file in os.listdir(self.tmp_dir):
            file_path = os.path.join(self.tmp_dir, file)
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.remove(file_path)

    def add(self, code_str) -> None:
        self.code.append(code_str)
        self.current_iter += 1

    def get_current_iter(self) -> int:
        return self.current_iter

    def get_latest(self) -> str:
        return self.code[-1]

    def run_latest(self) -> List[str]:
        try:
            # setup tmp_file at tmp_path before running
            self.__create_tmp_file()
            
            print('\nRunning: {}\n'.format(self.tmp_path))
            proc = Popen([sys.executable, self.tmp_path], stdout=PIPE, stderr=PIPE, cwd=self.tmp_dir)
            proc.wait()
            out, err = proc.communicate()
            out = out.decode('utf-8')
            err = err.decode('utf-8')

            # cleanup tmp_file at tmp_path after running
            self.__delete_tmp_file()
            
            return out, err
        except FileNotFoundError as e:
            print('FileNotFoundError: when trying to run snippet {}#{}\n'.format(self.snippet_path, str(len(self.code)-1)))

    def register_mock_definition(self, iter_n: int, rewritten_snippet: str, target: str, value: Any) -> None:
        self.def_history[iter_n] = target
        
        self.mocked_values[target] = value
        self.mocked_values['ident_'+str(self.temp_identifier_counter)] = value

        # We will use identifier dependency mappings to determine the root 'ident_#' identifier that causes a certain TypeError (e.g. 'NoneType' object is not iterable --> we need to find out which NoneType ident_# is responsible for this TypeError)
        class NameVisitor(ast.NodeVisitor):
            def __init__(self, **kwargs):
                self.lhs = kwargs['lhs']
                self.potential_rhs = kwargs['potential_rhs']
                self.identifier_dependency = kwargs['identifier_dependency']
            def visit_Name(self, node):
                if node.id in self.potential_rhs:
                    self.potential_rhs.append(self.lhs)

                    # lhs is dependent on rhs
                    # We try to maintain association between the lhs and the root dependency (containing ident_); we don't keep track of the chain of assignments. e.g: ident_0=None \n x=ident_0 \n y=x \n z=y --> {x: ident_0, y: ident_0, z: ident_0}. Note here that, y and z are being shown as directly dependent on ident_0 without showing y's intermediate dependency on x or z's intermediate dependency on y.
                    self.identifier_dependency[self.lhs] = self.identifier_dependency[node.id] if 'ident_' not in node.id else node.id
                return node
        class IdentifierDependencyVisitor(ast.NodeVisitor):
            def __init__(self, **kwargs):
                self.potential_rhs = kwargs['potential_rhs']
                self.identifier_dependency = kwargs['identifier_dependency']
            def visit_Assign(self, node):
                NameVisitor(lhs=node.targets[0].id, potential_rhs=self.potential_rhs, identifier_dependency=self.identifier_dependency).visit(node.value)
                return node
        
        self.identifier_dependency[target] = 'ident_'+str(self.temp_identifier_counter)
        tree = ast.parse(rewritten_snippet)
        IdentifierDependencyVisitor(potential_rhs=[target, 'ident_'+str(self.temp_identifier_counter)], identifier_dependency=self.identifier_dependency).visit(tree)

        self.temp_identifier_counter += 1

    def get_mocked_value(self, target: str) -> Any:
        return self.mocked_values[target]
    
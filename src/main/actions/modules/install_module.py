from path_config import DATA_DIR
from main.utils.snippet import Snippet
from main.actions.action_base_class import ActionBaseClass
from typing import Any

from subprocess import Popen, DEVNULL
import os
import sys
import ast
import pickle

class InstallModule(ActionBaseClass):
    def __init__(self, snippet: Snippet=None, lineno: int=0, **kwargs: dict) -> None:
        super().__init__(snippet, lineno)

        self.module_name = kwargs['module_name']
        self.package_list = self.__get_popular_package_list()

    def __str__(self) -> str:
        desc = super().__str__()
        desc += 'Module name: {}\n'.format(self.module_name)

        return desc

    def __get_popular_package_list(self) -> dict:
        with open(os.path.join(DATA_DIR, 'package_meta/popular_packages_list.pickle'), 'rb') as package_list_pickle:
            if package_list := pickle.load(package_list_pickle):
                return package_list
        return None

    def check_criteria(self) -> bool:
        if self.package_list is not None:
            if self.module_name in self.package_list:
                return True
        return False

    def apply_pattern(self) -> str:
        installer = Popen([sys.executable, '-m', 'pip', 'install', self.module_name], stdout=DEVNULL, stderr=DEVNULL)
        installer.wait()

        tree = ast.parse(self.snippet.get_latest())
        return ast.unparse(ast.fix_missing_locations(tree))


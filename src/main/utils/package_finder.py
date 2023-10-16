from path_config import DATA_DIR

from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from github import Auth, Github
from github.PaginatedList import PaginatedList
from github.ContentFile import ContentFile

from pathlib import Path
from typing import List, Tuple
import json
import os
import base64

import ast

import_dict, import_from_dict, import_alias_dict = {}, {}, {}

# Top PyPI Search
__top_pypi_path = os.path.join(DATA_DIR, 'package_meta', 'top_pypi.json')

def __create_cache(__top_pypi_path: str) -> None:
    top_pypi_file = Path(__top_pypi_path)
    top_pypi_file.parent.mkdir(parents=True, exist_ok=True)

    return None

def __top_pypi_read_cache() -> dict:
    try:
        if os.path.exists(__top_pypi_path):
            with open(__top_pypi_path, 'r') as __top_pypi_file:
                return json.loads(__top_pypi_file.read())
        else:
            __create_cache(__top_pypi_path)
            return None
    except FileNotFoundError as e:
        print('FileNotFoundError: when trying to read from top pypi package list cache')
        return None

def __top_pypi_validate_cache(cached_json: str = None, retrieved_json: str = None) -> bool:
    if cached_json == None or retrieved_json == None: return False
    return hash(json.dumps(cached_json)) == hash(json.dumps(retrieved_json))

def __get_top_pypi_json() -> dict:
    top_json_latest = None
    try:
        top_url = 'https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.min.json'
        top_json_latest = json.loads(urlopen(top_url).read())
    except HTTPError as e:
        print('HTTPError: when trying to read the top pypi packages')
    except URLError as e:
        print('URLError: when trying to read the top pypi packages')

    top_json_cached = __top_pypi_read_cache()
    if top_json_latest != None:
        if not __top_pypi_validate_cache(top_json_latest, top_json_cached):
            with open(__top_pypi_path, 'w+') as __top_pypi_file:
                json.dump(top_json_latest, __top_pypi_file)
                return top_json_latest
        else:
            return top_json_cached
    
    return __top_pypi_read_cache()

# Github Search

def __new_github_object() -> Github:
    try:
        with open(os.path.join(DATA_DIR, 'package_meta', 'gh.key'), 'r') as gh_key:
            auth = Auth.Token(gh_key.read())
            return Github(auth=auth)
    except FileNotFoundError as e:
        print('FileNotFoundError: when trying to read secret gh.key in data/package_meta')

    return None

def __search_github_code(query: str) -> List[str]:
    gh: Github = __new_github_object()
    search_results: PaginatedList[ContentFile] = gh.search_code(query=query, language='python')

    result_code = []
    for res in search_results:
        result_code.append(base64.b64decode(res.content).decode('utf-8'))
    
    return result_code

# Parse Github Search Results

def __parse_imports(references: List[str]) -> Tuple[dict, dict, dict]:
    pass


if __name__ == "__main__":
    top_pypi_json = __get_top_pypi_json()

    for project in top_pypi_json['rows']:
        package_meta[project['project']] = { 'aliases': [], 'submodules': [] }

    print(package_meta)

    # __search_github_code('import numpy')


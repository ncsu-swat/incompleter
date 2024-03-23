import os
import re
import gc
import sys
import ast
import json
import shutil
import psutil
import signal

from typing import List, Dict, Tuple, Any
from pathlib import Path

import subprocess
from subprocess import Popen, PIPE

from multiprocessing import Process, Queue

class Snippet:
    TIMEOUT = 60 #seconds
    timedout_counter = 0

    def __init__(self, snippet: str) -> None:
        self.current_iter = 0

        self.tmp_path: str = self.__create_tmp_path()
        self.tmp_dir: str = 'tmp'

        self.latest: int = 0
        self.history: List[str] = [snippet]

    def __clean_snippet(self, code: str) -> str:
        lines = code.split('\n')
        cleaned_lines = []

        for line in lines:
            line = re.sub(r'(?m)^ *#.*\n?', '', line) # removing lines that only have comments
            if len(line) > 0 and not line.isspace():
                cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)

    def __place_original_start_marker(self, code: str) -> str:
        return '__original_start_marker = None # pragma: no cover\n' + code

    def __create_tmp_path(self) -> str:
        tmp_path = os.path.join('check_snippet.py')
        tmp_file = Path(tmp_path)
        tmp_file.parent.mkdir(parents=True, exist_ok=True)

        return tmp_path

    def __create_tmp_file(self, content=None) -> str:
        if content is None: content = self.get_latest()

        with open(os.path.join('tmp', self.tmp_path), 'w+') as tmp_file:
            try:
                tmp_file.write(content)
            except Exception as e:
                print('__create_tmp_file Exception: ' + e)

    def __delete_tmp_file(self) -> None:
        try:
            os.remove(os.path.join('tmp', self.tmp_path))
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
        lines = code_str.split('\n')
        for idx in range(len(lines)):
            if '__original_start_marker' in lines[idx]:
                lines[idx] = lines[idx] + ' # pragma: no cover'

        self.history.append('\n'.join(lines))
        self.current_iter += 1

    def get_current_iter(self) -> int:
        return self.current_iter

    def get_latest(self) -> str:
        return self.history[-1]

    def get_mocked_original(self) -> str:
        all_lines = self.get_latest().split('\n')
        start_idx = 0
        for (idx, line) in enumerate(all_lines):
            if '__original_start_marker' in line:
                start_idx = idx
        return '\n'.join(all_lines[start_idx:])

    def get_next_tbd_name(self) -> str:
        tbd_name = 'TBD'+str(self.tbd_counter)
        self.tbd_counter += 1
        return tbd_name

    def is_infinite(self) -> bool:
        proc_q = Queue()
        proc = Process(target=self.run_latest, args=(proc_q, ))
        proc.start()
        proc.join(timeout=60)
        if proc.is_alive():
            # print('\nEXECUTION TIMEOUT\n')
            proc.terminate()
            return True
        else:
            return False

    def run_timed_latest(self) -> Tuple[str, str]:
        try:
            proc_q = Queue()
            proc = Process(target=self.run_latest, args=(proc_q, ))
            proc.start()
            proc.join(timeout=Snippet.TIMEOUT)
            if proc.is_alive():
                # print('\nEXECUTION TIMEOUT\n')
                Snippet.timedout_counter += 1
                proc.terminate()
                return False
            else:
                out = proc_q.get()
                err = proc_q.get()

                if 'Error:' in err:
                    return False
                else:
                    return True
        except Exception as e:
            print('Exception: {}'.format(e))
        
        return False

    def run_latest(self, proc_q) -> Tuple[str, str]:
        try:
            # setup tmp_file at tmp_path before running
            self.__create_tmp_file()
            
            # print('\nRunning: {}\n'.format(self.tmp_path))
            proc = Popen([sys.executable, self.tmp_path], stdout=PIPE, stderr=PIPE, cwd=self.tmp_dir)
            proc.wait()
            out, err = proc.communicate()
            out = out.decode('ISO-8859-1')
            err = err.decode('ISO-8859-1')

            # cleanup tmp_file at tmp_path after running
            self.__delete_tmp_file()

            proc_q.put(out)
            proc_q.put(err)
            
            return out, err
        except FileNotFoundError as e:
            print('FileNotFoundError: when trying to run snippet {}#{}\n'.format(self.snippet_path, str(self.latest)))
            proc_q.put(None)
            proc_q.put(None)
            return None, None

    def __kill_child_processes(self, pid):
        try:
            parent = psutil.Process(pid)
            children = parent.children(recursive=True)
            for child in children:
                process.send_signal(signal.SIGTERM)
        except psutil.NoSuchProcess:
            return
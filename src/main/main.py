from path_config import PROJECT_DIR, DATA_DIR
from collections import defaultdict

from main.utils.moxecutor import Moxecutor
from main.utils.reporter import Reporter

import os

report_aggregate = {}

if __name__ == '__main__':
    path='{}/lexecutor_fails'.format(DATA_DIR)
    reporter = Reporter()
    
    for file_name in os.listdir(path):
        if file_name.endswith('snippet_45.py.orig'):
            file_path = os.path.join(path, file_name)
            
            mox = Moxecutor(snippet_path=file_path)
            report = mox.moxecute()

            reporter.collect_report(report)

    reporter.sort()
    print(reporter)

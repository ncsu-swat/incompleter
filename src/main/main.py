from path_config import PROJECT_DIR, DATA_DIR
from collections import defaultdict

from main.utils.moxecutor import Moxecutor
from main.utils.reporter import Reporter

import os
import sys

import argparse

report_aggregate = {}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', metavar='target_directory', help='The directory where the target snippets are located. The path should be with relative to the DATA_DIR of the project. Please check "src/path_config.py" for DATA_DIR reference. Possible value for this argument is most likely one of the following: ["lexecutor_success", "lexecutor_fail"]')
    parser.add_argument('-s', '--snippet_name', dest='snippet_name', metavar='snippet_name (optional)', help='If you wish to run for a single snippet, please specify the name of the snippet through this argument. E.g. "snippet_47.py.orig"', default='.orig')
    parser.add_argument('-c', '--cov', action='store_true', dest='cov', help='If you wish to compute code coverage while moxecuting the code, you can use this argument to specify that. Possible values are either True or False. Defaults to False.')
    args = parser.parse_args()

    path=os.path.join(DATA_DIR, args.dir)
    reporter = Reporter(is_cov=args.cov)
    
    for file_name in os.listdir(path):
        if file_name.endswith(args.snippet_name):
            file_path = os.path.join(path, file_name)
            
            mox = Moxecutor(snippet_path=file_path, is_cov=args.cov)
            executability_report, action_iteration_report, action_progress_report, coverage_report = mox.moxecute()

            reporter.collect_report(executability_report, action_iteration_report, action_progress_report, coverage_report)

    reporter.sort()
    print(reporter)

    sys.exit(0)

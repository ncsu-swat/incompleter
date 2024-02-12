from path_config import PROJECT_DIR, DATA_DIR
from collections import defaultdict

from main.utils.moxecutor import Moxecutor
from main.utils.reporter import Reporter

import os
import sys

import argparse
from glob import glob
from tqdm import tqdm

report_aggregate = {}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', metavar='target_directory', help='The directory where the target snippets are located. The path should be with relative to the DATA_DIR of the project. Please check "src/path_config.py" for DATA_DIR reference. Possible value for this argument is most likely one of the following: ["lexecutor_success", "lexecutor_fail"]')
    parser.add_argument('-s', '--snippet_name', dest='snippet_name', metavar='snippet_name (optional)', help='If you wish to run for a single snippet, please specify the name of the snippet through this argument. E.g. "snippet_47.py.orig"', default='.py.orig')
    parser.add_argument('-c', '--cov', action='store_true', dest='cov', help='If you wish to compute code coverage while moxecuting the code, you can use this argument to specify that. Possible values are either True or False. Defaults to False.')
    args = parser.parse_args()

    path=os.path.join(DATA_DIR, args.dir)
    reporter = Reporter(chunk_num=args.dir.split('/')[-1], is_cov=args.cov)
    
    print()
    for file_name in tqdm(glob(os.path.join(path, '*'+args.snippet_name)), desc='Moxecution (mock+execution) Progress'):
        file_path = os.path.join(path, file_name)
        
        mox = Moxecutor(snippet_path=file_path, is_cov=args.cov)
        executability_report, action_iteration_report, action_progress_report, action_sequence_length, coverage_report, unresolved_report = mox.moxecute()

        if executability_report is not None and action_iteration_report is not None and action_progress_report is not None and action_sequence_length is not None and coverage_report is not None and unresolved_report is not None:
            reporter.collect_report(file_name, executability_report, action_iteration_report, action_progress_report, action_sequence_length, coverage_report, unresolved_report)

    reporter.sort()
    reporter.compute_venn()
    print(reporter)

    sys.exit(0)

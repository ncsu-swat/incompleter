from path_config import PROJECT_DIR, DATA_DIR
from collections import defaultdict

from main.utils.moxecutor import Moxecutor

import os

report_aggregate = {}

if __name__ == '__main__':
    total_count = 0
    path='{}/lexecutor_fails'.format(DATA_DIR)
    
    for file_name in os.listdir(path):
        if file_name.endswith('.orig'):
            total_count += 1

            file_path = os.path.join(path, file_name)
    
            mox = Moxecutor(snippet_path=file_path)
            report = mox.moxecute()

            for epoch, err_type in report.items():
                if err_type not in report_aggregate.keys():
                    report_aggregate[err_type] = {}
                if epoch not in report_aggregate[err_type].keys():
                    report_aggregate[err_type][epoch] = 0
                report_aggregate[err_type][epoch] += 1

    print('\n\n===============================\nTotal errors at the beginning: {}\nError report:'.format(str(total_count)))
    for err_type, err_counts in report_aggregate.items():
        print('\n\tError type: {}'.format(err_type))
        for epoch, counts in err_counts.items():
            print('\t\tStep# {}: {} (# of err_types at this step)'.format(epoch, counts))


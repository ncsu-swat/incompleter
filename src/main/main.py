from path_config import PROJECT_DIR, DATA_DIR
from collections import defaultdict

from main.utils.moxecutor import Moxecutor

import os

if __name__ == '__main__':
    total_count = 0
    err_counts_by_steps = defaultdict(lambda: 0)
    path='{}/lexecutor_fails'.format(DATA_DIR)
    
    for file_name in os.listdir(path):
        if file_name.endswith('.orig'):
            total_count += 1

            file_path = os.path.join(path, file_name)
    
            mox = Moxecutor(snippet_path=file_path)
            is_fixed, last_epoch = mox.moxecute()

            if not is_fixed:
                err_counts_by_steps[last_epoch] += 1


    print('\n\n===============================\nTotal count: {}\nError count by steps:'.format(str(total_count)))
    for key, value in err_counts_by_steps.items():
        print('After step {}: {}\n'.format(str(key), str(value)))


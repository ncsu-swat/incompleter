from path_config import PROJECT_DIR, DATA_DIR
from main.utils.snippet import Snippet
from main.errors.error import Error

import os

if __name__ == '__main__':
    total_count = 0
    err_counts_by_steps = [0, 0]
    path='{}/LExecutorFails'.format(DATA_DIR)
    
    for file_name in os.listdir(path):
        if file_name.endswith('.orig'):
            total_count += 1

            file_path = os.path.join(path, file_name)
    
            s = Snippet(file_path)
            out, err = s.run(0)

            print('Error:\n{}\n'.format(err))

            if len(err) > 0:
                err_counts_by_steps[0] += 1
                e = Error(file_path, err)

                var_name, Action_Class = e.find_action_class()

                if var_name != None and Action_Class != None:
                    action = Action_Class(snippet=s, lineno=e.lineno, var_name=var_name, var_val=1)
                    action.apply_pattern()

                    out, err = s.run(1)
                    if len(err) > 0:
                        err_counts_by_steps[1] += 1

    print('\n\n===============================\nTotal count: {}\nError count before step 0: {}\nError count after step 0: {}\n'.format(total_count, err_counts_by_steps[0], err_counts_by_steps[1]))

    


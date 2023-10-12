from path_config import PROJECT_DIR, DATA_DIR
from main.utils.snippet import Snippet
from main.errors.error import Error

import os

if __name__ == '__main__':
    path='{}/LExecutorFails'.format(DATA_DIR)
    
    for file_name in os.listdir(path):
        if file_name.endswith('.orig'):
            file_path = os.path.join(path, file_name)
    
            s = Snippet(file_path)
            out, err = s.run(0)

            # print('Error:\n{}\n'.format(err))

            e = Error(file_path, err)
            var_name, Action_Class = e.find_action_class()

            action = Action_Class(snippet=s, lineno=e.lineno, var_name=var_name, var_val=1)
            action.apply_pattern()

    


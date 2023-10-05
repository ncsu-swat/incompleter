from main.utils.runner import Runner
from main.errors.error import Error

if __name__ == '__main__':
    path='data/LExecutorFails/snippet_45.py.orig'
    r = Runner(path)
    out, err = r.run()

    print('Error:\n{}\n'.format(err))

    e = Error(path, err)
    var_name, Action_Class = e.find_action_class()

    


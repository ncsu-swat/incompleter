from main.utils.snippet import Snippet
from main.errors.error import Error

if __name__ == '__main__':
    path='data/LExecutorFails/snippet_45.py.orig'
    s = Snippet(path)
    out, err = s.run(0)

    print('Error:\n{}\n'.format(err))

    e = Error(path, err)
    var_name, Action_Class = e.find_action_class()

    action = Action_Class(snippet=s, lineno=e.lineno, var_name=var_name, var_val=1)
    action.apply_pattern()

    


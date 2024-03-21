def func():
    is_local_var = 'a_variable' in locals()
    print(is_local_var)
func()
# Extracted from https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe

run_step = 4

# Original (run_step == 0)
# Error 1 ~ NameError: name 'df' is not defined
# Executes: false
if run_step == 0:
    count_row = df.shape[0]
    count_col = df.shape[1]

    r, c = df.shape

# Step 1 (run_step == 1)
# Action: Define a variable "df" as an integer with value 1.
# Error 1 ~ AttributeError: 'int' object has no attribute 'shape'
# Executes: false
elif run_step == 1:
    df = 1

    count_row = df.shape[0]
    count_col = df.shape[1]

    r, c = df.shape

# Step 2 (run_step == 2)
# Action: From the error, "df" is expected to be an object with an integer attribute "shape". So, I define a class "DF" with attribute "shape". I instantiate an object "df" of class "DF".
# Error 1 ~ TypeError: 'int' object is not subscriptable
# Executes: false
elif run_step == 2:
    class DF:
        shape = 1
    df = DF()

    count_row = df.shape[0]
    count_col = df.shape[1]

    r, c = df.shape

# Step 3 (run_step == 3)
# Action: Error occurred in line 35, which uses the "shape" attribute of "df" object as a subscriptable i.e. a list. So, define "shape" as an empty list of size "list_size". Arbitrarily, list_size is set as 1.
# Error 1 ~ IndexError: list index out of range
# Executes: false
elif run_step == 3:
    class DF:
        list_size = 1
        shape = [None] * list_size
    df = DF()

    count_row = df.shape[0]
    count_col = df.shape[1]

    r, c = df.shape

# Step 4 (run_step == 4)
# Action: In line 51, when accessing an element of "shape" list of "df" object, list index 1 was out of range which means we have to increase the size of the list by 1.
# Executes: true
elif run_step == 4:
    class DF:
        list_size = 2
        shape = [None] * list_size
    df = DF()

    count_row = df.shape[0]
    count_col = df.shape[1]

    r, c = df.shape
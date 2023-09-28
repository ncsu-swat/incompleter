# Extracted from https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

run_step = 0

# Original (run_step == 0)
# Error 1 ~ NameError: name 'os' is not defined
# Executes: false
if run_step == 0:
    L = [os.path.join(os.getcwd(),f) for f in os.listdir('.') if os.path.isfile(os.path.join(os.getcwd(),f))]

# Step 1 (run_step == 1)
# Action: Since 'os' is a popular python library, I am adding an import statement for 'os'
# Executes: true
elif run_step == 1:
    import os
    L = [os.path.join(os.getcwd(),f) for f in os.listdir('.') if os.path.isfile(os.path.join(os.getcwd(),f))]

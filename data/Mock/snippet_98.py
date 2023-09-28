# Extracted from https://stackoverflow.com/questions/5574702/how-do-i-print-to-stderr-in-python

run_step = 2

# Original (run_step == 0)
# Error 1 ~ NameError: name 'sys' is not defined
# Executes: false
if run_step == 0:
    print >> sys.stderr, 'spam' 

    print("spam", file=sys.stderr) 

# Step 1 (run_step == 1)
# Action: 'sys' is a popular python module. So, I import 'sys'.
# Error 1 ~ TypeError: unsupported operand type(s) for >>: 'builtin_function_or_method' and '_io.TextIOWrapper'. Did you mean "print(<message>, file=<output_stream>)"?
# Executes: false
elif run_step == 1:
    import sys
    print >> sys.stderr, 'spam' 

    print("spam", file=sys.stderr)

# Step 2 (run_step == 2)
# Action: In line 19, deprecated "print" function is used. Replace the entire print statement with the new print(...) function.
# Executes: true
elif run_step == 2:
    import sys
    print(sys.stderr, 'spam')

    print("spam", file=sys.stderr)


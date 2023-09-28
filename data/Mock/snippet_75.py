# Extracted from https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list

run_step = 1

# Original (run_step == 0)
# Error 1 ~ FileNotFoundError: yourfile.dat not found
# Executes: false
if run_step == 0:
    import numpy as np
    data = np.genfromtxt("yourfile.dat",delimiter="\n")

# Step 1 (run_step == 1)
# Action: Create file "yourfile.dat" if it does not exist.
# Warning 1 ~ UserWarning: genfromtxt: Empty input file: "yourfile.dat"
# Executes: true
if run_step == 1:
    import numpy as np

    # Action start: creating "yourfile.dat"
    from pathlib import Path
    import time
    _file = Path("yourfile.dat")
    if not _file.exists():
        with open("yourfile.dat", "w"):
            time.sleep(1)
    # Action ends

    data = np.genfromtxt("yourfile.dat",delimiter="\n")

    # Action cleanup: remove "yourfile.dat" file
    import os
    import time
    time.sleep(1)
    os.remove("yourfile.dat")
    # Action cleanup ends

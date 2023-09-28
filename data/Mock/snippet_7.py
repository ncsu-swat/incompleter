# Extracted from https://stackoverflow.com/questions/89228/how-do-i-execute-a-program-or-call-a-system-command

run_step = 2

# Original (run_step == 0)
# Error 1 ~ ValueError: creationflags is only supported on Windows platforms
# Error 2 ~ /Users/adminuser/miniconda3/envs/lexecutor/bin/python3: can't open file 'longtask.py': [Errno 2] No such file or directory
# Executes: false
if run_step == 0:
    import subprocess
    import sys

    pid = subprocess.Popen([sys.executable, "longtask.py"])
    DETACHED_PROCESS = 0x00000008
    pid = subprocess.Popen([sys.executable, "longtask.py"],
                        creationflags=DETACHED_PROCESS).pid
    pid = subprocess.Popen([sys.executable, "longtask.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

# Step 1 (run_step == 1)
# Action: Remove "creationflags" argument since error 1 mentions that "creationflags" is not supported
# Error 1 ~ /Users/adminuser/miniconda3/envs/lexecutor/bin/python3: can't open file 'longtask.py': [Errno 2] No such file or directory
# Executes: false
elif run_step == 1:
    import subprocess
    import sys

    pid = subprocess.Popen([sys.executable, "longtask.py"])
    DETACHED_PROCESS = 0x00000008
    pid = subprocess.Popen([sys.executable, "longtask.py"]).pid
    pid = subprocess.Popen([sys.executable, "longtask.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

# Step 2 (run_step == 2)
# Action: Check if "longtask.py" file exists. Otherwise, create an empty file "longtask.py" since "longtask.py" file could not be opened
# Executes: true
elif run_step == 2:
    import subprocess
    import sys

    # Action start: creating "longtask.py"
    from pathlib import Path
    import time
    _file = Path("longtask.py")
    if not _file.exists():
        with open("longtask.py", "w"):
            time.sleep(1)
    # Action ends

    pid = subprocess.Popen([sys.executable, "longtask.py"])
    DETACHED_PROCESS = 0x00000008
    pid = subprocess.Popen([sys.executable, "longtask.py"]).pid
    pid = subprocess.Popen([sys.executable, "longtask.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    # Action cleanup: remove "longtask.py" file
    import os
    import time
    time.sleep(1)
    os.remove("longtask.py")
    # Action cleanup ends
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67000739/slurm-job-nameerror-name-python3-is-not-defined
#!/usr/bin/python3

#SBATCH --job-name=testjob       # Job name
#SBATCH --output=job.%j.out      # Name of output file (%j expands to jobId)
#SBATCH --cpus-per-task=4        # Schedule one core
#SBATCH --gres=gpu               # Schedule a GPU
#SBATCH --time=71:59:59          # Run time (hh:mm:ss) - run for one hour max
#SBATCH --partition=red          # Run on either the Red or Brown queue
#SBATCH --mail-type=END          # Send an email when the job finishes
#SBATCH --export=ALL             # All of the users environment will be loaded from callers environment


from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(437637, "python3", lambda: python3) /_n_(437638, "home", lambda: home)/_n_(437639, "username", lambda: username)/_n_(437640, "test", lambda: test)/_a_(437642, _n_(437641, "test", lambda: test), "py")
_l_(437643)
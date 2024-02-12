[TNAME]:incompleter

# incompleter

### Execution Instructions

From the root directory of the project run the following commands.

1. Build a docker image as follows:
   ```
   user@host> docker build -t incompleter-docker .
   ```
2. Run the docker container and open a shell inside the container as follows:
   ```
   user@host> docker run -it incompleter-docker /bin/bash
   ```
3. Run incompleter inside the docker container as follows:
   ```
   root@container:/app/src> python3 -m main.main lexecutor_all -c
   ```

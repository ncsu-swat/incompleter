[TNAME]:incompleter

# incompleter

Requirements:
* Python 3.11

Setup:

1. Installing Python 3.11 environment (optional, if you already have Python 3.11):
   
    ```
    $> conda create --name myenv -c conda-forge python=3.11
    $> conda activate myenv
    ```

2. Install the required packages using the following command:
   ```
   (myenv)$> python3 -m pip install -r requirements.txt
   ```

3. Clone the repository using the following command:
   ```
   (myenv)$> git clone git@github.com:ncsu-swat/incompleter.git
   ```

4. CD into `incompleter/src` repository as follows:
   ```
   (myenv)$> cd incompleter/src
   ```

6. Include the project directory in the python path as follows:
   ```
   (myenv)$> PYTHONPATH=$PYTHONPATH:$PWD && export PYTHONPATH
   ```

7. Then, run the `main.main` module as follows:
    ```
    python3 -m main.main
    ```

<!--
```
$> bash create_env.sh
$> source env/bin/activate
```
-->

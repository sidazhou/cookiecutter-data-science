import os 
import subprocess

# run in scripts path
def shell_run(cmd, my_env_variables={}):
    cmd_dir = os.path.dirname(os.path.abspath(cmd))
    my_env = {**os.environ, **my_env_variables}
    
    wd = os.getcwd()
    os.chdir(cmd_dir)
    process = subprocess.Popen(cmd,
                         env=my_env,
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    status = process.returncode
    os.chdir(wd)
    
    return status, stdout, stderr

import os 
import subprocess

# run in scripts path
def shell_run(cmd):
    cmd_dir = os.path.dirname(os.path.abspath(cmd))
    
    wd = os.getcwd()
    os.chdir(cmd_dir)
    process = subprocess.Popen(cmd,
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    status = process.returncode
    os.chdir(wd)
    
    return status, stdout, stderr

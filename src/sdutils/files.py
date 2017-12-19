import os, errno
import re

def ensure_dir(dir_str):
    try:
        os.makedirs(dir_str)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    return dir_str

def root_dir(project_name):
    end_ind = re.search(project_name, os.getcwd()).end() # finds the last index of the first occurance
    return os.getcwd()[:end_ind]

def get_asset_dir_list(asset_path="../../assets", start_dir=None, end_dir=None): # assuming sorted
    '''
        dir_list_raw = ['2.0.0', '2.0.4', '2.0.2', '2.0.3', '.ipynb_checkpoints', '2.0.1', '2.0.5']
        with start_dir='2.0.1', end_dir='2.0.3' will return ['2.0.1', '2.0.2', '2.0.3']
    '''
#     print(os.path.abspath(asset_path))
    dir_list_raw = os.listdir(asset_path)
    dir_list = sorted([d for d in dir_list_raw if re.search(r'^\d+\.\d+.\d+', d)])
    
    if(end_dir):
        dir_list = dir_list[:dir_list.index(end_dir)+1]
    if(start_dir):
        dir_list = dir_list[dir_list.index(start_dir):]
        
    return dir_list

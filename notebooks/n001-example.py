# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# ### Method:
# from n000, trying method xyz, using data abc
#
# ### Notes:
# Put tmp stuff into n9xx
#
# ### Result:
# We noted that method xyz took 5 minutes to run and the result is 5% different compared to n000

# %% code_folding=[0]
############### root_dir ###############
ROOT_DIR, = !git rev-parse --show-toplevel
SRC_DIR = f'{ROOT_DIR}/src'
sys.path.append(SRC_DIR)

############### general imports ###############
import numpy as np, scipy, matplotlib.pyplot as plt, seaborn as sns, traceback, logging, pickle, csv, random, time
import datetime; DATETIME_FMT = "%Y%m%d %H:%M:%S"

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

from pdb import set_trace as bp
from sdutils.files import ensure_dir
# from sdutils.plot import plot
# from sdutils.describe import describe
from sdutils.shell import shell_run

# sdMANUAL
import pandas as pd
# import modin.pandas as pd; print('import modin.pandas as pd')

############### settings ###############

# sdMANUAL
# # %matplotlib notebook
# %matplotlib inline 
plt.style.use('seaborn-white')
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 0)

# %load_ext memory_profiler
# %load_ext autoreload
# %autoreload

# sdMANUAL
seed = int(time.time()); random.seed(seed); np.random.seed(seed); print("Seed was:", seed)
# seed = 1519972733; random.seed(seed); np.random.seed(seed); print('Warning: MANUAL seed'); print("Seed was:", seed);

# %% code_folding=[0]
# project imports

from sklearn.model_selection import GridSearchCV, ParameterGrid, RandomizedSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.base import TransformerMixin, BaseEstimator

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier, AdaBoostClassifier, RandomForestClassifier
import scikitplot as skplt
from sklearn.metrics import classification_report 
from sklearn.dummy import DummyClassifier

from imblearn.under_sampling import NearMiss
from imblearn.combine import SMOTETomek

import sklearn.model_selection
import sklearn.datasets
import sklearn.metrics

import multiprocessing

# sanity check for NUM_TAG and comfirming OUTPUT_DIR
try:
    match = re.search(r'^.\d\d\d', theNotebook)
    NUM_TAG = match.group() # will error if not found
except: 
    print('WARNING: Please check NUM_TAG and set it MANUALLY.')
    NUM_TAG = 'n001'
ASSET_DIR = f'{ROOT_DIR}/notebook_assets'
OUTPUT_DIR = ensure_dir(f'{ASSET_DIR}/{NUM_TAG}')
DATA_DIR = f'{ROOT_DIR}/data'
print(OUTPUT_DIR)

# %%
# # useful commands

# df_train = pd.read_csv('../data/xxx/file_train.csv')
# df_test = pd.read_csv('../data/xxx/file_test.csv')

# # !cat "{OUTPUT_DIR}/0_0_1_experiments_roc_summary.txt"
# # !rm "{OUTPUT_DIR}/0_0_1_experiments_roc_summary.txt"

# with open(f"{OUTPUT_DIR}/0_0_1_experiments_roc_summary.txt", "a") as fp:
#     print('hep', file= fp )

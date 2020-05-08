Project Name
==============================

A short description of the project.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── assets
    │   └── a000           <- figures, pickles, intermediate stuff from notebook goes here
    │   └── a001           <- figures, pickles, intermediate stuff from notebook goes here
    │   └── a002           <- figures, pickles, intermediate stuff from notebook goes here
    │
    ├── data
    │   ├── d001-local_data          <- Contains all necessary information to reproduce the dataset
    │   ├── d002-hdfs_data           <- Contains all necessary information to reproduce the dataset
    │   └── d003-other_data          <- Contains all necessary information to reproduce the dataset
    │
    ├── docker             <- Contains the whole environment
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── experiment_notes
    │   ├── e001-init             <- Contains any misc notes
    │   ├── e002-20200501         <- Contains any misc notes
    │   └── e003-20200504         <- Contains any misc notes
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks.
    │   └── n001-exp1                      <- ipynb, save all extra files in ../assets
    │   └── n002-more_weight-from_exp1     <- ipynb, save all extra files in ../assets
    │   └── n003-a_new_start               <- ipynb, save all extra files in ../assets
    │
    ├── references         <- bibtex files, relevant papers
    │
    ├── reports            <- Summaries of notebooks
    │   └── r001-n001ton005-summary.dio            <- flowchart of the notebooks
    │   └── r001-n001ton005-summary.csv            <- data to csv table, exportable to subl or excel for manual addition
    │   └── r001-n001ton005-summary.ipnb           <- use qgrid to interactively view summary tables
    │
    ├── requirements.txt   <- Using docker instead.  # generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   ├── metric         <- Scripts calculate difference metrics
    │   │   ├── m001-custom-euc.py
    │   │   └── m002-custom-cos.py
    │   │
    │   ├── sdutils        <- Utility functions
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

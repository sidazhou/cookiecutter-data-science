import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
import scipy
import random


def plot_df(df):
    df = df.fillna(df.mean())
    col_names = list(df)

    fig = plt.figure()
    ax = plt.gca()

    colors=iter(plt.cm.rainbow(np.linspace(0,1,len(col_names))))

    for col_name in col_names:
        df_described = df.groupby(df.index).describe()
        xs = df_described.index
        maxs = df_described[col_name]['max']
        means = df_described[col_name]['mean']
        mins = df_described[col_name]['min']
        ax.errorbar(xs, means, yerr=np.vstack((means-mins, maxs-means)), fmt='o-', alpha=0.55, color=next(colors))

        plt.xticks(xs)

    plt.legend(col_names)
    return fig
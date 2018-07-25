import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
import scipy
import random

from mpl_toolkits.axes_grid.inset_locator import inset_axes, InsetPosition


# private
def prettify_M(M, aspect_ratio = 50):
    if (M.shape[0] > M.shape[1]):
        M = scipy.sparse.csc_matrix.transpose(M)
        print('INFO: scipy.sparse.csc_matrix.transpose(M) is called')

    # take a pretty sub-sample for plotting
    if (aspect_ratio * M.shape[0] < M.shape[1]):
        num_cols = aspect_ratio * M.shape[0]
        start_ind = random.randint(0, M.shape[1] - num_cols)
        end_ind = start_ind + num_cols

        M = M[:, start_ind:end_ind]
        print('INFO: M = M[:,start_ind:end_ind] is called with',
              'start_ind =', start_ind,
              'end_ind =', end_ind,
             )

    return M

def describe_M(M, **opts):
    print('M.max:', M.max())
    print('M.min:', M.min())
    print('M.mean:', M.mean())

    fig, ax = plt.subplots(1, 2, figsize=(14, 7))

    plt.sca(ax[0])
    matshow(M, **opts.get('plot1',{})) # self.draw_networkx
    plt.sca(ax[1])
    spy(M, **opts.get('plot2', {}) )

'''
    Always to dense matrix
'''
def matshow(M, **opt):
    M = prettify_M(M)

    if scipy.sparse.issparse(M):
        M = M.todense()
        print('INFO: M.todense() is called')

    fig = plt.gcf()
    ax = plt.gca()
    h = ax.matshow(M, **opt)
    # plt.yticks(range(len(M.columns)), M.columns);
    #cbar_ax = ax.add_axes([0.09, 0.06, 0.84, 0.02]) # fig.colorbar(... , cax=cbar_ax)


    cbar_ax = inset_axes(ax,
                        width="100%", # width = 30% of parent_bbox
                        height="3%", # heigh=1.
                        loc=3
                        )
    fig.colorbar(h, ax=ax, cax=cbar_ax, orientation="horizontal")

    plt.set_cmap('Greys')
    plt.title("matshow")


def spy(M, **opt):
    M = prettify_M(M)
    plt.spy(M, **{**{'markersize':2.5}, **opt})
    plt.title("spy")

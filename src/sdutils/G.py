import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
import scipy
import random

import networkx as nx
import networkx as networkx
import collections


def plot_cores(G):
    fig, ax = plt.subplots(1, 4, figsize=(30, 7.5))
    n_core = nx.core_number(G)
    pos = nx.spring_layout(G)

    plt.sca(ax[0])
    nx.draw_networkx(G, pos,
                     node_list = list(n_core.keys()),
                     node_color = list(n_core.values()),
                     cmap=plt.cm.bwr)
    plt.title('nx.core_number')
    xlim = plt.gca().get_xlim()
    ylim = plt.gca().get_ylim()

    plt.sca(ax[1])
    nx.draw_networkx(nx.k_core(G,core_number=n_core), pos,
                     cmap=plt.cm.bwr)
    plt.title('nx.k_core')
    plt.xlim(xlim)
    plt.ylim(ylim)

    plt.sca(ax[2])
    nx.draw_networkx(nx.k_shell(G,core_number=n_core), pos,
                     cmap=plt.cm.bwr)
    plt.title('nx.k_shell')
    plt.xlim(xlim)
    plt.ylim(ylim)

    plt.sca(ax[3])
    nx.draw_networkx(nx.k_crust(G,core_number=n_core), pos,
                     cmap=plt.cm.bwr)
    plt.title('nx.k_crust')
    plt.xlim(xlim)
    plt.ylim(ylim)

def plot_centralities(G):
    # private
    def centrality_scatter(dict1, dict2, xlabel="",ylabel=""):
        ax = plt.gca()
        # Create items and extract centralities
        items1 = sorted(dict1.items())
        items2 = sorted(dict2.items())
        xdata=[b for a,b in items1]
        ydata=[b for a,b in items2]
        # Add each actor to the plot by ID
        for p in np.arange(len(items1)):
             ax.text(x=xdata[p], y=ydata[p],s=str(items1[p][0]), color="b")

        # Set new x- and y-axis limits
        plt.xlim((0.0,max(xdata)+(.15*max(xdata))))
        plt.ylim((0.0,max(ydata)+(.15*max(ydata))))
        # Add labels and save
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

    fig = plt.figure(figsize=(30, 10))
    ax1 = plt.subplot2grid((1, 3), (0, 0))
    ax2 = plt.subplot2grid((1, 3), (0, 1))
    ax3 = plt.subplot2grid((1, 3), (0, 2))

    # Betweenness centrality
    bet_cen = nx.betweenness_centrality(G)
    # Closeness centrality
    clo_cen = nx.closeness_centrality(G)
    # Eigenvector centrality
    eig_cen = nx.eigenvector_centrality(G)

    plt.sca(ax1)
    centrality_scatter(bet_cen, eig_cen, xlabel="bet_cen",ylabel="eig_cen")
    plt.sca(ax2)
    centrality_scatter(bet_cen, clo_cen, xlabel="bet_cen",ylabel="clo_cen")
    plt.sca(ax3)
    centrality_scatter(clo_cen, eig_cen, xlabel="clo_cen",ylabel="eig_cen")

def plot_degree_histogram(G, **opt):
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
    # print "Degree sequence", degree_sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())

    plt.bar(deg, cnt, **{**{'width':0.80, 'color':'b'}, **opt} )
    plt.xlim([0,100])

    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax = plt.gca()
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)

def draw_networkx(G, **opt):
    nx.draw_networkx(G, **{**{'node_size':30, 'alpha':0.5, 'with_labels':False}, **opt})
    plt.title("draw_networkx")

def draw_circular(G, **opt):
    nx.draw_circular(G, **{**{'node_size':30, 'alpha':0.5, 'with_labels':False}, **opt})
    plt.title("draw_circular")

def draw_random(G, **opt):
    nx.draw_random(G, **{**{'node_size':30, 'alpha':0.5, 'with_labels':False}, **opt})
    plt.title("draw_random")

def describe_G(G, **opts):
    print('Number of nodes:',G.number_of_nodes())
    print('Number of edges:',G.number_of_edges())
    print('---------------------------------')

    print('Min degree:', np.min([d for n, d in G.degree()]))
    print('Max degree:', np.max([d for n, d in G.degree()]))
    print('Mean degree:', np.mean([d for n, d in G.degree()]))
    print('---------------------------------')

    fig = plt.figure(figsize=(15, 15))
    ax1 = plt.subplot2grid((2, 2), (0, 0))
    ax2 = plt.subplot2grid((2, 2), (0, 1))
    ax3 = plt.subplot2grid((2, 2), (1, 0))
    ax4 = plt.subplot2grid((2, 2), (1, 1))

    plt.sca(ax1)
    plt.spy(nx.adjacency_matrix(G), **{**{'markersize':10}, **opts.get('plot1',{})} )
    plt.title('plt.spy adjacency_matrix (unordered)')
    plt.sca(ax2)
    plot_degree_histogram(G, **opts.get('plot2',{}) )
    if (len(G) <= 99):
        print('Degree Assortativity Coeff:', nx.degree_assortativity_coefficient(G))
        print('Clustering Coeff:', nx.average_clustering(G))
        print('---------------------------------')

        plt.sca(ax3)
        draw_networkx(G, **opts.get('plot3',{})) # self.draw_networkx
        plt.sca(ax4)
        draw_networkx(G, **{**{'node_size':300, 'alpha':0.5, 'with_labels':True}, **opts.get('plot4',{})}) # self.draw_networkx
    else:
        ax3.remove()
        ax4.remove()
        print('INFO: len(G) > 99, skipping time consuming plots...')

    print('INFO: See also plot_centralities()')
    print('INFO: See also plot_cores()')

# NOT USED
# def prettify_G(G, G_size=99):
#     centrality = nx.eigenvector_centrality(G) # returns dict of (node_id: score)
#     # take top G_size=99 as the sub graph
#     sub_graph_nodes = list(map(lambda x: x[0], sorted(centrality.items(), key = lambda x: x[1], reverse=True)))[0:G_size]

#     print('INFO: G.subgraph() is called')
#     return G.subgraph(sub_graph_nodes)






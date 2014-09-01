# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 16:33:54 2014

@author: lachmaxwell
"""

import digraph
import loadcitation
import ergraph
from matplotlib.pyplot import *
def make_plot(digraph_dist):
	normalized_degree = {}
	total = 0
	for degree in digraph_dist:
    		total = total + digraph_dist[degree]
	for degree in digraph_dist:
    		normalized_degree[degree] = float(digraph_dist[degree])/float(total)
	x = normalized_degree.keys()
	y = normalized_degree.values()
	loglog(x,y,'ro',alpha=0.5)
	show()
#import matplotlib.pyplot as plt
citation_graph = loadcitation.load_graph(loadcitation.CITATION_URL)
print "Graph loaded, now computing degrees"
(in_distribution,out_distribution) = digraph.degree_distribution(citation_graph)
make_plot(in_distribution)
er_graph = ergraph.make_directed_er_graph(2000,.1)
er_distribution = digraph.in_degree_distribution(er_graph)
make_plot(er_distribution)

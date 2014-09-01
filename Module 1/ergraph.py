# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 17:42:16 2014

@author: lachmaxwell
"""
import random
random.seed(5)
def make_directed_er_graph(num_nodes,p) :
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete directed graph with the specified number of nodes

    """
    complete_graph = {}
    if (num_nodes <= 0):
        return complete_graph
    for node_index in range(num_nodes) :
        # Loop through all possible nodes and edges, adding edges to set
        complete_graph[node_index] = set([])
        for edge_index in range(num_nodes) :
            if (node_index != edge_index) :
                val = random.random()
                if (val < p):
                    complete_graph[node_index].add(edge_index)
    return complete_graph
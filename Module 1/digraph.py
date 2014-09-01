# -*- coding: utf-8 -*-
"""
Degree distribution of graphs

"""
EX_GRAPH0 = {0 : set([1,2]), 1 : set([]), 2: set([])}
EX_GRAPH1 = {0 : set([1,4,5]), 1 : set([2,6]), 2: set([3]), 3 : set([0]), 4 : set([1]), 5 : set([2]), 6 : set([])}
EX_GRAPH2 = {0 : set([1,4,5]), 1 : set([2,6]), 2 : set([3,7]), 3 : set([7]), 4 : set([1]), 5 : set([2]), 6 : set([]), 7 : set([3]), 8 : set([1,2]), 9 : set([0,3,4,5,6,7])}
EX_GRAPH3 = {0 : set([1,4,5]), 1 : set([2,6]), 2 : set([3,7]), 3 : set([0,7]), 4 : set([1]), 5 : set([2]), 6 : set([]), 7 : set([3,4])}



def make_complete_graph(num_nodes) :
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
                complete_graph[node_index].add(edge_index)
    return complete_graph
def compute_in_degrees_slow(digraph) :
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the in-degrees for the nodes in the graph
    return a dictionary with the same set of keys (nodes) as digraph 
    whose corresponding values are the number of edges whose head matches a particular node.
    """
    in_degrees = {}
    for node_index in (digraph) :
        in_degrees[node_index] = 0
        #iterate through all nodes searching for in-links
        for search_node in (digraph) :
            for edge_index in (digraph[search_node]) :
                #increment counter of in-links for node
                if (edge_index == node_index) :
                    in_degrees[node_index] = in_degrees[node_index] + 1
    return in_degrees
def compute_degrees(digraph) :
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the in-degrees for the nodes in the graph
    return a dictionary with the same set of keys (nodes) as digraph 
    whose corresponding values are the number of edges whose head matches a particular node.
    """
    in_degrees = {}
    out_degrees = {}
    for node_index in (digraph) :
        #in_degrees[node_index] = 0
        #iterate through all nodes searching for in-links
        out_degrees[node_index] = 0
        if (node_index not in in_degrees) :
            in_degrees[node_index] = 0
        for edge_index in (digraph[node_index]) :
            #increment counter of in-links for node
            out_degrees[node_index] = out_degrees[node_index] + 1
            if (edge_index in in_degrees) :
                in_degrees[edge_index] = in_degrees[edge_index] + 1
            else :
                in_degrees[edge_index] = 1
    return (in_degrees,out_degrees)
def compute_in_degrees(digraph) :
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the in-degrees for the nodes in the graph
    return a dictionary with the same set of keys (nodes) as digraph
    whose corresponding values are the number of edges whose head matches a particular node.
    """
    in_degrees = {}
    for node_index in (digraph) :
        #in_degrees[node_index] = 0
        #iterate through all nodes searching for in-links
        if (node_index not in in_degrees) :
            in_degrees[node_index] = 0
        for edge_index in (digraph[node_index]) :
            #increment counter of in-links for node
            if (edge_index in in_degrees) :
                in_degrees[edge_index] = in_degrees[edge_index] + 1
            else :
                in_degrees[edge_index] = 1
    return in_degrees
def in_degree_distribution(digraph) :
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the unnormalized distribution of the in-degrees of the
    graph. The function returns a dictionary whose keys correspond to in-degrees of nodes in the graph. The value associated with each
    particular in-degree is the number of nodes with that in-degree. In-degrees with no corresponding nodes in the graph are not included
    in the dictionary.
    """
    in_degree_distributions = {}
    in_degrees = compute_in_degrees(digraph)
    for node_index in (in_degrees) :
        # map names of distribution dictionary to values of in_degree dictionary
        if (in_degrees[node_index] in in_degree_distributions) :
            in_degree_distributions[in_degrees[node_index]] = in_degree_distributions[in_degrees[node_index]] + 1
        else :
            in_degree_distributions[in_degrees[node_index]] = 1
    return in_degree_distributions

def degree_distribution(digraph) :
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the unnormalized distribution of the in-degrees of the 
    graph. The function returns a dictionary whose keys correspond to in-degrees of nodes in the graph. The value associated with each 
    particular in-degree is the number of nodes with that in-degree. In-degrees with no corresponding nodes in the graph are not included
    in the dictionary.
    """
    in_degree_distributions = {}
    out_degree_distributions = {}
    (in_degrees,out_degrees) = compute_degrees(digraph)
    for node_index in (in_degrees) :
        # map names of distribution dictionary to values of in_degree dictionary
        if (in_degrees[node_index] in in_degree_distributions) :
            in_degree_distributions[in_degrees[node_index]] = in_degree_distributions[in_degrees[node_index]] + 1
        else :
            in_degree_distributions[in_degrees[node_index]] = 1
    for node_index in (out_degrees) :
        # map names of distribution dictionary to values of in_degree dictionary
        if (out_degrees[node_index] in out_degree_distributions) :
            out_degree_distributions[out_degrees[node_index]] = out_degree_distributions[out_degrees[node_index]] + 1
        else :
            out_degree_distributions[out_degrees[node_index]] = 1
    return (in_degree_distributions,out_degree_distributions)
    
#print(in_degree_distribution(EX_GRAPH3))
#print(compute_in_degrees(make_complete_graph(5)))              


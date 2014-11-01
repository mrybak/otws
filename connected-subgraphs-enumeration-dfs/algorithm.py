"""
    Prints out all connected subgraphs of G using DFS.

    :param G examined graph
"""


def dfs_enumerate(G):
    keys = keys_sorted_by_degree(G)
    keys.reverse()
    # print "keys: ", keys
    G = sort_neighbour_list_by_degree(G)
    # print G
    for i, v in enumerate(keys):
        # initialize dfs search from the node with highest degree
        dfs_enumerate_rec(G, [v], [v], keys[:i], 1)


"""
    :param G examined graph
    :param path contains all visited nodes
    :param S a set of nodes that are forming connected subgraph
    :param X a set of excluded nodes
    :param start_from which neighbour of node do we start from
    (this is to avoid redundant recursive calls for already excluded nodes)
    # ???


    For each node v we first search for all subgraphs containing v,
    then add v to excluded nodes to find all subgraphs not containing v.
"""


def dfs_enumerate_rec(G, path, S, X, start_from):
    v = path[-1]                                                # last visited node
    for i in range(start_from, len(G[v])):                      # iterate over neighbours of v, starting from...
        n = G[v][i]                                             # neighbour we'll work with
        if n not in S and n not in X:                           # if it is yet unprocessed...
            dfs_enumerate_rec(G, path + [n], S + [n], X, 1)     # add it to subgraph and search starting from it
            X += [n]                                            # then add to excluded nodes and proceed to next neighbour
    path.pop()                                                  # backtrack
    if len(path) > 0:                                           # if we still have nodes in our path from root
        last_node = path[-1]                                    # node we've backtracked to
        start_from = G[last_node].index(v) + 1                  # start from next node after v
        dfs_enumerate_rec(G, path, S, X, start_from)            # continue
    else:
        print S                                                 # we've found a subgraph



def keys_sorted_by_degree(G):
    return sorted(G.keys(), key=lambda v: len(G[v]))


def sort_neighbour_list_by_degree(G):
    for key, neighbour_list in G.items():
        G[key] = sorted(neighbour_list, key=lambda v: len(G[v]))
        G[key].reverse()
    return G

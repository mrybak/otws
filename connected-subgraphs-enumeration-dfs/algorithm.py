"""
    Prints out all connected subgraphs of G using DFS.

    :param G examined graph
"""


def dfs_enumerate(G):
    keys = keys_sorted_by_degree_desc(G)
    sort_neighbour_list_by_degree_desc(G)
    for i, v in enumerate(keys):
        dfs_enumerate_rec(G, [v], [v], keys[:i], 0)


"""
    :param G examined graph
    :param path contains all visited nodes
    :param S a set of nodes that are forming connected subgraph
    :param X a set of excluded nodes
    :param start_from which neighbour of node do we start from
    (this is to avoid redundant recursive calls for already excluded nodes)

    For each node v we first search for all subgraphs containing v,
    then add v to excluded nodes to find all subgraphs not containing v.
"""


def dfs_enumerate_rec(G, path, S, X, start_from):
    # we create copy of X; otherwise changes in X made by recursive calls would be reflected in current call, which is undesired
    newX = X[:]

    v = path[-1]  # last visited node

    for i in range(start_from, len(G[v])):
        n = G[v][i]
        if n not in S and n not in X:
            # first: add this (unprocessed) node to subgraph and continue search starting from it
            dfs_enumerate_rec(G, path + [n], S + [n], X, start_from)
            # second: add it to excluded nodes and proceed to next neighbour
            newX += [n]
    # if we reached this line, all neighbours of v are processed; time to backtrack:
    path.pop()

    if len(path) > 0:
        last_node = path[-1]  # node we've backtracked to
        start_from = G[last_node].index(v) + 1  # start from next node after v
        dfs_enumerate_rec(G, path, S, newX, start_from)
    else:
        # search is over
        print S


def keys_sorted_by_degree_desc(G):
    keys = sorted(G.keys(), key=lambda v: len(G[v]))
    keys.reverse()
    return keys


def sort_neighbour_list_by_degree_desc(G):
    for key, neighbour_list in G.items():
        G[key] = sorted(neighbour_list, key=lambda v: len(G[v]))
        G[key].reverse()
    return G

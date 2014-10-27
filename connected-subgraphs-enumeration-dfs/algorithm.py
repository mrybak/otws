def keys_sorted_by_degree(G):
    return sorted(G.keys(), key = lambda v: len(G[v]))


def DFSEnumerateRec(G, path, S, X, startFrom):
    v = path[-1]
    for i in range(startFrom, len(G[v])):
        n = G[v][i]
        if n not in S and n not in X:
            DFSEnumerateRec(G, path + [n], S + [n], X, 1)
            X += [n]
    path.pop()
    if len(path) > 0:
        startFrom = G[path[-1]].index(v) + 1
        DFSEnumerateRec(G, path, S, X, startFrom)
    else:
        print S


def DFSEnumerate(G):
    keys = keys_sorted_by_degree(G)
    keys.reverse()
    for i, v in enumerate(keys):
        DFSEnumerateRec(G, [v], [v], keys[:i], 1)


from algorithm import dfs_enumerate

G = dict()

G[1] = [2,3,4]
G[2] = [1,3]
G[3] = [1,2]
G[4] = [1]

print "ENUMERATING G: "
dfs_enumerate(G)


# 4
# |
# 1--2
# | /
# 3



G2 = dict()

G2[1] = [2]
G2[2] = [1,3]
G2[3] = [2]
G2[4] = []

# 4
#
# 1--2--3

print "ENUMERATING G2: "
dfs_enumerate(G2)
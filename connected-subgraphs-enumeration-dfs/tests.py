from algorithm import DFSEnumerate

G = dict()

G[1] = [2,3,4]
G[2] = [1,3]
G[3] = [1,2]
G[4] = [1]

# 4
# |
# 1--2
# | /
# 3



DFSEnumerate(G)
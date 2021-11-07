import numpy as np
from sklearn.neighbors import NearestNeighbors


samples =[[0,0,2],[1,0,0],[0,0,1]]


# 3つの配列のうちどれが一番近いか
# n_neighborsは探す対象の数
neigh =NearestNeighbors(n_neighbors=1)
neigh.fit(samples)


# return値は距離とindex
print(neigh.kneighbors([[1.,1.,1.]]))
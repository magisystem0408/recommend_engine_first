import pandas as pd
from sklearn.neighbors import NearestNeighbors

# アイテムベースの投稿フィルタリングで映画をリコメンド



df =pd.read_csv("ml-latest/ratings.csv")

# 疎行列(ほとんどの要素が0の行列)を作成する。
# indexをmovieIdにセットする +ベクトル化
df_rating =df.pivot(index="movieId",columns="userId",values="rating").fillna(0)

print(df_rating.head())

# 最近某探索
neigh =NearestNeighbors(metric="cosine")

# 学習
neigh.fit(df_rating)

neigh.kneighbors([[1,1,1.]])
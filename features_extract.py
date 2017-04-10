import pandas as pd
import numpy as np

"""
Get features vector by sku_id
通过sku_id获取商品特征向量

若之前没有计算过，则重新计算，然后将结果保存在'../sku_feature.csv'中；
若计算过，直接查找'../sku_feature.csv'中的结果。

Args:
    sku_id: str类型，商品ID

Returns:
    numpy.array类型，n * 1的矩阵，商品特征向量
"""
def get_features_by_sku_id(sku_id):
    pass


"""
Get features vector by user_id
通过user_id获取用户特征向量

若之前没有计算过，则重新计算，然后将结果保存在'../user_feature.csv'中；
若计算过，直接查找'../user_feature.csv'中的结果。

Args:
    user_id: 用户ID

Returns:
    numpy.array类型，n * 1的矩阵，用户特征向量
"""
def get_features_by_user_id(user_id):
    pass


"""
通过用户的特征向量对用户进行聚类
聚类的结果保存在'../user_cluster.csv'中
（也可以加入用户的特征向量中）

Args:
    N: int类型，聚类个数

Returns:
    void
"""
def user_id_clustering(N = 100):
    pass


"""
通过商品的特征向量对商品进行聚类
聚类的结果保存在'../sku_cluster.csv'中
（也可以加入商品的特征向量中）

Args:
    N: int类型，聚类个数

Returns:
    void
"""
def sku_id_clustering(N = 100):
    pass
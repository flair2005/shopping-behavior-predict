import pandas as pd
import numpy as np

"""
通过user_id获取该用户喜欢的商品

Args:
    user_id: str类型，用户ID

Returns:
    list类型，商品列表
"""
def get_favourite_sku_id_by_user_id(user_id):
    pass


"""
通过user_id获取与该用户相似的用户列表
在返回结果中：
    特征向量最相似的用户个数占10%；
    聚类结果属于同一类的用户占20%；
    浏览相同商品最多的用户占10%；
    加入购物车相同商品最多的用户占10%；
    下单相同商品最多的用户占30%；
    关注相同商品最多的用户占10%；
    点击相同商品最多的用户占10%；

Args:
    user_id: str类型，用户ID
    N: int类型，返回的最大结果数目

Returns:
    list类型，用户列表
"""
def get_similar_user(user_id):
    pass


"""
通过sku_id获取与该商品相似的商品列表
在返回结果中：
    特征向量最相似的商品个数占10%；
    聚类结果属于同一类的商品占20%；
    同时被同一个购买过的商品占70%；

Args:
    sku_id: str类型，商品ID
    N: int类型，返回的最大结果数目

Returns:
    list类型，商品列表
"""
def get_similar_sku(sku_id):
    pass
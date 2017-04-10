import pandas as pd
import numpy as np

"""
求某一商品的所有用户的行为集合，并保存在文件中，方便之后的读取。

等同于数据库操作：
SELECT * 
FROM JData_Action
WHERE sku_id = 'xxxxx'

商品ID为sku_id，保存在'../sku_action/sku_id.csv'当中

Args:
    void

Returns:
    void
"""
def get_action_by_sku_id():
    pass


"""
求某一用户的所有行为集合，并保存在文件中，方便之后的读取。

等同于数据库操作：
SELECT * 
FROM JData_Action
WHERE user_id = 'xxxxx'

用户ID为user_id，保存在'../user_action/user_id.csv'当中

Args:
    void

Returns:
    void
"""
def get_action_by_user_id():
    pass


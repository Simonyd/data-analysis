import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import  association_rules

pd.set_option('display.width', 300) # 设置字符显示宽度
pd.set_option('display.max_rows', None) # 设置显示最大行
pd.set_option('display.max_columns', None)

###################关联分析
''''
目的：找出物品间的关联规则
算法：Apriori算法
详解：以超市为例，
1. 找出频繁购买项集合。如{{啤酒,尿布},{鸡蛋,牛奶},{香蕉,苹果}}
2. 使用关联算法找出物品的关联结果。
支持度support= 包含A物品的记录数量/ 总记录数量。（表示A物品出现的概率P(A)、流行程度）
置信度（A->B）confidence= P(AB)/P(A) .（即条件概率P(B|A)）
提升度（A->B）lift = P(B|A)/P(A) . （lift = 1 无关联;>1，正相关；<1负相关）
关联程度主要看置信度和提升度。
3. Apriori的作用是找出物品中的频繁项集,计算各相集出现的概率。（递归）
4. 函数介绍
def apriori(df, min_support=0.5, use_colnames=False,max_len=None)
参数如下：
df：就是我们的数据集。
min_support：给定的最小支持度。
use_colnames：默认False，则返回的物品组合用编号显示，为True的话直接显示物品名称。
max_len：最大物品组合数，默认是None，不做限制。如果只需要计算两个物品组合的话，便将这个值设置为2。
'''
def loadset():
    data = {'ID': [1, 2, 3, 4, 5, 6],
            'Onion': [1, 0, 0, 1, 1, 1],
            'Potato': [1, 1, 0, 1, 1, 1],
            'Burger': [1, 1, 0, 0, 1, 1],
            'Milk': [0, 1, 1, 1, 0, 1],
            'Beer': [0, 0, 1, 0, 1, 0]}
    df = pd.DataFrame(data)
    df1 = df[['Onion','Potato','Burger','Milk','Beer']]
    frequent_itemsets = apriori(df1,min_support=0.5,use_colnames=True,max_len=2)
    print(frequent_itemsets)

    rules = association_rules(frequent_itemsets,metric='lift',min_threshold=1)
    print(rules)

def loadset2():
    file_path = 'F:\\DATALIB\\dataset.xlsx'
    df = pd.read_excel(file_path)
    frequent_itemsets = apriori(df,min_support=0.1,use_colnames=True,max_len=2)
    print(frequent_itemsets)

    rules = association_rules(frequent_itemsets,metric='lift',min_threshold=1)
    print(rules)
    rules_result = rules[rules['support'] <= 0.8]
    print(rules_result)

if __name__ == "__main__":
    loadset2()
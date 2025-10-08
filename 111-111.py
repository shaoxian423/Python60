import pandas as pd
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
df = pd.DataFrame({'Name': ['A', 'B'], 'Sales': [200, 300]})
df.loc[0, 'Sales']  # 按标签
df.iloc[1, 0]       # 按位置

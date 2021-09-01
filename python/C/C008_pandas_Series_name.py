# 참조 - https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html

import pandas as pd
import numpy as np

# name

# 시리즈의 이름을 반환

s = pd.Series([1, 2, 3], dtype=np.int64, name='Numbers')
print(s)
# 0    1
# 1    2
# 2    3
# Name: Numbers, dtype: int64

s.name = "Integers"
print(s)
# 0    1
# 1    2
# 2    3
# Name: Integers, dtype: int64

df = pd.DataFrame([[1, 2], [3, 4], [5, 6]],
                  columns=["Odd Numbers", "Even Numbers"])
print(df)
#    Odd Numbers  Even Numbers
# 0            1             2
# 1            3             4
# 2            5             6

print(df["Even Numbers"].name)
# Even Numbers
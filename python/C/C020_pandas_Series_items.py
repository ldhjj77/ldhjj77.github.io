# 참조 - https://pandas.pydata.org/docs/reference/api/pandas.Series.items.html

import pandas as pd
import numpy as np

# items 

# Series.items
# 튜플을 천천히 반복


s = pd.Series(['A', 'B', 'C'])
for index, value in s.items():
    print(f"Index : {index}, Value : {value}")
# Index : 0, Value : A
# Index : 1, Value : B
# Index : 2, Value : C



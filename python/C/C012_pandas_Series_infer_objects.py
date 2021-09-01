# 참조 - https://pandas.pydata.org/docs/reference/api/pandas.Series.infer_objects.html

import pandas as pd
import numpy as np

# infer_objects
# 개체 열에 대해 더 나은 dtypes를 추론하려고 시도



df = pd.DataFrame({"A": ["a", 1, 2, 3]})
df = df.iloc[1:]
print(df)
#    A
# 1  1
# 2  2
# 3  3

print(df.dtypes)
# A    object
# dtype: object

print(df.infer_objects().dtypes)
# A    int64
# dtype: object



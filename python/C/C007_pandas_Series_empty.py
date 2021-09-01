# 참조 - https://pandas.pydata.org/docs/reference/api/pandas.Series.empty.html

import pandas as pd
import numpy as np

# empty

# DataFrame이 비어 있는지 여부를 표시



df_empty = pd.DataFrame({'A' : []})
print(df_empty)
# Empty DataFrame
# Columns: [A]
# Index: []

print(df_empty.empty)
# True


df = pd.DataFrame({'A' : [np.nan]})
print(df)
#     A
# 0 NaN

print(df.empty)
# False

print(df.dropna().empty)
# True
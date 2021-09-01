# 참조 - https://pandas.pydata.org/docs/reference/api/pandas.Series.bool.html

import pandas as pd
import numpy as np

# bool
# 단일 요소 Series 또는 DataFrame의 bool을 반환


# 이 메서드는 부울 값이 있는 단일 요소 개체에 대해서만 작동
print(pd.Series([True]).bool())
# True
print(pd.Series([False]).bool())
# False


print(pd.DataFrame({'col': [True]}).bool())
# True
print(pd.DataFrame({'col': [False]}).bool())
# False
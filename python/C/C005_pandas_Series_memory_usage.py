# 참조 - https://pandas.pydata.org/docs/reference/api/pandas.Series.memory_usage.html#

import pandas as pd
import numpy as np

# memory_usage

# Series의 메모리 사용량을 반환


s = pd.Series(range(3))
print(s.memory_usage())
# 152

print(s.memory_usage(index=False))
# 24

s = pd.Series(["a", "b"])
print(s.values)
# ['a' 'b']

print(s.memory_usage())
# 144

print(s.memory_usage(deep=True))
# 244


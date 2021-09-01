# 참조 - https://pandas.pydata.org/docs/reference/api/pandas.Series.flags.html

import pandas as pd
import numpy as np

# flags / set_flags

# 이 pandas 객체와 관련된 속성을 가져옴


df = pd.DataFrame({"A": [1, 2]})
print(df.flags)
# <Flags(allows_duplicate_labels=True)>


print(df.flags.allows_duplicate_labels)
True
df.flags.allows_duplicate_labels = False



print(df.flags["allows_duplicate_labels"])
False
df.flags["allows_duplicate_labels"] = True



## set_flags
## 업데이트된 플래그가 있는 새 객체를 반환

df = pd.DataFrame({"A": [1, 2]})
print(df.flags.allows_duplicate_labels)
# True
df2 = df.set_flags(allows_duplicate_labels=False)
print(df2.flags.allows_duplicate_labels)
# False

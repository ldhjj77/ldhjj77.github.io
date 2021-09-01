# 참조 - https://pandas.pydata.org/docs/reference/api/pandas.Series.values.html

import pandas as pd
import numpy as np

# values


print(pd.Series([1, 2, 3]).values)
# [1 2 3]

print(pd.Series(list('aabc')).values)
# ['a' 'a' 'b' 'c']

print(pd.Series(list('aabc')).astype('category').values)
# ['a', 'a', 'b', 'c']
# Categories (3, object): ['a', 'b', 'c']

print(pd.Series(pd.date_range('20130101', periods=3,
                        tz='US/Eastern')).values)
# ['2013-01-01T05:00:00.000000000' '2013-01-02T05:00:00.000000000'
#  '2013-01-03T05:00:00.000000000']
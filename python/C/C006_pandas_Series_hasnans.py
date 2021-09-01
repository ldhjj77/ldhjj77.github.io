# 참조 - https://www.geeksforgeeks.org/python-pandas-index-hasnans/

import pandas as pd
import numpy as np

# hasnans

# nans값이 있으면 반환


idx = pd.Index(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
  
# Print the index
print(idx)
# Index(['Jan', 'Feb', 'Mar', 'Apr', 'May'], dtype='object')

result = idx.hasnans
  

print(result)
# False

idx = pd.Index(['2012-12-12', None, '2002-1-10', None])
  

print(idx)
# Index(['2012-12-12', None, '2002-1-10', None], dtype='object')

result = idx.hasnans
  

print(result)
# True
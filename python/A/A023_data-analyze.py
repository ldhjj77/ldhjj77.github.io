import pandas as pd
from pandas.core.frame import DataFrame

# pandas 자료구조 DataFrame(2차원배열) / Serise(1차원배열)

s1 = pd.Series([3, 5, 8, 3, 2])
print(s1)
print(s1.values)
print(s1.index)
print(s1.dtypes)

s2 = pd.Series([3, 5, 8, 3, 2], index=['b', 'p', 'a', 'r', 's'])    # 인덱스와 값을 따로 입력
print(s2)
print(s2['b'])
print(s2[0])
print(s2.b)
print(s2[:2])
print(s2.reindex(['p', 'a', 's', 'r', 'b']))    # 기존 인덱스값을 넣지 않으면 값이 사라짐(순서만 조정하는경우 사용)

s3 = pd.Series({'math':95, 'lang':90, 'code':95})   # 인덱스와 값을 같이 입력
print(s3)


s3.name = 'Scores'
s3.index.name = 'Subject'
print(s3)


x = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x)
print(x.values)

data = {'subject': ['math', 'comp', 'phys', 'music'], 'score': [90, 80, 90, 100], 'student': [95, 85, 75, 90]}
print(pd.DataFrame(data))
y = pd.DataFrame(data)
print(y.dtypes)
print(len(y))       # 인덱스의 길이가 나옴
print(y.shape)      # 행과 열의 길이
print(y.shape[0])   # 열의 길이
print(y.shape[1])   # 행의 길이











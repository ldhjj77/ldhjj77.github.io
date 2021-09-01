







# 인덱싱 관련 오류

# Reindexing only valid with uniquely valued Index objects
# 중복된 인덱스값이 있을경우 발생
# 딕셔너리형태로 컬럼명을 지정했을경우 발생함(이중 컬럼명이 생성됨)
# 아래와같이 컬럼명을 지정해줘야함
# 전세계코로나현황1.columns = ['국가', '확진자', '사망자']




# 'NoneType' object has no attribute 'drop'
# inplace = True 를 사용하면 나타날수 있는 에러
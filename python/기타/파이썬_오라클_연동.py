import cx_Oracle        # 오라클
import pandas as pd
from sqlalchemy import create_engine    # 데이터프레임 추가시 필요






# 데이터 프레임을 데이터베이스에 넣기
# PROTOCOL=TCP / HOST = 서버주소 / PORT = 서버포트 / SERVICE_NAME = 데이터베이스이름
dsn_tns = "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))\
       (CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))"
pwd = 'tiger'
engine = create_engine('oracle+cx_oracle://c##scott:' + pwd + '@%s' % dsn_tns)
전국코로나현황.to_sql('전국코로나현황', engine.connect(), if_exists='replace', index=False)







# 개별데이터를 넣을 경우 사용
# 접속 설정(호스트명, 포트, SID)
dsn = cx_Oracle.makedsn("localhost",1521,"orcl")
# 디비접속 설정(계정명, 비밀번호, 접속설정)
db = cx_Oracle.connect("c##scott","tiger",dsn)

# SQL문 실행 메모리 영역 열기
cursor = db.cursor()


# 테이블 생성하기(pthon3 -> 테이블명( id1-> 컬럼명  char -> 데이터형식))
# cursor.execute("create table python3(id1 char(50), id2 char(50))")
# 데이터 삽입하기(python3 -> 테이블명  id1 -> 컬럼명  values('aa' -> 삽입할 내용))
cursor.execute("insert into python3(id1) values('aa')")
cursor.execute("insert into python3(id2) values('aa')")
# 한번에 모든컬럼값을 같이 넣어줘야함 안넣으면 NULL처리됨

# 적용
db.commit()


# 디비에 있는 테이블 불러오기
cursor.execute("select * from DEPT")
x = cursor.fetchall()
df = pd.DataFrame(x)
print(df)


# cursor.close()
# db.close()
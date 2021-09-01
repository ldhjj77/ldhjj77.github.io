import numpy as np


# 배열의 복사

a = np.array([[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]])
b = a           # 새 개체가 생성되지 않습니다.
print(b is a)           # a와 b는 동일한 ndarray 객체에 대한 두 개의 이름입니다.
# True


def f(x):
    print(id(x))

print(id(a))  # id는 개체의 고유 식별자입니다.
# 2053601008592  # 다를 수 있습니다
print(f(a))
# 2053601008592  # 다를 수 있습니다







# View or Shallow Copy

c = a.view()
print(c is a)
# False
print(c.base is a)           # c는 a가 소유 한 데이터보기입니다.
# True
print(c.flags.owndata)
# False

c = c.reshape((2, 6))  # a의 모양은 변하지 않는다
print(a.shape)
# (3, 4)
c[0, 4] = 1234         # a의 데이터 변경
print(a)
# [[   0    1    2    3]
#  [1234    5    6    7]
#  [   8    9   10   11]]


s = a[:, 1:3]
s[:] = 10  # s [:]는 s의 뷰입니다. s = 10과 s [:] = 10의 차이에 유의하십시오.
print(a)
# [[   0   10   10    3]
#  [1234   10   10    7]
#  [   8   10   10   11]]






# Deep Copy

d = a.copy()  # 새 데이터가있는 새 배열 객체가 생성됩니다.
print(d is a)
# False
print(d.base is a)  # d는 a와 아무것도 공유하지 않습니다
# False
d[0, 0] = 9999
print(a)
# [[   0   10   10    3]
#  [1234   10   10    7]
#  [   8   10   10   11]]

a = np.arange(int(1e8))
b = a[:100].copy()
del a   # ``a ''의 메모리를 해제 할 수 있습니다.
# b = a [: 100]이 대신 사용되면 a는 b에 의해 참조되고 del a가 실행 되더라도 메모리에 유지됩니다.
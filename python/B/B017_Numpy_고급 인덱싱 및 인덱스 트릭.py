import numpy as np

# 인덱스 배열로 인덱싱


a = np.arange(12)**2  # 처음 12 개의 제곱수
i = np.array([1, 1, 3, 8, 5])  # 인덱스 배열
print(a[i])  # 위치 'i'에있는 'a'의 요소
# [ 1  1  9 64 25]

j = np.array([[3, 4], [9, 7]])  # 인덱스의 2 차원 배열
print(a[j]) # 'j'와 같은 모양
# [[ 9 16] 
#  [81 49]]


palette = np.array([[0, 0, 0],         # black
                  [255, 0, 0],       # red
                  [0, 255, 0],       # green
                  [0, 0, 255],       # blue
                  [255, 255, 255]])  # white
image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
                [0, 3, 4, 0]])
print(palette[image])  # the (2, 4, 3) color image

# [[[  0   0   0]
#   [255   0   0]
#   [  0 255   0]
#   [  0   0   0]]

#  [[  0   0   0]
#   [  0   0 255]
#   [255 255 255]
#   [  0   0   0]]]
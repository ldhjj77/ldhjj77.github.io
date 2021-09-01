import numpy as np

# 인덱싱, 슬라이싱 및 반복


c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
            [ 10, 12, 13]],
            [[100, 101, 102],
            [110, 112, 113]]])
print(c.shape)
# (2, 2, 3)
print(c[1, ...])  # same as c[1, :, :] or c[1]
# [[100 101 102]
#  [110 112 113]]
print(c[..., 2])  # same as c[:, :, 2]
# [[  2  13]
#  [102 113]]

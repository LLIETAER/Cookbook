import numpy as np

b = np.arange(9).reshape(3,3)

b = b * 1.0

var_1 = var_2 = var_3 = 99.

for i in range(3):
    tmp = ('var_'+str(i+1))
    b[2, i] = locals()[tmp]

c = np.zeros(shape=(100, 100), dtype=np.float32)

print(c)

print(c[:,0])

# result
#[[ 0.  1.  2.]
# [ 3.  4.  5.]
# [99. 99. 99.]]
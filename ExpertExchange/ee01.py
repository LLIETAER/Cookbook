import pandas as pd
import numpy as np
from subprocess import *
import sys

array = np.array([[75, 89, 63, 44, 96],
       [16, 94, 70, 95, 75],
       [ 8, 65, 51, 13,  1],
       [65, 51, 39, 38, 77],
       [76, 78, 91, 85, 19],
       [20, 28, 57, 79,  1],
       [56, 58, 64, 41, 14],
       [75, 57, 31, 21, 59],
       [97, 64, 74, 77, 92],
       [22, 49, 57, 20, 48],
       [73, 72, 79, 62, 37],
       [11, 69, 65, 83, 83],
       [81, 22, 54, 77, 58],
       [80, 23, 73, 98, 37],
       [33, 89, 42, 31, 15],
       [42, 48, 27, 14, 12],
       [56, 12, 51, 68, 19],
       [37, 72, 68, 61, 14],
       [78, 58, 55, 33, 70],
       [89, 38, 70, 76, 87],
       [44, 39, 22, 15, 81],
       [60,  0, 33, 65, 98],
       [21, 32, 58, 68, 99],
       [10, 43, 22, 65, 40]])


OldDataSet = {
    'id': [20, 30, 40, 50, 60, 70]
    , 'OdoLength': [26.12, 43.12, 46.81, 56.23, 111.07, 166.38]}

NewDataSet = {
    'id': [3000, 4000, 5000, 6000, 7000, 8000]
    , 'OdoLength': [25.03, 42.12, 45.74, 46, 110.05, 165.41]}

df1 = pd.DataFrame(OldDataSet)
df2 = pd.DataFrame(NewDataSet)

OldArray = df1.to_numpy()
NewArray = df2.to_numpy()

results = np.zeros((6, 4))

results[:, :-2] = OldArray
#print(np.count_nonzero(array[:, 0:1] == 75))



results[:, 2:] = NewArray

for row in range(6):
    closest = 99999999.
    line = 0
    print(results[row])
    for i in range(row, 6):
        diff_value = abs(results[row, 1] - results[i, 3])
        if diff_value < closest:
            closest = diff_value
            line = i
    if line > row:
        results[row:-1, 2:] = results[line:, 2:]
        results[5:, 2:] = (0, 0)

#print('\n', results)


c = 'python cons.py'

handle = Popen(c, stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)
print handle.stdout.read()
handle.flush()

print("toto")







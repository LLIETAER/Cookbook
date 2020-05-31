import numpy as np

np.genfromtxt
an_array = np.array([[75, 89, 63, 44, 96],
       [16, 94, 70, 95, 75],
       [ 8, 65, 51, 13,  1],
       [65, 51, 39, 38, 77],
       [76, 78, 91, 85, 19],
       [37, 72, 68, 61, 14],
       [78, 58, 55, 33, 70],
       [89, 38, 70, 76, 87],
       [44, 39, 22, 15, 81],
       [60,  0, 33, 65, 98],
       [21, 32, 58, 68, 99],
       [75, 43, 22, 65, 40]])

# this is to visualize first columns (where we will search for value 75)

print(an_array)
print(an_array[:, 0])
exit(0)


[[75 89 63 44 96]
 [16 94 70 95 75]
 [ 8 65 51 13  1]
 [65 51 39 38 77]
 [76 78 91 85 19]
 [37 72 68 61 14]
 [78 58 55 33 70]
 [89 38 70 76 87]
 [44 39 22 15 81]
 [60  0 33 65 98]
 [21 32 58 68 99]
 [75 43 22 65 40]]
[75 16  8 65 76 37 78 89 44 60 21 75]

result = []

# tmp_array[0] represent the list of rows that are equal to 75
tmp_array = np.where(an_array[:, 0:1] == 75)

# loop the tmp_array to calculate intervals
for i in range(1, len(tmp_array[0])):
    result.append(tmp_array[0][i] - tmp_array[0][i - 1])

#convert final result to np array
result = np.array(result)
print(result)


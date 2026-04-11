import numpy as np

data = [10,20,30,40,50,60,70,80,90,100,110,120]

arr = np.array(data)

reshaped = arr.reshape(4, 3)

print(reshaped)
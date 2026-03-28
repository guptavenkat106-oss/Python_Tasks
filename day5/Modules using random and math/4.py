import random
import math
numbers=[random.randint(1,200) for i in range(20)]
print("numbers:",numbers)
maximum = max(numbers)
minimum = min(numbers)
print("maximum value:",maximum)
print("minimum value:",minimum)
print("square root of maximum:",math.sqrt(maximum))

import numpy as np

# Creating 5x4 array
array = np.arange(20).reshape(5, 4)
print(array)
print()

# If no axis mentioned, then it works on the entire array
print(np.argmax(array))

# If axis=1, then it works on each row
print(np.argmax(array, axis=1))

# If axis=0, then it works on each column
print(np.argmax(array, axis=0))
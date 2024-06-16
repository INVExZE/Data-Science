# sort() - the numpy ndarray object has a function which is called sort(), and this will sort a specified array.
import numpy as np
sanjay = np.array([3,2,0,1])
print(np.sort(sanjay)) # this method is like the copy()

# sort the array alphabetically
import numpy as np
sanjay = np.array(['banana', 'cherry', 'apple'])
print(np.sort(sanjay))

# sort the boolean array:
import numpy as np
sanjay = np.array([True, False, True])
print(np.sort(sanjay))

# sorting the 2-D array
import numpy as np
sanjay = np.array([[3,2,4], [5,0,1]])
print(np.sort(sanjay))
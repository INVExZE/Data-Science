# ARRAY JOINING

# Joining the numpy array - here for this we will pass concatenate()

import numpy as np
sanjay = np.array([1,2,3])
sanjay1 = np.array([4,5,6])
sanjay2 = np.concatenate((sanjay, sanjay1))
print(sanjay2)

# Joining of 2-D arrays along with rows(axis = 1)
import numpy as np
sanjay = np.array([[1,2],[3,4]])
sanjay1 = np.array([[5,6], [7,8]])
sanjay2 = np.concatenate((sanjay, sanjay1), axis=1)
print(sanjay2)

# Joining array using the stack function: 
import numpy as np
sanjay = np.array([1,2,3])
sanjay1 = np.array([4,5,6])
sanjay2 = np.stack((sanjay, sanjay1), axis=1)
print(sanjay2)

# Stacking along with rows: hstack()
import numpy as np
sanjay = np.array([1,2,3])
sanjay1 = np.array([4,5,6])
sanjay2 = np.hstack((sanjay, sanjay1))
print(sanjay2)

# Stacking along with column
import numpy as np
sanjay = np.array([1,2,3])
sanjay1 = np.array([4,5,6])
sanjay2 = np.vstack((sanjay, sanjay1))
print(sanjay2)

# Stacking along with height(depth)
# import numpy as np
sanjay = np.array([1,2,3])
sanjay1 = np.array([4,5,6])
sanjay2 = np.dstack((sanjay, sanjay1))
print(sanjay2) 


# ARRAY SPLITTING 

# spliting arrays in numpy- it is reverse to joining, breaking the array.
# array_split()

# split the array in 3 parts:
import numpy as np
sanjay = np.array([1,2,3,4,5,6])
sanjaynew = np.array_split(sanjay, 3)
print(sanjaynew)

# now we will split this array in 4 parts
import numpy as np
sanjay = np.array([1,2,3,4,5,6])
sanjaynew = np.array_split(sanjay, 4)
print(sanjaynew)

# split into array with index

import numpy as np
sanjay = np.array([1,2,3,4,5,6])
sanjaynew = np.array_split(sanjay, 3)
print(sanjaynew[0])
print(sanjaynew[1])
print(sanjaynew[2])


# splitting the 2-D array
import numpy as np
sanjay = np.array([[1,2], [3,4], [5,6], [7,8], [9,10], [11,12]])
sanjaynew = np.array_split(sanjay, 3)
print(sanjaynew)

# split the 2-D array into three 2-D arrays
import numpy as np
sanjay = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
sanjaynew = np.array_split(sanjay, 3)
print(sanjaynew)

# spliting the 2-D into three 2-Dalong with rows
import numpy as np
sanjay = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
sanjaynew = np.array_split(sanjay, 3, axis=1)
print(sanjaynew)

#alternate solution is using the hsplit(), opposite hstack()
import numpy as np
sanjay = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
sanjaynew = np.hsplit(sanjay, 3)
print(sanjaynew)



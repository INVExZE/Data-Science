# shape of an array - the shape of an array is the number of elements in each dimensions.
# now we will try to get the shape of any array.
import numpy as np
sanjay = np.array([[1,2,3,4], [5,6,7,8]])
print(sanjay.shape)

# (2,4) which means the array has 2 dimensions and it has 4 elements ( 2 rows and 4 columns)

# now we will create a 5-D array using ndmin :
import numpy as np
sanjay = np.array([1,2,3,4], ndmin=5)
print(sanjay)
print('shape of array is ', sanjay.shape)


# ARRAY RESHAPING
# reshaping - means changing the shape of an array ,like adding or removing the elements.

# reshaping from 1-D to 2-D
import numpy as np
sajay = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
sanjay1 = sajay.reshape(4, 3)
print(sanjay1)

# reshping from 1-D to 3-D
import numpy as np
sajay = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
sanjay1 = sajay.reshape(2, 3, 2)
print(sanjay1)

# Return copy or view
import numpy as np
sajay = np.array([1,2,3,4,5,6,7,8])
print(sajay.reshape(2, 4).base)

# unknown dimension - you are only allowed to have one unknown dimension. pass -1.

import numpy as np
sajay = np.array([1,2,3,4,5,6,7,8])
sanjay1 = sajay.reshape(2, 2, -1)
print(sanjay1)

# Flattening the array by converting multidimensional array in 1-D.
import numpy as np
sajay = np.array([[1,2,3], [4,5,6]])
sanjay1 = sajay.reshape(-1)
print(sanjay1)

# there are alot of functions for changing the shapes pf an array in numpy. like flatten, ravel and also rearranging the element rot90, flip,fliplr, flipud. they all are actually comes under advanced numpy.
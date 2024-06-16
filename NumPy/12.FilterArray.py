'''# Getting some elements out of an 
existing array and creating a new array 
is called filtering.
# A boolean index list is a list ofboolean 
corresponding to indexes in the array. 
(True and False)
# create an array from the element on 
index 0 to 2:'''

import numpy as np
sanjay = np.array([41,42,43,44])
sanjay1 = [True, False, True, False]
finalsanjay = sanjay[sanjay1]
print(finalsanjay)

'''# now we will create a filter array
# that will return only values higher 
than 42.'''

import numpy as np
sanjay = np.array([41,42,43,44])
emptysanjay = []
for element in sanjay:
    if element > 42:
        emptysanjay.append(True)
    else:
        emptysanjay.append(False)
sanjaynew = sanjay[emptysanjay]
print(emptysanjay)
print(sanjaynew)

'''# Create a filter array that will 
return only even elements from the 
original array.'''

import numpy as np
sanjay = np.array([1,2,3,4,5,6,7])
sanjayempty = []
for i in sanjay:
    if i%2 == 0:
        sanjayempty.append(True)
    else:
        sanjayempty.append(False)
sanjaynew = sanjay[sanjayempty]
print(sanjayempty)
print(sanjaynew)

# Yes, you can also create filter directly from array
# that will return only values higher than 42.
import numpy as np
sanjay = np.array([41,42,43,44])
sanjayempty = sanjay > 42
sanjaynew = sanjay[sanjayempty]
print(sanjayempty)
print(sanjaynew)

'''# Yes, you can also create filter 
directly from array
# Create a filter array that will return 
only even elements from the original array.'''
import numpy as np
sanjay = np.array([1,2,3,4,5,6,7])
sanjayempty = sanjay % 2 == 0
sanjaynew = sanjay[sanjayempty]
print(sanjayempty)
print(sanjaynew)
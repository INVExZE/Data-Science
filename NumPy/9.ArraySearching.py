# searching array - you can search an array for a certain value and return the indexes that get the match. by using where()
import numpy as np
sanjay = np.array([1,2,3,4,5,4,4])
sanjaynew = np.where(sanjay == 4)
print(sanjaynew)

# now we will find the indexes where the values are even:
import numpy as np
sanjay = np.array([1,2,3,4,5,6,7,8])
sanjay1 = np.where(sanjay%2 == 0)
print(sanjay1)

# now we will find the indexes where the values are odd:
import numpy as np
sanjay = np.array([1,2,3,4,5,6,7,8])
sanjay1 = np.where(sanjay%2 == 1)
print(sanjay1)

# Searchsorted() - perform binary search in array.
# we will now find the index where the value 7 should be insterted.
import numpy as np
sanjay = np.array([6,7,8,9])
sanjay1 = np.searchsorted(sanjay, 7)
print(sanjay1)

# now we will search fron right side
import numpy as np
sanjay = np.array([6,7,8,9])
sanjay1 = np.searchsorted(sanjay, 7, side='right')
print(sanjay1)

# how to search multiple values:
import numpy as np
sanjay = np.array([1,3,5,7])
sanjay1 = np.searchsorted(sanjay, [2,4,6])
print(sanjay1)
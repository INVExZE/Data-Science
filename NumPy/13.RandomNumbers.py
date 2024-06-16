# RANDOM NUMBERS

# Random means - something that cannot be predicated logically.
# Generating a random number

from numpy import random
sanjay = random.randint(100)
print (sanjay)

# Generating a float() via rand() in btw range 0 to 1.

from numpy import random
sanjay = random.rand()
singh = random.rand(5)
print (sanjay, "\n",singh)

# Generate a random array 
# Generating a random array 1-D array containing 5 random integer from 0 to 100.

from numpy import random
sanjay = random.randint(100, size = 5)
print(sanjay)

# Generating a random array 2-D array containing 2 rows with 5 random integer from 0 to 100.

from numpy import random
sanjay = random.randint(100, size = (2, 5))
print(sanjay)

# Random meaning - something that cannot be predicted logically.
# Now we will generate a random number from 0 to 100
from numpy import random 
sanjay = random.randint(100)
print(sanjay) 

# You can also genetrate float() via rand() from 0 to 1
from numpy import random 
sanjay = random.rand()
print(sanjay) 

# You can also generate random Array.
# we will generate a 1-D array containing 5 random int from 0 to 100:
from numpy import random 
sanjay = random.randint(100, size=(5))
print(sanjay) 

# You can also generate random Array.
# we will generate a 2-D array with 3 rows, each row  containing 5 random int from 0 to 100:
from numpy import random 
sanjay = random.randint(100, size=(3, 5))
print(sanjay) 

# You can also generate random Array.
# we will generate a 1-D array containing 5 random float:
from numpy import random 
sanjay = random.rand(5)
print(sanjay) 

# You can also generate random Array.
# we will generate a 2-D array with 3 rows, each containing 5 random float:
from numpy import random 
sanjay = random.rand(3, 5)
print(sanjay) 

# you can also generate random numbers from an array
# choice()

from numpy import random 
sanjay = random.choice([3,5,7,9,1,4,6])
print(sanjay) 

# you can also generate random numbers from an 2-D array
# choice()

from numpy import random 
sanjay = random.choice([3,5,7,9,1,4,6], size=(3, 5))
print(sanjay) 
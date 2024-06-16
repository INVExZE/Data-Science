# logistic dist - describe growth it is basically imp in regression and neural network.
# param - loc(mean- 0),scale(standard deviation, 1), size
# 
# draw 2*2 samples of logistic with mean at 1 and stddev 2.0 
from numpy import random
sanjay = random.logistic(loc=1, scale=2, size=(2,3))
print(sanjay)

# visualization of logistic dist

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.logistic(size=1000), hist=False)
plt.show()
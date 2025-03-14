# cleaning data : it means fixing the bad data in your data set. bad data could be: empty cell, data in a wrong format, duplicate data and wrong data.
# emplty cell: it will give you wrong result always, we will have to remove the rows always that contain the bad data.
# loading and reading the original dataframe
import pandas as pd
sanjay = pd.read_csv('dirtydata.csv')
print(sanjay.to_string())

# here we will return a new data frame with no empty cell.

import pandas as pd
sanjay = pd.read_csv('dirtydata.csv')
sharadnew = sanjay.dropna()
print(sharadnew.to_string())

# if at any case you want to change the original dataframe, than use the inplace=True argument. it will remove the rows containing the NULL(NaN) values.
import pandas as pd
sanjay = pd.read_csv('dirtydata.csv')
sanjay.dropna(inplace=True)
print(sanjay.to_string())

# replacing the empty value: we will use the fillna() method which will allow us to replace the empty cell with a value.
import pandas as pd
sanjay = pd.read_csv('dirtydata.csv')
sanjay.fillna(130, inplace=True)
print(sanjay.to_string())

# to replace only the empty value for one column , you need to specify the column name.
import pandas as pd
sanjay = pd.read_csv('dirtydata.csv')
sanjay["Calories"].fillna(130, inplace=True)
print(sanjay.to_string())

# here we can also replace the empty cell using mean(), median() or mode().
#calculate the MEAN and replace the empty values with it.
import pandas as pd
sanjay = pd.read_csv('dirtydata.csv')
x = sanjay["Calories"].mean()
sanjay["Calories"].fillna(x, inplace=True)
print(sanjay.to_string())

# calculate the MEDIAN and replace any empty values in it.:
import pandas as pd
sanjay = pd.read_csv('dirtydata.csv')
x = sanjay["Calories"].median()
sanjay["Calories"].fillna(x, inplace=True)
print(sanjay.to_string())

# calculate the MODE and replace the empty cell with it.
import pandas as pd
sanjay = pd.read_csv('dirtydata.csv')
x = sanjay["Calories"].mode()[0]
sanjay["Calories"].fillna(x, inplace=True)
print(sanjay.to_string())
import pandas as pd

# Read the Titanic dataset from the provided URL
MyData = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Print the length of MyData (number of rows)
print(len(MyData)) 

# Select the 'Name' column of the first 10 rows
s = MyData['Name'][0:10]

# Create a Series s1 with the selected 'Name' values and custom index
l = ['a','b','c','d','e','f','g','h','i','j']
s1 = pd.Series(list(s), index=l) 

# Append s1 to itself
s2 = s1.append(s) 

# Access the value at index 4 in s2
s2[4] 

# Create a Series s4 with values and custom index
s4 = pd.Series([3,4,5,6,6], index=[2,4,5,6,1]) 

# Create a Series s5 with values and custom index
s5 = pd.Series([34,345,45,45,454], index=[9,4,5,6,7]) 

# Append s5 to s4
s6 = s4.append(s5) 

# Access the value at index 4 in s6
s6[4] 

# Perform element-wise multiplication of s4 and s5
s4 * s5 

# Perform element-wise addition of s4 and s5
s4 + s5 


import pandas as pd

# Create a dictionary of data
data = {"a":[1,2,3,4],
       "b":[4,5,6,7],
       "c":["sudh","krish","hitesh","navin"]} 

# Create a DataFrame df from the data dictionary
df = pd.DataFrame(data)

# Set the 'a' column as the index of df
df.set_index('a', inplace=True) 

# Reset the index of df
df = df.reset_index() 

# Create another DataFrame df1 with custom index
df1 = pd.DataFrame(data,index = ['a','b','c','d'])

# Reindex df1 with specified index values
df1.reindex(['b','c','d','a']) 

# Iterate over the rows of df1
for i, j in df1.iterrows():
    print(j)

# Iterate over the columns of df1
for col_name, column in df1.iteritems():
    print(col_name, column) 

# Convert the 'a' column of df to a list
list(df['a']) 

# Create a list comprehension to extract values from the 'a' column of df
[i for i in df['a']]

# Define a function test that returns the sum of its input
def test(x):
    return x.sum()

# Apply the test function to each column of df1 using axis=0
df1.apply(test, axis=0) 

# Create a new DataFrame df2 by selecting columns 'a' and 'b' from df1
df2 = df1[['a','b']] 

# Apply a lambda function to each element in df2 to square the values
df2.applymap(lambda x : x**2)

# Sort df by the 'c' column
df.sort_values('c') 

# Sort df by the index in descending order
df.sort_index(ascending=False) 

# Set the display option to show a maximum column width of 1000
pd.set_option("display.max_colwidth" ,1000)

# Create a DataFrame df3x with a single column 'Desc' containing a long text
df3x = pd.DataFrame({"Desc" :["Data Science Masters course is highly curated and uniquely designed according to the latest industry standards. This program instills students the skills essential to knowledge discovery efforts to identify standard, novel, and truly differentiated solutions and decision-making, including skills in managing, querying, analyzing, visualizing, and extracting meaning from extremely large data sets. This trending program provides students with the statistical, mathematical and computational skills needed to meet the large-scale data science challenges of today's professional world. You will learn all the stack required to work in data science industry including cloud infrastructure and real-time industry projects. This course will be taught in Hindi language."] })

# Display df3x
df3x 

# Create another DataFrame df3 with multiple 'Desc' values
df3 = pd.DataFrame({"Desc" :["Data Science Masters course is highly curated and uniquely designed according to the latest industry standards. This program instills students the skills essential to knowledge discovery efforts to identify standard, novel, and truly differentiated solutions and decision-making, including skills in managing, querying, analyzing, visualizing, and extracting meaning from extremely large data sets. This trending program provides students with the statistical, mathematical and computational skills needed to meet the large-scale data science challenges of today's professional world. You will learn all the stack required to work in data science industry including cloud infrastructure and real-time industry projects. This course will be taught in Hindi language." , 
                            "my name is sudh" ,"i use to teach data science "] }) 

# Add a new column 'len' to df3, representing the length of each 'Desc' value
df3['len'] = df3['Desc'].apply(len) 

# Count the number of words in each 'Desc' value using lambda function and add a new column 'word_count'
df3['word_count'] = df3['Desc'].apply(lambda x :len(x.split())) 

# Calculate various statistical measures on the 'a' column of df
df['a'].mean()
df['a'].median()
df['a'].mode()
df['a'].std()
df['a'].sum()
df['a'].min()
df['a'].max()
df['a'].var()

# Create a DataFrame df4 with a single column 'a'
df4 = pd.DataFrame({'a' : [3,4,5,2,1,3,4,5,6]}) 

# Calculate rolling mean on column 'a' with various window sizes
df4['a'].rolling(window=1).mean() 
df4['a'].rolling(window=2).mean()
df4['a'].rolling(window=3).mean() 
df4['a'].rolling(window=3).sum()

# Calculate cumulative sum on column 'a'
df4['a'].cumsum() 

# Create a date range from '2023-04-23' to '2023-06-23'
date = pd.date_range(start='2023-04-23', end='2023-06-23')
df_date = pd.DataFrame({'date':date})
df_date 

# Create a DataFrame df7 with a single column 'date' and convert it to datetime
df7 = pd.DataFrame({"date" : ['2023-06-23' , '2023-06-22','2023-06-20']})
df7['updated_date'] = pd.to_datetime(df7['date']) 

# Extract year, day, and month from the 'updated_date' column
df7['year'] = df7['updated_date'].dt.year
df7['day'] = df7['updated_date'].dt.day
df7['month'] = df7['updated_date'].dt.month 

# Create a timedelta of 1 day, 5 hours, and 45 minutes
td = pd.Timedelta(days=1, hours=5, minutes=45)   

# Add the timedelta to a specific date
dt = pd.to_datetime('2023-06-20')
dt + td 

# Create a list of categorical data
data = ["sudh", "krish", "hitesh", "navin","sudh" ,"sudh" ]

# Convert the list to a Categorical object and count the occurrences of each category
cat = pd.Categorical(data)
cat.value_counts() 

# Create a Series and plot it
d = pd.Series([1,2,3,3,5,6,6,8])
d.plot() 

# Create a DataFrame and plot a line graph
df = pd.DataFrame({'a':[3,4,5,6,7],
                  'b':[4,5,6,7,8]}) 
df.plot(x='a', y='b') 

# Create a scatter plot
df.plot.scatter(x='a', y='b') 

# Create a pie chart
dx = pd.Series([1,2,3,3,5,6,6,8]) 
dx.plot.pie()

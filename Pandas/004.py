import pandas as pd

# Read the Titanic dataset from the provided URL
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Drop the 'PassengerId' column from df
df.drop('PassengerId', axis=1, inplace=True)

# Drop the row at index 3 from df
df.drop(3, inplace=True)

# Set the 'Name' column as the index of df
df.set_index("Name", inplace=True)

# Reset the index of df
df.reset_index(inplace=True)

# Create a dictionary
d = {'key1': [3, 4, 5, 6, 7],
     'key2': [5, 6, 7, 8, 6],
     'key3': [4, 5, 6, 7, 8]
}

# Create a DataFrame from the dictionary
pd.DataFrame(d)

# Read data from 'Taxonomy.csv' into df1
df1 = pd.read_csv('Taxonomy.csv')

# Drop rows with missing values from df1
df1.dropna(inplace=True)

# Read data from 'Taxonomy.csv' into df2
df2 = pd.read_csv('Taxonomy.csv')

# Drop columns with missing values from df2
df2.dropna(axis=1)

# Fill missing values in df2 with 'ROY'
df2.fillna("ROY")

# Reset the index of df
df.reset_index(inplace=True)

# Group df by 'Survived'
g = df.groupby('Survived')
g.sum()
g.mean()

# Group df by 'Pclass'
g1 = df.groupby('Pclass')
g1.sum()
g1.mean()

# Select specific columns from df and concatenate them
df5 = df[['Name', 'Survived', 'Pclass']][0:5]
df6 = df[['Name', 'Survived', 'Pclass']][5:10]
pd.concat([df5, df6])

# Concatenate df5 and df6 along the columns axis
df7 = pd.concat([df5, df6], axis=1)

# Fill missing values in df7 with 'ROY'
df7.fillna('ROY')

# Create data1 DataFrame
data1 = pd.DataFrame({'key1': [1, 2, 4, 5, 6],
                      'key2': [4, 5, 6, 7, 8],
                      'key3': [3, 4, 5, 6, 6]})

# Create data2 DataFrame
data2 = pd.DataFrame({'key1': [1, 2, 45, 6, 67],
                      'key4': [56, 5, 6, 7, 8],
                      'key5': [3, 56, 5, 6, 6]})

# Merge data1 and data2 on their common key ('key1')
pd.merge(data1, data2)

# Perform left join of data1 and data2
pd.merge(data1, data2, how='left')

# Perform right join of data1 and data2
pd.merge(data1, data2, how='right')

# Perform outer join of data1 and data2 on 'key1'
pd.merge(data1, data2, how='outer', on='key1')

# Perform cross join of data1 and data2
pd.merge(data1, data2, how='cross')

# Create data1 DataFrame with custom index
data1 = pd.DataFrame({'key1': [1, 2, 4, 5, 6],
                      'key2': [4, 5, 6, 7, 8],
                      'key3': [3, 4, 5, 6, 6]},
                     index=['a', 'b', 'c', 'd', 'e'])

# Create data2 DataFrame with custom index
data2 = pd.DataFrame({'key11': [1, 2, 4, 5, 6],
                      'key22': [4, 5, 6, 7, 8],
                      'key33': [3, 4, 5, 6, 6]},
                     index=['a', 'b', 'h', 'i', 'j'])

# Perform inner join of data1 and data2 using index
data1.join(data2)

# Perform right join of data1 and data2 using index
data1.join(data2, how='right')

# Perform inner join of data1 and data2 using index
data1.join(data2, how='inner')

# Perform outer join of data1 and data2 using index
data1.join(data2, how='outer')

# Perform cross join of data1 and data2 using index
data1.join(data2, how='cross')

# Apply lambda function to create 'Fare_INR' column in df
df['Fare_INR'] = df['Fare'].apply(lambda x: x * 80)

# Define a function to convert Euro to INR
def euro_inr(x):
    return x * 80

# Apply euro_inr function to create 'Fare_INR2' column in df
df['Fare_INR2'] = df['Fare'].apply(euro_inr)

# Define a function to categorize fare values
def cat_fare(x):
    if x < 10:
        return "cheap"
    elif 10 <= x < 20:
        return 'mid'
    else:
        return 'high'

# Apply cat_fare function to create 'car_fare' column in df
df['car_fare'] = df['Fare'].apply(cat_fare)


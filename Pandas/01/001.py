import pandas as pd
import lxml 

# Read the CSV file "Services.csv" into a DataFrame called DataFrame
DataFrame = pd.read_csv("Services.csv")

# Display the first few rows of the DataFrame
DataFrame.head()

# Display the first three rows of the DataFrame
DataFrame.head(3)

# Display the last two rows of the DataFrame
DataFrame.tail(2)

# Check the type of the DataFrame
type(DataFrame)

# Convert the DataFrame columns into a list
list(DataFrame.columns)

# Access the 'status' column of the DataFrame
DataFrame['status']

# Check the type of the 'status' column
type(DataFrame['status'])

# Convert the 'status' column into a list called ConToList
ConToList = list(DataFrame['status'])

# Print the type of the ConToList variable
print(type(ConToList))

# Access specific columns ('email', 'keywords', 'name') of the DataFrame
DataFrame[['email','keywords','name']]

# Check the data types of the DataFrame columns
DataFrame.dtypes

# Read an Excel file "LUSID Excel - Setting Up Your Mark Data.xlsx" into a DataFrame called MyDataF
MyDataF = pd.read_excel("LUSID Excel - Setting Up Your Mark Data.xlsx")

# Read a CSV file from a URL into a DataFrame called MyDataF2
MyDataF2 = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Read HTML tables from a URL and store them in a list called Url_Data
Url_Data = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2015_totals.html")

# Print the length of the Url_Data list
print(len(Url_Data))

# Assign the first table from Url_Data to a DataFrame called MyDataF3
MyDataF3 = Url_Data[0]

# Save MyDataF3 as a CSV file named "Player_Data.csv"
MyDataF3.to_csv("Player_Data.csv", index=False)

# Display descriptive statistics of MyDataF2
MyDataF2.describe()

# Check if the data types of MyDataF2 are 'object'
MyDataF2.dtypes == 'object'

# Retrieve the column names of MyDataF2 with data type 'object'
MyDataF2.dtypes[MyDataF2.dtypes == 'object'].index

# Display descriptive statistics of columns in MyDataF2 with data type 'object'
MyDataF2[MyDataF2.dtypes[MyDataF2.dtypes == 'object'].index].describe()

# Add a new column 'New_Colums' to MyDataF2 and initialize it with zeros
MyDataF2['New_Colums'] = 0

# Add a new column 'New_Col1' to MyDataF2 by adding 'PassengerId' and 'Pclass' columns
MyDataF2['New_Col1'] = MyDataF2['PassengerId'] + MyDataF2['Pclass']

# Create a categorical variable from the 'Pclass' column
pd.Categorical(MyDataF2['Pclass'])

# Get the unique values in the 'Cabin' column of MyDataF2
MyDataF2['Cabin'].unique()

# Print the count of rows in MyDataF2 where the 'Age' column is greater than 18, subtracting 890 from the count
print(len(MyDataF2[MyDataF2['Age'] > 18]) - 890)

# Filter rows from MyDataF2 based on conditions: 'Sex' is 'felmale' or 'Fare' is greater than 32
Var0 = MyDataF2[(MyDataF2['Sex'] == 'felmale') | (MyDataF2['Fare'] > 32)]
print(Var0)

# Select the 'Name' column from rows in MyDataF2 where the 'Fare' is equal to the maximum fare
Var1 = MyDataF2[MyDataF2['Fare'] == max(MyDataF2['Fare'])]['Name']
print(Var1)

# Retrieve every second row from MyDataF2
MyDataF2[0::2]

# Select specific columns ('PassengerId', 'Survived', 'Pclass') from the first two rows of MyDataF2
MyDataF2[['PassengerId','Survived','Pclass']][0:2]

# Select the first two rows and columns ('PassengerId', 'Survived', 'Pclass') using integer-based indexing
MyDataF2.iloc[0:2,[0,1,2]]

# Select the first three rows and columns ('PassengerId', 'Survived', 'Pclass') using label-based indexing
MyDataF2.loc[0:2,['PassengerId','Survived','Pclass']]


import pandas as pd
import lxml 

DataFrame = pd.read_csv("Services.csv")

DataFrame.head()
DataFrame.head(3)
DataFrame.tail(2)


type(DataFrame)
list(DataFrame.columns) 


DataFrame['status']
type(DataFrame['status']) 
ConToList = list(DataFrame['status'])
print(type(ConToList)) 



DataFrame[['email','keywords','name']]  # Printing Colums 
DataFrame.dtypes 


MyDataF = pd.read_excel("LUSID Excel - Setting Up Your Mark Data.xlsx")   
MyDataF2 = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

Url_Data = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2015_totals.html")

print(len(Url_Data)) 

MyDataF3= Url_Data[0] 
MyDataF3.to_csv("Player_Data.csv", index=False) 


MyDataF2.describe() 
MyDataF2.dtypes == 'object'
MyDataF2.dtypes[MyDataF2.dtypes == 'object'].index

MyDataF2[MyDataF2.dtypes[MyDataF2.dtypes == 'object'].index].describe() 

MyDataF2['New_Colums'] = 0

MyDataF2['New_Col1'] = MyDataF2['PassengerId'] + MyDataF2['Pclass'] 

pd.Categorical(MyDataF2['Pclass']) 

MyDataF2['Cabin'].unique() 

print(len(MyDataF2[MyDataF2['Age'] > 18]) - 890 ) 

Var0 = MyDataF2[(MyDataF2['Sex'] == 'felmale') | (MyDataF2['Fare'] > 32)]
print(Var0) 

Var1 = MyDataF2[MyDataF2['Fare'] == max(MyDataF2['Fare'])]['Name']
print(Var1)  



MyDataF2 [0::2]
MyDataF2[['PassengerId','Survived','Pclass']][0:2]

MyDataF2.iloc[0:2,[0,1,2]]
MyDataF2.loc[0:2,['PassengerId','Survived','Pclass']]





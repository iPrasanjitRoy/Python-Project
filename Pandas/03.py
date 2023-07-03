import pandas as pd 
data = {"a":[1,2,3,4],
       "b":[4,5,6,7],
       "c":["sudh","krish","hitesh","navin"]} 

df= pd.DataFrame(data)

df.set_index('a', inplace=True) 
df = df.reset_index() 


df1 = pd.DataFrame(data,index = ['a','b','c','d'])
df1.reindex(['b','c','d','a']) 


for i,j in df1.iterrows():
    print( j)

for col_name , column in df1.iteritems():
    print( col_name , column) 


list(df['a']) 
[i for i in df['a']]


def test(x):
    return x.sum()
df1.apply(test,axis=0) 


df2 = df1[['a','b']] 
df2.applymap(lambda x : x**2)


df.sort_values('c') 
df.sort_index(ascending = False) 


pd.set_option("display.max_colwidth" ,1000)
df3x = pd.DataFrame({"Desc" :["Data Science Masters course is highly curated and uniquely designed according to the latest industry standards. This program instills students the skills essential to knowledge discovery efforts to identify standard, novel, and truly differentiated solutions and decision-making, including skills in managing, querying, analyzing, visualizing, and extracting meaning from extremely large data sets. This trending program provides students with the statistical, mathematical and computational skills needed to meet the large-scale data science challenges of today's professional world. You will learn all the stack required to work in data science industry including cloud infrastructure and real-time industry projects. This course will be taught in Hindi language."] })


df3x 

pd.set_option("display.max_colwidth" ,1000)
df3 = pd.DataFrame({"Desc" :["Data Science Masters course is highly curated and uniquely designed according to the latest industry standards. This program instills students the skills essential to knowledge discovery efforts to identify standard, novel, and truly differentiated solutions and decision-making, including skills in managing, querying, analyzing, visualizing, and extracting meaning from extremely large data sets. This trending program provides students with the statistical, mathematical and computational skills needed to meet the large-scale data science challenges of today's professional world. You will learn all the stack required to work in data science industry including cloud infrastructure and real-time industry projects. This course will be taught in Hindi language." , 
"my name is sudh" ,"i use to teach data science "] }) 


df3

df3['len'] = df3['Desc'].apply(len) 



t ="i use to teach data science	"
len(t.split()) 

df3['word_count'] = df3['Desc'].apply(lambda x :len(x.split())) 

df['a'].mean()
df['a'].median()
df['a'].mode()
df['a'].std()
df['a'].sum()
df['a'].min()
df['a'].max()
df['a'].var()



#Python Pandas - Window Functions
df4 = pd.DataFrame({'a' : [3,4,5,2,1,3,4,5,6]}) 

df4['a'].rolling(window=1).mean() 
df4['a'].rolling(window=2).mean()
df4['a'].rolling(window=3).mean() 
df4['a'].rolling(window=3).sum()

df4['a'].cumsum() 



#Python Pandas - Date Functionality

date = pd.date_range(start='2023-04-23' , end = '2023-06-23')
df_date = pd.DataFrame({'date':date})
df_date 


df7 = pd.DataFrame({"date" : ['2023-06-23' , '2023-06-22','2023-06-20']})
df7['updated_date'] = pd.to_datetime(df7['date']) 
df7['year'] = df7['updated_date'].dt.year
df7['day'] = df7['updated_date'].dt.day
df7['month'] = df7['updated_date'].dt.month 



#Python Pandas –Time Delta 
td = pd.Timedelta(days= 1,hours = 5 ,minutes = 45)   
dt = pd.to_datetime('2023-06-20')
dt+td 


#Python Pandas - Categorical Data

data = ["sudh" , "krish" , "hitesh" , "navin","sudh" ,"sudh" ]
cat = pd.Categorical(data)
cat.value_counts() 


#Python Pandas – Visualization 
d = pd.Series([1,2,3,3,5,6,6,8])
d.plot() 

df = pd.DataFrame({'a':[3,4,5,6,7],
                  'b':[4,5,6,7,8]}) 

df.plot(x= 'a',y='b') 
df.plot.scatter(x= 'a',y='b') 

dx = pd.Series([1,2,3,3,5,6,6,8]) 
dx.plot.pie() 







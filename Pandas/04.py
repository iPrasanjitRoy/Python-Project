import pandas as pd  
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

df.drop('PassengerId',axis=1,inplace=True)
df.drop(3,inplace=True) 

df.set_index("Name",inplace=True) 
df.reset_index()




d = {'key1' :[3,4,5,6,7],
     'key2':[5,6,7,8,6],
     'key3':[4,5,6,7,8]
}
pd.DataFrame(d)


df1 = pd.read_csv('Taxonomy.csv')
df1.dropna(inplace=True)


df2 = pd.read_csv('Taxonomy.csv')
df2.dropna(axis=1) 
df2.fillna("ROY") 

df.reset_index(inplace=True) 

g = df.groupby('Survived') 
g.sum() 
g.mean() 

g1 = df.groupby('Pclass') 
g1.sum() 
g1.mean() 

df5 = df[['Name',	'Survived',	'Pclass']][0:5]
df6 = df[['Name',	'Survived',	'Pclass']][5:10]
pd.concat([df5,df6]) 

df7 = pd.concat([df5,df6],axis=1)

df7.fillna('ROY') 




data1 = pd.DataFrame({'key1':[1,2,4,5,6],
                      'key2':[4,5,6,7,8],
                      'key3':[3,4,5,6,6]
}
)

data2 = pd.DataFrame({'key1':[1,2,45,6,67],
                      'key4':[56,5,6,7,8],
                      'key5':[3,56,5,6,6]
}
)


pd.merge(data1,data2)
pd.merge(data1,data2,how = 'left') 
pd.merge(data1,data2,how = 'right') 
pd.merge(data1,data2,how = 'outer',on = 'key1')
pd.merge(data1,data2,how = 'cross')




data1 = pd.DataFrame({'key1':[1,2,4,5,6],
                      'key2':[4,5,6,7,8],
                      'key3':[3,4,5,6,6]},
                     index = ['a','b','c','d','e']
)

data2 = pd.DataFrame({'key11':[1,2,4,5,6],
                      'key22':[4,5,6,7,8],
                      'key33':[3,4,5,6,6]
},index=['a','b','h','i','j']
)



data1.join(data2)
data1.join(data2,how='right') 
data1.join(data2,how='inner') 
data1.join(data2,how='outer') 
data1.join(data2,how='cross')



df['Fare_INR'] = df['Fare'].apply(lambda x : x*80)


def euro_inr(x):
    return x*80

df['Fare_INR2'] = df['Fare'].apply(euro_inr)






def cat_fare(x):
    if x<10 :
        return "cheap"
    elif x>=10 and x<20:
        return 'mid'
    else :
        return 'high'
    

df['car_fare'] = df['Fare'].apply(cat_fare)





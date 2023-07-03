import pandas as pd 

MyData = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(len(MyData)) 


s = MyData['Name'][0:10]

l = ['a','b','c','d','e','f','g','h','i','j']

s1 =pd.Series(list(s),index=l) 

s2 = s1.append(s) 
s2[4] 

s4 = pd.Series([3,4,5,6,6] , index=[2,4,5,6,1]) 
s5 = pd.Series([34,345,45,45,454] , index=[9,4,5,6,7]) 

s6 = s4.append(s5) 
s6[4] 

s4*s5 
s4+s5 


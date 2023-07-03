import requests 
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging 


Flipcart_url = "https://www.flipkart.com/search?q=" + "redmi" 
urlclient = urlopen(Flipcart_url)
flipcart_page = urlclient.read()  

flipcart_html = bs(flipcart_page,'html.parser')  

bigbox = flipcart_html.findAll("div" , {"class":"_1AtVbE col-12-12"}) 

print (len(bigbox)) 
del bigbox[0:3]


productlink = "https://www.flipkart.com" +bigbox[3].div.div.div.a['href']  



product_req = requests.get(productlink)
product_html = bs(product_req.text,'html.parser')  
comment_box = product_html.find_all("div",{"class" : "_16PBlm"}) 
print (len(comment_box)) 


for i in comment_box:
    print(i.div.div.find_all('p',{"class":"_2sc7ZR _2V5EHH"})[0].text)




for i in comment_box:
    print(i.div.div.div.div.text)




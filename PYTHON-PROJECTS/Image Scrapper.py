import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import logging
import pymongo 
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


save_dir = "images/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

query = "Prasanjit Roy" 
response = requests.get(f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M")

soup = BeautifulSoup(response.content ,'html.parser')

images_tags = soup.find_all("img")
print(len(images_tags)) 

del images_tags[0]

img_data_mongo = []
for i in images_tags:
    image_url = i['src']
    image_data = requests.get(image_url).content
    mydict = {"index":image_url , "image" : image_data}
    img_data_mongo.append(mydict)
    with open(os.path.join(save_dir,f"{query}_{images_tags.index(i)}.jpg"),"wb") as f :
              f.write(image_data)



uri = "mongodb+srv://prasanji:12345@cluster0.bxthqdz.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

db = client["image_scrap"] 
coll_image = db["image_scrap"]
coll_image.insert_many(img_data_mongo) 


    



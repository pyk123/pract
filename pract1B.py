import requests # requests module allows to send HTTP request.
import csv
from bs4 import BeautifulSoup
import mysql.connector as mysql
import pandas as pd
req = requests.get("https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&asshow=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_Quer
yStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&astype=RECENT&suggestionId=mobiles%7CMobiles&requestId=d880cadf-96c3-472d-b134-
4fc05ac82697&as-backfill=on")
soup = BeautifulSoup(req.content, "html.parser")
# print(soup.prettify())
res = soup.head 
print(res.text) 
# Mobiles- Buy Products Online at Best Price in India - All Categories | Flipkart.com
all_products = [] 
products = soup.findAll("div", {"class": "_3pLy-c row"})
#print(products)
mydb = mysql.connect(
 host="localhost",
 user="root",
 password="root",
 database="flipkartdb"
)
mycursor = mydb.cursor()
for product in products:
 mname = product.select("div > div._4rR01T")[0].text.strip()
 print(mname)
 mprice = product.select("div > div._30jeq3")[0].text.strip()

 x = mprice.split("₹")
 print(x[1])
 mratings = product.select("div > span._1lRcqv")[0].text.strip()
 print(mratings)
 mresolution = product.select("ul > li.rgWa7D")[1].text.strip()
 s = mresolution.split()
 # print(s)
 # print(s[0: 2]) #['16.51', 'cm']
 mr = "".join(s[0: 2])
 print(mr)
 mram = product.select("ul > li.rgWa7D")[0].text.strip()
 r = mram.split()
 # print(r)
 # print(r[0: 2])
 ram = "".join(r[0: 2])
 print(ram)
 mstorage = product.select("ul > li.rgWa7D")[0].text.strip()
 store = mstorage.split()
 # print(store)
 # print(store[4: 6])
 storage = "".join(store[4: 6])
 print(storage)
 sql = "INSERT INTO products_info (Mobile_Name, Price, Ratings, Resolution, Ram, Storage) 
VALUES (%s, %s, %s, %s, %s, %s)"
 val = (mname, x[1], mratings, mr, ram, storage)
 mycursor.execute(sql, val)
 mydb.commit()
 all_products.append({
 "Name": mname,
 "Price": x[1],
 "Ratings": mratings,
 "Resolution": mr,
 "Ram": ram,
 "Storage": storage
 })
print("Record Inserted Successfully...")
mydb.close()
print(all_products)
keys = all_products[0].keys() 

print(keys) # dict_keys(['Name', 'Price'])
# Generating CSV from data
with open('flipkart2.csv', 'w', newline="", encoding="utf-8") as output_file:
 dict_writer = csv.DictWriter(output_file, keys)
 dict_writer.writeheader()
 dict_writer.writerows(all_products)
print("CSV file created...")
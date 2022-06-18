import requests 
import csv
from bs4 import BeautifulSoup
import mysql.connector as mysql
req = 
requests.get("https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search
&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY")
soup = BeautifulSoup(req.content, "html.parser")
# print(soup.prettify())
res = soup.head 
print(res.text) 
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

 print(mprice) 
 sql = "INSERT INTO products (Mobile_Name, Price) VALUES (%s, %s)"
 val = (mname, x[1])
 mycursor.execute(sql, val)
 mydb.commit()
 all_products.append({
 "Name": mname,
 "Price": mprice
 })
print("Record Inserted Successfully...")
mydb.close()
print(all_products)
keys = all_products[0].keys() 
print(keys) 
with open('flipkart.csv', 'w', newline="", encoding="utf-8") as output_file:
 dict_writer = csv.DictWriter(output_file, keys)
 dict_writer.writeheader()
 dict_writer.writerows(all_products)
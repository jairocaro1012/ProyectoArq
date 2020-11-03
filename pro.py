import mysql.connector
from mysql.connector import errorcode
import requests
from bs4 import BeautifulSoup
print('Content-Type: text/plain')
print('')
print('working')
x="2"
y="pp"

#--hola desde putty--#
#--hola--#
#-hola x2---#
url= "https://visa-signature.com/co/ofertas-exclusivas"
req=requests.get(url)
soup=BeautifulSoup(req.content,"html.parser")
datos=soup.find_all('div',class_ ="offer restaurantes")
total=list()
total1=list()
total2=list()
total3=list()
for i in datos:
  total1.append(i.h3.text)
for i in datos:
  total.append(i.p.text)
for i in datos:
  total2.append(i.span.text)

print(total)
print(total1)
print(total2[0])
print(total3)
try:
        cnx = mysql.connector.connect(user='Jairo', password='Jairo1012#',
                                      host='127.0.0.1',
                                      database='proyecto')
        cursor=cnx.cursor()

        for i in range(len(total)):
                sql=("insert into promociones"
                        "(id,nombre,descripcion,fecha,img)"
                        "VALUES (%s,%s,%s,%s,%s)")
                data=(i,total1[i],total[i],total2[i],i)
                cursor.execute(sql,data)
                cnx.commit()
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()


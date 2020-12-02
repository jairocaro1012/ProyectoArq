#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify ,json
from flask_cors import CORS
import numpy as np;
print('Content-Type: text/plain')

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


x="2"
y="pp"
import cgi
data=cgi.FieldStorage()
clave = format(data.getvalue('user'))
print (clave)
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

print(total1[0])
print(total1)
print(total2)
print(type(total1))
obj=np.array([])

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
try:
    connection = mysql.connector.connect(user='Jairo', password='Jairo1012#',
                                      host='127.0.0.1',
                                      database='proyecto')

    sql_select_Query = "select * from promociones"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Laptop is: ", cursor.rowcount)

    print("\nPrinting each laptop record")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Price  = ", row[2])
        print("Purchase date  = ", row[3], "\n")
        obj[j]=row[3]
        j=j+1
        


except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")


# sanity check route
@app.route('/prueba', methods=['GET'])
def ping_pong():

    return jsonify({'nombre': obj})


if __name__ == '__main__':
    app.run(host="0.0.0.0")


import psycopg2

conn = psycopg2.connect(host='000.000.000.000', dbname='TestDb',user='postgres',password='XXXX',port=5432)
cursor=conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''

cursor.execute(sql)
print("Table created successfully........")
conn.commit()

#Closing the connection
conn.close()
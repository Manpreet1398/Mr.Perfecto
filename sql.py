import mysql.connector

db = mysql.connector.connect(user='root', password='manpreet123!@#$%^', host='localhost')
print(db)
cursor =db.cursor(buffered=True)
#cursor.execute("create database table123")
cursor.execute("use table123")
#cursor.execute("create table employee(id int NOT NULL AUTO_INCREMENT,name varchar(255),address varchar(255),email varchar(265),joining_date varchar(255),Primary Key(id))")
#cursor.execute("insert into employee values(1,'manpreet','delhi','man@gmail.com','2019/01/01')")
#cursor.execute("insert into employee values(NULL,'manpr','mumbai','manr@gmail.com','2019/02/02')")
#cursor.execute("insert into employee values(NULL,'man','haryana','manp@gmail.com','2019/03/03')")
#
# cursor.execute("select * from employee")
# print(cursor.fetchall())
# query="insert into employee(id,name,address,email,joining_date) values(null,%s,%s,%s,%s)"
# data=[('am','noida','am@gmail.com','2019/01/04'),
#       ('amit','bangalore','amit@gmail.com','2019/06/05'),
#       ('sumit','gurgaon','sumit@gmail.com','2019/05/06')]
# cursor.executemany(query,data)
# #print(cursor.fetchall())
#
# cursor.execute("update employee set name='anurag' where id=4")
# db.commit()
cursor.execute("delete from employee where id=5")
db.commit()
#select e.name,s.salary from eployee e left join salaary s on e.id=s.employee_id where joining_date="  "
#init (cursor,db)
# self.cursor=
# self.db=
# createTable(self,query)
# self.cursor.execute(query)
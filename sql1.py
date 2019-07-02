import mysql.connector

db = mysql.connector.connect(user='root', password='manpreet123!@#$%^', host='localhost')
print(db)
cursor =db.cursor(buffered=True)
#cursor.execute("create database ")
cursor.execute("use user")
#cursor.execute("create table user_de(id int NOT NULL AUTO_INCREMENT,username varchar(255),email varchar(265),Primary Key(id))")
cursor.execute("insert into user_de values(1,'manpreet','man@gmail.com')")
cursor.execute("insert into user_de values(NULL,'manpr','manr@gmail.com')")
cursor.execute("insert into user_devalues(NULL,'man','manp@gmail.com')")
db.commit()
cursor.execute("select * from user_de")
print(cursor.fetchall())
# query="insert into user_de(id,username,email) values(null,%s,%s)"
# data=[('am','am@gmail.com'),
#       ('amit','amit@gmail.com'),
#       ('sumit','sumit@gmail.com')]
# cursor.executemany(query,data)
# #print(cursor.fetchall())
# db.commit()
# cursor.execute("update employee set username='anurag' where id=4")
# db.commit()
# cursor.execute("delete from employee where id=5")
# db.commit()
#select e.name,s.salary from eployee e left join salaary s on e.id=s.employee_id where joining_date="  "
#init (cursor,db)
# self.cursor=
# self.db=
# createTable(self,query)
# self.cursor.execute(query)
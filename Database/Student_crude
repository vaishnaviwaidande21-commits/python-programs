import sqlite3

con=sqlite3.connect("student.db")

cursor = con.cursor()

cursor.execute('''
       create table if not exists stud(
               sid integer primary key,
               name text not null,
               age integer null
               )        
               
               ''')
print(" Table Created!!")

# cursor.execute("insert into stud(sid,name,age) values(?,?,?)",(1,"Alice",21))
con.commit()
print(" Data Inserted!!")

# user input
# sid=int(input(" enter your id: "))
# name=input(" enter your name: ")
# age=int(input(" enter your age: "))

# cursor.execute("insert into stud(sid,name,age) values(?,?,?)",(sid,name,age))
# con.commit()
# print("  Data Inserted")

# cursor.execute(" select * from stud ")
# rows=cursor.fetchall()
# print(rows)

# for r in rows:
#     print(f"{r[0]}")

# # single

# sid=int(input(" enter the id : "))
# cursor.execute(" select * from stud where sid=?",(sid,))
# row=cursor.fetchone()
# print(row)


#update
# sid=int(input(" enter the id : "))
# cursor.execute(" select * from stud where sid=?",(sid,))
# row=cursor.fetchone()
# print(row)

# if sid==row[0]:
#     newname=input("enter the name: ")
#     cursor.execute(" update stud set name=? where sid=?",(newname,sid,))

#     con.commit()
#     print(" Update succesful")
# else:
#     print(" no record found!!")


cursor.execute(" select name ,age from stud where age between 18 and 25 ")
rows=cursor.fetchall()
print(rows)

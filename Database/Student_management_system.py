import smtplib
from email.message import EmailMessage
from reportlab.pdfgen import canvas
import sqlite3

con=sqlite3.connect("student1.db")
cursor =con.cursor()

cursor.execute('''
            create table if not exists student2(
            name text not null,
            rollno integer primary key,
            maths integer not null,
            science integer not null,
            english integer not null,
            total_marks integer not null,
            percentage float not null
            )

               ''')
while True:

    print(" -----------------operations -----------------------")
    print("\n 1. Insert data \n 2.Update data \n 3. View data \n 4. Search records \n 5.Delete record \n 6.View result \n 7. Download result and send to email")
    ch=int(input(" enter your choice : "))

    match ch:

        case 1:
            no=int(input(" enter the no of students data to be filled: "))
            for i in range(1,no+1):

                name=input("\n enter student name : ")
                rollno=int(input(" enter the roll no: "))
                m1=int(input(" enter the marks of maths: "))
                m2=int(input(" enter the marks of science: "))
                m3=int(input(" enter the marks of english : "))
                total=m1+m2+m3
                percent=(total/300)*100

                cursor.execute(" insert into student2 values (?,?,?,?,?,?,?)",(name,rollno,m1,m2,m3,total,percent,))
                con.commit()
            print(" Data inserted !!")





        case 2:
            print("\n press \n 1. for single update \n 2. for multiple updates : \n ")
            choice=int(input(" enter your choice: "))

            if choice==1:
                u_ch=input(" enter what you want to update (name,rollno,maths_marks,science_marks,english_marks): ")
                if u_ch=="name":
                    rollno=input(" enter the rollno: ")
                    new_name=input(" enter the name : ")
                    cursor.execute(" update student2 set name=? where rollno=?",(new_name,rollno,))
                    con.commit()

                elif u_ch=="rollno":
                    name=input(" enter the name: ")
                    new_rollno=int(input(" enter new roll no: "))
                    cursor.execute(" update student2 set rollno=? where name=?",(name,new_rollno,))
                    con.commit()

                elif u_ch=="maths_marks":
                    rollno=input(" enter the rollno: ")
                    new_marks=int(input(" enter new marks: "))
                    cursor.execute(" update student2 set maths=? where rollno=?",(new_marks,rollno,))
                    con.commit()

                elif u_ch=="science_marks":
                    rollno=input(" enter the rollno: ")
                    new_marks=int(input(" enter new marks: "))
                    cursor.execute(" update student2 set science=? where rollno=?",(new_marks,rollno,))
                    con.commit()

                elif u_ch=="english_marks":
                    rollno=input(" enter the rollno: ")
                    new_marks=int(input(" enter new marks: "))
                    cursor.execute(" update student2 set english=? where rollno=?",(new_marks,rollno,))
                    con.commit()

                else:
                    print(" Invalid input!!")

            elif choice==2:
                
                cho=input(" enter what you want to update : ")

                if cho=='name' and 'maths_marks':
                    rollno=input(" enter the rollno : ")
                    new_name=input(" enter the name : ")
                    new_marks=int(input(" enter new marks: "))
                    cursor.execute(" update student2 set name=? , maths=? where rollno=?",(new_name,new_marks,rollno,))
                    con.commit()

                elif cho=='name' and 'science_marks':
                    rollno=input(" enter the rollno : ")
                    new_name=input(" enter the name : ")
                    new_marks=int(input(" enter new marks: "))
                    cursor.execute(" update student2 set name=? , science=? where rollno=?",(new_name,new_marks,rollno,)) 
                    con.commit()              

                elif cho=='name' and 'english_marks':
                    rollno=input(" enter the rollno : ")
                    new_name=input(" enter the name : ")
                    new_marks=int(input(" enter new marks: "))
                    cursor.execute(" update student2 set name=? , maths=? where rollno=?",(new_name,new_marks,rollno,))
                    con.commit()

                elif cho=='maths_marks' and 'science_marks':
                    rollno=input(" enter the rollno : ")
                    new_maths=int(input(" enter new marks: "))
                    new_science=int(input(" enter new marks: "))
                    cursor.execute(" update student2 set maths=?,science=? where rollno=?",(new_maths,new_science,rollno,))
                    con.commit()

                elif cho=='science_marks' and 'english_marks':
                    rollno=input(" enter the rollno : ")
                    new_english=int(input(" enter new marks: "))
                    new_science=int(input(" enter new marks: "))
                    cursor.execute(" update student2 set science=?,english=? where rollno=?",(new_science,new_english,rollno,))
                    con.commit()

                elif cho=='maths_marks' and 'english_marks':
                    rollno=input(" enter the rollno : ")
                    new_english=int(input(" enter new marks: "))
                    new_maths=int(input(" enter new marks: "))
                    cursor.execute(" update student2 set maths=?,english=? where rollno=?",(new_maths,new_english,rollno,))
                    con.commit()

                else:
                    print(" Invalid input !!")


            else:
                print(" Invalid choice !!!")






        case 3:
            cursor.execute(" select * from student2 ")
            rows=cursor.fetchall()
            print(rows)




        case 4:
            choi=int(input("\n press \n 1. for search using name \n 2. for search using rollno : \n"))

            if choi==1:
                name=input(" enter the name : ")

                cursor.execute(" select * from student2 ")
                rows=cursor.fetchall()
                print(rows)

                if name in rows[0]:
                    cursor.execute(" select * from student2 where name=?",(name,))
                    row=cursor.fetchall()
                    print(row)
                    print(" Data Found !!")
                else:
                    print(" Data not found !!")

            elif choi==2:

                rollno=int(input(" enter the rollno : "))

                cursor.execute(" select * from student2 ")
                rows=cursor.fetchall()
                print(rows)

                if rollno in rows[1]:
                    cursor.execute(" select * from student2 where rollno=?",(rollno,))
                    row=cursor.fetchall()
                    print(row)
                    print(" Data found !!")

                else:
                    print(" Data not found !! ")



        case 5:

            choic=int(input(" \n press \n 1. for single delete \n 2. for delete all : \n "))

            if choic==1:
                rollno=input(" enter the rollno: ")

                cursor.execute(" delete from student2 where rollno=?",(rollno,))
                con.commit()

                print(" record deleted successfully !!")

            elif choic==2:

                cursor.execute(" delete from student2 ")
                con.commit()

                print(" all records deleted !!")

            else:
                print(" Invalid choice ")




        case 6:
            rollno=int(input(" enter the roll no: "))

            cursor.execute(" select * from student2 where rollno=?",(rollno,))
            row=cursor.fetchone()
            
            if row:

                print("\n ====================== RESULT ========================")

                print(" Name         : ",row[0])
                print(" Rollno       : ",row[1])
                print(" Maths        : ",row[2])
                print(" Science      : ",row[3])
                print(" English      : ",row[4])
                print("---------------------------------------------------------")
                print(" Total Marks  : ",row[5])
                print(" Percentage   : ",row[6])

                if row[6]>=40:
                    print(" Result   : PASS ")
                else:
                    print(" Result   : FAIL ")

                print("===========================================================")



        case 7:
            

            rollno = int(input("Enter Roll Number : "))

            cursor.execute("select * from student2 where rollno=?", (rollno,))
            row = cursor.fetchone()

            if row:

                name = row[0]
                roll = row[1]
                maths = row[2]
                science = row[3]
                english = row[4]
                total = row[5]

                percentage = (total / 300) * 100

                if percentage >= 35:
                    result = "PASS"
                else:
                    result = "FAIL"

                # ---------------- Create PDF ----------------

                pdf = canvas.Canvas("Result.pdf")

                pdf.setFont("Helvetica-Bold",20)
                pdf.drawString(170,800,"STUDENT RESULT")

                pdf.setFont("Helvetica",14)

                pdf.drawString(70,760,"Name : "+name)
                pdf.drawString(70,735,"Roll No : "+str(roll))
                pdf.drawString(70,710,"Maths : "+str(maths))
                pdf.drawString(70,685,"Science : "+str(science))
                pdf.drawString(70,660,"English : "+str(english))
                pdf.drawString(70,635,"Total Marks : "+str(total))
                pdf.drawString(70,610,"Percentage : "+str(round(percentage,2))+" %")
                pdf.drawString(70,585,"Result : "+result)

                pdf.save()

                print("Result PDF Created Successfully.")

                # ---------------- Email ----------------

                receiver = input("Enter Email Address : ")

                sender = "purva.ransing0@gmail.com"
                password = "wrip jzxl jtej hgol"

                msg = EmailMessage()

                msg["Subject"] = "Student Result"
                msg["From"] = sender
                msg["To"] = receiver

                msg.set_content("Your Result is attached with this email.")

                with open("Result.pdf","rb") as f:
                    file = f.read()

                msg.add_attachment(file,
                                maintype="application",
                                subtype="pdf",
                                filename="Result.pdf")

                server = smtplib.SMTP_SSL("smtp.gmail.com",465)

                server.login(sender,password)

                server.send_message(msg)

                server.quit()

                print("Result Sent Successfully!!")

            else:

                print("Student Record Not Found!!")

import sqlite3
import time
import datetime
import math

class Student:
    def __init__(self,unix,date,name,surname,sex,maths,mathGrade,shona,shoGrade,english,engGrade,agriculture,agricGrade,science,sciGrade,total):
        self.unix = unix
        self.date = date
        self.name = name
        self.surname = surname
        self.sex = sex
        self.maths = maths
        self.shona =shona
        self.english = english
        self.agriculture = agriculture
        self.science = science
        self.total = total
        self.mathGrade = mathGrade
        self.shoGrade = shoGrade
        self.engGrade = engGrade
        self.agricGrade = agricGrade
        self.sciGrade = sciGrade
       
    

conn = sqlite3.connect('studentmarks.db')
c = conn.cursor()

#creating table
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS markschedule( name TEXT, surname TEXT, sex TEXT,maths INTEGER, mathGrade TEXT,shona INTEGER,shoGrade TEXT,english INTEGER,engGrade TEXT, agriculture INTEGER, agricGrade TEXT, science INTEGER, sciGrade TEXT, total INTEGER)")
    conn.commit()

#inserting student
def insert_student(student):
    with conn:
        c.execute("INSERT INTO markschedule VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", student)
                  
#updating student marks        
def update_mark(name,subject):
    with conn:
        c.execute("UPDATE markschedule SET subject = :subject WHERE name =:name AND surname = :surname",
                  {'name' :student.name, 'surname' :student.surname, 'maths' :student.maths, 'shona':student.shona,'english':student.english,'agriculture':student.agriculture,'science':student.science,'total':student.total})

#removing student fromdatabase        
def remove_student(name,surname):
    with conn:
        c.execute("DELETE from markschedule WHERE name =:name AND surname = :surname",{'name' :student.name, 'surname' :student.surname})
        return c.fetchall() 

#viewing student record
def get_student_by_name(surname):
    c.execute("SELECT *FROM markschedule WHERE surname=:surname",{'surname':surname})
    return c. fetchall()

#giving class position to student                   
def give_position(total):
    with conn:
        c.execute("SELECT*FROM markschedule ORDER BY total DESC")
        return c.fetchall() 

mark = [75, 64, 84, 45, 52]
detl =['nyasha', 'muzinda', 'f']
total = mark[0]  + mark[1] + mark[2] + mark[3] + mark[4]
grade  = ['mathGrade', 'shoGrade', 'engGrade', 'agricGrade', 'sciGrade']

if  mark[0]   >= 75:
    grade[0] = 'A'
elif 60 < mark[0] < 75:
    grade[0] = 'B'
elif 50 < mark[0] < 60:
    grade[0] = 'C'
elif 45 <mark[0]  < 50:
    grade[0] = 'D'
elif 40 <mark[0]  < 44:
    grade[0] = 'E'
else:
    grade[0] = 'U'
        

if  mark [1] >= 75:
    grade[1] = 'A'
elif 60 < mark [1]  < 75:
    grade[1] = 'B'
elif 50 < mark [1] < 60:
    grade[1]  = 'C'
elif 45 < mark [1]  < 50:
    grade[1] = 'D'
elif 40 < mark [1] < 44:
    grade[1] = 'E'
else:
    grade[1] = 'U'
      

if  mark [2]  >= 75:
    grade[2]  = 'A'
elif 60 < mark [2] < 75:
    grade[2] = 'B'
elif 50 < mark [2] < 60:
    grade[2] = 'C'
elif 45 <mark [2]  < 50:
    grade[2]  = 'D'
elif 40 < mark [2] < 44:
   grade[2]  = 'E'
else:
    grade[2] = 'U'
       

if  mark [3] >= 75:
    grade[3]  = 'A'
elif 60 < mark [3] < 75:
    grade[3]  = 'B'
elif 50 < mark [3] < 60:
    grade[3] = 'C'
elif 45 < mark [3] < 50:
    grade[3]  = 'D'
elif 40 < mark [3] < 44:
    grade[3] = 'E'
else:
    grade[3] = 'U'
  

if  mark [4] >= 75:
    grade[4]  = 'A'
elif 60 < mark [4] < 75:
    grade[4]  = 'B'
elif 50 < mark [4] < 60:
    grade[4] = 'C'
elif 45 < mark [4] < 50:
    grade[4] = 'D'
elif 40 < mark [4] < 44:
    grade[4]  = 'E'
else:
    grade[4] = 'U'
    
unix = time.time()
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-5m-%d %H:%M:%S'))
student = [unix, date, detl[0], detl[1], detl[2], mark[0],grade[0] , mark[1], grade[1], mark[2], grade[2], mark[3], grade[3], mark[4], grade[4], total]

create_table()
insert_student(student)
#students = get_student_by_name('madhuro')
#print(students)
#subject = update_mark('Tinashe',maths=98)
#student = remove_student('tinashe','madhuro')
#give_position(total)
#conn.close()
#c.close()
#print('tinashe')

import mysql.connector 
con=mysql.connector.connect(host='localhost',user='root',password='#Rahul*123$',db='tutorsclub')
my_cursor=con.cursor()

#creating student info table in the database
student_info="""
    create table student_info(subject_id int auto_increment primary key,
                                student_name varchar(100) not null,
                                class varchar(20) not null,
                                DOB DATE NOT NULL,
                                father_name varchar(100) not null,
                                mother_name varchar(100) not null,
                                location varchar(100),
                                type char,
                                joining_date date not null,
                                communication varchar(220),
                                audibility char,
                                punctuality char,
                                listening char
                                )
            """
    
my_cursor.execute(student_info)


# creating faculty info table

faculty_info="""
   create table FACULTY_INFO(faculty_id int auto_increment primary key,
                              name varchar(255) not null,
                              dob date not null,
                              location varchar(255) not null,
                              subject varchar(50) not null,
                              subject_key int,
                              joining_date date not null
                              )
            """
my_cursor.execute(faculty_info)





    


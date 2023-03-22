import openpyxl

# Create a new Excel file
workbook = openpyxl.load_workbook("tutorsclubexcel.xlsx")

# Select the active sheet
worksheet = workbook["student_info"]


# Insert data into the student_info
data = [
         [1,"Sasmitha","XI","2005-9-5","Ravi","Sunitha","Kollam","Daily","2021-5-27",2,3,5,2],
                    [2,"Keerthana","XI",'2006-4-27',"Sasi","Rema","Kozhikode","Daily",'2021-11-17',1,3,3,3],
                    [3,"Arjun","VII cbse",'2010-10-5',"Das","Lakshmi","Kochi","Weekly",'2021-7-26',2,3,1,0],
                    [4,"Kuriakose","VIII cbse",'2009-12-17',"Tony","Leena","Kottayam","Daily",'2021-9-21',5,1,4,0],
                    [5,"Norah","I cbse",'2016-4-26',"Fateh","Nooriya","Kollam","Daily",'2021-10-2',2,3,3,0],
                    [6,"Arthreya","II state",'2015-8-20',"ShankaranKutty","Lavanya","Trivandrum","Weekly",'2021-10-25',5,5,2,4],
                    [7,"Thomas","X cbse",'2007-3-12',"Alva Edison","Mariya","Kannur","Daily",'2021-9-2',4,1,4,1],
                    [8,"Rinaz","X igcse",'2007-7-25',"Navas","Jazi","Paripally","weekly",'2021-4-26',0,2,5,5],
                    [9,"Samarjeet","XI",'2006-8-9',"Koya","Ayisha","Kassargod","Daily",'2021-5-9',0,5,5,4],
                    [10,"Norah","I cbse",'2016-4-26',"Fateh","Nooriya","Kollam","Daily",'2021-10-2',2,3,3,0]
        ]
for row in data:
    worksheet.append(row)



worksheet = workbook["faculty_info"]


# Insert data into the faculty_info
data = [ [1001,"Akash","1998-10-12","calicut","maths",501,"2021-3-26"],
              [1002,"Aksa","1997-5-11","trivandrum","physics",502,"2021-11-23"],
              [1003,"Reshma","1998-10-12","calicut","english",503,"2021-8-14"],
              [1004,"Lakshmi","1998-10-12","calicut","maths",504,"2021-4-5"],
              [1005,"Kavya","1998-10-12","calicut","english",505,"2021-7-8"],
              [1006,"Sreelatha","1998-10-12","calicut","maths",506,"2021-12-12"],
              [1007,"Azbara","1998-10-12","calicut","maths",507,"2021-6-29"],
              [1008,"Teena","1998-10-12","calicut","mentoring",508,"2021-10-30"],
              [1009,"Anu","1998-10-12","calicut","maths",509,"2021-12-10"],
              [1010,"Sreeja","1998-10-12","calicut","science",510,"2021-3-10"]
         
        ]
for row in data:
    worksheet.append(row)   


worksheet = workbook["mark_sheet"]


# Insert data into the mark_sheet
data = [ [101,1,"Sasmitha","XI","maths","online","2 hrs","2022-2-12",100,82,82,"A"],
                    [102,2,"Keerthana","XI","physics","online","1 hr","2022-3-12",100,70,70,"B+"],
                    [103,3,"Arjun","VII cbse","english","online","2 hrs","2022-5-12",100,80,80,"A"],
                    [104,4,"Kuriakose","VIII cbse","english","online","30 mins","2022-4-12",100,90,90,"A+"],
                    [105,5,"Norah","I cbse","maths","online","10 mins","2022-1-12",100,70,70,"B+"],
                    [106,6,"Arthreya","II state","mentoring","online","15 mins","2022-8-12",100,50,50,"D"],
                    [107,7,"Thomas","X cbse","maths","online","2 hrs","2022-1-12",100,30,30,"F"],
                    [108,8,"Rinaz","X igcse","maths","online","2 hrs","2022-9-12",100,60,60,"B"],
                    [109,9,"Samarjeet","XI","accountancy","online","1 hr","2022-7-12",100,63,63,"B"],
                    [110,10,"Norah","I cbse","English","online","30 mins","2022-10-12",100,77,77,"B+"]
         
        ]
for row in data:
    worksheet.append(row)  


worksheet = workbook["subject_table"]


# Insert data into the subject_table
data = [[501,"Maths","quarterly",60,"midterm",64,"model",75,"final",74,"Akash"],
                  [502,"Physics","quarterly",72,"midterm",78,"model",80,"final",79,"Deepu"],
                  [503,"Chemistry","quarterly",83,"midterm",81,"model",79,"final",85,"Aksa"],
                  [504,"Science","quarterly",89,"midterm",91,"model",90,"final",92,"Sreeja"],
                  [505,"History","quarterly",60,"midterm",69,"model",78,"final",74,"Arun"],
                  [506,"Politics","quarterly",79,"midterm",80,"model",76,"final",89,"Gokul"],
                  [507,"Monitoring","quarterly",80,"midterm",86,"model",89,"final",87,"Amal"],
                  [508,"Economics","quarterly",78,"midterm",64,"model",77,"final",79,"Lekshmi"],
                  [509,"Finanace","quarterly",74,"midterm",69,"model",78,"final",80,"Anuja"],
                  [510,"accountancy","quarterly",90,"midterm",88,"model",89,"final",95,"Meenu"]
         
        ]
for row in data:
    worksheet.append(row)  

worksheet = workbook['grade_table']


# Insert data into the grade_table
data = [ [11,70,"c"],
            [12,60,"d"],
            [13,70,"c"],
            [14,50,"e"],
            [15,80,"b"],
            [16,90,"a"],
            [17,75,"c"],
            [18,20,"f"],
            [19,52,"e"],
            [20,88,"b"]
         
        ]
for row in data:
    worksheet.append(row)  

worksheet = workbook["feedback_table"]


# Insert data into the feedback_table
data = [ [201,1001,501,1,"good","2022-3-26"],
                   [202,1002,502,2,"average","2022-3-26"],
                   [203,1003,503,3,"good","2022-3-26"],
                   [204,1004,504,4,"excellent","2022-3-26"],
                   [205,1005,505,5,"poor","2022-3-26"],
                   [206,1006,506,6,"good","2022-3-26"],
                   [207,1007,507,7,"average","2022-3-26"],
                   [208,1008,508,8,"good","2022-3-26"],
                   [209,1009,509,9,"good","2022-3-26"],
                   [210,1010,510,10,"good","2022-3-26"]
         
        ]
for row in data:
    worksheet.append(row)  

workbook.save("tutorsclubexcel.xlsx")

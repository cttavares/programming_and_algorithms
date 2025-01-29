from functools import reduce
from variables import student_list
from variables import course_grades
from variables import course_names

def show_all_grades_from_course (course_index):
    for i in course_grades:
        print ("Student ",i, ". Grade: ", course_grades [i][course_index-1])    

def show_courses_below_average (average):
    #r = map (lambda z: [course_grades [i][z] for i in course_grades], [c for c in range (0, len (course_names))])
    r = filter (lambda z: reduce (lambda x, y: x + y, [course_grades [i][z] for i in course_grades])/len (course_grades) < average, [c for c in range (0, len (course_names))])
    for i in r:
        #print (i)
        print (course_names [i+1])

def show_student_by_id (id):
    for i in student_list:
        if i [0] == id:
            print ("Name: ", i [1],"; Email: ", i [2])
            grades = course_grades [id]
            for i, g in enumerate (grades):
                print (course_names [i+1], ": ", g)
            
            print ("Average: ", reduce (lambda x, y: x + y, grades)/len (grades))

def free_search (query):
    for i in student_list:
        if query in i [0] or query in i [1] or query in i [2]:
            print (i [0],";",i [1],";",i [2])
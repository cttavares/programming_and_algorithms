from variables import student_list
from variables import course_grades
from variables import course_names
    
def load_students ():
    with open('students.txt', 'r') as file:
        lines = file.readlines ()
    
    for i in lines:
        s = i.split (";")
        student_list.append ((s [0].strip(), s [1].strip(), s [2].strip()))
    #print ("Student list: ", student_list)

def load_courses_and_names():
    
    with open('grades.txt', 'r') as file:
        lines = file.readlines ()
    
    index = 1
    for name in (lines [0].split (";"))[1:]:
        course_names [index] = (name.strip ())
        index = index + 1

    for l in lines [1:]:
        grades = l.split (";")
        course_grades [grades [0]] = [float (i.strip()) for i in grades [1:]]

    #print (course_names)
    #print (course_grades)
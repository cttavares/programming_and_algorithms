from variables import student_list
from variables import course_grades
from variables import course_names

from file_functionality import load_students
from file_functionality import load_courses_and_names
from logic_functionality import show_all_grades_from_course
from logic_functionality import show_courses_below_average
from logic_functionality import show_student_by_id
from logic_functionality import free_search

def load_data ():
    load_students ()
    load_courses_and_names ()

def show_courses_available ():
    for i in course_names:
        print ("Course ", i, ":", course_names [i])

def do_show_all_grades_from_course ():
    show_courses_available ()
    course = int (input ("Write course number: "))
    show_all_grades_from_course (course)

def do_show_courses_below_average ():
    average = float (input ("Write the average: "))
    show_courses_below_average (average)

def do_show_student_by_id ():
    id = input ("Write the id: ")
    show_student_by_id(id)

def do_free_search ():
    free_query = input ("Write the query: ")
    free_search (free_query)

load_data ()
opcao = -1 
while (opcao != 5):
    print ("1. Show all grades per course")
    print ("2. Show all courses below average")
    print ("3. Show student by id")
    print ("4. Free query on students")
    print ("5. Exit")
    opcao = int (input ("Write option: "))

    if (opcao == 1):
        do_show_all_grades_from_course()
    elif opcao == 2:
        do_show_courses_below_average()
    elif opcao == 3:
        do_show_student_by_id ()
    elif opcao == 4:
        do_free_search ()

print ("Good bye!")
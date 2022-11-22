import random
from datetime import datetime as dt
from models.models import Student, Grade

def create_students(num_people):
    people = []
    first_names = ['jack', 'geoff', 'thomas', 'brock', 'tank', 'cheeseman','jessie','hank','toil','pale','mane','stump']
    last_names = ['horn', 'blade', 'books', 'cracken', 'stank', 'cheeseman','johnson','freeman','jack']
    i = 0
    while(i < num_people):
        person = []
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        now = dt.now()
        person = Student(first_name=first_name, last_name = last_name, created_by = 'Seed', created_on = now)
        people.append(person)
        i+=1
    return people

def create_grades(students):
    classes = ['french', 'math', 'english', 'stuff','pottery','breadmaking','woodwork','yeezy','breezy']
    for student in students:
        i = 0
        while(i < random.randint(1,3)):
            now = dt.now()
            grade = Grade(class_name = random.choice(classes), score = random.randint(1,100), created_by = 'Seed', created_on = now)
            student.grades.append(grade)
            i+=1
    return students

def generate_students_with_grades(num_students):
    students = create_students(num_students)
    graded_students = create_grades(students)
    return graded_students
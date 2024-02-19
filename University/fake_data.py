# Necessary Imports
from django.db.models import Sum
from faker import Faker
from.models import *
import random

'''-------------------------------------------------------------------------------------------------------------------'''

# Create an instance of Faker Class.
fake = Faker()

'''-------------------------------------------------------------------------------------------------------------------'''

# Function 1: One Time only, unless we add more Departments.
''' YOE Function:
    Function to randomly assign an Year Of Establisment to each Department.
    We can also manually update the YOE in the database useing the INSERT query.
'''
def YOE():
    queryset = Department.objects.all()
    for query in queryset:
        if query.YOE is None:
            query.YOE = random.randint(1990,2002)
            query.save()

'''-------------------------------------------------------------------------------------------------------------------'''

# Function 2: Fake Data to create 10 Student instances every time.
def create_students(n):
    department_obj = Department.objects.all()
    try:    
        for _ in range(n):
            # Creates a Student Object with all necessary data.
            Student.objects.create(
                department = random.choice(department_obj),
                student_id = StudentId.objects.create(student_id = 'STD' + str(random.randint(101,999))),
                student_name = fake.name(),
                student_email = fake.email(),
                student_age = random.randint(18,22),
                student_address = fake.address()
            )

        # Update student_count of Department Class everytime a set of new Student instances are created.
        queryset = Department.objects.all()
        for query in queryset:
            students = Student.objects.filter(department = query).count()
            query.student_count = students
            query.save()

    except Exception as e:
        print(e)

'''-------------------------------------------------------------------------------------------------------------------'''

# Function 3: Create Fake marks and assign to each subject resoective to each student.
def create_marks():
    students = Student.objects.all()
    subjects = Subject.objects.all()
    
    try:
        for student in students:
            for subject in subjects:

                # Check if a SubjectMarks instance already exists for the student and subject
                existing_students = SubjectMarks.objects.filter(student=student,subject=subject).exists()
                
                if not existing_students:
                    # If no existing marks, create a new Subject_Marks instance
                    SubjectMarks.objects.create(
                        student=student,
                        subject=subject,
                        marks=random.randint(30,100)
                    )
    except Exception as e:
        print(e)

'''-------------------------------------------------------------------------------------------------------------------'''

# Function 4:
def create_report_card():
    ranks = Student.objects.annotate(
        total_marks=Sum('stdt_marks__marks')).order_by('-total_marks')
    
    # Start rank from 1
    i = 1
    for rank in ranks:
        Report_Card.objects.create(
            student = rank,
            total = rank.total_marks,
            rank = i
        )

        # Increment rank
        i += 1
    

'''-------------------------------------------------------------------------------------------------------------------'''

# Function 5:
def create_data(n):
    create_students(n)
    create_marks()
    create_report_card()
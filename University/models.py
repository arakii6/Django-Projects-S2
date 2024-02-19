from django.db import models

# Student Manager Class
class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)
        
'''--------------------------------------------------------------'''
# Department Class
class Department(models.Model):

    department_name = models.CharField(max_length = 100)
    YOE = models.IntegerField(default = 1990, null = True)
    student_count = models.PositiveIntegerField(default = 0,null = True)

    def __str__(self) -> str:
        return self.department_name

    class Meta:
        ordering = ['department_name']
        verbose_name_plural = 'Department'

'''--------------------------------------------------------------'''
# Student Id Class
class StudentId(models.Model):

    student_id = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.student_id
    
    class Meta:
        verbose_name_plural = 'Student Id'

'''--------------------------------------------------------------'''
# Student Class
class Student(models.Model):

    department = models.ForeignKey(Department, related_name = 'stdt_dept', on_delete = models.CASCADE)
    student_id = models.OneToOneField(StudentId, related_name = 'stdt_id', on_delete = models.SET_NULL, null=True)

    student_name = models.CharField(max_length = 100)
    student_email = models.EmailField(unique = True)
    student_age = models.PositiveIntegerField(default = 18)
    student_address = models.TextField(null = True)
    is_deleted = models.BooleanField(default = False)

    # Student Manager
    objects = StudentManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name_plural = 'Student'

'''--------------------------------------------------------------'''
# Subject Class
class Subject(models.Model):
    subject_name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.subject_name
    
    class Meta:
        verbose_name_plural = 'Subject'

'''--------------------------------------------------------------'''
# Marks Class
class SubjectMarks(models.Model):
    student = models.ForeignKey(Student,related_name='stdt_marks',on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,related_name='stdt_sub',on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f'Student: {self.student.student_name}, Subject: {self.subject.subject_name}, Marks: {self.marks}'
    
    class Meta:
        unique_together = ['student','subject']
        verbose_name_plural ='Marks'

'''--------------------------------------------------------------'''
# Report Card Class
class Report_Card(models.Model):
    student = models.ForeignKey(Student, related_name = 'stdt_report_card', on_delete = models.CASCADE)
    total = models.SmallIntegerField()
    rank = models.SmallIntegerField()
    date = models.DateField(auto_now_add = True)

    class Meta:
        unique_together = ['total','rank','date']
        verbose_name_plural = 'Report Card'

'''--------------------------------------------------------------'''
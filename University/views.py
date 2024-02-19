from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import *
from .models import *

'''--------------------------------------------------------'''

# Advanced Search
def advanced_search(queryset,search_term,search_field):

    if search_term and search_field:
        if search_field == 'name':
            queryset = Student.objects.filter(student_name__icontains = search_term)
        elif search_field == 'department':
            queryset = Student.objects.filter(department__department_name__icontains = search_term)
        elif search_field == 'email':
            queryset = Student.objects.filter(student_email__icontains = search_term)
    
    return queryset

'''--------------------------------------------------------'''

# Student List
def student_list(request):

    # Create an instance of Student Class
    students = Student.objects.all()

    # Add Advanced Search
    search_term = request.GET.get('search_term')
    search_field = request.GET.get('search_field')
    students = advanced_search(students,search_term,search_field)

    # Add Pagination
    paginator = Paginator(students, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'page_name':'Student Details','students':page_obj}
    return render(request,'student-list.html',context)

'''--------------------------------------------------------'''

def report_card(request,student_id):

    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)

    context = {'report': queryset, 'page_name': 'Report Card'}

    return render(request,'report_card.html',context)

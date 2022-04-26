from django.shortcuts import render

# Create your views here.
def login_student(request):
    return render(request,'login_student.html')
def login_staff(request):
    return render(request,'login_staff.html')
def login_teacher(request):
    return render(request,'login_teacher.html')
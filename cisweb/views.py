from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def edit_profile(request):
    return render(request,'edit_profile.html')

def cishome1(request):
    return render(request,'teacher_profile2.html') 
    #หน้าป่าวยังไม่เชื่อม 

def profile(request):
    # teacher_id = 
    # role = 
    prefix = request.GET['prefix']
    gender = request.GET['gender']
    firstname = request.GET['firstname']
    lastname = request.GET['lastname']
    #teacher_img = request.GET['teacher_img']
    #certificate = request.GET['certificate']
    teacher_tel = request.GET['teacher_tel']
    teacher_email = request.GET['teacher_email']
    #status = request.GET['status']
    
    return render(request,'teacher_profile.html',
    {'prefix':prefix,
    'gender':gender,
    'firstname':firstname,
    'lastname':lastname,
    'teacher_tel':teacher_tel,
    'teacher_email':teacher_email
    })
    #มีปัญหา 


def responsibiility(request):
    return render(request,'responsibiility.html')

def student_profile(request):
    return render(request,'student_profile.html')
    
def student_profile(request):
    return render(request,'student_profile.html')

def train(request):
    return render(request,'Co-op_train.html')

def traindetails(request):
    return render(request,'train_details.html')

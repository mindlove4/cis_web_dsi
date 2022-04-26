from msilib.schema import Class
from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator

class Log_in(models.Model):
    user_id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    def __str__(self):
        return ("<id>: %s <username>: %s  <password>: %s"%(self.user_id, self.username, self.password))

class Address_Student(models.Model):
    address_stu_id= models.AutoField(primary_key=True)
    house_number= models.CharField(max_length=255)
    village_number= models.CharField(max_length=255)
    soi = models.CharField(max_length=255)
    road = models.CharField(max_length=255)
    subdistrict= models.CharField(max_length=255) 
    district= models.CharField(max_length=255)
    province= models.CharField(max_length=255)
    postcode= models.IntegerField(max_length=5, validators=[MinLengthValidator(5)])

class Teacher(models.Model):
    teacher_id= models.AutoField(primary_key=True)
    user_id= models.ForeignKey(Log_in, on_delete=models.CASCADE)
    teacher_prefix= models.CharField(max_length=10)
    teacher_firstname= models.CharField(max_length=255)
    teacher_lastname= models.CharField(max_length=255)
    gender= models.CharField(max_length=1)
    teacher_img= models.CharField(max_length=255)
    id_card= models.IntegerField(max_length=13, validators=[MinLengthValidator(13)])
    role= models.CharField(max_length=255)
    certificate= models.CharField(max_length=255)
    status= models.BooleanField()
    phone_regex = RegexValidator(regex=r'^\d{9,15}$')
    teacher_tel = models.CharField(validators=[phone_regex,MinLengthValidator(13)], max_length=10)
    teacher_email= models.EmailField(max_length=255)

class Student(models.Model):
    student_id=models.AutoField(primary_key=True)
    user_id= models.ForeignKey(Log_in, on_delete=models.CASCADE)
    teacher_id= models.ForeignKey(Teacher, on_delete=models.CASCADE)
    address_stu_id= models.ForeignKey(Address_Student, on_delete=models.CASCADE)
    student_prefix= models.CharField(max_length=10),
    student_firstname= models.CharField(max_length=255)
    student_lastname= models.CharField(max_length=255)
    gender= models.CharField(max_length=1)
    student_img= models.CharField(max_length=255)
    date_of_birth= models.DateTimeField()
    id_card= models.IntegerField(max_length=13, validators=[MinLengthValidator(13)])
    campus= models.CharField(max_length=255)
    education_level= models.CharField(max_length=255)
    study_year= models.CharField(max_length=255)
    faculty= models.CharField(max_length=255)
    major= models.CharField(max_length=255)
    gpax= models.DecimalField(max_digits=3,decimal_places=2)
    phone_regex = RegexValidator(regex=r'^\d{9,15}$')
    student_tel = models.CharField(validators=[phone_regex,MinLengthValidator(13)], max_length=10)
    student_email= models.EmailField(max_length=255)

class Staff(models.Model):
    staff_id=models.AutoField(primary_key=True)
    user_id= models.ForeignKey(Log_in, on_delete=models.CASCADE)
    staff_prefix= models.CharField(max_length=10),
    staff_firstname= models.CharField(max_length=255)
    staff_lastname= models.CharField(max_length=255)
    gender= models.CharField(max_length=1)
    staff_img = models.CharField(max_length=1)
    id_card= models.IntegerField(max_length=13, validators=[MinLengthValidator(13)])
    phone_regex = RegexValidator(regex=r'^\d{9,15}$')
    staff_tel = models.CharField(validators=[phone_regex,MinLengthValidator(13)], max_length=10)
    staff_email= models.EmailField(max_length=255)

class Address_Company(models.Model):
    address_company_id=models.AutoField(primary_key=True)
    phone_regex = RegexValidator(regex=r'^\d{9,15}$')
    company_tel = models.CharField(validators=[phone_regex,MinLengthValidator(13)], max_length=10)
    company_name= models.CharField(max_length=255)
    soi=models.CharField(max_length=255)
    road=models.CharField(max_length=255)
    subdistrict= models.CharField(max_length=255)
    district=models.CharField(max_length=255)
    postcode= models.IntegerField(max_length=5, validators=[MinLengthValidator(5)])

class Coop_Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    staff_id= models.ForeignKey(Staff, on_delete=models.CASCADE)
    address_company_id= models.ForeignKey(Address_Company, on_delete=models.CASCADE)
    company_name=models.CharField(max_length=255)
    company_type=models.CharField(max_length=255)
    company_career_link=models.CharField(max_length=255)

class Company_Position(models.Model):
    position_id=models.AutoField(primary_key=True)
    company_id =models.ForeignKey(Coop_Company, on_delete=models.CASCADE)
    company_name=models.CharField(max_length=255)
    department=models.CharField(max_length=255)
    position=models.CharField(max_length=255)
    start_apply= models.DateTimeField() 
    deadline_apply=models.DateTimeField()
    internship_period=models.CharField(max_length=1)
    amount=models.IntegerField(max_length=4)
    allowance=models.IntegerField(max_length=4)
    link_register=models.CharField(max_length=255)

class Train_Contact(models.Model):
    train_contact_id=models.AutoField(primary_key=True)
    institute_number=models.CharField(max_length=255)
    institute_name=models.CharField(max_length=255)
    soi=models.CharField(max_length=255)
    road=models.CharField(max_length=255)
    subdistrict=models.CharField(max_length=255)
    district=models.CharField(max_length=255)
    province=models.CharField(max_length=255)
    postcode= models.IntegerField(max_length=5, validators=[MinLengthValidator(5)])
    phone_regex = RegexValidator(regex=r'^\d{9,15}$')
    institute_tel = models.CharField(validators=[phone_regex,MinLengthValidator(13)], max_length=10)
    institute_email=models.EmailField(max_length=255)

class Coop_Train(models.Model):
    coop_train_id=models.AutoField(primary_key=True)
    staff_id =models.ForeignKey(Staff, on_delete=models.CASCADE)
    train_contact_id=models.ForeignKey(Train_Contact, on_delete=models.CASCADE)
    intstitute_name=models.CharField(max_length=255)
    curriculum=models.CharField(max_length=255)
    datetime_event=models.CharField(max_length=255) 
    start_apply=models.DateTimeField()
    deadline_apply=models.DateTimeField()
    amount= models.CharField(max_length=255) 
    location=models.CharField(max_length=255) 
    cost=models.IntegerField(max_length=6)
    link_detail=models.CharField(max_length=255)

class Agenda(models.Model):
    agenda_id=models.AutoField(primary_key=True)
    coop_train_id=models.ForeignKey(Coop_Train, on_delete=models.CASCADE)
    curriculum=models.CharField(max_length=255)
    agenda_link=models.CharField(max_length=255)

class Upload_Document (models.Model):
    upload_id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher_id=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    staff_id=models.ForeignKey(Staff, on_delete=models.CASCADE)
    date=models.DateTimeField()
    internship_application_form=models.CharField(max_length=255)
    job_application=models.CharField(max_length=255)
    establishment_proposal=models.CharField(max_length=255)
    transcript=models.CharField(max_length=255)
    student_certificate=models.CharField(max_length=255)
    copy_ID_card=models.CharField(max_length=255)
    courtesy_letter=models.CharField(max_length=255)
    acceptance_form=models.CharField(max_length=255)
    letter_of_surrender=models.CharField(max_length=255)

class Internship_Document(models.Model):
    doc_id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staff, on_delete=models.CASCADE)
    internship_policy= models.CharField(max_length=255)
    steps_for_internships=models.CharField(max_length=255)
    internship_schedule=models.CharField(max_length=255)
    internship_application_form=models.CharField(max_length=255)
    establishment_proposal=models.CharField(max_length=255)
    job_application=models.CharField(max_length=255)
    internship_documents=models.CharField(max_length=255)

class Visualization(models.Model):
    visualization_id=models.AutoField(primary_key=True)
    staff_id= models.CharField(max_length=255)
    propotion_of_company= models.CharField(max_length=255)
    total_account_company=models.CharField(max_length=255)




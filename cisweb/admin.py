from django.contrib import admin
from .models import Log_in,Address_Student,Teacher,Student,Staff,Address_Company,Coop_Company,Company_Position,Train_Contact,Coop_Train,Agenda,Upload_Document,Internship_Document,Visualization
#Registor model

class Log_inAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Log_in._meta.fields]
admin.site.register(Log_in,Log_inAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Student._meta.fields]
admin.site.register(Student,StudentAdmin)

class Address_StudentAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Address_Student._meta.fields]
admin.site.register(Address_Student,Address_StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Teacher._meta.fields]
admin.site.register(Teacher,TeacherAdmin)

class StaffAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Staff._meta.fields]
admin.site.register(Staff,StaffAdmin)

class Coop_TrainAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Coop_Train._meta.fields]
admin.site.register(Coop_Train,Coop_TrainAdmin)

class Train_ContactAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Train_Contact._meta.fields]
admin.site.register(Train_Contact,Train_ContactAdmin)

class AgendaAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Agenda._meta.fields]
admin.site.register(Agenda,AgendaAdmin)

class Coop_CompanyAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Coop_Company._meta.fields]
admin.site.register(Coop_Company,Coop_CompanyAdmin)

class Address_CompanyAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Address_Company._meta.fields]
admin.site.register(Address_Company,Address_CompanyAdmin)

class Company_PositionAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Company_Position._meta.fields]
admin.site.register(Company_Position,Company_PositionAdmin)

class Upload_DocumentAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Upload_Document._meta.fields]
admin.site.register(Upload_Document,Upload_DocumentAdmin)

class Internship_DocumentAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Internship_Document._meta.fields]
admin.site.register(Internship_Document,Internship_DocumentAdmin)

class VisualizationAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Visualization._meta.fields]
admin.site.register(Visualization,VisualizationAdmin)


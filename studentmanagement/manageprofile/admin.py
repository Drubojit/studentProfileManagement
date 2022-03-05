from django.contrib import admin
from .models import StudentProfileModel

@admin.register(StudentProfileModel)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display=['id','name','dateofbirth','gender','note']

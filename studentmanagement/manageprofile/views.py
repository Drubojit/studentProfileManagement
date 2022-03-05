from django.shortcuts import render,redirect
from django.views import View
from .models import StudentProfileModel
from .forms import AddStudentForm
# Create your views here.


class Home(View):
    def get(self,request):
        studentData = StudentProfileModel.objects.all()
        return render(request,'manageprofile/home.html',{'stuData':studentData})


class AddNewStudent(View):
    def get(self,request):
        fm = AddStudentForm()
        return render(request,'manageprofile/addnewstudent.html',{'form':fm})
    
    def post(self,request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'manageprofile/addnewstudent.html',{'form':fm})


class DeleteStudent(View):
    def post(self,request):
        data=request.POST
        id=data.get('id')
        studata=StudentProfileModel.objects.get(id=id)
        studata.delete()
        return redirect('/')


class UpdateStudentInfo(View):
  def get(self,request,id):
      stu = StudentProfileModel.objects.get(id=id)
      fm=AddStudentForm(instance=stu)
      return render(request,'manageprofile/updatestudent.html',{'form':fm})

  def post(self,request,id):
       stu=StudentProfileModel.objects.get(id=id)
       fm=AddStudentForm(request.POST,instance=stu)
       if fm.is_valid():
            fm.save()
            return redirect('/')
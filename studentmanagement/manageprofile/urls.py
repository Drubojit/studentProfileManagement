from django.urls import path
from .views import Home,AddNewStudent,DeleteStudent,UpdateStudentInfo
urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('add-new-student/', AddNewStudent.as_view(),name='add-new-student'),
    path('delete-student/', DeleteStudent.as_view(),name='delete-student'),
    path('update-student/<int:id>/', UpdateStudentInfo.as_view(),name='update-student')
]

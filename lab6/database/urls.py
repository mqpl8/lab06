from django.urls import path 
from .  import views 
app_name ='database'

urlpatterns = [
    path('students',views.students,name='students'),
    path("<int:student_id>",views.details,name='details'),
    path("courses",views.courses,name="courses"),
]
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Student,Course
from django import forms

# Create your views here.

class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['Fname','Lname','id_number','age']


class CourseModelForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=["course_name","course_num"]


def students(request):
     # For a post request, add a new student
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if (form.is_valid):
            form.save()

            return HttpResponseRedirect(reverse("database:students"))

        else:
            return render(request,"database/students.html",{
                "message": "invalid data entered for student"
    })

    return render(request,"database/students.html",{
        "students":Student.objects.all(),
        "form":StudentModelForm()
    })



def courses(request):

    if request.method == "POST":
        form =  CourseModelForm(request.POST)
        if (form.is_valid):

            form.save()

            return HttpResponseRedirect(reverse("database:courses"))

        else:
            return render(request,"database/courses.html",{
        "message":"invalid data entered for course"
    })

    return render(request,"database/courses.html",{
        "courses":Course.objects.all(),
        "form":CourseModelForm()
    })






def details(request,student_id):
    student = Student.objects.get(id=student_id)

    not_registered_courses = Course.objects.exclude(id__in=student.courses.all())


    student_courses = student.courses.all()

    if request.method == 'POST':
        selected_course_id = request.POST.get('course')
        selected_course = Course.objects.get(id=selected_course_id)
        
        student.courses.add(selected_course)
        
        return redirect('database:details', student_id=student_id)
    else:

        return render(request, 'database/details.html', {
            'student': student,
            'courses': not_registered_courses,
            'student_courses': student_courses
        })

    



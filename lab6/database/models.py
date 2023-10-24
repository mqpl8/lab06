from django.db import models

# Create your models here.\



class Course(models.Model):
    course_name=models.CharField(max_length=64)
    course_num=models.CharField(max_length=64)


    def __str__(self):
      return f"{self.course_name} , ({self.course_num})"


class Student(models.Model):
    Fname=models.CharField(max_length=64)
    Lname=models.CharField(max_length=64)
    id_number=models.CharField(max_length=64)
    age=models.IntegerField()
    courses=models.ManyToManyField(Course, blank=True, related_name="students")

    def __str__(self):
         return f"{self.Fname} , ({self.Lname})  {self.id_number} , {self.age}"






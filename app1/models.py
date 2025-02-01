from django.db import models

# Create your models here.

class Uesrmaster(models.Model):

    email = models.EmailField( max_length=254)
    password = models.CharField(max_length=50)
    role  = models.CharField(max_length=50)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)



def __str__(self):
        return str(self.id)

class  Student (models.Model):
    s_id = models.ForeignKey(Uesrmaster,on_delete=models.CASCADE,default=1)
    Name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, default="none")
    S_class = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to="app1/templates/img/student", default="none")
    user_id = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)

class Teacher(models.Model):
    t_id = models.ForeignKey(Uesrmaster,on_delete=models.CASCADE,default=1)
    Name = models.CharField(max_length=50)
    age = models.IntegerField()
    educetion = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    T_class = models.CharField(max_length=10)
    Teacher_pic = models.ImageField(upload_to="app1/templates/img/teacher")
    user_id = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)



class subject(models.Model):
    sub_code = models.CharField(max_length=50)
    sub_name = models.CharField(max_length=50)


class result(models.Model):
    pnr = models.ForeignKey(Student, on_delete=models.CASCADE)
    scode = models.ForeignKey(subject, on_delete=models.CASCADE)
    
    obtained_marks = models.IntegerField()





    class Meta:
        # Ensure a student can't have multiple results for the same subject
        unique_together = ['pnr', 'scode']
    

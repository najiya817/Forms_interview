from django.db import models

# Create your models here.
class Register(models.Model):
    reg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    def get_courses(self):
        return ', '.join(self.courses.all().values_list('name', flat=True))
    class Meta:
        unique_together = ('name', 'email')

class Courses(models.Model):
    course_id=models.ForeignKey(Register,related_name='courses',on_delete=models.CASCADE,null=True)
    degree=models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    def __str__(self):
        return self.degree

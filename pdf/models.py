from django.db import models

# Create your models here.
class Profile(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    c_o = models.TextField(max_length=2000)
    degree = models.CharField(max_length=200)
    grade = models.CharField(max_length=10)
    university = models.CharField(max_length=200)
    work_experience = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)

    def __str__(self):
        return '{}'.format(self.name)

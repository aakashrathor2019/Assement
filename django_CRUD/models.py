from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    emp_name = models.CharField(max_length=255)
    emp_img=models.ImageField(upload_to='images/')
    emp_email = models.EmailField(max_length=50,unique=True)
    emp_add = models.CharField(max_length=255)
    emp_dept = models.CharField(max_length=10)

    def __str__(self):
        return self.emp_name


from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=20,null=False)
    last_name=models.CharField(max_length=20)
    dept=models.ForeignKey("Department",on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey("Role",on_delete=models.CASCADE)
    phone_number=models.IntegerField()
    hire_date=models.DateField()

    def __str__(self):
        return self.first_name

class Role(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Department(models.Model):
    name=models.CharField(max_length=40,null=False)
    location=models.CharField(max_length=20)

    def __str__(self):
        return self.name

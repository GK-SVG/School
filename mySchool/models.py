from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    rollNo=models.CharField(max_length=10)
    Class=models.CharField(max_length=2, default='')
    father=models.CharField(max_length=120)
    mobileNo=models.CharField(max_length=10)
    fees=models.IntegerField(default=0)
    traFees=models.IntegerField(default=0)

    @property
    def totalFee(self):
        total=sum(self.fees,self.traFees)
        return total

    def __str__(self):
        return self.name
class StudentFees(models.Model):
    name=models.CharField(max_length=100,default='')
    roll=models.CharField(max_length=10,default='')
    payment=models.IntegerField(default=0)
    transaction_id=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.roll
    
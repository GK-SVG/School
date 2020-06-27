from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    rollNo=models.CharField(max_length=10)
    Class=models.CharField(default='')
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
    
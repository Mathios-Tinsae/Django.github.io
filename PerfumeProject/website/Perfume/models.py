from django.db import models

# Create your models here.

class CompanyInformation(models.Model):
  name=models.CharField(max_length=100)
  Description=models.TextField()
  def __str__(self)-> str:
    return self.Perfume_name


class catagory(models.Model):
  name=models.CharField(max_length=100)
  def __str__(self)-> str:
    return self.name
  
class Perfume(models.Model):
  Pname=models.CharField(max_length=100)
  PDescription=models.TextField()
  catagory=models.ForeignKey(catagory,on_delete=models.CASCADE)
  image=models.ImageField(null=True)
  price=models.FloatField(null=True)
  def __str__(self)-> str:
    return self.Perfume_name


   
  
    
from django.db import models
# Create your models here.
class signupfeilds(models.Model):
    First_name = models.CharField(max_length=50,blank=False, null=False)
    Last_name= models.CharField(max_length=50,blank=False, null=False)
    Email_address=models.EmailField(max_length=50,unique=True,blank=False, null=False) 
    Password=models.CharField(max_length=128,blank=False, null=False)
    



  
      
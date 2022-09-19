from django.db import models
class Newuser(models.Model):
    Name=models.TextField()
    Email=models.EmailField()
    Password=models.TextField()
    Confirm_Password = models.TextField()
    Select_Member = models.TextField()
    Mobile=models.TextField()
class Adds(models.Model):
    Stater=models.TextField()
class Adds_property(models.Model):
    Stater=models.TextField()
    District= models.TextField()
    Local_Address = models.TextField()
    Description= models.TextField()
    Rent= models.TextField()
    Mobile = models.TextField()


class Python(models.Model):
    Name=models.TextField()
    Class= models.TextField()
    Course = models.TextField()
    Punjabi= models.TextField()
    Hindi= models.TextField()
    English = models.TextField()
    Math = models.TextField()
class Adds_property1(models.Model):
    Uid=models.TextField()
    Stater=models.TextField()
    District= models.TextField()
    Local_Address = models.TextField()
    Description= models.TextField()
    Rent= models.TextField()
    Mobile = models.TextField()

class Api(models.Model):
    uname  =models.TextField()
    Email = models.TextField()
    Password = models.TextField()
    Fname= models.TextField()
    Mobile = models.TextField()

class Contact(models.Model):
    Uid=models.TextField()
    Name  = models.TextField()
    Mobile = models.TextField()
    Message = models.TextField()

class Contact1(models.Model):
    Uid=models.TextField()
    Name  = models.TextField()
    Mobile = models.TextField()
    Message = models.TextField()

from django.db import models

# Create your models here.
class donation(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    orderid=models.IntegerField(default=1)
    Contact=models.IntegerField()
    address=models.CharField(max_length=200)
    amount=models.IntegerField()
    Pan_no=models.CharField(max_length=20,default="PAN")
    who=models.CharField(max_length=50)
    massage=models.CharField(max_length=200)

    def __str__(self):
        return self.Name
class volunteer(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Contact=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    def __str__(self):
        return self.Name
class donationMade(models.Model):
    orderid=models.IntegerField(default=0)
    Pan_no=models.CharField(max_length=20)
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Contact=models.CharField(max_length=10)
    amount=models.CharField(max_length=200)
    t_id=models.CharField(max_length=100)
    date=models.CharField(max_length=30,default="00/00/0000")
    def __str__(self):
        return self.Name
class massage(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    subject=models.CharField(max_length=10)
    messages=models.CharField(max_length=200)
    def __str__(self):
        return self.Name
class recipt(models.Model):
    r_no=models.IntegerField()
    name=models.CharField(max_length=30)
    amount=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    def __str__(self):
        return self.name

from django.db import models

class mstuser(models.Model):
    sno=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=40)
    gender=models.CharField(max_length=10)
    mobile=models.BigIntegerField()
    address=models.CharField(max_length=60)
    emailid=models.CharField(max_length=45, unique=True)
    pwd=models.CharField(max_length=13)
    role=models.CharField(max_length=15)

class course(models.Model):
    courseid=models.AutoField(primary_key=True)
    coursename=models.CharField(max_length=20)
    fees=models.CharField(max_length=20)
    courseduration=models.CharField(max_length=20)
    coursedetail=models.CharField(max_length=100)
    courseicon=models.FileField()

class batch(models.Model):
    batchno=models.AutoField(primary_key=True)
    batchtitle=models.CharField(max_length=20)
    startdate=models.DateField()
    facultyname=models.CharField(max_length=40)
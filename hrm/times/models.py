from django.db import models

class Adata(models.Model):
    emp_id = models.CharField(max_length=10)
    cardno = models.CharField(max_length=10)

class EmpMst(models.Model):
    empid = models.IntegerField()
    ename = models.CharField(max_length=100)
    orgid = models.IntegerField(null=True,blank=True)
    jdate = models.DateField()
    bdate = models.DateField()
    tdate = models.DateField()
    edept = models.IntegerField(null=True,)

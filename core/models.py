from django.db import models
from django.conf import settings

# Create your models here.
class React(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=500)

class helplines(models.Model):
    orgname = models.CharField(max_length=400)
    number = models.TextField()
    address = models.TextField()
    description = models.TextField()
    state = models.CharField(max_length=80)
    city =  models.CharField(max_length=80)
    date = models.DateField()
    orgtype = models.CharField(max_length=80)
    ophrs = models.CharField(max_length=80)
    email = models.EmailField()
    cost = models.CharField(max_length=100)
    url =  models.URLField()
    

class feedback(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    frel = models.ForeignKey(helplines, on_delete = models.CASCADE)

class issues(models.Model):
    issue = models.CharField(max_length=80, primary_key=True)

class avail(models.Model):
    helpline = models.ForeignKey(helplines, on_delete = models.CASCADE)
    iss = models.ForeignKey(issues, on_delete = models.CASCADE)


#interndata
class verify(models.Model):
    isvalid = models.BooleanField(default=True)
    OrganizationName = models.CharField(max_length=100,default='TBD')
    OrganizationAddress = models.TextField(blank=False, null=True,default='TBD')
    PhoneNumber = models.TextField(blank=False,default='TBD')
    City = models.CharField(max_length=100,default='TBD')
    State = models.CharField(max_length=100,default='TBD')
    Issues = models.CharField(max_length=500,default='TBD')
    OrganizationDescription = models.TextField(null=True,default='TBD')
    OrganizationType = models.CharField(max_length=30,default='TBD')
    Charges = models.CharField(max_length=200,default='TBD')
    Email = models.EmailField(max_length=254,default='TBD')
    Website = models.URLField(max_length=200,default='TBD')
    OperationalHours = models.CharField(max_length=200,default='TBD')
    VerificationStatus = models.BooleanField(default=False)

class comment(models.Model):
    intern = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comments = models.TextField(blank = False,null = False, default='')
    time = models.DateTimeField(default='')

class assignhelpline(models.Model):
    intern = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    helpline = models.ForeignKey(verify, on_delete = models.CASCADE)
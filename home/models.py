from django.db import models

# Create your models here.
class Contact(models.Model):
    First_name=models.CharField(blank=True,null=True, max_length=122)
    Last_name=models.CharField(blank=False, null=True, max_length=122)
    phone_no=models.CharField(blank=False, null=True, max_length=12)
    City=models.CharField(blank=False, null=True, max_length=50)
    state=models.CharField(blank=False, null=True, max_length=50)
    Zip=models.CharField(blank=False, null=True ,max_length=50)
    
from django.db import models

class Quiz(models.Model):
    test= models.CharField(max_length=255,name='test')
    a= models.CharField(max_length=255,name='A',null=False)
    b= models.CharField(max_length=255,name='B',null=False)
    c= models.CharField(max_length=255,name='C')
    d= models.CharField(max_length=255,name='D')











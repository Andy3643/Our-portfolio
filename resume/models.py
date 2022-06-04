from distutils.command.upload import upload
from email.mime import image
from turtle import title
from django.db import models
import datetime as dt

# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=50)
    project_image =models.ImageField(upload_to='project/')
    description =models.TextField()
    date_created =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

from django.db import models
from django.contrib.auth.models import User
# from django.core.validators import MaxValueValidator, MinValueValidator
import numpy as np

class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    link=models.URLField(max_length=100)
    project_image=models.ImageField(upload_to='projects/')
    owner=models.ForeignKey(User,on_delete=models.CASCADE)


    @classmethod
    def search_by_title(cls,search_term):
        projects=cls.objects.filter(title__icontains=search_term)
        return projects

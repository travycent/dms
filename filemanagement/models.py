from django.db import models
from django.db.models.deletion import CASCADE
from autoslug import AutoSlugField

from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
#FileCategory Model
class FileCategory(models.Model):
    cat_id=models.AutoField(primary_key=True)
    cat_name=models.CharField(max_length=100)
    created_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cat_name
    class Meta:
        verbose_name_plural = 'File Categories'
#FileCategory Model
class DepartmentModel(models.Model):
    dept_id=models.AutoField(primary_key=True)
    dept_name=models.CharField(max_length=100)
    created_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.dept_name
    class Meta:
        verbose_name_plural = 'Departments'

#Files Model
class FilesModel(models.Model):
    file_id=models.AutoField(primary_key=True)
    cat_id=models.ForeignKey(FileCategory,on_delete=models.CASCADE)
    dept_id=models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)
    file_name=models.CharField(unique=True,max_length=200)
    file_media_link=models.FileField(upload_to='files',blank=True)
    slug = AutoSlugField(populate_from='file_name',unique=True, max_length=255)
    created_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.file_name
    class Meta:
        ordering = ['created_on']
        verbose_name_plural = 'Files'

        def __unicode__(self):
            return self.file_name



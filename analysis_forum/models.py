from django.db import models

# Create your models here.
class File_Forms(models.Model):
    file_name = models.FileField(upload_to="datasets")
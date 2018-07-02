from django.db import models


class File(models.Model):
  file_url = models.CharField (max_length=200 )
  name = models.CharField(max_length=20)


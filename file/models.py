from django.db import models


class File(models.Model):
  file_url = models.CharField (max_length=200 )
  name = models.CharField(max_length=20)

# Create your models here.
# username= admin1
#password = pass1234
#aditi_
#aditi1234
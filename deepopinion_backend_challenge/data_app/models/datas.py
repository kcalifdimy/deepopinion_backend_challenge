import uuid
from django.db import models



# Create your models here.
class Data(models.Model):
    text = models.TextField(blank=True)


    def __str__(self):
        return f'{self.text}'





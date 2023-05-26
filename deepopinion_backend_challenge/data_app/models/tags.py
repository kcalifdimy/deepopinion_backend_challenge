import uuid
from django.db import models
from deepopinion_backend_challenge.data_app.models import Tag



# Create your models here.
class Tag(models.Model):
    aspect = models.CharField(max_length=100)
    senttiments = models.CharField(max_length=100)
    text = models.ForeignKey(Tag, related_name="tags")




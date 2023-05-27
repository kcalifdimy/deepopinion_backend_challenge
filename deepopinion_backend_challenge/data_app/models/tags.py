from django.db import models
from deepopinion_backend_challenge.data_app.models import Data



# Create your models here.
class Tag(models.Model):
    aspect = models.CharField(max_length=100, blank=True, null=True)
    senttiments = models.CharField(max_length=100, blank=True, null=True)
    text = models.ForeignKey(Data, on_delete=models.CASCADE, related_name="tags")






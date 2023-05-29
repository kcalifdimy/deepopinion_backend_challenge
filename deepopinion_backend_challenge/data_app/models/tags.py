from django.db import models
from deepopinion_backend_challenge.data_app.models import Text



# Create your models here.
class Tag(models.Model):
    aspect = models.CharField(max_length=100, blank=True, null=True)
    sentiment = models.CharField(max_length=100, blank=True, null=True)
    text = models.ForeignKey(Text, on_delete=models.CASCADE, related_name="tags")






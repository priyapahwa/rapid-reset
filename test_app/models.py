from django.db import models

# Create your models here.

class testmodelmy(models.Model):
    text = models.TextField(null=True, blank=True)

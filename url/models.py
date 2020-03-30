from django.db import models

# Create your models here.
class Url(models.Model):
    """Model definition for Url."""
    actual_url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length = 15,null=True, blank = True)
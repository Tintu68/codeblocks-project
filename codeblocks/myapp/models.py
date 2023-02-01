from django.db import models

# Create your models here.

class Domain(models.Model):
    d_name = models.CharField(max_length=100)
    d_desc = models.TextField()
    
    def __str__(self):
        return self.d_name
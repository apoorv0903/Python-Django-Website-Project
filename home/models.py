from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=100)
    date = models.DateField(null=True)

    def __str__(self):
        return self.email
    

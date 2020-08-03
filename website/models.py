from django.db import models

# Create your models here.
class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=122)
    # date = models.DateField() 

    def __str__(self):
        return self.name
    
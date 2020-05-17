from django.db import models

# Create your models here.
class Human(models.Model):
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    
    def __str__(self):
        return "{} {}".format(self.fname,self.lname)

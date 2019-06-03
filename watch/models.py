from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class neighbourhood(models.Model):
    name= models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    occupant_count= models.CharField(max_length=100)
    user= models.ForeignKey(User, max_length=100)



    def __str__(self):
        return self.neighbourhood

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(neighbourhood=neighbourhood).delete()

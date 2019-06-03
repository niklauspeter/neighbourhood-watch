from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Neighbourhood(models.Model):
    name= models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    occupant_count= models.CharField(max_length=100)
    user= models.ForeignKey(User, max_length=100)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(neighbourhood=name).delete()

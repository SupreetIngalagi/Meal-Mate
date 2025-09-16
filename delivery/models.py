from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    mobile = models.CharField(max_length = 10)
    address = models.CharField(max_length = 50)

class Restaurant(models.Model):
    name = models.CharField(max_length = 20)
    picture = models.URLField(max_length=200, default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.vecteezy.com%2Ffree-vector%2Featery-logo&psig=AOvVaw1c5Sd6ltPFc9L0uhY2gaj6&ust=1758085101490000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCNDGgMG_3I8DFQAAAAAdAAAAABAE")
    cuisine = models.CharField(max_length = 20)
    rating = models.FloatField()
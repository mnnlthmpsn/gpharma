from django.db import models
from accounts.models import MyUser as User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    is_pharmacist = models.BooleanField(default=False)
    firstname = models.CharField(max_length=100, default='firstname', null=False)
    lastname = models.CharField(max_length=100, default='lastname', null=False)
    contact = models.CharField(max_length=20, default='contact')
    city = models.CharField(max_length=100, default='city')
    region = models.CharField(max_length=100, default='region')
    country = models.CharField(max_length=100, default='country')
    
    def __str__(self):
        return self.user.email


class Pharmacy(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin')
    name = models.CharField(max_length=100)
    loc_lat = models.FloatField(verbose_name='Latitude')
    loc_long = models.FloatField(verbose_name='Longitude')
    contact = models.CharField(max_length=20)
    website = models.URLField(default='www.google.com')

    def __str__(self):
        return self.name

class Drug(models.Model):
    pharmacy = models.ManyToManyField(Pharmacy)
    name = models.CharField(max_length=100, null=False)
    quantity = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.name
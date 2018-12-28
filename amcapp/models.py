from django.db import models
from PIL import Image
from django.contrib.auth.models import User

# CITY_CHOICES = (
# 	('Pune', 'Pune'),
#     ('Mumbai', 'Mumbai'),
#     ('Vadodara', 'Vadodara'),
#     ('Jabalpur', 'Jabalpur'),
#     ('Bhopal', 'Bhopal'),
#     ('Trivandrum', 'Trivandrum'),
#     ('Chennai', 'Chennai'),
#     ('Kochi', 'Kochi'),
#     ('Kolkata', 'Kolkata'),
    
#     ('Indore', 'Indore'),

# 	)

# Create your models here.
class Customer(models.Model):
	first_name = models.CharField(max_length=800, blank=False)
	last_name = models.CharField(max_length=500, blank=False)
	phone_number = models.CharField(max_length=10, blank=True)
	city = models.CharField(
            max_length = 255,
            null = True,
            blank = True )



# class Booking(models.Model):
#     user = models.ForeignKey(User, related_name='teacher',default='teacher')
#     name = models.CharField(max_length=250)


class Cleaner(models.Model):
    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    date = models.DateField(unique=True)  # Unique booking per day
    address = models.TextField()
    program = models.CharField(max_length=200)

    def __str__(self):
        return f"Booking on {self.date} by {self.name} for {self.program}"

class homepagedesign (models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='media')
from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"{self.user.username} - {self.service.name}"


class Venue(models.Model):   # 👈 MUST BE OUTSIDE other classes
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField(default=4)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.name



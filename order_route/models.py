from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class TouristGroup(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField(validators=[MaxValueValidator(30)])
    description = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.size}"


class Route(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="routes", null=True)
    price = models.IntegerField(validators=[MinValueValidator(0)], null=True)
    description = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    tourist_group = models.ForeignKey(TouristGroup, on_delete=models.SET_NULL, null=True, related_name="routes")

    def __str__(self):
        return f"{self.name}, {self.rating}"


class Tourist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(1)])
    address = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=80)
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, related_name="tourists")

    def __str__(self):
        return f"{self.last_name}, {self.age}"









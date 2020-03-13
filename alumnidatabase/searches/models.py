from django.db import models

# Create your models here.


class College(models.Model):
    """Model representing a College within university."""
    name = models.CharField(max_length=100)


class Major(models.Model):
    """Model representing a Major."""
    name = models.CharField(max_length=100)


class Industry(models.Model):
    """Model representing a Industry."""
    name = models.CharField(max_length=100)


class Employer(models.Model):
    """Model representing a Employer."""
    name = models.CharField(max_length=100)


class Location(models.Model):
    """Model representing a Location."""
    name = models.CharField(max_length=100)


class Alumni(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    graduation_date = models.IntegerField()

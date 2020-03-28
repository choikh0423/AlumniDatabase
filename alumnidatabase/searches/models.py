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
    photo = models.ImageField(null=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True)
    graduation_date = models.IntegerField()
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, null=True)
    current_employer = models.ForeignKey(
        Employer, related_name='current_employer', on_delete=models.CASCADE, null=True)
    past_employer = models.ManyToManyField(Employer)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name

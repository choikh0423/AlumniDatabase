from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joined_year = models.IntegerField(default=2018, null=False)

    def __str__(self):
        return self.user.first_name

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()


class College(models.Model):
    """Model representing a College within university."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Major(models.Model):
    """Model representing a Major."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Industry(models.Model):
    """Model representing a Industry."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employer(models.Model):
    """Model representing a Employer."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(models.Model):
    """Model representing a Location."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Alumni(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(default='null', max_length=100)
    photo = models.ImageField(upload_to='uploads/', null=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True)
    graduation_date = models.IntegerField()
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, null=True)
    current_employer = models.ForeignKey(
        Employer, related_name='current_employer', on_delete=models.CASCADE, null=True)
    past_employer = models.ManyToManyField(Employer)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.first_name

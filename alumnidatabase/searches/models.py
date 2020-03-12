from django.db import models

# Create your models here.


class Alumni(models.Model):
    COLLEGE_CHOICES = [('CALS', 'Collge of Agriculture and Life Sciences'),
                       ('COE', 'College of Engineering')]
    name = models.CharField(max_length=100)
    college = models.CharField(choices=COLLEGE_CHOICES, max_length=4)
    graduation_date = models.IntegerField()

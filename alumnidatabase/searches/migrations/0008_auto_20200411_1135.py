# Generated by Django 3.0.3 on 2020-04-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searches', '0007_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='joined_year',
            field=models.IntegerField(null=True),
        ),
    ]
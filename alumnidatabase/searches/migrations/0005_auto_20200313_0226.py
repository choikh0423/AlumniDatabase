# Generated by Django 3.0.3 on 2020-03-13 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searches', '0004_auto_20200313_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='name',
            field=models.CharField(choices=[('COE', 'College of Engineering'), ('CALS', 'College of Agriculture and Life Sciences')], max_length=100),
        ),
    ]
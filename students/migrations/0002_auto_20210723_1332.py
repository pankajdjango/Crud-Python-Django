# Generated by Django 3.2.5 on 2021-07-23 08:02

from django.db import migrations, models
import students.models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_opted',
            field=models.CharField(choices=[('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10)], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(validators=[students.models.MinAgeValidator(10)]),
        ),
    ]
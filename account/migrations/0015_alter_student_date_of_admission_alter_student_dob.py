# Generated by Django 4.0 on 2021-12-14 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_student_date_of_admission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_admission',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(),
        ),
    ]
# Generated by Django 4.0 on 2021-12-14 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_student_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_admission',
            field=models.DateField(),
        ),
    ]

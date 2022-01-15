# Generated by Django 4.0 on 2021-12-14 08:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_student_date_of_admission_alter_student_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonteaching_staff',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(default=datetime.datetime(2021, 12, 14, 8, 38, 42, 934805, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0 on 2021-12-13 07:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_remove_semester_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=datetime.datetime(2021, 12, 13, 7, 41, 30, 292317, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
    ]

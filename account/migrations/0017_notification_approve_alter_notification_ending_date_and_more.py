# Generated by Django 4.0 on 2021-12-14 10:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_nonteaching_staff_email_teacher_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='ending_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='notification',
            name='starting_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

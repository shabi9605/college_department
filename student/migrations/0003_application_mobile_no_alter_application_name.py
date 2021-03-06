# Generated by Django 4.0 on 2021-12-12 14:40

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_basic_details_remove_application_adhar_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='mobile_no',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.basic_details'),
        ),
    ]

# Generated by Django 4.0 on 2021-12-11 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_addhar_no_student_adhar_no_student_semster_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.semester'),
        ),
    ]

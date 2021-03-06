# Generated by Django 4.0 on 2021-12-12 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0008_alter_student_pincode'),
        ('payment', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.application'),
        ),
        migrations.AddField(
            model_name='coursefee',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.course'),
        ),
    ]

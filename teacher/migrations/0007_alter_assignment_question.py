# Generated by Django 4.0 on 2021-12-14 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_remove_assignment_answer_remove_assignment_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='question',
            field=models.FileField(blank=True, null=True, upload_to='assignment_question'),
        ),
    ]

# Generated by Django 4.0 on 2021-12-14 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('teacher', '0002_alter_audio_video_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_video',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]

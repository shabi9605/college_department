# Generated by Django 4.0 on 2021-12-13 06:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0010_remove_semester_course'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('book_file', models.FileField(upload_to='book_file')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_admission', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(3000)])),
                ('book_name', models.CharField(max_length=50)),
                ('edition', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(max_length=100)),
                ('issue_date', models.DateField()),
                ('due_date', models.DateField()),
                ('return_date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.student')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]

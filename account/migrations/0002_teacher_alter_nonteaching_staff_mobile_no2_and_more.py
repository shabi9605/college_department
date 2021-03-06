# Generated by Django 4.0 on 2021-12-10 10:05

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('mobile_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('mobile_no2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('house_name', models.CharField(blank=True, max_length=50, null=True)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.PositiveIntegerField(blank=True, null=True)),
                ('district', models.CharField(choices=[('Thiruvananthapuram', 'Thiruvananthapuram'), ('Kollam', 'Kollam'), ('Alappuzha', 'Alappuzha'), ('Pathanamthitta', 'Pathanamthitta'), ('Kottayam', 'Kottayam'), ('Idukki', 'Idukki'), (' Ernakulam', ' Ernakulam'), ('Thrissur', 'Thrissur'), ('Palakkad', 'Palakkad'), ('Malappuram', 'Malappuram'), (' Kozhikode', ' Kozhikode'), ('Wayanadu', 'Wayanadu'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod')], default='Thrissur', max_length=40)),
                ('designation', models.CharField(max_length=60)),
                ('job_type', models.CharField(choices=[('teacher', 'teacher'), ('HOD', 'HOD')], default='teacher', max_length=50)),
                ('department_post', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=40)),
                ('other_qualifications', models.CharField(blank=True, max_length=100, null=True)),
                ('certificate_proof', models.FileField(upload_to='certificate_teacher')),
                ('mphill', models.BooleanField(default=False)),
                ('phd', models.BooleanField(default=False)),
                ('net', models.BooleanField(default=False)),
                ('year_of_experience', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='teacher_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.AlterField(
            model_name='nonteaching_staff',
            name='mobile_no2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='parent',
            name='mothers_mobile_no',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile_no2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
    ]

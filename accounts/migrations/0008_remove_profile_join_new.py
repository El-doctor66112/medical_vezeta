# Generated by Django 4.1.7 on 2023-03-27 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_specialist_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='join_new',
        ),
    ]

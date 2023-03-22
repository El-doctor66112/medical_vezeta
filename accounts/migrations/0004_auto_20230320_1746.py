# Generated by Django 2.2.7 on 2023-03-20 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_type_of_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='google',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='twitter',
        ),
        migrations.AddField(
            model_name='profile',
            name='join_new',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='وقت الانضمام :'),
        ),
    ]

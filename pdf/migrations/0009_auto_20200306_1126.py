# Generated by Django 2.2.5 on 2020-03-06 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0008_auto_20200214_2244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='summary',
            new_name='c_o',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='previous_work',
            new_name='work_experience',
        ),
    ]

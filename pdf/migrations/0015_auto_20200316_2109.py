# Generated by Django 2.2.5 on 2020-03-16 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0014_auto_20200316_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='p_d',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='p_t',
        ),
    ]

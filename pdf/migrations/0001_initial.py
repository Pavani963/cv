# Generated by Django 2.2.5 on 2020-01-12 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('summary', models.TextField(max_length=2000)),
                ('degree', models.CharField(max_length=200)),
                ('grade', models.CharField(max_length=200)),
                ('university', models.CharField(max_length=200)),
                ('previous_work', models.TextField(max_length=1000)),
                ('skills', models.TextField(max_length=1000)),
            ],
        ),
    ]

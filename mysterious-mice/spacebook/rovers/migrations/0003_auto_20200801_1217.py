# Generated by Django 3.0.8 on 2020-08-01 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rovers", "0002_rover_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rover",
            name="username",
            field=models.SlugField(default=models.CharField(max_length=50)),
        ),
    ]

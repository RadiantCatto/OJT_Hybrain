# Generated by Django 3.2.13 on 2023-04-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='passphrase',
            field=models.TextField(max_length=255),
        ),
    ]

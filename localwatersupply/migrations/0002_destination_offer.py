# Generated by Django 2.2.3 on 2019-07-17 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localwatersupply', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='offer',
            field=models.BooleanField(default=False),
        ),
    ]
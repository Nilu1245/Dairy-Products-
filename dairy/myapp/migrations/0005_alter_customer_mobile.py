# Generated by Django 5.0.3 on 2024-05-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(default=0),
        ),
    ]

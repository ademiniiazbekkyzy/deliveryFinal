# Generated by Django 4.2 on 2023-05-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_ordermodel_city_ordermodel_email_ordermodel_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

# Generated by Django 3.1.13 on 2021-08-31 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dates_and_telephones', '0003_auto_20210831_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneanddate',
            name='phone_number',
            field=models.CharField(blank=True, max_length=18, null=True, unique=True, verbose_name='Номер телефона'),
        ),
    ]
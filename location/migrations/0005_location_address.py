# Generated by Django 2.0.3 on 2018-03-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_auto_20180326_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.CharField(default='Add an address', help_text='Enter an address', max_length=300),
        ),
    ]

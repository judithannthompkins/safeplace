# Generated by Django 2.0.3 on 2018-03-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0007_auto_20180327_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime',
            name='block_street_number_begin',
            field=models.CharField(default='000', help_text='Enter a street number begin', max_length=20),
        ),
        migrations.AlterField(
            model_name='crime',
            name='block_street_number_end',
            field=models.CharField(default='000', help_text='Enter a street number end', max_length=20),
        ),
    ]

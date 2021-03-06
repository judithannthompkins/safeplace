# Generated by Django 2.0.3 on 2018-03-26 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_auto_20180326_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crime',
            old_name='street_name',
            new_name='block_street_name',
        ),
        migrations.RenameField(
            model_name='crime',
            old_name='location_id',
            new_name='block_street_number_begin',
        ),
        migrations.RenameField(
            model_name='crime',
            old_name='street_number',
            new_name='block_street_number_end',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='block_street_name',
            new_name='street_name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='block_street_number_begin',
            new_name='street_number',
        ),
        migrations.RemoveField(
            model_name='location',
            name='block_street_number_end',
        ),
        migrations.RemoveField(
            model_name='location',
            name='crime',
        ),
    ]

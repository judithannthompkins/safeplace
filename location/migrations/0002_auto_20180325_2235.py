# Generated by Django 2.0.3 on 2018-03-26 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locationinstance',
            old_name='Location',
            new_name='location',
        ),
    ]
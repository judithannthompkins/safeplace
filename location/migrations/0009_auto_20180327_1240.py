# Generated by Django 2.0.3 on 2018-03-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0008_auto_20180327_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime',
            name='id',
            field=models.CharField(default='000', help_text='Enter a number', max_length=10, primary_key=True, serialize=False),
        ),
    ]
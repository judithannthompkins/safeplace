# Generated by Django 2.0.3 on 2018-03-26 02:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('category_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offense', models.CharField(help_text='Enter a crime', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=200)),
                ('rating', models.FloatField()),
                ('crime', models.ManyToManyField(help_text='Enter a crime', to='location.Crime')),
            ],
        ),
        migrations.CreateModel(
            name='LocationInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('Location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='location.Location')),
            ],
        ),
    ]

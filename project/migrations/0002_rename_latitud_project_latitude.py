# Generated by Django 4.1.1 on 2022-11-10 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='latitud',
            new_name='latitude',
        ),
    ]
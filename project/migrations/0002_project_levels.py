# Generated by Django 4.1.1 on 2022-10-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='levels',
            field=models.SmallIntegerField(default=1, verbose_name='Niveles'),
        ),
    ]
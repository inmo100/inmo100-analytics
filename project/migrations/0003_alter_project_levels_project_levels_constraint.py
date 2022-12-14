# Generated by Django 4.1.1 on 2022-11-29 06:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_rename_latitud_project_latitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='levels',
            field=models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Niveles'),
        ),
        migrations.AddConstraint(
            model_name='project',
            constraint=models.CheckConstraint(check=models.Q(('levels__gte', 0)), name='Levels_constraint'),
        ),
    ]

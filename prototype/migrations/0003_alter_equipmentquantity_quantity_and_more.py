# Generated by Django 4.1.1 on 2022-11-29 06:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0002_alter_prototype_equipments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentquantity',
            name='quantity',
            field=models.PositiveIntegerField(null=True, verbose_name='Equipment quantity per prototype'),
        ),
        migrations.AlterField(
            model_name='historical',
            name='available_units',
            field=models.PositiveIntegerField(null=True, verbose_name='Available Units'),
        ),
        migrations.AlterField(
            model_name='historical',
            name='price',
            field=models.PositiveIntegerField(null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='prototype',
            name='floors',
            field=models.SmallIntegerField(default=1, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Pisos'),
        ),
        migrations.AlterField(
            model_name='prototype',
            name='m2_constructed',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Constructed area in square meters'),
        ),
        migrations.AlterField(
            model_name='prototype',
            name='m2_habitable',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Habiable area in square meters'),
        ),
        migrations.AlterField(
            model_name='prototype',
            name='m2_terrain',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Terrain in square meters'),
        ),
        migrations.AlterField(
            model_name='prototype',
            name='total_units',
            field=models.PositiveIntegerField(null=True, verbose_name='Total units'),
        ),
        migrations.AddConstraint(
            model_name='prototype',
            constraint=models.CheckConstraint(check=models.Q(('m2_terrain__gte', 0.0)), name='Terrain_constraint'),
        ),
        migrations.AddConstraint(
            model_name='prototype',
            constraint=models.CheckConstraint(check=models.Q(('m2_constructed__gte', 0.0)), name='Constraint_constraint'),
        ),
        migrations.AddConstraint(
            model_name='prototype',
            constraint=models.CheckConstraint(check=models.Q(('m2_habitable__gte', 0.0)), name='Habitable_constraint'),
        ),
        migrations.AddConstraint(
            model_name='prototype',
            constraint=models.CheckConstraint(check=models.Q(('floors__gte', 0)), name='Floors_constraint'),
        ),
    ]
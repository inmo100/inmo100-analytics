# Generated by Django 4.1.1 on 2022-11-10 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prototype',
            name='equipments',
            field=models.ManyToManyField(through='prototype.EquipmentQuantity', to='prototype.equipment'),
        ),
    ]

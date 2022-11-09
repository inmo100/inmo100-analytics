<<<<<<< HEAD
# Generated by Django 4.1.1 on 2022-10-21 22:20
=======
# Generated by Django 4.1.1 on 2022-10-25 19:56
>>>>>>> 947d701e193ff13c6bbcd66fa3a4b437a408b02f

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Equipment",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.basemodel",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("INT", "Interior"), ("EXT", "Exterior")],
                        default="INT",
                        max_length=100,
                        verbose_name="Type",
                    ),
                ),
            ],
            bases=("core.basemodel",),
        ),
        migrations.CreateModel(
            name="EquipmentQuantity",
            fields=[
                (
                    "abstractmodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.abstractmodel",
                    ),
                ),
                (
                    "quantity",
                    models.IntegerField(
                        null=True, verbose_name="Equipment quantity per prototype"
                    ),
                ),
                (
                    "equipment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="prototype.equipment",
                    ),
                ),
            ],
            bases=("core.abstractmodel",),
        ),
        migrations.CreateModel(
            name="Finishing",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.basemodel",
                    ),
                ),
                ("description", models.TextField(verbose_name="Description")),
            ],
            bases=("core.basemodel",),
        ),
        migrations.CreateModel(
            name="FinishingType",
            fields=[
<<<<<<< HEAD
                ('abstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.abstractmodel')),
                ('type', models.CharField(choices=[('SC', 'Sistema Constructivo'), ('P', 'Pisos'), ('M', 'Muros'), ('CV', 'Cancelería Ventanas'), ('CC', 'Cubierta Cocina'), ('C', 'Carpintería')], default='P', max_length=100, verbose_name='Types')),
                ('finishing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prototype.finishing')),
            ],
            bases=('core.abstractmodel',),
=======
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.basemodel",
                    ),
                ),
            ],
            bases=("core.basemodel",),
>>>>>>> 947d701e193ff13c6bbcd66fa3a4b437a408b02f
        ),
        migrations.CreateModel(
            name="PropertyType",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.basemodel",
                    ),
                ),
                ("description", models.TextField(verbose_name="Description")),
            ],
            bases=("core.basemodel",),
        ),
        migrations.CreateModel(
            name="Prototype",
            fields=[
<<<<<<< HEAD
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('price', models.IntegerField(null=True, verbose_name='Price')),
                ('total_units', models.IntegerField(null=True, verbose_name='Total units')),
                ('sold_units', models.IntegerField(null=True, verbose_name='Sold units')),
                ('m2_terrain', models.FloatField(null=True, verbose_name='Terrain in square meters')),
                ('m2_constructed', models.FloatField(null=True, verbose_name='Constructed area in square meters')),
                ('m2_habitable', models.FloatField(null=True, verbose_name='Habiable area in square meters')),
                ('floors', models.SmallIntegerField(default=1, null=True, verbose_name='Pisos')),
                ('equipments', models.ManyToManyField(null=True, through='prototype.EquipmentQuantity', to='prototype.equipment')),
                ('finishings', models.ManyToManyField(null=True, through='prototype.FinishingType', to='prototype.finishing')),
                ('project_field', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.project')),
                ('propertyType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='prototype.propertytype')),
=======
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.basemodel",
                    ),
                ),
                ("price", models.IntegerField(null=True, verbose_name="Price")),
                (
                    "total_units",
                    models.IntegerField(null=True, verbose_name="Total units"),
                ),
                (
                    "sold_units",
                    models.IntegerField(null=True, verbose_name="Sold units"),
                ),
                (
                    "m2_terrain",
                    models.FloatField(
                        null=True, verbose_name="Terrain in square meters"
                    ),
                ),
                (
                    "m2_constructed",
                    models.FloatField(
                        null=True, verbose_name="Constructed area in square meters"
                    ),
                ),
                (
                    "m2_habitable",
                    models.FloatField(
                        null=True, verbose_name="Habiable area in square meters"
                    ),
                ),
                (
                    "floors",
                    models.SmallIntegerField(
                        default=1, null=True, verbose_name="Pisos"
                    ),
                ),
                (
                    "equipments",
                    models.ManyToManyField(
                        null=True,
                        through="prototype.EquipmentQuantity",
                        to="prototype.equipment",
                    ),
                ),
                (
                    "finishings",
                    models.ManyToManyField(null=True, to="prototype.finishing"),
                ),
                (
                    "project_field",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="project.project",
                    ),
                ),
                (
                    "propertyType",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="prototype.propertytype",
                    ),
                ),
>>>>>>> 947d701e193ff13c6bbcd66fa3a4b437a408b02f
            ],
            bases=("core.basemodel",),
        ),
        migrations.CreateModel(
            name="Segment",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.basemodel",
                    ),
                ),
                ("description", models.TextField(verbose_name="Description")),
            ],
            bases=("core.basemodel",),
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "abstractmodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.abstractmodel",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("S", "Sell"), ("D", "Refund")],
                        default="S",
                        max_length=100,
                        verbose_name="Type",
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        default=datetime.datetime.now, verbose_name="Date"
                    ),
                ),
                ("quantity", models.IntegerField(verbose_name="Quantity")),
                (
                    "prototype",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="prototype.prototype",
                    ),
                ),
            ],
            bases=("core.abstractmodel",),
        ),
        migrations.AddField(
            model_name="prototype",
            name="segment_field",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="prototype.segment"
            ),
        ),
        migrations.AddField(
<<<<<<< HEAD
            model_name='finishingtype',
            name='prototype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prototype.prototype'),
        ),
        migrations.AddField(
            model_name='equipmentquantity',
            name='prototype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='prototype.prototype'),
=======
            model_name="finishing",
            name="finishing_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="prototype.finishingtype",
            ),
        ),
        migrations.AddField(
            model_name="equipmentquantity",
            name="prototype",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="prototype.prototype"
            ),
>>>>>>> 947d701e193ff13c6bbcd66fa3a4b437a408b02f
        ),
    ]

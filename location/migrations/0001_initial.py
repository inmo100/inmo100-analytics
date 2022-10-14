# Generated by Django 4.1.1 on 2022-10-13 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('state_field', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='location.state')),
                ('zones', models.ManyToManyField(to='location.zone')),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Colony',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('municipality_field', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='location.municipality')),
            ],
            bases=('core.basemodel',),
        ),
    ]

from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from core.models import BaseModel, AbstractModel
from project.models import Project
from .managers import PrototypesManager,EquipmentQuantityManager,TrianguloManager,HistoricalManager
from django.db.models import CheckConstraint, Q
from django.core.validators import MinValueValidator
# arreglar el MER y MR


class Material(BaseModel):
    pass


class Finishing(BaseModel):  # Acabados en el MER
    pass


class PropertyType(BaseModel):
    '''
    Refers to:
    Loft
    Casa
    Duplex
    Departamento
    Etc.
    '''
    description = models.TextField(verbose_name=_("Description"))


class Segment(BaseModel):
    description = models.TextField(verbose_name=_("Description"))


class Equipment(BaseModel):
    '''
    Refers to:
    Baño
    Habitación
    Cochera

    '''
    class EquipmentType(models.TextChoices):
        # Choice menu
        interior = "INT", _("Interior")  # enum for interior equipment
        exterior = "EXT", _("Exterior")  # enum for exterior equipment

    type = models.CharField(verbose_name=_(
        "Type"), choices=EquipmentType.choices, default=EquipmentType.interior, max_length=100)


class Prototype(BaseModel):
    project_field = models.ForeignKey(Project, on_delete=models.PROTECT)
    segment_field = models.ForeignKey(Segment, on_delete=models.PROTECT)
    propertyType = models.ForeignKey(
        PropertyType, on_delete=models.PROTECT, null=True)
    equipments = models.ManyToManyField(Equipment, through='EquipmentQuantity')

    total_units = models.PositiveIntegerField (verbose_name=_("Total units"), null=True)
    m2_terrain = models.FloatField(validators=[MinValueValidator(0.0)],verbose_name=(
        "Terrain in square meters"), null=True)
    m2_constructed = models.FloatField(validators=[MinValueValidator(0.0)],verbose_name=(
        "Constructed area in square meters"), null=True)
    m2_habitable = models.FloatField(validators=[MinValueValidator(0.0)],verbose_name=(
        "Habiable area in square meters"), null=True)
    floors = models.SmallIntegerField(validators=[MinValueValidator(0)],
        verbose_name=("Pisos"), default=1, null=True)
    objects = PrototypesManager()

    class Meta:
        constraints = (
            CheckConstraint(
                check=Q(m2_terrain__gte=0.0),
                name='Terrain_constraint'),
            CheckConstraint(
                check=Q(m2_constructed__gte=0.0),
                name='Constraint_constraint'),
            CheckConstraint(
                check=Q(m2_habitable__gte=0.0),
                name='Habitable_constraint'),
            CheckConstraint(
                check=Q(floors__gte=0),
                name='Floors_constraint'),
            )


class EquipmentQuantity(AbstractModel):
    equipment = models.ForeignKey(Equipment, on_delete=models.PROTECT)
    prototype = models.ForeignKey(Prototype, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(verbose_name=(
        "Equipment quantity per prototype"), null=True)
    objects = EquipmentQuantityManager()


class Triangulo(AbstractModel):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['finishings', 'material', 'prototype'], name='Unique triangles')
        ]

    finishings = models.ForeignKey(Finishing, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    prototype = models.ForeignKey(Prototype, on_delete=models.PROTECT)
    objects = TrianguloManager()

# Handles prototype historical data


class Historical(models.Model):  # Historical only needs abstract model
    prototype = models.ForeignKey(Prototype, on_delete=models.PROTECT)

    date = models.DateTimeField(verbose_name=_("Date"), default=datetime.now)
    price = models.PositiveIntegerField(verbose_name=_("Price"), null=True)
    available_units = models.PositiveIntegerField(
        verbose_name=_("Available Units"), null=True)
    objects = HistoricalManager()

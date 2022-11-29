from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel
from location.models import Colony
from django.db.models import CheckConstraint, Q
from django.core.validators import MinValueValidator

class Amenity(BaseModel):
    description = models.TextField(verbose_name=_("Description"))

# Use Case: 16, 17, 18, 19
class Developer(BaseModel):
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(verbose_name=_("Image"), null=True, blank=True)
    social_networks = models.JSONField(verbose_name=_("Social networks"))

# Use Case: 8, 9, 10, 11
class Project(BaseModel):
    colony_field = models.ForeignKey(Colony, on_delete=models.PROTECT)
    developer_field = models.ForeignKey(Developer, on_delete=models.PROTECT)

    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(verbose_name=_("Image"))
    logo = models.ImageField(verbose_name=_("Logo"))
    initial_date = models.DateField(verbose_name=_("Initial date"))
    latitude = models.FloatField(verbose_name=_("Latitud"))
    longitude = models.FloatField(verbose_name=_("Longitude"))
    address = models.CharField(verbose_name=_("Address"), max_length=100)
    phone = models.CharField(verbose_name=_("Phone"), max_length=100)
    brochure = models.FileField(verbose_name=_("Brochure"))
    social_networks = models.JSONField(verbose_name=_("Social networks"))
    levels = models.SmallIntegerField(validators=[MinValueValidator(0)],verbose_name=("Niveles"), default=1)

    class Meta:
        constraints = (
            CheckConstraint(
                check=Q(levels__gte=0),
                name='Levels_constraint'),
            )
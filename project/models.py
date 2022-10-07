from msvcrt import open_osfhandle
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel
from location.models import Colony

class Amenity(BaseModel):
  description = models.TextField(verbose_name=_("Description"))

class Developer(BaseModel):
  description = models.TextField(verbose_name=_("Description"))
  image = models.ImageField(verbose_name=_("Image"))
  social_networks = models.JSONField(verbose_name=_("Social networks"))

class Project(BaseModel):
  colony = models.ForeignKey(Colony, on_delete=models.PROTECT)
  developer = models.ForeignKey(Developer, on_delete=models.PROTECT)

  description = models.TextField(verbose_name=_("Description"))
  image = models.ImageField(verbose_name=_("Image"))
  logo = models.ImageField(verbose_name=_("Logo"))
  initial_date = models.DateField(verbose_name=_("Initial date"))
  latitud = models.FloatField(verbose_name=_("Latitud"))
  longitude = models.FloatField(verbose_name=_("Longitude"))
  address = models.CharField(verbose_name=_("Address"))
  phone = models.CharField(verbose_name=_("Phone"))
  brochure = models.FileField(verbose_name=_("Brochure"))
  social_networks = models.JSONField(verbose_name=_("Social networks"))

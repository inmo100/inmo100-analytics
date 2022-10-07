from django.db import models
from core.models import BaseModel

class State(BaseModel):
  pass

class Zone(BaseModel):
  pass

class Municipality(BaseModel):
  state = models.ForeignKey(State, on_delete = models.PROTECT)
  zones = models.ManyToManyField(Zone)

class Colony(BaseModel):
  municipality = models.ForeignKey(Municipality, on_delete = models.PROTECT)

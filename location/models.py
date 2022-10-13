from django.db import models
from core.models import BaseModel

class State(BaseModel):
  # nothing here because base model already has name
  pass

class Zone(BaseModel):
  # nothing here because base model already has name
  pass

class Municipality(BaseModel):
  state_field = models.ForeignKey(State, on_delete = models.PROTECT)
  zones = models.ManyToManyField(Zone)

class Colony(BaseModel):
  municipality_field = models.ForeignKey(Municipality, on_delete = models.PROTECT)

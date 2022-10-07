from django.db import models
from django.utils.translation import gettext_lazy as _

class AbstractModel(models.Model):
  created_at = models.DateTimeField(verbose_name=_("Creation date"), auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name=_("Last update date"), auto_now=True)
  hidden = models.BooleanField(default=False)

  class Meta:
    ordering = ["-created_at"]

class BaseModel(AbstractModel):
  name = models.TextField(verbose_name=_("Name"))
  
  def __str__(self):
      return self.name
  
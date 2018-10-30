from django.db import models

# Create your models here.
class Chisme (models.Model):
  title = models.CharField(_("Titulo"), max_length=50)
  body = models.CharField(_("Contenido"), max_length=50)
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Decedent(models.Model):
    first_name = models.CharField(_('first name'), max_length=255)
    middle_name = models.CharField(_('middle name'), max_length=255, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=255)
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
    date_of_death = models.DateField(_('date of death'))

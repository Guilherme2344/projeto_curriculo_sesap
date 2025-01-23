from django.core.validators import FileExtensionValidator
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .Candidato import Candidato
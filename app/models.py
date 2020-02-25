from django.db import models
from django.contrib.postgres.fields import JSONField


class MyModel(models.Model):
    files = JSONField(default=list)
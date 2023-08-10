from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True, auto_now_add=False)
    deleted = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Base model'
        verbose_name_plural = 'Base models'
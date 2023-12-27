from django.db import models


class Dogs(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Dogs"


from django.db import models

# Create your models here.

class Branch(models.Model):
    nameB = models.CharField(max_length=100, verbose_name="branch name")
    location = models.CharField(max_length=255, verbose_name="branch location")

    def __str__(self):
        return self.nameB

    class Meta:
        verbose_name = "branch"
        verbose_name_plural = "branches"

from django.db import models


class PageHit(models.Model):
    url = models.CharField(unique=True, max_length=2000)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'счётчик'
        verbose_name_plural = 'счётчики'

    def __str__(self):
        return self.url

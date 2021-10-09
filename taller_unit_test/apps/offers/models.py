from django.db import models

class Offer(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description", blank=True)
    price = models.FloatField("Price", default=0.0)


    class Meta:
        ordering = ['-price']
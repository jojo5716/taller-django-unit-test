from django.db import models

class Offer(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description", blank=True)
    price = models.FloatField("Price", default=0.0)  # To be calculed using an external api
    is_expired = models.BooleanField("Is expired offer", default=False)
    is_active = models.BooleanField("Is active", default=True)

    class Meta:
        ordering = ['-id']
    
    def __str__(self) -> str:
        return self.name

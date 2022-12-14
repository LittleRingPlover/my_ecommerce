from datetime import datetime
from django.db import models


class Product(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


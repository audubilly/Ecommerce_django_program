from django.db import models

from merchant.models import Merchant


class Product(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='product_images/')
    description = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='merchant')
    category = models.CharField(max_length=20)
    rating = models.IntegerField(default=0)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

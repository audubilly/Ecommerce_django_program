from django.db import models


class Merchant(models.Model):
    name = models.CharField(max_length=20)
    profile_picture = models.ImageField(default='', upload_to='merchant_images/')
    description = models.TextField()
    store_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name



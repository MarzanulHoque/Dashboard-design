from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.name

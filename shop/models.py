from distutils.command.upload import upload
from traceback import print_exception
from django.db import models




# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to = 'images/', default='', null = True, blank = True)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
from django.db import models


class Category(models.Model):
    """
    Creates a category model containing the names of the
    product categories
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    product_code = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    scent = models.ForeignKey('Scent', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Scent(models.Model):
    name = models.CharField(max_length=50)

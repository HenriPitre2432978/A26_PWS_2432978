from django.db import models


class Category(models.Model):
  name = models.CharField(max_length=50, verbose_name="Nom")

  def __str__(self):
    return self.name

  class Meta:
    ordering = ('name', )
    verbose_name = "catégorie"
    verbose_name_plural = "catégories"


class Product(models.Model):
  code = models.CharField(max_length=15)
  name = models.CharField(max_length=50, verbose_name="Nom")
  category = models.ForeignKey(Category, verbose_name="Catégorie", related_name='products', on_delete=models.CASCADE)

  def __str__(self):
    return '{} - {}'.format(self.code, self.name)

  class Meta:
    ordering = ('code', 'name', )
    verbose_name = "produit"
    verbose_name_plural = "produits"

from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductCategory(models.Model):
    name = models.CharField(_('Name'), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')


class Product(models.Model):
    categories = models.ManyToManyField(
        ProductCategory,
        related_name='products',
        verbose_name=_('Category'),
        blank=True
    )
    name = models.CharField(_('Name'), max_length=100)
    price = models.DecimalField(_('Price'), max_digits=7, decimal_places=2)
    stock = models.PositiveIntegerField(_('Stock'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

from django.db import models
from store.choices import Category
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    price = models.DecimalField(_('Price'), max_digits=7, decimal_places=2)
    stock = models.PositiveIntegerField(_('Stock'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductCategory(models.Model):
    product = models.ManyToManyField(
        Product,
        related_name='categories',
        verbose_name=_('Product'),
        blank=True
    )
    category = models.PositiveSmallIntegerField(_('Category'), choices=Category.choices, default=Category.OTHER)

    def __str__(self):
        return self.get_category_display()

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')

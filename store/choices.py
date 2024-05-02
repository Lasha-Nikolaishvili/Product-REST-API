from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class Category(IntegerChoices):
    ELECTRONICS = 1, _('Electronics')
    BOOKS = 2, _('Books')
    CLOTHING = 3, _('Clothing')
    SPORTS = 4, _('Sports')
    OTHER = 5, _('Other')

from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel



class MeasureUnit(BaseModel):
    description = models.CharField(max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Measure Unit'
        verbose_name_plural = 'Measure Units'


class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50, null=True, blank=True, unique=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='measure unit')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Discount(BaseModel):
    discount_value = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return f'Oferta en {self.category.name} de {self.discount_value}%'

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'


class Product(BaseModel):
    name = models.CharField('Product name', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Product description', blank=True, null=True)
    image = models.ImageField('Product image', upload_to='products/', blank=True, null=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return f'{self.name} | {self.price}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    
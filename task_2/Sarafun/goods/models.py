from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.CharField(max_length=200, unique=True, null=True, blank=True, verbose_name='URL')
    image = models.ImageField(upload_to='images/categories/', verbose_name='Изображение')

    class Meta:
        db_table = 'category'
        verbose_name='категорию'
        verbose_name_plural='категории'

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.CharField(max_length=200, unique=True, null=True, blank=True, verbose_name='URL')
    image = models.ImageField(upload_to='images/subcategories/', verbose_name='Изображение')
    category = models.ForeignKey(
        to=Category, related_name='subcategories', on_delete=models.CASCADE, verbose_name='Категория'
        )
    
    class Meta:
        db_table = 'sub_category'
        verbose_name='подкатегория'
        verbose_name_plural='подкатегории'

    def __str__(self):
        return f"{self.category.name}: {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.CharField(max_length=200, unique=True, null=True, blank=True, verbose_name='URL')
    # Уточнить как загружается изображение
    small_img = models.ImageField(upload_to='images/goods/small/', blank=True, null=True)
    medium_img = models.ImageField(upload_to='images/goods/medium/', blank=True, null=True)
    large_img = models.ImageField(upload_to='images/goods/large/', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Цена')
    sub_category = models.ForeignKey(to=SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')

    class Meta:
        db_table = 'product'
        verbose_name='продукт'
        verbose_name_plural='продукты'
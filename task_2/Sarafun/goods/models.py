from django.db import models


class Categories(models.Model):
    name = models.CharField('Название', max_length=150, unique=True)
    slug = models.CharField('URL', max_length=200, unique=True, null=True, blank=True)
    image = models.ImageField('Изображение', upload_to=None, height_field=None, width_field=None)

    class Meta:
        db_table = 'category'
        verbose_name='категорию'
        verbose_name_plural='категории'


class SubCategories(models.Model):
    name = models.CharField('Название', max_length=150, unique=True)
    slug = models.CharField('URL', max_length=200, unique=True, null=True, blank=True) #################
    image = models.ImageField('Изображение', upload_to=None, height_field=None, width_field=None)
    category = models.ForeignKey('Категория', to=Categories, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'sub_category'
        verbose_name='подкатегория'
        verbose_name_plural='подкатегорию'


class Products(models.Model):
    name = models.CharField('Название', max_length=150, unique=True)
    slug = models.CharField('URL', max_length=200, unique=True, null=True, blank=True) #################
    description = models.TextField('Описание', blank=True, null=True)
    # Уточнить как загружается изображение
    small_img = models.ImageField(upload_to='goods_images/small/', blank=True, null=True)
    medium_img = models.ImageField(upload_to='goods_images/medium/', blank=True, null=True)
    large_img = models.ImageField(upload_to='goods_images/large/', blank=True, null=True)
    price = models.DecimalField('Цена', default=0.00, max_digits=10, decimal_places=2)
    sub_category = models.ForeignKey('Категория', to=SubCategories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'
        verbose_name='продукт'
        verbose_name_plural='продукты'

    def __str__(self):
        return f'{self.name} Количесво: {self.amount}'
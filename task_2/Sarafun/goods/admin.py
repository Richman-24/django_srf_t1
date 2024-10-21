from django.contrib import admin

from goods.models import Category, SubCategory, Product

@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name',]


@admin.register(SubCategory)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name',]
    fields = [
        'category',
        'name',
        'slug',
        'image',
    ]


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'price',]
    list_editable = ['price',]
    search_fields = ['name']
    fields = [
        'sub_category',
        'name',
        'slug',
        ('small_img', 'medium_img', 'large_img'),
        'price',
    ]
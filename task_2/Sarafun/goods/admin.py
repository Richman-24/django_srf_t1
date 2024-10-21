from django.contrib import admin

from .models import Categories, Products, SubCategories


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name',]


@admin.register(SubCategories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name',]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'price',]
    list_editable = ['price',]
    search_fields = ['name']
    fields = [
        'name',
        'category',
        'slug',
        ('small_img', 'medium_img', 'large_img')
        ('price', 'discount'),
        'amount',
    ]
from django.contrib import admin
from .models import Product, Category, Review, Mood


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'product_code',
        'name',
        'description',
        'price',
        'image',
    )

    ordering = ('product_code',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'subject',
        'review',
        'user',
        'status',
        'updated_at',
        'created_at',
    )


class MoodAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'mood',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Mood, MoodAdmin)

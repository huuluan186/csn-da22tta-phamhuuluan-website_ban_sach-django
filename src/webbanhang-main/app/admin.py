from django import forms
from django.contrib import admin
from .models import *
from django.db import transaction
# Register your models here.

class OrderItemAdmin(admin.ModelAdmin):
    list_display=('id','product','order','quantity','date_added')

class OrderAdmin(admin.ModelAdmin):
    list_display=('id','customer')

class ProductInline(admin.TabularInline):
    model = Product.category.through  # Mối quan hệ nhiều-nhiều giữa Product và Category
    extra = 0  # Không thêm dòng trống
  

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'get_categories')
    search_fields = ('name', 'categories__name')  # Tìm kiếm theo danh mục
    filter_horizontal = ('category',)  # Cung cấp giao diện chọn nhiều danh mục cho sản phẩm
    
    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.category.all()])
    get_categories.short_description = 'Categories'

    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'slug', 'is_sub')  # Các cột hiển thị
    search_fields = ('name',)
    list_filter = ('is_sub',)  # Bộ lọc
    inlines = [ProductInline]  # Hiển thị sản phẩm trong trang chỉnh sửa danh mục

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
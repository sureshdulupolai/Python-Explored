from django.contrib import admin
from .models  import Product,Category

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','description','price')

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','name','slug')


admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)



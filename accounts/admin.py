from django.contrib import admin

# Register your models here.
from accounts.models import MenuItem, Category, OrderModel

admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderModel)
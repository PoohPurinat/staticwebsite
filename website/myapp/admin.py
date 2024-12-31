from django.contrib import admin
from .models import Product ,Staff,ContactUs,ProductStock

admin.site.register(Product) # เอา database ไปอยู่ backend
admin.site.register(Staff)
admin.site.register(ContactUs)
admin.site.register(ProductStock)
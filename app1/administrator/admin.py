from django.contrib import admin

# Register your models here.
from administrator.models import Applications, Income

admin.site.register(Applications)
admin.site.register(Income)
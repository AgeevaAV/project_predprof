from django.contrib import admin

# Register your models here.
from catalog.models import Catalog,Box,BuyBox, Rating

admin.site.register(Catalog)
admin.site.register(Box)
admin.site.register(BuyBox)
admin.site.register(Rating)


from django.contrib import admin
from listings.models import Ref

class RefAdmin(admin.ModelAdmin):
	list_display = ('gtin', 'expiration_date')

admin.site.register(Ref, RefAdmin)

# Register your models here.

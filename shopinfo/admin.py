from django.contrib import admin
from shopinfo.models import Shopinformation

# Register your models here.

class Shopinfo(admin.ModelAdmin):
  search_fields = ('name', 'addr')
  list_display = ('id', 'name', 'tel', 'addr')
  list_filter = ('name',)
#  date_hierachy = ''
  ordering = ('id',)
  

admin.site.register(Shopinformation, Shopinfo)


from django.contrib import admin
from .models import Income

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('tanggal', 'jumlah', 'sumber', 'deskripsi')
    
admin.site.register(Income, IncomeAdmin)

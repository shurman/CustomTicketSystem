from django.contrib import admin
from .models import *

class A_Ticket(admin.ModelAdmin):
    list_display = ('id', 't_type', 'title', 'status', 'creator', 'create_date')

    fieldsets = (
        ('1', {'fields':('title', 'description', 'status')}),
        ('2', {'fields':('t_type', 'severity')}),
        ('3', {'fields':('creator', 'create_date', 'last_date')}),
    )
    readonly_fields = ('create_date', 'last_date')
    search_fields = ('id',)


admin.site.register(Ticket, A_Ticket)

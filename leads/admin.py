from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'estado', 'fecha_creacion', 'fecha_asignacion')
    list_filter = ('estado', 'fecha_creacion', 'fecha_asignacion')
    search_fields = ('nombre', 'telefono', 'email')
    readonly_fields = ('fecha_creacion', 'fecha_asignacion')

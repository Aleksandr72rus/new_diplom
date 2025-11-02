from django.contrib import admin
from .models import Order, StatusCrm


class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_theme', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('id', 'order_name', 'order_theme')
    list_editable = ('order_status', 'order_phone')
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt', 'order_theme')
    list_filter = ('order_status', 'order_theme')
    fields = ('id', 'order_theme', 'order_status', 'order_dt', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_dt')
    # inlines = [Comment]
    # list_per_page = 10


admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)

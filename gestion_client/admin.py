from django.contrib import admin

from .models import *

# Register your models here.
class AdminCustomer(admin.ModelAdmin):
  list_display = ('name',
                  'contact_name', 
                  'email', 
                  'phone', 
                  'address',
                  'city',
                  'zip_code',
                  'created_at',
                  )

admin.site.register(Customer, AdminCustomer)

class AdminInvoice(admin.ModelAdmin):
  list_display = ('customer', 
                  'invoice_date', 
                  'total',
                  'last_update',
                  'paid',
                  'invoice_type',
                  'comment'
                  )

admin.site.register(Invoice, AdminInvoice)
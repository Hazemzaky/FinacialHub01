from django.contrib import admin
from .models import Account, JournalEntry, Transaction

# This new class tells Django how to safely handle the Account model
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'name', 'account_type', 'parent')
    list_filter = ('account_type',)
    search_fields = ('name', 'account_number')
    # This is the line that prevents the infinite loop recursion
    raw_id_fields = ('parent',)

# We register the Account model using our new custom class
admin.site.register(Account, AccountAdmin)

# The other models are still registered simply
admin.site.register(JournalEntry)
admin.site.register(Transaction)

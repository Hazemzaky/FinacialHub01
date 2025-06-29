from django.contrib import admin
from .models import Account, JournalEntry, Transaction

# This line tells Django to show the Account model in the admin site
# We can add some customizations later if we want.
admin.site.register(Account)

# We can also register the other models to view them later
admin.site.register(JournalEntry)
admin.site.register(Transaction)

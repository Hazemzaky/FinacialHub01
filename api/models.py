from django.db import models
from django.conf import settings
from decimal import Decimal

class Account(models.Model):
    class AccountTypes(models.TextChoices):
        ASSET = 'ASSET', 'Asset'
        LIABILITY = 'LIABILITY', 'Liability'
        EQUITY = 'EQUITY', 'Equity'
        REVENUE = 'REVENUE', 'Revenue'
        EXPENSE = 'EXPENSE', 'Expense'
    name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    account_type = models.CharField(max_length=10, choices=AccountTypes.choices)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField(blank=True)
    opening_balance = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))
    fiscal_year_of_opening_balance = models.DateField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "Chart of Accounts"
        ordering = ['account_number', 'name']
    def __str__(self):
        return f"{self.account_number} - {self.name}" if self.account_number else self.name

class JournalEntry(models.Model):
    date = models.DateField(db_index=True)
    description = models.CharField(max_length=512)
    fiscal_year = models.PositiveIntegerField(help_text="The starting year of the fiscal period, e.g., 2024 for the April 2024 - March 2025 year.")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"JE-{self.id}: {self.date} - {self.description}"

class Transaction(models.Model):
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name='transactions')
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    debit = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))
    credit = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))
    class Meta:
        ordering = ['journal_entry']
    def __str__(self):
        if self.debit > 0:
            return f"{self.account} | Debit: {self.debit}"
        return f"{self.account} | Credit: {self.credit}"

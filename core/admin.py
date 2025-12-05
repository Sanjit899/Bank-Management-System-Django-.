# core/admin.py
from django.contrib import admin
from .models import BankAccount, Transaction

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_number', 'balance', 'created_at')
    search_fields = ('user__username', 'account_number')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'txn_type', 'amount', 'timestamp', 'counterparty')
    list_filter = ('txn_type',)
    search_fields = ('account__user__username', 'counterparty')

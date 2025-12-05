# core/models.py
from django.db import models
from django.contrib.auth.models import User
import random
from django.db.models import F

def generate_account_number():
    # 12-digit numeric account number, ensure uniqueness in save()
    return ''.join(str(random.randint(0,9)) for _ in range(12))

class BankAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bank_account')
    account_number = models.CharField(max_length=20, unique=True, blank=True)
    balance = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.account_number:
            # ensure uniqueness
            while True:
                acct = generate_account_number()
                if not BankAccount.objects.filter(account_number=acct).exists():
                    self.account_number = acct
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.account_number}"

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw'),
        ('transfer', 'Transfer'),
    )

    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="transactions")
    txn_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    counterparty = models.CharField(max_length=20, blank=True, null=True)  # optional for transfers

    def __str__(self):
        return f"{self.account.user.username} - {self.txn_type} - {self.amount}"


    def __str__(self):
        return f"{self.account.user.username} - {self.txn_type} - {self.amount}"

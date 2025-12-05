# core/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=14, decimal_places=2, min_value=0.01)

class WithdrawForm(forms.Form):
    amount = forms.DecimalField(max_digits=14, decimal_places=2, min_value=0.01)

class TransferForm(forms.Form):
    to_account_number = forms.CharField(max_length=20)
    amount = forms.DecimalField(max_digits=14, decimal_places=2, min_value=0.01)

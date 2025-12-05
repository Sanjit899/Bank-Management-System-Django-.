# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, DepositForm, WithdrawForm, TransferForm
from .models import BankAccount, Transaction
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # bank account auto-created by signal
            login(request, user)
            messages.success(request, "Account created and logged in.")
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    account = get_object_or_404(BankAccount, user=request.user)
    txns = account.transactions.order_by('-timestamp')[:20]
    return render(request, 'core/dashboard.html', {'account': account, 'transactions': txns})

@login_required
def deposit_view(request):
    account = get_object_or_404(BankAccount, user=request.user)
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            with transaction.atomic():
                account.balance = account.balance + amount
                account.save()
                Transaction.objects.create(account=account, txn_type='deposit', amount=amount)
            messages.success(request, f"Deposited {amount}.")
            return redirect('dashboard')
    else:
        form = DepositForm()
    return render(request, 'core/deposit.html', {'form': form, 'account': account})

@login_required
def withdraw_view(request):
    account = get_object_or_404(BankAccount, user=request.user)
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if account.balance < amount:
                messages.error(request, "Insufficient balance.")
            else:
                with transaction.atomic():
                    account.balance = account.balance - amount
                    account.save()
                    Transaction.objects.create(account=account, txn_type='withdraw', amount=amount)
                messages.success(request, f"Withdrew {amount}.")
                return redirect('dashboard')
    else:
        form = WithdrawForm()
    return render(request, 'core/withdraw.html', {'form': form, 'account': account})

@login_required
def transfer_view(request):
    account = get_object_or_404(BankAccount, user=request.user)
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            to_acc_no = form.cleaned_data['to_account_number']
            amount = form.cleaned_data['amount']
            try:
                target = BankAccount.objects.get(account_number=to_acc_no)
            except BankAccount.DoesNotExist:
                messages.error(request, "Target account not found.")
                return redirect('transfer')
            if account == target:
                messages.error(request, "Cannot transfer to same account.")
                return redirect('transfer')
            if account.balance < amount:
                messages.error(request, "Insufficient balance.")
                return redirect('transfer')
            # perform atomic transfer
            with transaction.atomic():
                account.balance = account.balance - amount
                account.save()
                target.balance = target.balance + amount
                target.save()
                Transaction.objects.create(account=account, txn_type='transfer', amount=amount, counterparty=target.account_number)
                Transaction.objects.create(account=target, txn_type='deposit', amount=amount, counterparty=account.account_number)
            messages.success(request, f"Transferred {amount} to {to_acc_no}.")
            return redirect('dashboard')
    else:
        form = TransferForm()
    return render(request, 'core/transfer.html', {'form': form, 'account': account})

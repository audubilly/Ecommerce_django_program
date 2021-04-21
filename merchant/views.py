from django.shortcuts import render, redirect
from django.contrib import redirects

from merchant.forms import MerchantForm


def merchant_creation(request):
    if request.method != 'POST':
        form = MerchantForm()
    else:
        form = MerchantForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'merchant/success.html')

    context = {
        "form": form
    }
    return render(request, 'merchant/merchant_creation.html', context)

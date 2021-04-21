from django import forms

from merchant.models import Merchant


class MerchantForm(forms.ModelForm):
    class Meta:
        model = Merchant
        fields = '__all__'

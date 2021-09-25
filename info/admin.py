from django.contrib import admin
from django import forms
from .models import Info, Prices, Condition, Insurance, Wallet, Transaction

class InfoAdminForm(forms.ModelForm):

    class Meta:
        model = Info
        fields = '__all__'


class InfoAdmin(admin.ModelAdmin):
    form = InfoAdminForm
    list_display = ['created', 'last_updated', 'type', 'blood', 'code', 'health', 'age', 'weight']
    readonly_fields = ['created', 'last_updated', 'type', 'blood', 'code', 'health', 'age', 'weight']

admin.site.register(Info, InfoAdmin)


class PricesAdminForm(forms.ModelForm):

    class Meta:
        model = Prices
        fields = '__all__'


class PricesAdmin(admin.ModelAdmin):
    form = PricesAdminForm
    list_display = ['created', 'last_updated', 'value', 'weight_value']
    readonly_fields = ['created', 'last_updated', 'value', 'weight_value']

admin.site.register(Prices, PricesAdmin)


class ConditionAdminForm(forms.ModelForm):

    class Meta:
        model = Condition
        fields = '__all__'


class ConditionAdmin(admin.ModelAdmin):
    form = ConditionAdminForm
    list_display = ['created', 'last_updated', 'insurance_condition', 'insurance_date']
    readonly_fields = ['created', 'last_updated', 'insurance_condition', 'insurance_date']

admin.site.register(Condition, ConditionAdmin)


class InsuranceAdminForm(forms.ModelForm):

    class Meta:
        model = Insurance
        fields = '__all__'


class InsuranceAdmin(admin.ModelAdmin):
    form = InsuranceAdminForm
    list_display = ['created', 'last_updated', 'name']
    readonly_fields = ['created', 'last_updated', 'name']

admin.site.register(Insurance, InsuranceAdmin)


class WalletAdminForm(forms.ModelForm):

    class Meta:
        model = Wallet
        fields = '__all__'


class WalletAdmin(admin.ModelAdmin):
    form = WalletAdminForm
    list_display = ['created', 'last_updated', 'value']
    readonly_fields = ['created', 'last_updated', 'value']

admin.site.register(Wallet, WalletAdmin)


class TransactionAdminForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionAdmin(admin.ModelAdmin):
    form = TransactionAdminForm
    list_display = ['created', 'last_updated', 'value']
    readonly_fields = ['created', 'last_updated', 'value']

admin.site.register(Transaction, TransactionAdmin)



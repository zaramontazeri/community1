from django.contrib import admin
from django import forms
from .models import Category, Info, Prices, Condition, Insurance, SubCategory, Wallet, Transaction

class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ['created', 'last_updated', 'name', 'type']
    readonly_fields = ['created', 'last_updated', ]

admin.site.register(Category, CategoryAdmin)

class SubCategoryAdminForm(forms.ModelForm):

    class Meta:
        model = SubCategory
        fields = '__all__'


class SubCategoryAdmin(admin.ModelAdmin):
    form = SubCategoryAdminForm
    list_display = ['created', 'last_updated', 'blood', 'category']
    readonly_fields = ['created', 'last_updated', ]

admin.site.register(SubCategory, SubCategoryAdmin)

class InfoAdminForm(forms.ModelForm):

    class Meta:
        model = Info
        fields = '__all__'


class InfoAdmin(admin.ModelAdmin):
    form = InfoAdminForm
    list_display = ['created', 'last_updated', 'subcategory', 'code', 'health', 'dateـofـbirth', 'weight']
    readonly_fields = ['created', 'last_updated', ]

admin.site.register(Info, InfoAdmin)


class PricesAdminForm(forms.ModelForm):

    class Meta:
        model = Prices
        fields = '__all__'


class PricesAdmin(admin.ModelAdmin):
    form = PricesAdminForm
    list_display = ['created', 'last_updated', 'value', 'weight_value']
    readonly_fields = ['created', 'last_updated']

admin.site.register(Prices, PricesAdmin)


class ConditionAdminForm(forms.ModelForm):

    class Meta:
        model = Condition
        fields = '__all__'


class ConditionAdmin(admin.ModelAdmin):
    form = ConditionAdminForm
    list_display = ['created', 'last_updated', 'insurance_condition','insurance_from_date', 'insurance_to_date']
    readonly_fields = ['created', 'last_updated']

admin.site.register(Condition, ConditionAdmin)


class InsuranceAdminForm(forms.ModelForm):

    class Meta:
        model = Insurance
        fields = '__all__'


class InsuranceAdmin(admin.ModelAdmin):
    form = InsuranceAdminForm
    list_display = ['created', 'last_updated', 'name']
    readonly_fields = ['created', 'last_updated']

admin.site.register(Insurance, InsuranceAdmin)


class WalletAdminForm(forms.ModelForm):

    class Meta:
        model = Wallet
        fields = '__all__'


class WalletAdmin(admin.ModelAdmin):
    form = WalletAdminForm
    list_display = ['created', 'last_updated', 'value']
    readonly_fields = ['created', 'last_updated']

admin.site.register(Wallet, WalletAdmin)


class TransactionAdminForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionAdmin(admin.ModelAdmin):
    form = TransactionAdminForm
    list_display = ['created', 'last_updated', 'value']
    readonly_fields = ['created', 'last_updated']

admin.site.register(Transaction, TransactionAdmin)



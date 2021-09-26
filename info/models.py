from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import DecimalField
from django.db.models import IntegerField
from django.db.models import TextField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields

class Category(models.Model):
    LIVESTOCK="livestock"
    POULTRY="poultry"
    AQUATIC="aquatic"
    TYPE_STATUS=((LIVESTOCK,LIVESTOCK),(POULTRY,POULTRY),(AQUATIC,AQUATIC))
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name=models.CharField(max_length=30)
    type=models.CharField(max_length=11,choices=TYPE_STATUS)
    class Meta:
        ordering = ('name',)
        verbose_name="Category"
        verbose_name_plural="Categories"
    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('Info_category_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Info_category_update', args=(self.pk,))

class SubCategory(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    blood=models.CharField(max_length=30)
    category=models.ForeignKey('info.Category',on_delete=models.CASCADE,related_name="subcategories")
    class Meta:
        ordering = ('category',)
        verbose_name="SubCategory"
        verbose_name_plural="SubCategories"
    def __str__(self):
        return f'{self.category}-{self.blood}'

    def get_absolute_url(self):
        return reverse('Info_subcategory_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Info_subcategory_update', args=(self.pk,))

class Info(models.Model):
    HEALTHY="healthy"
    PATIENT="patient"
    HEALTH_STATUS=((HEALTHY,HEALTHY),(PATIENT,PATIENT))

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    code = models.IntegerField(default=0)
    health = models.CharField(max_length=7,choices=HEALTH_STATUS)
    age = models.IntegerField(default = 0)
    weight = models.IntegerField(default=0)

    # Relationship Fields
    subcategory=models.ForeignKey('info.SubCategory',on_delete=models.CASCADE,related_name="info")

    class Meta:
        ordering = ('-created',)
        verbose_name="Info"
        verbose_name_plural="Info"

    def __str__(self):
        return f'{self.code}'

    def get_absolute_url(self):
        return reverse('Info_info_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Info_info_update', args=(self.pk,))


class Prices(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    value = models.DecimalField(max_digits=10, decimal_places=0)
    weight_value = models.DecimalField(max_digits=10, decimal_places=0)


    class Meta:
        ordering = ('-created',)
        verbose_name="Price"
        verbose_name_plural="Prices"

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('Info_prices_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Info_prices_update', args=(self.pk,))

##vazyat
class Condition(models.Model):
    STAPPED ="stapped"
    LIVE ="live"
    FINISHED = "finished"
    VALID="valid"
    STATUS = ((STAPPED,STAPPED),(LIVE,LIVE))
    INSURANCE_STATUS = ((FINISHED,FINISHED),(VALID,VALID))
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    insurance_condition = models.CharField(max_length=10,choices=INSURANCE_STATUS)   ##sharayet bime
    insurance_to_date = models.DateField() 
    insurance_from_date=models.DateField()
    status = models.CharField(max_length=8, choices=STATUS)
    # Relationship Fields
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="conditions", 
    )
    info = models.OneToOneField(
        'info.Info',
        on_delete=models.CASCADE, related_name="conditions", 
    )
    insurance = models.OneToOneField(
        'info.Insurance',
        on_delete=models.CASCADE, related_name="conditions", 
    )

    class Meta:
        ordering = ('-created',)
        verbose_name="Condition"
        verbose_name_plural="Conditions"

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('Info_condition_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Info_condition_update', args=(self.pk,))


class Insurance(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=30)


    class Meta:
        ordering = ('-created',)
        verbose_name="Insurance"
        verbose_name_plural="Insurances"

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('Info_insurance_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Info_insurance_update', args=(self.pk,))


class Wallet(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    value = models.DecimalField(max_digits=10, decimal_places=0)

    # Relationship Fields
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="wallets", 
    )

    class Meta:
        ordering = ('-created',)
        verbose_name="Wallet"
        verbose_name_plural="Wallets"

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('Info_wallet_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Info_wallet_update', args=(self.pk,))


class Transaction(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    value = models.DecimalField(max_digits=10, decimal_places=0)


    class Meta:
        ordering = ('-created',)
        verbose_name="Transaction"
        verbose_name_plural="Transactions"

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('Info_transaction_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Info_transaction_update', args=(self.pk,))



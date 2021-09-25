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


class Info(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type = models.CharField(max_length=30)
    blood = models.CharField(max_length=30)
    code = models.IntegerField(default=0)
    health = models.CharField(max_length=30)
    age = models.IntegerField(default = 0)
    weight = models.IntegerField(default=0)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

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

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('Info_prices_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Info_prices_update', args=(self.pk,))


class Condition(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    insurance_condition = models.CharField(max_length=30)
    insurance_date = models.TextField(max_length=100)

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
    name = models.TextField(max_length=100)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

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

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('Info_transaction_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Info_transaction_update', args=(self.pk,))



from datetime import timedelta, timezone, datetime
from . import models
import decimal
from django.utils.datetime_safe import date
from rest_framework import serializers

class CategorySrializer(serializers.ModelSerializer):
    class Meta:
        model=models.Category
        fields=(
            'pk',
            'created',
            'last_updated',
            'name',
            'type',
        )

class SubCategorySerializer(serializers.ModelSerializer):
    category =CategorySrializer()
    class Meta:
        model=models.SubCategory
        fields=(
            'pk',
            'created',
            'last_updated',
            'blood',
            'category',
        )

class InfoSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer()
    class Meta:
        model = models.Info
        fields =(
            'pk', 
            'created', 
            'last_updated', 
            'subcategory', 
            'code', 
            'health', 
            'age', 
            'weight', 
        )


class PricesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Prices
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'value', 
            'weight_value', 
        )


class ConditionSerializer(serializers.ModelSerializer):
    remaining_time=serializers.SerializerMethodField()
    passed_time=serializers.SerializerMethodField()
    class Meta:
        model = models.Condition
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'insurance_condition', 
            'insurance_from_date',
            'insurance_to_date', 
            'remaining_time',
            'passed_time',
        )
    def get_remaining_time(self,obj):
        # today=date.today()
        # remaining_time=obj.insurance_to_date-today
        today=date.today()
        remaining_time=obj.insurance_to_date-today
        return remaining_time.days
    def get_passed_time(self,obj):
        today=date.today()
        passed_time=today-obj.insurance_from_date
        return passed_time.days



class InsuranceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Insurance
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'name', 
        )


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Wallet
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'value', 
        )


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Transaction
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'value', 
        )



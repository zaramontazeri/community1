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
    age=serializers.SerializerMethodField()
    class Meta:
        model = models.Info
        fields =(
            'pk', 
            'created', 
            'last_updated', 
            'subcategory', 
            'code', 
            'health',  
            'weight', 
            'dateـofـbirth',
            'age',
            'image',
        )

    def get_age(self,obj):
        today=date.today()
        if(today>obj.dateـofـbirth):
            age=today-obj.dateـofـbirth
            return age.days
        else:
            return "0"


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
class InsuranceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Insurance
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'name', 
        )

class ConditionSerializer(serializers.ModelSerializer):
    remaining_time=serializers.SerializerMethodField()
    passed_time=serializers.SerializerMethodField()
    info = InfoSerializer()
    insurance = InsuranceSerializer()
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
            'info',
            'insurance',

        )
    def get_remaining_time(self,obj):
        today=date.today()
        if obj.insurance_to_date:
            remaining_time=obj.insurance_to_date-today
            return remaining_time.days
        else :
            return None
    def get_passed_time(self,obj):
        if obj.insurance_from_date:
            today=date.today()
            passed_time=today-obj.insurance_from_date
            return passed_time.days
        else :
            return None



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
            'user',
        )



from . import models

from rest_framework import serializers


class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Info
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'type', 
            'blood', 
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

    class Meta:
        model = models.Condition
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'insurance_condition', 
            'insurance_date', 
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



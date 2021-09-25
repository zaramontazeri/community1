from . import models
from . import serializers
from rest_framework import viewsets, permissions


class InfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Info class"""

    queryset = models.Info.objects.all()
    serializer_class = serializers.InfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class PricesViewSet(viewsets.ModelViewSet):
    """ViewSet for the Prices class"""

    queryset = models.Prices.objects.all()
    serializer_class = serializers.PricesSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConditionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Condition class"""

    queryset = models.Condition.objects.all()
    serializer_class = serializers.ConditionSerializer
    permission_classes = [permissions.IsAuthenticated]


class InsuranceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Insurance class"""

    queryset = models.Insurance.objects.all()
    serializer_class = serializers.InsuranceSerializer
    permission_classes = [permissions.IsAuthenticated]


class WalletViewSet(viewsets.ModelViewSet):
    """ViewSet for the Wallet class"""

    queryset = models.Wallet.objects.all()
    serializer_class = serializers.WalletSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Transaction class"""

    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]



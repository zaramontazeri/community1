from rest_framework.views import APIView
from . import models
from . import serializers
from rest_framework import viewsets, permissions,response

class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Category class"""
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySrializer
    permission_classes = [permissions.IsAuthenticated]

class SubCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the SubCategory class"""
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

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

class GetWalletBalance(APIView):
    """View  for the Wallet balance"""

    permission_classes = [permissions.IsAuthenticated]
    def get(self ,request , *args , **kwargs):
        user = request.user
        wallet,_ = models.Wallet.objects.get_or_create(user=user , defaults={"value":0})
        return response.Response({"balance":wallet.value})


class TransactionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Transaction class"""

    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]



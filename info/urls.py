from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'info', api.InfoViewSet)
router.register(r'prices', api.PricesViewSet)
router.register(r'condition', api.ConditionViewSet)
router.register(r'insurance', api.InsuranceViewSet)
router.register(r'wallet', api.WalletViewSet)
router.register(r'transaction', api.TransactionViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)

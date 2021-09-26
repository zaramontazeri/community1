import unittest
from django.urls import reverse
from django.test import Client
from .models import Category, Info, Prices, Condition, Insurance, SubCategory, Wallet, Transaction
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)

def create_category(**kwargs):
    defaults = {}
    defaults["type"] = "type"
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Category.objects.create(**defaults)

def create_subcategory(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    if "category" not in defaults:
        defaults["category"] = create_category()
    defaults.update(**kwargs)
    return SubCategory.objects.create(**defaults)

def create_info(**kwargs):
    defaults = {}
    if "subcategory" not in defaults:
        defaults["subcategory"] = create_subcategory()
    defaults["blood"] = "blood"
    defaults["code"] = "code"
    defaults["health"] = "health"
    defaults["age"] = "age"
    defaults["weight"] = "weight"
    defaults.update(**kwargs)
    return Info.objects.create(**defaults)


def create_prices(**kwargs):
    defaults = {}
    defaults["value"] = "value"
    defaults["weight_value"] = "weight_value"
    defaults.update(**kwargs)
    return Prices.objects.create(**defaults)


def create_condition(**kwargs):
    defaults = {}
    defaults["insurance_condition"] = "insurance_condition"
    defaults["insurance_date"] = "insurance_date"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    if "info" not in defaults:
        defaults["info"] = create_info()
    if "insurance" not in defaults:
        defaults["insurance"] = create_insurance()
    return Condition.objects.create(**defaults)


def create_insurance(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Insurance.objects.create(**defaults)


def create_wallet(**kwargs):
    defaults = {}
    defaults["value"] = "value"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return Wallet.objects.create(**defaults)


def create_transaction(**kwargs):
    defaults = {}
    defaults["value"] = "value"
    defaults.update(**kwargs)
    return Transaction.objects.create(**defaults)

class CategoryViewTest(unittest.TestCase):
    '''
    Tests for Category
    '''
    def setUp(self):
        self.client = Client()

    def test_list_category(self):
        url = reverse('Info_category_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_category(self):
        url = reverse('Info_category_create')
        data = {
            "name": "name",
            "type": "type",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_category(self):
        category = create_category()
        url = reverse('Info_category_detail', args=[category.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_category(self):
        category = create_category()
        data = {
            "name": "name",
            "type": "type",
        }
        url = reverse('Info_category_update', args=[category.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

class SubCategoryViewTest(unittest.TestCase):
    '''
    Tests for SubCategory
    '''
    def setUp(self):
        self.client = Client()

    def test_list_subcategory(self):
        url = reverse('Info_subcategory_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_subcategory(self):
        url = reverse('Info_subcategory_create')
        data = {
            "name": "name",
            "category": create_category().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_subcategory(self):
        subcategory = create_subcategory()
        url = reverse('Info_subcategory_detail', args=[subcategory.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_subcategory(self):
        subcategory = create_subcategory()
        data = {
            "name": "name",
            "category": create_category().pk,
        }
        url = reverse('Info_subcategory_update', args=[subcategory.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

class InfoViewTest(unittest.TestCase):
    '''
    Tests for Info
    '''
    def setUp(self):
        self.client = Client()

    def test_list_info(self):
        url = reverse('Info_info_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_info(self):
        url = reverse('Info_info_create')
        data = {
            "subcategory": "subcategory",
            "blood": "blood",
            "code": "code",
            "health": "health",
            "age": "age",
            "weight": "weight",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_info(self):
        info = create_info()
        url = reverse('Info_info_detail', args=[info.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_info(self):
        info = create_info()
        data = {
            "subcategory": create_subcategory().pk,
            "blood": "blood",
            "code": "code",
            "health": "health",
            "age": "age",
            "weight": "weight",
        }
        url = reverse('Info_info_update', args=[info.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PricesViewTest(unittest.TestCase):
    '''
    Tests for Prices
    '''
    def setUp(self):
        self.client = Client()

    def test_list_prices(self):
        url = reverse('Info_prices_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_prices(self):
        url = reverse('Info_prices_create')
        data = {
            "value": "value",
            "weight_value": "weight_value",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_prices(self):
        prices = create_prices()
        url = reverse('Info_prices_detail', args=[prices.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_prices(self):
        prices = create_prices()
        data = {
            "value": "value",
            "weight_value": "weight_value",
        }
        url = reverse('Info_prices_update', args=[prices.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ConditionViewTest(unittest.TestCase):
    '''
    Tests for Condition
    '''
    def setUp(self):
        self.client = Client()

    def test_list_condition(self):
        url = reverse('Info_condition_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_condition(self):
        url = reverse('Info_condition_create')
        data = {
            "insurance_condition": "insurance_condition",
            "insurance_date": "insurance_date",
            "user": create_django_contrib_auth_models_user().pk,
            "info": create_info().pk,
            "insurance": create_insurance().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_condition(self):
        condition = create_condition()
        url = reverse('Info_condition_detail', args=[condition.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_condition(self):
        condition = create_condition()
        data = {
            "insurance_condition": "insurance_condition",
            "insurance_date": "insurance_date",
            "user": create_django_contrib_auth_models_user().pk,
            "info": create_info().pk,
            "insurance": create_insurance().pk,
        }
        url = reverse('Info_condition_update', args=[condition.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class InsuranceViewTest(unittest.TestCase):
    '''
    Tests for Insurance
    '''
    def setUp(self):
        self.client = Client()

    def test_list_insurance(self):
        url = reverse('Info_insurance_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_insurance(self):
        url = reverse('Info_insurance_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_insurance(self):
        insurance = create_insurance()
        url = reverse('Info_insurance_detail', args=[insurance.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_insurance(self):
        insurance = create_insurance()
        data = {
            "name": "name",
        }
        url = reverse('Info_insurance_update', args=[insurance.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class WalletViewTest(unittest.TestCase):
    '''
    Tests for Wallet
    '''
    def setUp(self):
        self.client = Client()

    def test_list_wallet(self):
        url = reverse('Info_wallet_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_wallet(self):
        url = reverse('Info_wallet_create')
        data = {
            "value": "value",
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_wallet(self):
        wallet = create_wallet()
        url = reverse('Info_wallet_detail', args=[wallet.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_wallet(self):
        wallet = create_wallet()
        data = {
            "value": "value",
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('Info_wallet_update', args=[wallet.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TransactionViewTest(unittest.TestCase):
    '''
    Tests for Transaction
    '''
    def setUp(self):
        self.client = Client()

    def test_list_transaction(self):
        url = reverse('Info_transaction_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_transaction(self):
        url = reverse('Info_transaction_create')
        data = {
            "value": "value",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_transaction(self):
        transaction = create_transaction()
        url = reverse('Info_transaction_detail', args=[transaction.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_transaction(self):
        transaction = create_transaction()
        data = {
            "value": "value",
        }
        url = reverse('Info_transaction_update', args=[transaction.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)



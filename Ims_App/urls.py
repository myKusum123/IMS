from django.urls import path
from .views import *
from django.urls import path
from .views import (
    ReadCategory, UpdateCategory, CreateCategory, DeleteCategory, ReadCategoryByID,
    ReadItem, UpdateItem, CreateItem, DeleteItem, ReadItemByID,
    ReadStocks, UpdateStock, CreateStock, DeleteStock, ReadStockByID,
    ReadSuppliers, UpdateSupplier, CreateSupplier, DeleteSupplier, ReadSupplierByID,
    ReadTransactions, UpdateTransaction, CreateTransaction, DeleteTransaction, ReadTransactionByID,
)

urlpatterns = [
    # Categories
    path('categories/', ReadCategory.as_view(), name='category-list'),
    path('categories/<uuid:pk>/', ReadCategoryByID.as_view(), name='category-detail'),
    path('categories/create/', CreateCategory.as_view(), name='category-create'),
    path('categories/<uuid:pk>/update/', UpdateCategory.as_view(), name='category-update'),
    path('categories/<uuid:pk>/delete/', DeleteCategory.as_view(), name='category-delete'),

    # Items
    path('items/', ReadItem.as_view(), name='item-list'),
    path('items/<uuid:pk>/', ReadItemByID.as_view(), name='item-detail'),
    path('items/create/', CreateItem.as_view(), name='item-create'),
    path('items/<uuid:pk>/update/', UpdateItem.as_view(), name='item-update'),
    path('items/<uuid:pk>/delete/', DeleteItem.as_view(), name='item-delete'),

    # Stocks
    path('stocks/', ReadStocks.as_view(), name='stock-list'),
    path('stocks/<uuid:pk>/', ReadStockByID.as_view(), name='stock-detail'),
    path('stocks/create/', CreateStock.as_view(), name='stock-create'),
    path('stocks/<uuid:pk>/update/', UpdateStock.as_view(), name='stock-update'),
    path('stocks/<uuid:pk>/delete/', DeleteStock.as_view(), name='stock-delete'),

    # Suppliers
    path('suppliers/', ReadSuppliers.as_view(), name='supplier-list'),
    path('suppliers/<uuid:pk>/', ReadSupplierByID.as_view(), name='supplier-detail'),
    path('suppliers/create/', CreateSupplier.as_view(), name='supplier-create'),
    path('suppliers/<uuid:pk>/update/', UpdateSupplier.as_view(), name='supplier-update'),
    path('suppliers/<uuid:pk>/delete/', DeleteSupplier.as_view(), name='supplier-delete'),

    # Transactions
    path('transactions/', ReadTransactions.as_view(), name='transaction-list'),
    path('transactions/<uuid:pk>/', ReadTransactionByID.as_view(), name='transaction-detail'),
    path('transactions/create/', CreateTransaction.as_view(), name='transaction-create'),
    path('transactions/<uuid:pk>/update/', UpdateTransaction.as_view(), name='transaction-update'),
    path('transactions/<uuid:pk>/delete/', DeleteTransaction.as_view(), name='transaction-delete'),
]

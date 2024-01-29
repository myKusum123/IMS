from django.shortcuts import render
from rest_framework import generics
from .models import*
from .serializers import*
# Create your views here.

class ReadCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class UpdateCategory(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CreateCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DeleteCategory(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ReadCategoryByID(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"
    

class ReadItem(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class UpdateItem(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CreateItem(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class DeleteItem(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class ReadItemByID(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "pk"


class ReadStocks(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
class UpdateStock(generics.RetrieveUpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class CreateStock(generics.CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
class DeleteStock(generics.CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class ReadStockByID(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = "pk"
    
class ReadSuppliers(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    
class UpdateSupplier(generics.RetrieveUpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class CreateSupplier(generics.CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class DeleteSupplier(generics.DestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    
class ReadSupplierByID(generics.RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    lookup_field = "pk"


class ReadTransactions(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
class UpdateTransaction(generics.RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
class CreateTransaction(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
class DeleteTransaction(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
class ReadTransactionByID(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "pk"
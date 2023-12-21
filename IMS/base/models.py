from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CompanyInfo(models.Model):
   name=models.CharField(max_length=200)
   description=models.TextField()
   logo=models.ImageField(null=True , blank=True)#value pass nagarepni object banau na milxa hamile yo field ma chai value narakhe pni banau na milxa kina ki null ra blank rakheko xau
   address=models.TextField()
   email=models.EmailField(unique=True)
   contact_no=models.IntegerField()

   def __str__(self):
        return self.name

class UserInfo(AbstractUser):
    email=models.EmailField(unique=True ,null=True)
    password=models.CharField(max_length=50)
    username=models.CharField(unique=True, max_length=200)
    comapny_info=models.ForeignKey(CompanyInfo,on_delete=models.CASCADE, null=True) #setnull le chai null gardinxa delete vayo vani company info ko object aba  sompanyinfo ko sab object delete vaus vani chai CASAD use garni
   
    USERNAME_FIELD="email"# instead use of username we use email so we override it username field ma arko field(email) pass garera overried gareko
    REQUIRED_FIELDS=["username"]

class ProductType(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=300)
    description=models.TextField()
    quantity=models.IntegerField()
    type=models.ForeignKey(ProductType, on_delete=models.CASCADE)# foreign key ma sadhai one to many nai hunxa
    
    def __str__(self):
        return self.name
    
class BuyerInfo(models.Model):
    name:models.CharField(max_length=250)
    email=models.EmailField(unique=True)
    address=models.TextField()
    contact_no=models.IntegerField()
    company=models.ForeignKey(CompanyInfo,on_delete=models.CASCADE )
 

    def __str__(self):
        return self.name 
    
class SellInfo(models.Model):
    buyer=models.ForeignKey(BuyerInfo, on_delete=models.SET_NULL, null = True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.IntegerField()
    company=models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.buyer

class VenderInfo(models.Model):# kasle hamilai saman bechyo vanera information rakhna ko lagi
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    address=models.TextField()
    contact_no=models.IntegerField()
    company_name=models.CharField(max_length=300)
    company=models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class PurchaseInfo(models.Model):
    vender=models.ForeignKey(VenderInfo, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.IntegerField()
    company=models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.vender
from django.db import models
from django.db.models import ForeignKey


class SalesPerson(models.Model):
   Sales_Person_ID = models.AutoField(primary_key=True)
   Last_Name = models.CharField(max_length=100)
   First_Name = models.CharField(max_length=100)
class Mechanic(models.Model):
    Mechanic_ID = models.AutoField(primary_key=True)
    Last_Name = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
class Sales_Invoice(models.Model):
    Invoice_ID = models.AutoField(primary_key=True)
    Invoice_Number = models.CharField(max_length=100)
    invoice_date = models.DateField()
    Car_ID = models.IntegerField()
    Customer_ID = models.DecimalField(max_digits=10, decimal_places=2)
    Sales_Person_ID = models.DecimalField(max_digits=10, decimal_places=2)
class Car(models.Model):
    Car_ID = models.AutoField(primary_key=True)
        Serial_Number = models.CharField(max_length=100)
   Make = models.CharField(max_length=100)
   Model = models.CharField(max_length=100)
   Year = models.IntegerField()
   Color = models.CharField(max_length=100)
   Car_for_Sale = models.BooleanField()

class Customer(models.Model):
    Customer_ID = models.AutoField(primary_key=True)
    Last_Name = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State_Province = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Postal_Code = models.CharField(max_length=100)
class Service (models.Model):
    Service_ID = models.AutoField(primary_key=True)
    Service_Name = models.CharField(max_length=100)
    Hourly_Rate = models.DecimalField(max_digits=10, decimal_places=2)
class Parts (models.Model):
    Parts_ID = models.AutoField(primary_key=True)
    Part_Number = models.CharField(max_length=100)
    Part_Description = models.CharField(max_length=100)
    Purchase_Price = models.DecimalField(max_digits=10, decimal_places=2)
    Retail_Price = models.DecimalField(max_digits=10, decimal_places=2)
class Parts_Used (models.Model):
    Parts_Used_ID = models.AutoField(primary_key=True)
    Part_ID = models.IntegerField(ForeignKey(Parts))
    Number_Used = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
class Service_Mechanic(models.Model):
    Service_Mechanic_ID = models.AutoField(primary_key=True)
    Service_Ticket_ID = models.IntegerField(ForeignKey(Service))
    Service_ID = models.IntegerField(ForeignKey(Service))
    Mechanic_ID = models.IntegerField(ForeignKey(Mechanic))
    Hours = models.IntegerField()
    Comment= models.CharField(max_length=100)
    Rate= models.DecimalField(max_digits=10, decimal_places=2)
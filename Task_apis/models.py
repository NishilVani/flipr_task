from django.db import models


class Users(models.Model):
    customerId = models.AutoField(primary_key=True)                         # Customer Unique ID(primary key)
    customerName = models.CharField(max_length=100)                         # Customer Name
    mobileNumber = models.CharField(max_length=15)                          # Customer Mobile Number
    city = models.CharField(max_length=100)                                 # Customer's City
    email = models.EmailField(max_length=100, blank=False)                  # Customer's Email Address


class Orders(models.Model):
    purchaseOrderId = models.AutoField(primary_key=True)                    # Orders Unique Purchase ID(primary key)
    productName = models.CharField(max_length=100)                          # Product Name
    pricing = models.IntegerField()                                         # Product Pricing
    quantity = models.IntegerField()                                        # Product Quantity
    mrp = models.IntegerField()                                             # Product MRP
    customerId = models.ForeignKey(Users, on_delete=models.CASCADE)         # User ID (ForeignKey)


class Shipping(models.Model):
    shippingId = models.AutoField(primary_key=True)                         # Unique Shipping ID(primary key)
    address = models.CharField(max_length=500)                              # Shipping Address
    city = models.CharField(max_length=100)                                 # Shipping City
    pincode = models.IntegerField()                                         # Shipping Pin Code
    purchaseOrderId = models.ForeignKey(Orders, on_delete=models.CASCADE)   # Purchase ID (ForeignKey)
    customerId = models.ForeignKey(Users, on_delete=models.CASCADE)         # User ID (ForeignKey)


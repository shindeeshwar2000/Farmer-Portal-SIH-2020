from django.db import models

class Product_List(models.Model):
    
    Product_Name = models.CharField(max_length=50, default="")
    Farmer_Name = models.CharField(max_length=50, default="")
    Location = models.CharField(max_length=50, default="")
    Price   = models.CharField(max_length=50, default="")
    Quantity = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.Farmer_Name
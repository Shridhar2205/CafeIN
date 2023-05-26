from django.db import models


class product(models.Model):
   product_id = models.AutoField
   product_name = models.CharField(max_length=100)
   price = models.IntegerField(default=0)
   product_desc = models.CharField(max_length=200)
   image = models.ImageField(upload_to="static/img",default="")

   def __str__(self):
    return self.product_name

class credentials(models.Model):
  userID = models.AutoField(primary_key=True)
  password = models.CharField(max_length=50)
   
class Customer(models.Model):
   userID = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   phone_no = models.PositiveBigIntegerField(max_length=11)
   address = models.CharField(max_length=200)
   email = models.EmailField
   rating = models.FloatField(range(0,5))

class cart(models.Model):
   userID = models.AutoField(primary_key=True)
   total_cost = models.IntegerField

class cart_items(models.Model):
   userID = models.AutoField(primary_key=True)
   product_id = models.IntegerField
   product_name = models.CharField(max_length=100)
   quantity = models.IntegerField
   total_item_cost = models.IntegerField

class Token(models.Model):
   userID = models.AutoField(primary_key=True),
   order_no = models.IntegerField
   order_date = models.DateField
   order_status = models.CharField(max_length=50)
   total_cost = models.IntegerField

class token_items(models.Model):
  order_no = models.IntegerField
  product_id = models.IntegerField
  product_name = models.CharField(max_length=100)
  quantity = models.IntegerField

class admin(models.Model):
  employee_id = models.PositiveIntegerField
  name = models.CharField(max_length=50)
  phone_no = models.IntegerField(max_length=11)
  address = models.CharField(max_length=200)
  email = models.EmailField

class Stock(models.Model):
  product_id = models.IntegerField
  product_name = models.CharField(max_length=50)
  stock_quantity = models.IntegerField 
   
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 200)
    desc = models.CharField(max_length = 300)
    pub_date = models.DateField()
    category = models.CharField(max_length = 100,default="")
    subcategory = models.CharField(max_length = 100,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images",default="")
    def __str__(self):
        return self.product_name
class Contact(models.Model):
    msg_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 20)
    desc = models.CharField(max_length = 1000)


class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    item_json = models.CharField(max_length = 5000)
    name = models.CharField(max_length = 90)
    amount = models.IntegerField(default=0)
    email = models.CharField(max_length = 121)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 111)
    zip_code = models.CharField(max_length = 10)
    state = models.CharField(max_length = 111)
    phone = models.CharField(max_length = 111,default='')

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "...."


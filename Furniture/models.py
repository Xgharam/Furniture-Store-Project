from django.db import models

#Items
class Items(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
         return self.name
#ItemDetails  
class ItemDetails(models.Model):
    color=models.CharField(max_length=50)
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    image=models.CharField(max_length=150)
    total=models.FloatField()
    date=models.DateTimeField(auto_now_add=True)
    itemsid=models.ForeignKey(Items, on_delete=models.CASCADE)

#Cart
class Cart(models.Model):
    id_product=models.IntegerField()
    id_user=models.IntegerField()
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    total=models.FloatField()
    discount=models.FloatField()
    net=models.FloatField()
    status=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
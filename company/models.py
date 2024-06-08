from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=3,unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    cat=models.CharField(max_length=50,unique=True,primary_key=True)
    def __str__(self):
        return self.cat



class Product(models.Model):
    avail=[
        ('yes','yes'),
        ('oou-of-stock','out-of-stock')
    ]
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    productName=models.CharField(max_length=100)
    price=models.IntegerField()
    rating=models.DecimalField(decimal_places=1,max_digits=3)
    discount=models.IntegerField()
    availability=models.CharField(choices=avail,max_length=100)

    def __str__(self):
        return self.productName
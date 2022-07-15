from django.db import models
from django.contrib.auth.models import User
from datetime import  datetime
# Create your models here
class category(models.Model):
    cid=models.AutoField
    main_category=models.CharField(max_length=40)
    category=models.CharField(max_length=40)
class subcategory(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=50)
    date=models.DateField()
    def __str__(self):
        return self.name
class product(models.Model):
    id=models.AutoField
    category=models.CharField(max_length=20)
    subcategory=models.ForeignKey(subcategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=60)
    price=models.FloatField()
    disprice=models.FloatField()
    size=models.CharField(max_length=10)
    color=models.CharField(max_length=30)
    description=models.CharField(max_length=300)
    date=models.DateField()
    img=models.ImageField(upload_to='static/user/img',default='palce.jpg')
    def __str__(self):
        return self.name
class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=15)
    contact=models.CharField(max_length=15)
    msg=models.CharField(max_length=300)
class signup(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=50)
    userid=models.CharField(max_length=50)
    mob=models.CharField(max_length=20)
    email=models.CharField(max_length=40,primary_key=True)
    userpic=models.ImageField(upload_to='static/user/profile',null=True)
    address=models.TextField(max_length=200)
    password=models.CharField(max_length=40)
    def __str__(self):
        return self.userid
class Cart(models.Model):
    id=models.AutoField
    Owner=models.ForeignKey(User,on_delete=models.CASCADE)
    cartproduct=models.ForeignKey(product,on_delete=models.CASCADE)
    odered=models.BooleanField(default=False)
    status=models.CharField(max_length=30)
    status_no=models.IntegerField(default=1);
    Datetime=models.DateTimeField(default=datetime.now())
    delivered=models.BooleanField(default=False)

class Product_Review(models.Model):
    id=models.AutoField
    Owner=models.ForeignKey(signup,on_delete=models.CASCADE)
    Product=models.ForeignKey(product,on_delete=models.CASCADE)
    Review=models.TextField(max_length=400)
    def __str__(self):
        return 'On ',self.Product.name,'by',self.Owner.name

class d_state(models.Model):
    id=models.AutoField
    status_value=models.CharField(max_length=30,default="status not available")
    def __str__(self):
        return self.status_value



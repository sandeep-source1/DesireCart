from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(category)
class subcat(admin.ModelAdmin):
    list_display = ('id','name','date')
admin.site.register(subcategory,subcat)
admin.site.register(contact)



class productdi(admin.ModelAdmin):
    list_display =('id','category','name','subcategory','size','color','price','disprice','description','date')
admin.site.register(product,productdi)



class userde(admin.ModelAdmin):
    list_display =('id','userid','name','password')
admin.site.register(signup,userde)



class Cart_view(admin.ModelAdmin):
    list_display =('id','Owner','cartproduct')
admin.site.register(Cart,Cart_view)


class Review_view(admin.ModelAdmin):
    list_display =('id','Owner','Product')
admin.site.register(Product_Review,Review_view)




class d_state_view(admin.ModelAdmin):
    list_display =('id','status_value')
admin.site.register(d_state,d_state_view)
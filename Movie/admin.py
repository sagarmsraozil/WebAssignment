from django.contrib import admin

# Register your models here.
from Movie.models import Product,Product_info


class ProductAdmin(admin.ModelAdmin):
    list_display = ('image','movie_name')


class SingleProduct(admin.ModelAdmin):
    list_display = ('description','title_img','img1','img2','img3','img4','product','AvailableSeats')




admin.site.register(Product,ProductAdmin)

admin.site.register(Product_info,SingleProduct)


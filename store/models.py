from django.db import models

class Category(models.Model):
    name = models.CharField(max_length= 40, unique=True,db_index=True)
    slug = models.SlugField(max_length=25 , unique=True,db_index=True)

    class Meta :
            verbose_name_plural = "Categories"


    def __str__(self) :
        return str(self.name)



class Product(models.Model):
    name = models.CharField(max_length=25 , unique=True)
    quantity = models.IntegerField(blank=True)
    category = models.ForeignKey(Category ,models.CASCADE)
    slug = models.SlugField(max_length=25 , unique=True)
    price = models.DecimalField(max_digits=6 , decimal_places= 2 , db_index = True)
    description = models.TextField(blank = True , null = True)
    image = models.ImageField(upload_to=r"C:\Users\Hazem Darwich\Desktop\WebProjects\New SHOP\Media")
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
       
    def __str__(self) :
        return str(self.name)
from django.urls import path
from .views import home , product_detail
from src import settings
from django.conf.urls.static import static

urlpatterns = [
    path("product/<slug:slug>/", product_detail , name="product_detail"),  
    path("", home, name = "home"),

] 
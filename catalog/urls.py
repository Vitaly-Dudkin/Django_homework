from django.urls import path
from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contacts/', views.contact_page, name='contact_page'),
    # path('<int:pk>/', views.product_detail, name='product_detail')
]

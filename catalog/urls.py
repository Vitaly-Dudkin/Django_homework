from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home_page'),
    path('create_product/', views.ProductCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_confirm_delete'),
    path('detail/<int:pk>/', cache_page(60)(views.ProductDetailView.as_view()), name='product_detail'),
    # path('contacts/', views.contact_page, name='contact_page'),
    path('blog/', views.BlogPostListView.as_view(), name='blogpost_list'),
    path('create/', views.BlogPostCreateView.as_view(), name='blog_create_post'),
    path('update/<int:pk>/', views.BlogPostUpdateView.as_view(), name='blogpost_update_form'),
    path('delete/<int:pk>/', views.BlogPostDeleteView.as_view(), name='blog_post_confirm_delete'),
    path('detail/<int:pk>/', views.BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('redactor/<int:pk>/', views.BlogPostRedactorView.as_view(), name='blog_post_edit')

]

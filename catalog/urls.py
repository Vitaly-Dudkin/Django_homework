from django.urls import path
from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home_page'),
    path('contacts/', views.contact_page, name='contact_page'),
    path('blog/', views.BlogPostListView.as_view(), name='blogpost_list'),
    path('create/', views.BlogPostCreateView.as_view(), name='blog_create_post'),
    path('update/<int:pk>/', views.BlogPostUpdateView.as_view(), name='blogpost_update_form'),
    path('delete/<int:pk>/', views.BlogPostDeleteView.as_view(), name='blog_post_confirm_delete'),
    path('detail/<int:pk>/', views.BlogPostDetailView.as_view(), name='blog_post_detail')

]

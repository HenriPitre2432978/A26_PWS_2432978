from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    
    path('category/list/', CategoryListView.as_view(), name="category_list"),
    path('category/<int:id>/', CategoryView.as_view(), name="category"),
    path('category/create/', CategoryCreateView.as_view(), name="category_create"),
    path('category/edit/<int:id>/', CategoryEditView.as_view(), name="category_edit"),
    path('category/delete/<int:id>/', CategoryDeleteView.as_view(), name="category_delete"),
    
    path('product/list/', ProductListView.as_view(), name="product_list"),
    path('product/create/', ProductCreateView.as_view(), name="product_create"),
    path('product/edit/<int:id>/', ProductEditView.as_view(), name="product_edit"),
    path('product/delete/<int:id>/', ProductDeleteView.as_view(), name="product_delete"),
]

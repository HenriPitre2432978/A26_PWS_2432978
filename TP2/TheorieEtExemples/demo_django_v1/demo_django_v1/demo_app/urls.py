from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('category/list/', views.CategoryListView.as_view(), name="category_list"),
    path('category/<int:id>/', views.CategoryView.as_view(), name="category"),
]

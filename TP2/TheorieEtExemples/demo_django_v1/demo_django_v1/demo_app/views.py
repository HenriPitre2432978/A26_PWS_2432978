from django.http import Http404
from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, Product


class IndexView(View):
    def get(self, request):
        return render(request, 'demo_app/index.html')


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()

        context = {
            'firstname': "Pierre-Marc",
            'categories': categories,
        }

        return render(request, 'demo_app/category_list.html', context)


class CategoryView(View):
    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404("Category does not exist")
        
        products = Product.objects.filter(category__id=id)

        context = {
            'category': category,
            'products': products,
        }

        return render(request, 'demo_app/category.html', context)

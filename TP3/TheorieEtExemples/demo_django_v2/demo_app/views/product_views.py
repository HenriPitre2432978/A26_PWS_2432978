from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic.base import View

# Il existe également des vues spécialisées, je vous laisse découvrir les cas d'utilisation.
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ..models import Category, Product
from ..forms import ProductForm


"""
class ProductListView(View):
    template_name = "demo_app/product/product_list.html"

    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template_name, { 'products': products })
"""

class ProductListView(View):
    template_name = "demo_app/product/product_list_pages.html"

    def get(self, request):
        products = Product.objects.all()

        paginator = Paginator(products, 5)
        page_number = request.GET.get('page') or 1

        context = {
            'range_pages': range(1, paginator.num_pages + 1),
            'page_products': paginator.get_page(page_number),
        }

        return render(request, self.template_name, context)


class ProductCreateView(PermissionRequiredMixin, View):
    permission_required = "demo_app.add_product"
    template_name = "demo_app/product/product_form.html"

    def get_init_category(self, request):
        category = None
        try:
            category_id = request.GET.get('catid') or 0
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            pass
        return category

    """
    def get(self, request):
        context = {
            'action_text': 'Ajouter',
            'form': ProductForm()
        }
        return render(request, self.template_name, context)
    """

    def get(self, request):
        init_category = self.get_init_category(request)
        
        if init_category != None:
            return_url = reverse("category", args=[init_category.id])
        else:
            return_url = reverse("product_list")

        context = {
            'action_text': 'Ajouter',
            'form': ProductForm(initial={ 'category': init_category }),
            'return_url': return_url
        }
        return render(request, self.template_name, context)
    
    """
    def post(self, request):
        form = ProductForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("product_list")
        
        context = {
            'action_text': 'Ajouter',
            'form': form
        }
        return render(request, self.template_name, context)
    """

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            if request.GET.get('catid'):
                category = form.cleaned_data["category"]
                return redirect("category", id=category.id)
            else:
                return redirect("product_list")
        
        context = {
            'action_text': 'Ajouter',
            'form': form
        }
        return render(request, self.template_name, context)


class ProductEditView(PermissionRequiredMixin, View):
    permission_required = "demo_app.change_product"
    template_name = "demo_app/product/product_form.html"

    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        context = {
            'action_text': 'Modifier',
            'form': ProductForm(instance=product)
        }
        return render(request, self.template_name, context)
    
    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        form = ProductForm(request.POST, request.FILES, instance=product)
        
        if form.is_valid():
            form.save()
            return redirect("product_list")
        
        context = {
            'action_text': 'Modifier',
            'form': form
        }
        return render(request, self.template_name, context)


class ProductDeleteView(PermissionRequiredMixin, View):
    permission_required = "demo_app.delete_product"
    template_name = "demo_app/product/product_delete.html"

    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        return render(request, self.template_name, { 'product': product})

    def post(self, request, id):
        try:
            product = get_object_or_404(Product, id=id)
            product.delete()
        except Product.DoesNotExist:
            pass
        return redirect("product_list")

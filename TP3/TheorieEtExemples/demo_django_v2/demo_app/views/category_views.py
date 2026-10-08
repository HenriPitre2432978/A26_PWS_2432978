from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import View

from ..models import Category, Product
from ..forms import CategoryForm


class CategoryListView(View):
    template_name = "demo_app/category/category_list.html"

    def get(self, request):
        context = {
            'categories': Category.objects.all(),
        }
        return render(request, self.template_name, context)


class CategoryView(PermissionRequiredMixin, View):
    permission_required = "demo_app.view_category"
    template_name = "demo_app/category/category.html"

    def get(self, request, id):
        context = {
            'category': get_object_or_404(Category, id=id),
            'products': Product.objects.filter(category__id=id),
        }
        return render(request, self.template_name, context)


class CategoryCreateView(PermissionRequiredMixin, View):
    permission_required = "demo_app.add_category"
    template_name = "demo_app/category/category_form.html"

    def get(self, request):
        context = {
            'action_text': 'Ajouter',
            'form': CategoryForm()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data["name"]
            #new_category = Category(name=name)
            #new_category.save()

            form.save()
            messages.success(
                request,
                f"Catérorie \"{name}\" ajoutée avec succès.",
            )
            return redirect("category_list")

        context = {
            'action_text': 'Ajouter',
            'form': form
        }
        return render(request, self.template_name, context)


class CategoryEditView(PermissionRequiredMixin, View):
    permission_required = "demo_app.change_category"
    template_name = "demo_app/category/category_form.html"

    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        context = {
            'action_text': 'Modifier',
            'form': CategoryForm(instance=category)
        }
        return render(request, self.template_name, context)
    
    def post(self, request, id):
        category = get_object_or_404(Category, id=id)
        form = CategoryForm(request.POST, instance=category)
        
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"Catérorie \"{category.name}\" modifiée avec succès.",
            )
            return redirect("category", category.id)
        
        context = {
            'action_text': 'Modifier',
            'form': form
        }
        return render(request, self.template_name, context)


class CategoryDeleteView(PermissionRequiredMixin, View):
    permission_required = "demo_app.delete_category"

    def get(self, request, id):
        try:
            category = get_object_or_404(Category, id=id)
            category.delete()
            messages.success(
                request,
                f"Catérorie \"{category.name}\" supprimée avec succès.",
            )
        except Category.DoesNotExist:
            pass
        return redirect("category_list")
    
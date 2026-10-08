from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe

from .models import Category, Product

#admin.site.register(Category)
#admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "view_products_link")
    ordering = ['name',]
    readonly_fields = ("products_list",)

    def products_list(self, obj):
        if not obj.pk:
            return "-"
        
        products = obj.products.all()
        if not products:
            product_links = "Aucun produit associé"
        else:
            product_links = format_html_join(
                mark_safe("<br>"),
                '<a href="{}">{}</a>',
                (
                    (
                        reverse("admin:demo_app_product_change", args=[p.pk]),
                        p.name,
                    )
                    for p in products
                )
            )

        # Lien pour ajouter un produit avec la catégorie pré-remplie
        add_url = (
            reverse("admin:demo_app_product_add")
            + f"?category={obj.pk}"
        )
        add_link = format_html(
            '<br><br><a class="addlink" href="{}">Ajouter un produit</a>',
            add_url
        )

        return format_html("{}{}", product_links, add_link)

    products_list.short_description = "Produits associés"

    def view_products_link(self, obj):
        url = (
            reverse("admin:demo_app_product_changelist")
            + f"?category__id__exact={obj.id}"
        )
        return format_html('<a href="{}">Voir les produits</a>', url)

    view_products_link.short_description = "Produits associés"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name_with_image', 'category', 'quantity', 'active']
    list_filter = ['active','category',]
    ordering = ['name',]
    readonly_fields = ['image_preview',]
    search_fields = ['name']

    def product_name_with_image(self, obj):
        if obj.image:
            return format_html(
                '<span style="display:flex; align-items:center;">'
                '<img src="{}" style="max-width:32px; margin-right:6px;" />'
                '{}'
                '</span>',
                obj.image.url,
                obj.name,
            )
        return obj.name
    product_name_with_image.short_description = "Nom"
    product_name_with_image.admin_order_field = 'name'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:200px" />', obj.image.url)
        return ""
    image_preview.short_description = "Prévisualisation"

    def get_readonly_fields(self, request, obj=None):
        # Permet de ne pas afficher "Image Preview" lors de l'ajout
        if obj:  # si c'est lors de la modification
            return self.readonly_fields
        return []

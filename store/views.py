from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models.products import Product
from .models.variations import Variation, VariationCategoryChoice


# class StoreView(LoginRequiredMixin,View):
#     model = Product

#     def get(self, request):
#         products = self.model.objects.filter(is_active=True)
#         context = {
#             "products": products
#         }
#         return render(request, 'store/list.html', context)


class StoreListView(LoginRequiredMixin, ListView):
    model = Product
    queryset = Product.objects.filter(is_available=True)
    template_name = 'store/list.html'
    context_object_name = "products"


# class ProductDetailView(LoginRequiredMixin, View):
#     model = Product

#     def get(self, request, slug):
#         product = self.model.objects.filter(slug=slug).first()
#         context = {
#             "product": product
#         }
#         return render(request, 'store/detail.html', context)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'store/detail.html'
    context_object_name = "product"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context["size_variations"] = Variation.objects.filter(
            product=product, variation_category=VariationCategoryChoice.SIZE
        )
        context["color_variations"] = Variation.objects.filter(
            product=product, variation_category=VariationCategoryChoice.COLOR
        )
        print(context["color_variations"].first(), "++++")
        return context

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Product.DoesNotExist:
            raise Http404("Mahsulot topilmadi!")

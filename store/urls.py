from django.urls import path
from .views import StoreListView, ProductDetailView

app_name = 'store'

urlpatterns = [
    path("", StoreListView.as_view(), name="store_list"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="product_detail")
]

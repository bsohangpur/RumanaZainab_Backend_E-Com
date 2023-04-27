from django.urls import path
from .views import ProductListView, ProductDetailView, RatingListView, RatingDetailView


urlpatterns = [
    path('products/', ProductListView.as_view({'get': 'list', 'post':'create'}), name='product-list'),
    path('products/int:pk/', ProductDetailView.as_view(), name='product-detail'),
    path('ratings/', RatingListView.as_view({'get': 'list'}), name='rating-list'),
    path('ratings/int:pk/', RatingDetailView.as_view(), name='rating-detail'),
]

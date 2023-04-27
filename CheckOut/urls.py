from django.urls import path
from .views import CustomerCreateView, CustomerRetrieveUpdateDestroyView, CustomerGetView

urlpatterns = [
    path('checkout/', CustomerCreateView.as_view()),
    path('checkout/get/', CustomerGetView.as_view()),
    path('checkout/int:pk/', CustomerRetrieveUpdateDestroyView.as_view()),
]

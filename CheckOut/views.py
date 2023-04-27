from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.request import Request
from django.template.loader import render_to_string
# Create your views here.
from rest_framework import generics, permissions
from .models import Customer
from .serializers import CustomerSerializer


class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        
        # Compose the email message
        message = f"New order details:\n\n"
        for key, value in validated_data.items():
            message += f"{key}: {value}\n"
        
        # Send the email
        html_message = render_to_string('checkout_email.html', validated_data)
        send_mail(
            f"New order created By: {validated_data['first_name']} {validated_data['last_name']}",
            '',
            'contact@rumanazainab.com',
            ['contact@rumanazainab.com'],
            fail_silently=False,
            html_message = html_message,
        )
        
        return self.create(request, *args, **kwargs)

class CustomerGetView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAdminUser]

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAdminUser]

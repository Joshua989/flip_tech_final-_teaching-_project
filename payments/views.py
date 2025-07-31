import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from cart.models import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSession(APIView):
    def post(self, request):
        cart = Cart.objects.get(user=request.user)
        total = sum(item.total_price() for item in cart.cartitem_set.all())
        
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Fashionista Order',
                        },
                        'unit_amount': int(total * 100),  # Stripe uses cents
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=settings.FRONTEND_URL + '/success/',
                cancel_url=settings.FRONTEND_URL + '/cancel/',
            )
            
            return Response({'id': checkout_session.id})
            
        except Exception as e:
            return Response({'error': str(e)}, status=400)
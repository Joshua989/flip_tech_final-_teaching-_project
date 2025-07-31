from django.db import models
from accounts.models import User
from cart.models import Cart


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    stripe_payment_id = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
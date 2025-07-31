from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .serializer import CartSerializer, CartItemSerializer
from products.models import Product


class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]


    def get_object(self):
        Cart, created = Cart.objects.get_or_create(user=self.request.user)
        return Cart

class AddToCartView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request,*args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)


        try:
            Product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
        


        cart, craeted = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=Product, defaults={'quantity': quantity})
        if not created:
            cart_item.quantity +=quantity
            cart_item.save()


        return Response({'message': 'product added to cart'}, status=status.HTTP_201_CREATED)




class RemoveFromCartView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        item_id = kwargs.get('item_id')

        try:
            Cart_item = CartItem.objects.get(
                id = item_id,
                cart___user=request.user
            )
            Cart_item.delete()
            return Response({'message': 'item removed from cart'}, status=status.HTTP_204_NO_CONTENT)
        except Cart_item.DoesNotExist:
            return Response({'error': 'item not found'}, status=status.HTTP_404_NOT_FOUND)
        
    
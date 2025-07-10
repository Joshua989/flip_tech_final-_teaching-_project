from django.shortcuts import render
from  rest_framework.response import Response
from  rest_framework import generics
from .serializer import UserRegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from .serializer import MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
 
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user =  serializer.save()
        return Response({
            "message": "User registered successfully",
            "user":serializer.data
        })
    

class MyTokenObtianPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    
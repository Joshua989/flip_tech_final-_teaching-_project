from django.shortcuts import render
from  rest_framework.response import Response
from  rest_framework import generics, permissions, viewsets, filters
from .serializer import UserRegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from .serializer import MyTokenObtainPairSerializer, ProfileSerializer, ChangePasswordSerializer
from django.contrib.auth import update_session_auth_hash
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import User

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
    


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_object(self):
        return self.request.user
    
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = self.request.user

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if  not user.check_password(serializer.data.get('old_password')):
                return Response({'error': 'wrong old password'}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.data.get('new_password'))


            user.save()
            update_session_auth_hash(request, user)
            return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


        fields = '__all__'


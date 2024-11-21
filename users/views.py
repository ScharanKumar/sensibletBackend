from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import LoginSerializer
# from rest_framework.permissions import IsAuthenticated

class UserCreateView(APIView):
    permission_classes = [IsAdminUser]
    
    # done
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response({"detail":"User creation is failed.","error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




class LoginView(APIView):
    # done
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                user_data = {
                    "id": user.id,
                    "username": user.username,
                    
                }
                return Response({'token': token.key, "user":user_data, "message":"Logged in successfully!"}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error":"Logging in failed, please enter all fields.","message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         request.user.auth_token.delete()
#         return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)


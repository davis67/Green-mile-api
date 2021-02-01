from django.shortcuts import render
from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status, views, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
# from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404

from .serializers import RegisterSerializer,LoginSerializer, MemberSerializer, UpdateMemberSerializer
from .renderers import UserRenderer
from .models import User
import json


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    renderer_classes = (UserRenderer, )

    def post(self, request):

        user = request.data

        serializer = self.serializer_class(data=user)

        if serializer.is_valid():

            serializer.save()

            user_data = serializer.data

            user = User.objects.get(email = user_data["email"])

            return Response(user_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):


        serializer = self.serializer_class(data  = request.data)

        serializer.is_valid(raise_exception = True)

        return Response(serializer.data, status = status.HTTP_200_OK)

class ProfileView(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    renderer_classes = (UserRenderer, )

    def get(self, request):

        header =  JWTAuthentication().get_header(request)

        raw_token =  JWTAuthentication.get_raw_token(self, header)

        validated_token =  JWTAuthentication().get_validated_token(raw_token)

        user = JWTAuthentication.get_user(self, validated_token)

        # print(user.created_at)

        return Response({
            "email": user.email,
            "name": user.name,
            "username": user.username,
            "is_superuser": user.is_superuser,
            "is_staff": user.is_staff,
            "is_verified": user.is_verified,
            # "created_at": user.created_at,
            # "updated_at": user.updated_at,
            # 'tokens': user.tokens,
            },  status = status.HTTP_200_OK)

class MembersView(ListCreateAPIView):

    serializer_class = MemberSerializer

    permission_classes = (permissions.IsAuthenticated,)

    renderer_classes = (UserRenderer, )

    queryset = User.objects.all()

class MemberView(RetrieveUpdateDestroyAPIView):

    serializer_class = MemberSerializer

    permission_classes = (permissions.IsAuthenticated,)

    renderer_classes = (UserRenderer, )

    queryset = User.objects.all()

    lookup_url_kwarg = "pk"


    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs['pk']
        obj = get_object_or_404(queryset, pk = pk)
        return obj

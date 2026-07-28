from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token



@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message":"This is public view"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def private_view(request):
    return Response({"message":f"Hello! {request.user.username}, this is private view"})


@api_view(['GET','POST'])
def blog_list(request):
    if request.method == 'GET':
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BlogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user 
    return Response({
        "username":user.username,
        "email":user.email,
        "is_staff":user.is_staff,
    })


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def admin_pannel(request):
    return Response({"message":f"Welcome {request.user.username} to admin pannel"})
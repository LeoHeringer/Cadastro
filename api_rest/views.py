from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_xml.renderers import XMLRenderer

from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

import json

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([XMLRenderer])
def get_users_xml(request):

    users = User.objects    

    serializer = UserSerializer(users, many=True) 
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users_json(request):

    users = User.objects

    serializer = UserSerializer(users, many=True) 
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@renderer_classes([XMLRenderer])
@permission_classes([IsAuthenticated])
def get_by_nick_xml(request):

    if not request.GET['user']:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    user_nickname = request.GET['user']

    user = User.objects.filter(username=user_nickname)

    if not user.exists():
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    serializer = UserSerializer(user.first())
    return Response(serializer.data, status=status.HTTP_200_OK)  

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_by_nick_json(request):

    if not request.GET['user']:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    user_nickname = request.GET['user']

    user = User.objects.filter(username=user_nickname)

    if not user.exists():
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    serializer = UserSerializer(user.first())
    return Response(serializer.data, status=status.HTTP_200_OK)  

@api_view(['POST'])
@renderer_classes([XMLRenderer])
@permission_classes([IsAuthenticated])
def create_user_xml(request):

    new_user = request.data

    serializer = UserSerializer(data=new_user)

    if serializer.is_valid():
        serializer.save()
        return Response({'message':'created'}, status=status.HTTP_201_CREATED)

    return Response({'message':'invalid'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user_json(request):

    new_user = request.data

    serializer = UserSerializer(data=new_user)

    if serializer.is_valid():
        serializer.save()
        return Response({'message':'created'}, status=status.HTTP_201_CREATED)

    return Response({'message':'invalid'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@renderer_classes([XMLRenderer])
@permission_classes([IsAuthenticated])
def update_user_xml(request):

    cliente_id = request.query_params.get('id-usuario')

    if not cliente_id: 
        return Response({'message': 'incorrect data'}, status=status.HTTP_400_BAD_REQUEST)

    update_user = User.objects.filter(id=cliente_id).first()
    
    if not update_user:
        return Response({'message': 'not exist'}, status=status.HTTP_404_NOT_FOUND)

    is_superuser = request.data.get('is_superuser')

    if is_superuser is None:
        return Response({'message': 'data not provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    if not isinstance(is_superuser, bool):
        return Response({'message': 'incorrect data'}, status=status.HTTP_400_BAD_REQUEST)
    
    update_user.is_superuser = is_superuser
    update_user.save()

    return Response({'message': 'User updated successfully'}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_json(request):

    cliente_id = request.query_params.get('id-usuario')

    if not cliente_id: 
        return Response({'message': 'incorrect data'}, status=status.HTTP_400_BAD_REQUEST)

    update_user = User.objects.filter(id=cliente_id).first()
    
    if not update_user:
        return Response({'message': 'not exist'}, status=status.HTTP_404_NOT_FOUND)

    is_superuser = request.data.get('is_superuser')

    if is_superuser is None:
        return Response({'message': 'data not provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    if not isinstance(is_superuser, bool):
        return Response({'message': 'incorrect data'}, status=status.HTTP_400_BAD_REQUEST)
    
    update_user.is_superuser = is_superuser
    update_user.save()

    return Response({'message': 'User updated successfully'}, status=status.HTTP_200_OK)
 
@api_view(['DELETE'])
@renderer_classes([XMLRenderer])
@permission_classes([IsAuthenticated])
def delete_user_xml(request):

    cliente_id = request.query_params.get('id-usuario')

    user_to_delete = User.objects.filter(id=cliente_id).first()

    if user_to_delete:
        user_to_delete.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_200_OK)

    return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user_json(request):

    cliente_id = request.query_params.get('id-usuario')

    user_to_delete = User.objects.filter(id=cliente_id).first()

    if user_to_delete:
        user_to_delete.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_200_OK)

    return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

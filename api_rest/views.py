from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

import json



@api_view(['GET'])
@permission_classes([AllowAny])
def get_users(request):

    if request.method == 'GET':                #Verifica o site que estamos entrando

        users = User.objects.all()              #irá buscar todos os objetos do banco de dados

        serializer = UserSerializer(users, many=True)   #vai usar o UserSerializar para transformar os objetos de user e serializar eles

        return Response(serializer.data)        # retorna para o serializer
    
    return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
@permission_classes([AllowAny])
def get_by_nick(request):

    if request.method == 'GET':

        try:
            if request.GET['user']:

                user_nickname = request.GET['user']

                try:
                    user = User.objects.get(pk=user_nickname)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = UserSerializer(user)
                return Response(serializer.data)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)   

    
@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):

    new_user = request.data
    print(new_user.get('password'))

    serializer = UserSerializer(data=new_user)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
 

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_user(request):

    cliente_id = request.query_params['id-usuario']

    try:
        update_user = User.objects.filter(id=cliente_id).first()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    update_user.is_superuser = request.data.get('is_superuser')
    update_user.save()
    
    return Response(status=status.HTTP_200_OK)
 
    
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_user(request):

        cliente_id = request.query_params['id-usuario']

        try:
            user_to_delete = User.objects.filter(id=cliente_id)
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



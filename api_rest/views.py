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
@permission_classes([IsAuthenticated])
def get_users(request):

    if request.method == 'GET':                #Verifica o site que estamos entrando

        users = User.objects.all()              #irá buscar todos os objetos do banco de dados

        serializer = UserSerializer(users, many=True)   #vai usar o UserSerializar para transformar os objetos de user e serializar eles

        if 'aplication/xml' in request.headers.get('Accept', ''):

            return Response(serializer.data, content_type='application/xml')        # retorna para o serializer o xml caso ele seja aceito, retorna os dados em xml
    
        return Response(serializer.data)
    
    return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_by_nick(request):

    if request.method == 'GET':

        try:
            if request.GET['user']:

                user_nickname = request.GET['user']

                try:
                    user = User.objects.get(pk=user_nickname)
                except User.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = UserSerializer(user)
                return Response(serializer.data)
            
            if 'application/xml' in request.headers.get('Accept', ''):
                return Response(serializer.data, content_type='application/xml')
                
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)   

    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user(request):

    new_user = request.data

    serializer = UserSerializer(data=new_user)

    if serializer.is_valid():
        serializer.save()

        if 'aplication/xml' in request.headers.get('Accept', ''): # verifica se 'application/xml' esta no dicionario
            return Response(serializer.data, status=status.HTTP_201_CREATED, content_type='application/xml') 
    
        return Response(serializer.data, status=status.HTTP_201_CREATED) # caso não tenha achado o xml retornar json por padrão
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
 

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):

    cliente_id = request.query_params['id-usuario']

    try:
        update_user = User.objects.filter(id=cliente_id).first()
    except:
        return Response({'mensagem': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    update_user.is_superuser = request.data.get('is_superuser')
    update_user.save()

    if 'application/xml' in request.headers.get('Accept', ''): # verifica se 'application/xml' esta no dicionario
        return Response({'mensagem': 'Usuário atualizado com sucesso'}, status=status.HTTP_200_OK, content_type='application/xml')
    
    return Response({'mensagem': 'Usuário atualizado com sucesso'}, status=status.HTTP_200_OK) # caso não tenha achado o xml retornar json por padrão
 
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):

    cliente_id = request.query_params.get('id-usuario')

    try:
        user_to_delete = User.objects.get(id=cliente_id)
        user_to_delete.delete()

        if 'application/xml' in request.headers.get('Accept', ''):  # verifica se 'application/xml' esta no dicionario
            data = {'mensagem': 'Usuario apagado com sucesso'}
            return Response(data, status=status.HTTP_200_OK, content_type='application/xml')
    
        data = {'mensagem': 'Usuario apagado com sucesso'} # caso não tenha achado o xml retornar json por padrão
        return Response(data, status=status.HTTP_200_OK)
    
    except User.DoesNotExist: 
        if 'application/xml' in request.headers.get('Accept', ''):  # verifica se 'application/xml' esta no dicionario
            data = {'mensagem': 'Usuario não encontrado'}
            return Response(data, status=status.HTTP_200_OK, content_type='application/xml')
            
        data = {'mensagem': 'Usuario não encontrado'} # caso não tenha achado o xml retornar json por padrão
        return Response({'mensagem': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)



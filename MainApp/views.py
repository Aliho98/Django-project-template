from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from .models import Fruit

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .serializers import FruitSerializers

class UserProfileView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    
    def get_object(self, fruit_id, user_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Fruit.objects.get(id=fruit_id, user = user_id)
        except Fruit.DoesNotExist:
            return None
        
        
    def get(self, request,*args,**kwargs):
        # Retrieve the user object based on the username
        Fruits=Fruit.objects.filter(user=request.user.id)
        serializers=FruitSerializers(Fruits,many=True)
        
        return Response(serializers.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        data={
            'name':request.data.get('name'),
            'taste':request.data.get('taste'),
            'user': request.user.id
            
           } 
        
        serializer=FruitSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, Fruit_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        Fruit_instance = self.get_object(Fruit_id, request.user.id)
        if not Fruit_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = FruitSerializers(instance = Fruit_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, fruit_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        fruit_instance = self.get_object(fruit_id, request.user.id)
        if not fruit_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        fruit_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

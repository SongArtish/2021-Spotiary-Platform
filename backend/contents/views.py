from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.shortcuts import render, get_object_or_404
from .models import Content
from .serializers import ContentSerializer
import datetime

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication]) # 토큰 유효한지 확인
@permission_classes([IsAuthenticated])  # user authenticated한지 DRF에서 검사한다!!
def content_list_create(request): 
    if request.method=='GET': 
        contents = Content.objects.all()
        serializer= ContentSerializer(contents, many=True)
        return Response(serializer.data)
    else:
        # new_data = request.data
        # new_data['user'] = request.user.pk
        serializer = ContentSerializer(data=request.data)
        # print('hello')
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def content_update_delete(request, content_pk): 
    content = get_object_or_404(Content, pk=content_pk)
    if request.method=='PUT' : 
        serializer = ContentSerializer(content, data=request.data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data)
    else:
        content.delete()
        # 삭제될 때 삭제된 데이터의 id 값을 보여준다.
        return Response({'id':content_pk})


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def content_detail(request, content_pk):
    content = get_object_or_404(Content, pk=content_pk)
    serializer = ContentSerializer(content)
    return Response(serializer.data)
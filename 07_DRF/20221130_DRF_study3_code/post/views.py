from django.shortcuts import render
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, RecommentSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# 글 목록 조회 - 로그인 없이 조회 가능
@api_view(['GET'])
@permission_classes([AllowAny])
def post_list(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)

# 글 생성 - 로그인 필요
@api_view(['POST'])
def post_create(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.validated_data['write_user'] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 글 상세 내용 확인 - 로그인 필요
@api_view(['GET'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PostSerializer(post)
    return Response(serializer.data)
    
# 글 수정 - 로그인 필요
@api_view(['PUT'])
def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    serializer = PostSerializer(post, request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 글 삭제 - 로그인 필요
@api_view(['DELETE'])
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# (테스트 확인용) 댓글, 대댓글 목록 확인하기 - 로그인 필요
@api_view(['GET'])
def comment_list(request):
    comment = Comment.objects.all()
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)

# 댓글 작성하기 - 로그인 필요
@api_view(['POST'])
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.validated_data['article'] = post
        serializer.validated_data['comment_user'] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 대댓글 작성하기 - 로그인 필요
@api_view(['POST'])
def recomment_create(request, post_pk, comment_pk):
    post = Post.objects.get(pk=post_pk)
    serializer = RecommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.validated_data['article'] = post
        serializer.validated_data['comment_user'] = request.user
        serializer.validated_data['parent_comment_id'] = comment_pk
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
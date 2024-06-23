from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .serializers import ArticleSerializer, ArticleDetailSerializer, CommentDetailSerializer, CommentSerializer, BoardSerializer
from .models import Article, Comment, Board
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404


User = get_user_model()


# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def article_list_create(request, board_name):
    board = get_object_or_404(Board, name=board_name)
    
    if request.method == 'GET':
        articles = Article.objects.filter(board=board.pk).order_by('-created_at')
        serializers = ArticleSerializer(articles, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializer = ArticleDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(board=board, author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
def article_detail(request, board_name, article_id):
    # 게시판과 일치할 때만 return
    board = Board.objects.get(name=board_name)
    article = get_object_or_404(Article, pk=article_id, board=board)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArticleDetailSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response({'result':'삭제가 완료되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def comment_list_create(request, board_name, article_id):
    board = Board.objects.get(name=board_name)
    article = get_object_or_404(Article, board=board, pk=article_id)

    if request.method == 'GET':
        comments = Comment.objects.filter(article=article)
        serializers = CommentSerializer(comments, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, author=request.user)
            return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([JWTAuthentication])
def comment_detail(request, board_name, article_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        comment.delete()
        return Response({'result':'삭제가 완료되었습니다.'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentDetailSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def article_likes(request, board_name, article_id):
    board = Board.objects.get(name=board_name)
    article = get_object_or_404(Article, board=board, pk=article_id)

    if request.method == 'GET':
        # 좋아요 판별용 변수
        isLike = False
        if article in request.user.likes.all() :
            isLike = True
        else:
            isLike = False
        return Response({'isLike': f'{isLike}', 'like_count':article.like.count() }, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        message = ''
        print(request.user.likes.all())        
        if article in request.user.likes.all() :
            request.user.likes.remove(article)
            message = '제거'
        else:
            request.user.likes.add(article)
            message = '등록'
        return Response({'result': f'좋아요 {message}'}, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def get_board(request):
    print('hi')
    boards = Board.objects.all()
    serializer = BoardSerializer(boards, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
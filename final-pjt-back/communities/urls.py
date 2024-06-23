from django.urls import path
from . import views


urlpatterns = [
    # 게시판명 조회
    path('boards/', views.get_board),
    # 게시판의 게시글 전체 조회 및 단일 게시글 생성
    path('<str:board_name>/', views.article_list_create),
    # 단일 게시글 상세 조회 및 수정, 삭제
    path('<str:board_name>/<int:article_id>/', views.article_detail),
    # 게시글의 댓글 전체 조회 및 생성
    path('<str:board_name>/<int:article_id>/comment/', views.comment_list_create),
    # 게시글의 단일 댓글 조회, 수정 및 삭제
    path('<str:board_name>/<int:article_id>/comment/<int:comment_id>/', views.comment_detail),
    # 게시글 <-> 유저 간 좋아요
    path('<str:board_name>/<int:article_id>/likes/', views.article_likes),
]
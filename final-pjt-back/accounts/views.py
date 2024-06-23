from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from products.models import DepositProducts,DepositOptions,SavingOptions,SavingProducts
from products.serializers import DepositProductsSerializer,DepositOptionsSerializer,SavingOptionsSerializer,SavingProductsSerializer
# Create your views here.

## 유저 프로필 조회, 수정 / 회원 삭제
@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([JWTAuthentication])
def profile_detail(request,username):
    user = get_object_or_404(User, username=username)
    if request.method=="GET":
        serializer=UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        if request.user.username == username:
            user.delete()
            return Response({'result':'삭제가 완료되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'result':'요청이 올바르지 않습니다'}, status=status.HTTP_400_BAD_REQUEST)

# 로그아웃
@api_view(['POST'])
def logout(request):
    # 로그아웃 요청 시 토큰을 검증하지 않음
    return Response({'message': 'Logout successful'}, status=200)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def subscribe_deposit(request, username, product_id):
    user = get_object_or_404(User, username=username)
    product = get_object_or_404(DepositProducts, id=product_id)
    
    if product in user.my_deposits.all():
        user.my_deposits.remove(product)
        return Response({'result': '이미 가입한 예금입니다. 가입을 취소합니다'}, status=status.HTTP_200_OK)
    
    user.my_deposits.add(product)
    user.save()
    return Response({'result': '가입이 완료되었습니다.'}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def subdeposit_list(request, username):
    user = get_object_or_404(User, username=username)
    subscribed_products = user.my_deposits.all()
    
    # 예금 상품의 상세 정보를 포함한 리스트를 생성합니다.
    products_list = [
        {
            'fin_prdt_cd': product.fin_prdt_cd,
            'kor_co_nm': product.kor_co_nm,
            'fin_prdt_nm': product.fin_prdt_nm,
            'etc_note': product.etc_note,
            'join_deny': product.join_deny,
            'join_member': product.join_member,
            'join_way': product.join_way,
            'spcl_cnd': product.spcl_cnd,
            'mtrt_int': product.mtrt_int,
            'views_count': product.views_count,
            'options': [
                {
                    'intr_rate_type_nm': option.intr_rate_type_nm,
                    'save_trm': option.save_trm,
                    'intr_rate': option.intr_rate,
                    'intr_rate2': option.intr_rate2
                }
                for option in product.depositoptions_set.all()
            ]
        } 
        for product in subscribed_products
    ]
    
    return Response({'deposit_list': products_list}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def subscribe_saving(request, username, product_id):
    user = get_object_or_404(User, username=username)
    product = get_object_or_404(SavingProducts, id=product_id)
    print(user.my_savings.all())
    print(product)
    if product in user.my_savings.all():
        user.my_savings.remove(product)
        return Response({'result': '이미 가입한 적금입니다. 가입을 취소합니다'}, status=status.HTTP_200_OK)
    
    user.my_savings.add(product)
    user.save()
    return Response({'result': '가입이 완료되었습니다.'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def subsaving_list(request, username):
    user = get_object_or_404(User, username=username)
    subscribed_products = user.my_savings.all()
    
    # 예금 상품의 상세 정보를 포함한 리스트를 생성합니다.
    products_list = [
        {
            'fin_prdt_cd': product.fin_prdt_cd,
            'kor_co_nm': product.kor_co_nm,
            'fin_prdt_nm': product.fin_prdt_nm,
            'etc_note': product.etc_note,
            'join_deny': product.join_deny,
            'join_member': product.join_member,
            'join_way': product.join_way,
            'spcl_cnd': product.spcl_cnd,
            'mtrt_int': product.mtrt_int,
            'views_count': product.views_count,
            'options': [
                {
                    'intr_rate_type_nm': option.intr_rate_type_nm,
                    'save_trm': option.save_trm,
                    'intr_rate': option.intr_rate,
                    'intr_rate2': option.intr_rate2
                }
                for option in product.savingoptions_set.all()
            ]
        } 
        for product in subscribed_products
    ]
    
    return Response({'saving_list': products_list}, status=status.HTTP_200_OK)
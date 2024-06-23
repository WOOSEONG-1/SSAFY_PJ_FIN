import requests
from django.shortcuts import render
from django.shortcuts import get_object_or_404,get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DepositProducts,DepositOptions,SavingOptions,SavingProducts
from .serializers import DepositProductsSerializer,DepositOptionsSerializer,SavingProductsSerializer,SavingOptionsSerializer
from django.conf import settings
# Create your views here.
API_KEY=settings.FIN_KEY
deposit_url=f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
saving_url=f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

# 0. Data Save
@api_view(['GET'])
def save_products(request):
    response=requests.get(deposit_url).json()
    for li in response.get('result').get('baseList'):
        fin_prdt_cd=li.get('fin_prdt_cd')
        kor_co_nm=li.get('kor_co_nm')
        fin_prdt_nm=li.get('fin_prdt_nm')
        etc_note=li.get('etc_note')
        join_deny=int(li.get('join_deny'))
        join_member=li.get('join_member')
        join_way=li.get('join_way')
        spcl_cnd=li.get('spcl_cnd')
        mtrt_int=li.get('mtrt_int')
        views_count=li.get('views_count')
        save_deposit={
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd,
            'mtrt_int':mtrt_int,
            'views_count':views_count
        }
        serializers=DepositProductsSerializer(data=save_deposit)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            
    for opt in response.get('result').get('optionList'):
        # product=opt.get('product')
        fin_prdt_cd=opt.get('fin_prdt_cd')
        intr_rate_type_nm=opt.get('intr_rate_type_nm')
        intr_rate=opt.get('intr_rate')
        intr_rate2=opt.get('intr_rate2')
        save_trm=int(opt.get('save_trm'))
        save_option={
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2,
            'save_trm':save_trm,
        }
        serializer=DepositOptionsSerializer(data=save_option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(fin_prdt_cd=DepositProducts.objects.get(fin_prdt_cd=save_option.get('fin_prdt_cd')))
            
    response=requests.get(saving_url).json()
    for li in response.get('result').get('baseList'):
        fin_prdt_cd=li.get('fin_prdt_cd')
        kor_co_nm=li.get('kor_co_nm')
        fin_prdt_nm=li.get('fin_prdt_nm')
        etc_note=li.get('etc_note')
        join_deny=int(li.get('join_deny'))
        join_member=li.get('join_member')
        join_way=li.get('join_way')
        spcl_cnd=li.get('spcl_cnd')
        mtrt_int=li.get('mtrt_int')
        views_count=li.get('views_count')
        save_deposit={
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd,
            'mtrt_int':mtrt_int,
            'views_count':views_count
        }
        serializers=SavingProductsSerializer(data=save_deposit)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
    for opt in response.get('result').get('optionList'):
        # product=opt.get('product')
        fin_prdt_cd=opt.get('fin_prdt_cd')
        intr_rate_type_nm=opt.get('intr_rate_type_nm')
        intr_rate=opt.get('intr_rate')
        intr_rate2=opt.get('intr_rate2')
        save_trm=int(opt.get('save_trm'))
        save_option={
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2,
            'save_trm':save_trm,
        }
        serializer=SavingOptionsSerializer(data=save_option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(fin_prdt_cd=SavingProducts.objects.get(fin_prdt_cd=save_option.get('fin_prdt_cd')))
    return Response({"message": "okay "})


# 1. Data View
@api_view(['GET'])
def deposit_products(request):
    product=DepositProducts.objects.all()
    serializer=DepositProductsSerializer(product,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def deposit_options(request):
    option=DepositOptions.objects.all()
    serializer=DepositOptionsSerializer(option,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def saving_products(request):
    product=SavingProducts.objects.all()
    serializer=SavingProductsSerializer(product,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def saving_options(request):
    option=SavingOptions.objects.all()
    serializer=SavingOptionsSerializer(option,many=True)
    return Response(serializer.data)

# 2. 상세 View
@api_view(['GET'])
def deposit_product_detail(request, pid):
    product=get_object_or_404(DepositProducts,id=pid)
    serializer=DepositProductsSerializer(product)
    return Response(serializer.data)
@api_view(['GET'])
def deposit_option_detail(request,pid):
    option=get_list_or_404(DepositOptions,id=pid)
    serializer=DepositOptionsSerializer(option,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def saving_product_detail(request,pid):
    product=get_object_or_404(SavingProducts,id=pid)
    serializer=SavingProductsSerializer(product)
    return Response(serializer.data)
@api_view(['GET'])
def saving_option_detail(request,pid):
    option=get_list_or_404(SavingOptions,id=pid)
    serializer=SavingOptionsSerializer(option,many=True)
    return Response(serializer.data)
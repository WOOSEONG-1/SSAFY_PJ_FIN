from rest_framework import serializers
from .models import DepositOptions,DepositProducts,SavingOptions,SavingProducts

class DepositProductsSerializer(serializers.ModelSerializer):
    class DepositOptionsSerializer(serializers.ModelSerializer):
        class Meta:
            model=DepositOptions
            fields=('__all__')
    options = DepositOptionsSerializer(many=True, read_only=True, source='depositoptions_set')
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    class DepositProductCustomSerializer(serializers.ModelSerializer):
        class Meta:
            model=DepositProducts
            exclude=('id','views_count', 'join_deny')
    product = DepositProductCustomSerializer(read_only=True, source = 'fin_prdt_cd')
    # depositproducts_set = DepositProductCustomSerializer(many=True, read_only=True)
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields=('fin_prdt_cd',)

class SavingProductsSerializer(serializers.ModelSerializer):
    class SavingOptionsSerializer(serializers.ModelSerializer):
        class Meta:
            model=DepositOptions
            fields=('__all__')
    options = SavingOptionsSerializer(many=True, read_only=True, source='savingoptions_set')
    class Meta:
        model = SavingProducts
        fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):
    class DepositProductCustomSerializer(serializers.ModelSerializer):
        class Meta:
            model=SavingProducts
            exclude=('id','views_count', 'join_deny')
    product = DepositProductCustomSerializer(read_only=True, source = 'fin_prdt_cd')
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields=('fin_prdt_cd',)
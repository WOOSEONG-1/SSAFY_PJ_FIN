from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email,user_username,user_field
from products.models import DepositProducts,SavingProducts,DepositOptions,SavingOptions
# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    my_products = models.TextField(blank=True, null=True) # 가입 상품들
    gender=models.IntegerField(blank=True,null=True)
    age = models.IntegerField(blank=True,null=True,default=0)
    money = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    my_deposits=models.ManyToManyField(DepositProducts,related_name="deposits",blank=True)
    my_savings=models.ManyToManyField(SavingProducts,related_name='savings',blank=True)
    my_deposit_options=models.ManyToManyField(DepositOptions,related_name="deposit_options",blank=True)
    my_saving_options=models.ManyToManyField(SavingOptions,related_name="saving_options",blank=True)
    USERNAME_FIELD = 'username'

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data=form.cleaned_data
        username=data.get('username')
        my_products=data.get('my_products')
        gender=data.get('gender')
        age=data.get('age')
        money=data.get('money')
        email=form.data.get('email')
        nickname=data.get('nickname')
        salary=data.get('salary')
        user_email(user,email)
        user_username(user,username)
        if nickname:
            user_field(user,'nickname',nickname)
        if age:
            user.age=age
        if money:
            user.money=money
        if salary:
            user.salary=salary
        if my_products:
            user_field(user,'my_products',my_products)
        if gender:
            user.gender=gender
        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user

from .models import User
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username', 'my_products', 'gender','age', 'email','money', 'nickname', 'salary']
        
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    gender=serializers.IntegerField(required=True)
    age = serializers.IntegerField(required=False)
    nickname=serializers.CharField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)  
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['gender']=self.validated_data.get('gender',0)
        data['age'] = self.validated_data.get('age', 0)
        data['nickname'] = self.validated_data.get('nickname', '')
        data['money'] = self.validated_data.get('money', 0)
        data['salary'] = self.validated_data.get('salary', 0)
    
        return data

    def save(self, request):
        user = super().save(request)
        user.gender=self.cleaned_data.get('gender',0)
        user.age = self.cleaned_data.get('age', 0)
        user.money = self.cleaned_data.get('money', 0)
        user.salary = self.cleaned_data.get('salary', 0)
        user.save()
        return user
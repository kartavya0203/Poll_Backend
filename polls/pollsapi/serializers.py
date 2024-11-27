from rest_framework import serializers
from .models import Poll,Choice,Vote
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vote
        fields='__all__'

class ChoiceSerialzier(serializers.ModelSerializer):
    votes=VoteSerializer(many=True,required=False)
    class Meta:
        model=Choice
        fields='__all__'

class PollSerializer(serializers.ModelSerializer):
    choices=ChoiceSerialzier(many=True,read_only=True)
    class Meta:
        model=Poll
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
        extra_kwargs={'password':{'write-only':True}}
    
    def create(self, validated_data):
        user=User(email=validated_data,password=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

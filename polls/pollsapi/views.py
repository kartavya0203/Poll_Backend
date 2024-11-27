from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics,status
from django.contrib.auth import authenticate
# Create your views here.
class PollList(APIView):
    def get(self,request):
        polls=Poll.objects.all()[:20]
        data=PollSerializer(polls,many=True).data
        return Response(data)
    
class PollDetail(APIView):
    def get(self,request,pk):
        poll=get_object_or_404(Poll,pk=pk)
        data=PollSerializer(poll).data
        return Response(data)
    
class ChoiceList(generics.ListCreateAPIView):
    queryset=Choice.objects.all()
    serializer_class=ChoiceSerialzier

class CreateVote(generics.ListCreateAPIView):
    serializer_class=VoteSerializer

    def post(self,request,pk,choice_pk):
        voted_by=request.data.get("voted_by")
        data={'choice':choice_pk,'poll':pk,'voted_by':voted_by}
        serializer=VoteSerializer(data=data)
        if serializer.is_valid():
            vote=serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class UserView(generics.CreateAPIView):
    serializer_class=UserSerializer


class LoginApiView(generics.CreateAPIView):
    permission_classes=()

    def post(sel,request):
        username=request.data.get("username")
        password=request.data.get("password")
        user=authenticate(username=username,password=password)

        if user:
            return Response({'token':user.auth_token.key})
        else:
            return Response({'error':"Wrong Credentials Provided"})

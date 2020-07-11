from django.shortcuts import render, get_object_or_404
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
# Create your views here.

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)
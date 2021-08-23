from django.contrib.auth.models import User
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def membershipListView(request):
    if request.method == 'GET':
            userList = User.objects.all()
            serializer = UserSerializer(userList, many=True)
            return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = UserSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)

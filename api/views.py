from django.db import connection
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework import status
from django.conf import settings

EZapiIm = settings.MEDIA_URL
URL = settings.URL_LINK

@csrf_exempt
def membershipListView(request,cm,fid,ut):
    cursor = connection.cursor()
    userList=''
    try:
        userList = cursor.execute("EXEC [dbo].[UserInfo] @cm='"+cm+"',@fid='"+fid+"',@user_type='"+ut+"'")
    except userList.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = []
        for i in userList:
            data.append({
                'id':i[0],
                'username':i[1],
                'first_name':i[2],
                'last_name':i[3],
                'gender':i[4],
                'nationality':i[5],
                'dateBirth':i[6],
                'jobs':i[7],
                'organization':i[8],
                'userImage':EZapiIm + i[9],
                'proName':i[10],
                'villageName':i[11],
                'districtName':i[12],
                'communceName':i[13],
                'provinceName':i[14],
                'email':i[15],
                'phone':i[16],
                'date_joined':i[17],
                'last_login':i[18],
                'detail_user':URL + 'profile/' + str(i[0]),
                'is_staff':i[19],
                'is_active':i[20],
            })
        return JsonResponse(data, safe=False)

import requests
from django.conf import settings

EZapi = settings.MEDIA_URL_API

def MemberControl(cm,id):
    data = requests.get(url=EZapi+"membershiplistview/"+cm+";"+id+"").json()
    print(data)
    return data


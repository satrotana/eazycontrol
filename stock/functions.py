
import requests
from django.conf import settings

EZapi = settings.MEDIA_URL_API

def MemberControl(cm,id,ut):
    data = requests.get(url=EZapi+"membershiplistview/"+cm+";"+id+";"+ut+"").json()
    return data


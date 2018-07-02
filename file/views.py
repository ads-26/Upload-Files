from django.shortcuts import render,redirect,render_to_response
from .models import File
from .forms import FileForm
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
import requests, os

"""
def generate_token(request, format=None):
    url = 'http://10.129.103.86:5000/v3/auth/tokens'
    headers = {'content-type': 'application/json'}
    data = '\n{ "auth": {\n    "identity": {\n      "methods": ["password"],\n      "password": {\n        "user": {\n          "name": "swift2",\n          "domain": { "name": "default" },\n          "password": "swift2"\n        }\n      }\n    },\n    "scope": {\n      "project": {\n        "name": "service2",\n        "domain": { "name": "default" }\n      }\n    }\n  }\n}'
    r = requests.post(url, headers=headers, data=data)
    headers = r.headers.get('X-Subject-Token')
    return render(request, 'files/success.html', {'header': headers})
"""

def choose_object(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            create_object(request.FILES['file'], request.POST['container'], request.POST['obj'])
            return render_to_response('file/success.html')
    else:
        form = FileForm()
    return render(request, 'file/form_upload.html', {'form': form})
    


def create_object( file, container, obj):

    r = requests.put('http://10.129.103.86:8080/v1/AUTH_0d979205409846a7a2950fe8279d1988/' + container + '/' + obj ,
	    headers={'X-Auth-Token': '3443cfc6f4d84ff499e82ee2db7b1637', 'Content-Type': 'application/json'},
	    data=(file))


    return render_to_response('file/success.html')
    

@api_view(['GET','PUT'])
def object_upload(request, container, format=None):
    """
    Generating Token each time
    """
    url = 'http://10.129.103.86:5000/v3/auth/tokens'
    headers = {'content-type': 'application/json'}
    data = '\n{ "auth": {\n    "identity": {\n      "methods": ["password"],\n      "password": {\n        "user": {\n          "name": "swift2",\n          "domain": { "name": "default" },\n          "password": "swift2"\n        }\n      }\n    },\n    "scope": {\n      "project": {\n        "name": "service2",\n        "domain": { "name": "default" }\n      }\n    }\n  }\n}'
    r = requests.post(url, headers=headers, data=data)
    token = r.headers.get('X-Subject-Token')

    if request.method == 'GET':
        r = requests.get('http://10.129.103.86:8080/v1/AUTH_0d979205409846a7a2950fe8279d1988/' + container, headers={'X-Auth-Token': token}).text
        obj_arr = r.split ("\n")
        obj_arr.pop()
        
        return Response(obj_arr)

    if request.method =='PUT':
        url = request.data
        obj = os.path.basename(url)
        r = requests.put ('http://10.129.103.86:8080/v1/AUTH_0d979205409846a7a2950fe8279d1988/'+container + '/' + obj ,
            headers={'X-Auth-Token': token}.text, data = open(url, "rb")).text
        return Response (r)

@api_view(['GET','PUT'])
def container_upload(request, format=None):

    url = 'http://10.129.103.86:5000/v3/auth/tokens'
    headers = {'content-type': 'application/json'}
    data = '\n{ "auth": {\n    "identity": {\n      "methods": ["password"],\n      "password": {\n        "user": {\n          "name": "swift2",\n          "domain": { "name": "default" },\n          "password": "swift2"\n        }\n      }\n    },\n    "scope": {\n      "project": {\n        "name": "service2",\n        "domain": { "name": "default" }\n      }\n    }\n  }\n}'
    r = requests.post(url, headers=headers, data=data)
    token = r.headers.get('X-Subject-Token')

    if request.method == 'GET':
        r = requests.get('http://10.129.103.86:8080/v1/AUTH_0d979205409846a7a2950fe8279d1988/', headers={'X-Auth-Token': token}).text
        cont_arr = r.split ("\n")
        cont_arr.pop()
        return Response(cont_arr)
    if request.method =='PUT':
        new_container = request.data
        r = requests.put ('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + new_container, headers={'X-Auth-Token': token}).text
        return Response (r)
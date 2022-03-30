from django.http.response import JsonResponse
from django.shortcuts import render
from .models import District, State
from rest_framework.decorators import api_view
import json
from register.controller.conection import database
from bson import json_util, ObjectId
from pprint import pprint
import bcrypt
import jwt
# Create your views here.

@api_view(('POST', ))
def create_state(request):
    if request.method=="POST":
        data = request.data
        name = data['name']
        des = data["description"]
        state = State(name=name, description=des)
        state.save()
        return JsonResponse({"Status":True, "response":json.loads(json_util.dumps(data)), "message":"user has been created successfully"})
    return JsonResponse({"Status":True, "message":"Input Correct request"})

@api_view(('GET', ))
def get_states(request):
    try:
        data = database.state.find({})
        return JsonResponse({'Status':True, "response":json.load(json_util.dumps(data))})
    except Exception as e:
        return JsonResponse({'Status': False, "response": e})

@api_view(('POST', ))
def create_district(request):
    try:
        data = request.data
        s_name = data['state_name']
        name = data['name']
        state = District(state_name=s_name, name=name)
        state.save()
        return JsonResponse({"Status":True, "response":json.loads(json_util.dumps(data)), "message":"user has been created successfully"})
    except Exception as e:
        return JsonResponse({"Status":False, "message":str(e)})

@api_view(('GET', ))
def get_district(request):
    try:
        data = database.district.find({})
        return JsonResponse({'Status':True, "response":json.load(json_util.dumps(data))})
    except Exception as e:
        return JsonResponse({'Status': False, "response": e})

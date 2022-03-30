from django.http.response import JsonResponse
from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view
import json
from .controller.conection import database
from bson import json_util, ObjectId
from pprint import pprint
import bcrypt
import jwt
# Create your views here.

@api_view(('POST', ))
def create_user(request):
    if request.method=="POST":
        data = request.data
        name = data['username']
        password = data["password"].encode("utf-8")
        print("password = ", password)
        password = bcrypt.hashpw(password, bcrypt.gensalt(14))
        print(password)
        print(name, password)
        user = User(username=name, password=password)
        user.save()
        return JsonResponse({"Status":True, "response":json.loads(json_util.dumps(data)), "message":"user has been created successfully"})
    return JsonResponse({"Status":True, "message":"Input Correct Values"})


@api_view(('POST', ))
def login(request):
    
    if request.method=="POST":
        data = request.data
        try:
            name = data['username']
            password = str(data["password"])
        
            db_data = database['user'].find({"username":name})
            db_data = json.loads(json_util.dumps(db_data))
            # import pdb;pdb.set_trace()
            print(db_data)
            if len(db_data)!=0:
                for i in range(len(db_data)):
                    hashed = db_data[i]['password']
                    
                    if bcrypt.checkpw(bytes(password, encoding="utf8"), bytes(hashed, encoding="utf8")):
                        encoded_jwt = jwt.encode(db_data[i], "secret", algorithm="HS256")
                        db_data[i]["token"] = encoded_jwt 
                        return JsonResponse({"Status":True, "response":db_data[i], "message":"Sign In successfull"})
                return JsonResponse({"Status":False, "message":"Please Enter Correct Password"})
            return JsonResponse({"Status":False, "message":"Please Enter correct username"})
        except Exception as e:
            return JsonResponse({"Status":False, "message":"Please Enter correct details"})
    
    return JsonResponse({"Status":True, "message":"Input Correct details"})


@api_view(('GET', ))
def get_user(request):
    try:
        token = request.data["token"]
        print(token)
        data = jwt.decode(token, "secret", algorithms=["HS256"])
        return JsonResponse({"Status":True, "response":data})
    except Exception as e:
        return JsonResponse({'Statue': False, "response": e})

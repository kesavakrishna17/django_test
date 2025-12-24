from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import CourseRegistration

# Create your views here.
@csrf_exempt
def registration(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            CourseRegistration.objects.create(name=data.get("name"),email=data.get("email"),course=data.get("course"),phone=data.get("phone"))
            return JsonResponse({"status":"Success","message":"registration successfully completed"},status=201)
        return JsonResponse({"status":"failure","message":"Only POST method allowed"},status=405)

    except Exception as e:
        return JsonResponse({"statuscode":500,"message":str(e)})
    

def getregistration(request):
    try:
        if request.method == 'GET':
            result = list(CourseRegistration.objects.values())
            print(result)
            if len(result) == 0:
                msg = "No records found"
            else:
                msg = "Data retrived successfully"

            return JsonResponse({"status":"success","message":msg,"data":result,"total no of records":len(result)})
        return JsonResponse({"status":"failure","message":"Only get method allowed"})
    
    except Exception as e:
        return JsonResponse({"message":"Something went wrong"})


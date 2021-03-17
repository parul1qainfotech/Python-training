from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from api.serializer import StudentSerializer
from api.models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class studentdetails(View):
    def get(self,request,args,**kwargs):
        stu=Student.objects.all() 
        serializer=StudentSerializer(stu,many=True)
        # json_data=JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def studentCreate(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")
        else:
            json_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type="application/json")
        
    
def student_read(request):
    if request.method=='GET':
        json_data=request.body
        python_data=io.BytesIO(json_data)
        data=JSONParser().parse(python_data)
        id=data.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            jsond=JSONRenderer().render(serializer.data)
            return HttpResponse(jsond,content_type="application/json")
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        json=JSONRenderer().render(serializer.data)
        return HttpResponse(json,content_type='application/json')
@csrf_exempt           
def student_update(request):
    if request.method=='PUT':
        json_data=request.body
        stu=io.BytesIO(json_data)
        data=JSONParser().parse(stu)
        id=data.get('id')
        stream=Student.objects.get(id=id)
        student=StudentSerializer(stream,data=data,partial=True)
        if student.is_valid():
            student.save()
            res={'msg':'data updated'}
            data=JSONRenderer().render(res)
            return HttpResponse(data,content_type="application/json")
        else:
            data=JSONRenderer().render(student.errors)
            return HttpResponse(data,content_type="application/json")
    
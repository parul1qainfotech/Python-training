from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from modelserial.serializer import DetailSerializer
from modelserial.models import Details
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
# @method_decorator(csrf_exempt,name='dispatch')

# class DetailView(View):
#     def get(self,request,*args,**kwargs):
#         if request.method=='GET':
#             json_data=request.body
#         python_data=io.BytesIO(json_data)
#         data=JSONParser().parse(python_data)
#         id=data.get('id',None)
#         if id is not None:
#             stu=Details.objects.get(id=id)
#             serializer=DetailSerializer(stu)
#             jsond=JSONRenderer().render(serializer.data)
#             return HttpResponse(jsond,content_type="application/json")
#         stu=Details.objects.all()
#         serializer=DetailSerializer(stu,many=True)
#         json=JSONRenderer().render(serializer.data)
#         return HttpResponse(json,content_type='application/json')


#function based api view
@api_view()
def hello_world(request):
    return Response({'msg':'hello world'})
    
@api_view(['GET','POST'])
def data(request):
    if request.method=='GET':
        return Response({'msg':'this is get method'})
    if request.method=='POST':
        data=request.data
        return Response({'msg':'this is post request','data':data})
    
@api_view(['GET','POST','PUT','DELETE'])

def all_method(request,pk=None):
    id=pk
    if request.method=='GET':
        id=request.data.get('id')
        if id is not None:
            data=Details.objects.get(pk=id)
            serializer=DetailSerializer(data)
            return Response(serializer)
        data=Details.objects.all()
        serializer=DetailSerializer(data=data,many=True)
        return Response(serializer)
    
    if request.method=='POST':
        data=request.data
        serializer=DetailSerializer(data=data)
        if serializer.is_valid:
            serializer.save()
            datas=Details.objects.all()
            return Response(datas,{'msg':'successfully added'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='PUT':
        id=request.data.get('id')
        stu=Details.objects.get(pk=id)
        serializer=DetailSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'successfully updated'})
        return Response(serializer.errors)
    
    if request.method=='DELETE':
        id=request.data.get('id')
        data=Details.objects.get(id) 
        data.delete()
        return Response({'msg':'data deleted'})
            
            
#classs based api view

class all_method_class(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            data=Details.objects.get(id=id)
            serializer=DetailSerializer(data)
            if serializer.data.is_valid():
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            data=Details.objects.all()
            serializer=DetailSerializer(data=data,many=True)
            return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
    def post(self,request,format=None):
        data=request.data
        serializer=DetailSerializer(data=data)
        if serializer.is_valid:
            serializer.save()
            datas=Details.objects.all()
            return Response(datas,{'msg':'successfully added'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format=None):
            id=pk
            stu=Details.objects.get(pk=id)
            serializer=DetailSerializer(stu,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'successfully updated'})
            return Response(serializer.errors)    
        
        
    def delete(self,request,pk=None,format=None):
        id=pk
        data=Details.objects.get(id) 
        data.delete()
        return Response({'msg':'data deleted'})
                
        
            


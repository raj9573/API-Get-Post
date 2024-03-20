from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView


from rest_framework.response import Response


from app.models import *


from app.serializers import *



class StudentDisplay(APIView):

    def get(self,request):  

        SO = stud.objects.all()
        print("above a")
        a  =  studentSerializer(SO,many=True)
        print("below a")
        print(a)
        return Response(a.data)

    def post(self,request):
        

        print(request.data)

        return Response("post method activated")
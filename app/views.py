from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response

# showing details
def DisPlay_details(request):
    DO=Details.objects.all()
    d={'Details':DO}
    return render(request,'Display_details.html',d)



# all curd operation using api
class Curd_Of_Details(APIView):
     def get(self,request,Id):
        PQS=Details.objects.all()
        PJSD=Details_Model_Serializer(PQS,many=True)
        return Response(PJSD.data)
    

     def post(self,request,Id):
        PMSD=Details_Model_Serializer(data=request.data) 
        if PMSD.is_valid():
                PMSD.save()
                return Response({'message':'Details are created'})
        else:
            return Response({'Failed':'Details are not created'})


     def put(self,request,Id):
        Pid=request.data['Id']
        PO=Details.objects.get(Id=Id)
        POD=Details_Model_Serializer(PO,data=request.data)
        if POD.is_valid():
                POD.save()
                return Response({'message':'Details  Update'})
        else:
            return Response({'Failed':'Details are not Update'})


     def patch(self,request,Id):
        Pid=request.data['Id']
        PO=Details.objects.get(Id=Id)
        POD=Details_Model_Serializer(PO,data=request.data,partial=True)
        if POD.is_valid():
                POD.save()
                return Response({'message':'Details  Update'})
        else:
            return Response({'Failed':'Product are not Update'})


     def delete(self,request,Id):
        PO=Details.objects.get(Id=Id)
        PO.delete()
        return Response({'Message':'Delete sucessfully'})


# showing database
def Show_Database(request):
     return render(request,'Show_Database.html')
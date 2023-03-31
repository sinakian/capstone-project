from django.shortcuts import render
from rest_framework import generics,viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import booking,menu
from .serializers import bookingSerializer,menuSerializer,MenuItemSerializer




def index(request):
    return render(request, 'index.html', {})

'''
class bookingview(APIView):
    def get(self,request):
        items = booking.objects.all()
        serializer = bookingSerializer(items,many=True)
        return Response(serializer.data) #return json
    def post (self,request):
        serializer = bookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"ststus":"success","data":serializer.data})
'''            
        
class menuview(APIView):
    def get(self,request):
        items = menu.objects.all()
        serializer = menuSerializer(items,many=True)
        return Response(serializer.data) #return json
    def post (self,request):
        serializer = menuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"ststus":"success","data":serializer.data})  

class MenuItemsView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuItemSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuItemSerializer  
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer 
    
   
                             
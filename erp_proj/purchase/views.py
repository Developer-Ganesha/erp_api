from rest_framework.response import Response
from rest_framework.views import APIView
from .seriliazers import PurchaseSerializer
from .seriliazers import (CountrySerializer, CurrencySerializer,Sector_masterSerializer ,Group_masterSerializer,
                          Business_partnerSerializer,Unit_codeSerializer,Item_tdc_MasterSerializer,Item_Grade_MasterSerializer,
                          Store_LocationSerializer, Item_Route_MasterSerializer,Item_parant_FG_Code_MasterSerializer,Sector_MastereSerializer,
                          Item_Section_MasterSerializer ,Unit_convesion_masterSerializer
                          

)
class PurchaseView(APIView):
    def post(self, request, format=None):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Msg': 'Registration Successful'})

class CountryView(APIView):
    def post(self,request,format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Msg':'Data Submitted'})
        
class CurrencyView(APIView): 
    def post(self,request,format=None):
        serializer=CurrencySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Msg':'Data Submmited'})

class Sector_masterView(APIView): 
    def post(self,request,format=None):
        serializer=Sector_masterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Msg':'Sector Data Submmited'})


class Group_masterView(APIView): 
    def post(self,request,format=None):
        serializer=Group_masterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Msg':'Group master Data Submmited'})

class Business_partnerView(APIView): 
    def post(self,request,format=None):
        serializer=Business_partnerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Msg':'Business_partner Data Submmited'})

class Unit_codeView(APIView): 
    def post(self,request,format=None):
        serializer=Unit_codeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Msg':'Unit_cade Data Submmited'})

class Item_tdc_masterView(APIView): 
    def post(self,request,format=None):
        serializer = Item_tdc_MasterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Msg':'Item master Data Submmited'})
        
class Item_Grade_MasterView(APIView): 
    def post(self,request,format=None):
        serializer = Item_Grade_MasterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Msg':'Item grade master Data Submmited'})        

class Store_LocationView(APIView): 
    def post(self,request,format=None):
        serializer = Store_LocationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Msg':'Store_Location Data Submmited'})        

class Item_Route_MasterView(APIView): 
    def post(self,request,format=None):
        serializer = Item_Route_MasterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Msg':'Item route master Data Submmited'})        

class Item_parant_FG_Code_MasterView(APIView): 
    def post(self,request,format=None):
        serializer = Item_parant_FG_Code_MasterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Msg':'parent FG code master Data Submmited'})        

class Sector_MastereView(APIView): 
    def post(self,request,format=None):
        serializer = Sector_MastereSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Msg':'sector code master Data Submmited'})        

class Item_Section_MastereView(APIView): 
    def post(self,request,format=None):
        serializer = Item_Section_MasterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Msg':'Item Section master Data Submmited'})        

class Unit_conversion_masterView(APIView): 
    def post(self,request,format=None):
        serializer = Unit_convesion_masterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Msg':'Unit Conversion Master Data Submmited'})        

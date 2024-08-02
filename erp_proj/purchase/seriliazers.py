from rest_framework import serializers
from .models import (Purchase,Country,Currency,Sector_master, Group_master,Business_partner,Unit_code,
                     Item_tdc_master , Item_Grade_Master ,Store_Location,Item_Route_Master,Item_parant_FG_Code_Master,
                     Sector_Mastere,Item_Section_Master ,Unit_conversion_master
)
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model= Country
        fields= '__all__'

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class Sector_masterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector_master
        fields = '__all__'        

class Group_masterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group_master
        fields = '__all__'        

class Business_partnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business_partner
        fields = '__all__'        

class Unit_codeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit_code
        fields = '__all__'   

class Item_tdc_MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_tdc_master
        fields = '__all__'        

class Item_Grade_MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Grade_Master
        fields = '__all__'        

class Store_LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store_Location
        fields = '__all__'        

class Item_Route_MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Route_Master
        fields = '__all__'        

class Item_parant_FG_Code_MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_parant_FG_Code_Master
        fields = '__all__'  

class Sector_MastereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector_Mastere
        fields = '__all__'        

class Item_Section_MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Section_Master
        fields = '__all__'        

class Unit_convesion_masterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit_conversion_master
        fields = '__all__'        


# from django.contrib import admin
# from .models import Purchase ,Country

# @admin.register(Purchase)
# class PurchaseAdmin(admin.ModelAdmin):
#     list_display = [ 'select_item', 'description', 'available_stoke', 'unit','machine_department',
#                       'quantity','type','remark','use_for','md_ref','sch_date']

# @admin.register(Country) 
# class CountryAdmin(admin.ModelAdmin):
#     list_display =['code','country']

# admin.site.register(Purchase)
# admin.site.register(Country)

from  django.contrib import admin
from .models import (Purchase,Country,Currency,Sector_master ,Group_master,Business_partner,Unit_code,
                     Item_tdc_master , Item_Grade_Master,Store_Location,Item_Route_Master,Item_parant_FG_Code_Master,
                     Sector_Mastere,Item_Section_Master,Unit_conversion_master
)
admin.site.register(Purchase)
admin.site.register(Country)
admin.site.register(Currency)
admin.site.register(Sector_master)
admin.site.register(Group_master)
admin.site.register(Business_partner)
admin.site.register(Unit_code)
admin.site.register(Item_tdc_master)
admin.site.register(Item_Grade_Master)
admin.site.register(Store_Location)
admin.site.register(Item_Route_Master)
admin.site.register(Item_parant_FG_Code_Master)
admin.site.register(Sector_Mastere)
admin.site.register(Item_Section_Master)
admin.site.register(Unit_conversion_master)
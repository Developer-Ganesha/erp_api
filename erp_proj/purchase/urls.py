
from django.urls import path 
from purchase.views import (PurchaseView ,CountryView,CurrencyView,Sector_masterView,Group_masterView,Business_partnerView
,Unit_codeView,Item_tdc_masterView,Item_Grade_MasterView,Store_LocationView,Item_Route_MasterView,Item_parant_FG_Code_MasterView,
Sector_MastereView,Item_Section_MastereView,Unit_conversion_masterView
)
urlpatterns = [

    path('api/purchase/', PurchaseView.as_view(),name='purchase'),
    path('api/country/', CountryView.as_view(),name='country'),
    path('api/currency/',CurrencyView.as_view(),name='currency'),
    path('api/sector_master',Sector_masterView.as_view(),name='sector_master'),
    path('api/group_master',Group_masterView.as_view(),name='group_master'),
    path('api/business_partner',Business_partnerView.as_view(),name='business_partner'),
    path('api/unit_code',Unit_codeView.as_view(),name='unit_code'),
    path('api/item_tdc_master',Item_tdc_masterView.as_view(),name='item_tdc_master'),
    path('api/item_grade_master',Item_Grade_MasterView.as_view(),name='item_grade_master'),
    path('api/store_location',Store_LocationView.as_view(),name='store_location'),
    path('api/Item_route_master',Item_Route_MasterView.as_view(),name='item_route_master'),
    path('api/fg_code_master',Item_parant_FG_Code_MasterView.as_view(),name='fg_code_master'),
    path('api/sector_mastere',Sector_MastereView.as_view(),name='sector_mastere'),
    path('api/item_section_mastere',Item_Section_MastereView.as_view(),name='item_section_mastere'),
    path('api/unit_conversion',Unit_conversion_masterView.as_view(),name='unit_conversion')
]

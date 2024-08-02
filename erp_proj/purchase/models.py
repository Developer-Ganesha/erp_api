from django.db import models
# 1 purchase master  
class Purchase(models.Model):
    select_item = models.CharField(max_length=200)
    description = models.TextField()
    available_stoke=models.CharField(max_length=200)
    unit     = models.CharField(max_length=200)
    machine_department = models.CharField(max_length=200)
    quantity = models.CharField( max_length=100)
    type     = models.CharField(max_length=200)
    remark   = models.CharField(max_length=200)
    use_for  = models.CharField(max_length=200)
    md_ref   = models.CharField(max_length=200)
    sch_date = models.DateField()

# 2 supplier customer master
class Country(models.Model):
    code=models.IntegerField()
    Country= models.CharField(max_length=200)

# 3 supplier customer master
class Currency(models.Model):
    code = models.IntegerField()
    symbol = models.CharField(max_length=200)
    description = models.TextField()

# 4 sector master
class Sector_master(models.Model): 
    sector_profile = models.CharField(max_length=200)
    sector_name = models.CharField(max_length=200)

# 5 group master api
class Group_master(models.Model):
    sector_profile = models.CharField(max_length=200)
    sector_name = models.CharField(max_length=200)

# 6 Business_partner api
class Business_partner(models.Model):
    code = models.IntegerField()
    Country = models.CharField(max_length=200)
    
# 7 Unit_code api
class Unit_code(models.Model): 
    unit = models.CharField(max_length=200)
    edit = models.CharField(max_length=200)
    delete = models.CharField(max_length=200)

# 8 Item_tdc_master
class Item_tdc_master(models.Model):
    prefix = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

# Item grade master
class Item_Grade_Master(models.Model): 
    sub_group = models.CharField(max_length=200)
    prefix = models.CharField(max_length=200)
    item_group_name = models.CharField(max_length=200)
    color_code =models.CharField(max_length=200)
    
# store location 
class Store_Location(models.Model):
    store_name=models.CharField(max_length=200)

# Item Route Master
class Item_Route_Master(models.Model):
    prefix = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

# Item parant FG code master
class Item_parant_FG_Code_Master(models.Model):
    parent_fg_code = models.CharField(max_length=230)      

# 4 sector master
class Sector_Mastere(models.Model): 
    sector_prefix = models.CharField(max_length=200)
    sector_name = models.CharField(max_length=200)

# 4 Item section master
class Item_Section_Master(models.Model): 
    prefix = models.CharField(max_length=200)
    section_name = models.CharField(max_length=200)

# unit conversion master
class Unit_conversion_master(models.Model):
    sub_group = models.CharField(max_length=200) 
    item = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    stock_qty= models.CharField(max_length=200)
    stock_unit = models.CharField(max_length=200)   

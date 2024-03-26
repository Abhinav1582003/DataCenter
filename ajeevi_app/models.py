from django.db import models

class user_admin(models.Model):
    user_name = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user_admin'


class master_table(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    user_name = models.ForeignKey(user_admin, on_delete=models.CASCADE, db_column='user_name')
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = False
        db_table = 'master_table'


class address(models.Model):
    id = models.OneToOneField(master_table, on_delete=models.CASCADE, db_column='id',primary_key=True)  # Changed db_column to 'master_id'
    line1 = models.CharField(max_length=50)
    line2 = models.CharField(max_length=50)
    district = models.CharField(max_length=20)
    district_zone = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=6)
    state = models.CharField(max_length=20)
    state_ward = models.IntegerField()
    country = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'address'

class entity_type(models.Model):
    id=models.OneToOneField(master_table,on_delete=models.CASCADE,primary_key=True,db_column='id')
    entity_name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    
    class Meta:
        managed=False
        db_table='entity_type'

class contact(models.Model):
    id=models.ForeignKey("master_table", on_delete=models.CASCADE,db_column='id')
    person_id=models.IntegerField(primary_key=True)
    person_name=models.CharField(max_length=50)
    number=models.BigIntegerField()
    email=models.CharField(max_length=50)
    
    class Meta:
        managed=False
        db_table='contact'
        
class branch_table(models.Model):
    id=models.ForeignKey('master_table',on_delete=models.CASCADE,db_column='id')
    branch_id=models.IntegerField(primary_key=True)
    branch_location=models.CharField(max_length=50)
    
    class Meta:
        managed=False
        db_table='branch_table'
        
class branch_address(models.Model):
    branch_id=models.OneToOneField('branch_table',on_delete=models.CASCADE,primary_key=True,db_column='branch_id')
    line1=models.CharField(max_length=50)
    line2=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    distric_zone=models.CharField(max_length=50)
    pin_code=models.CharField(max_length=6)
    state=models.CharField(max_length=50)

    class Meta:
        managed=False
        db_table='branch_address'
        

class branch_contact(models.Model):
    branch_id=models.ForeignKey('branch_table',on_delete=models.CASCADE,db_column='branch_id')
    person_id=models.IntegerField(primary_key=True)
    phone_number=models.BigIntegerField()
    email=models.CharField(max_length=50)
    
    class Meta:
        managed=False
        db_table='branch_contact'


# device master-table model:

class device_master_table(models.Model):
    packet_id=models.IntegerField(primary_key=True)
    device_name=models.CharField(max_length=30)
    quantity=models.CharField(max_length=20)
    remaining=models.CharField(max_length=20)
    coming_date=models.CharField(max_length=20)
    updated=models.CharField(max_length=20)
    
    class Meta:
        managed=False
        db_table='device_master_table'

#device part:

class device_part(models.Model):
    packet_id=models.ForeignKey(device_master_table,on_delete=models.CASCADE,db_column='packet_id')
    device_id=models.IntegerField(primary_key=True)
    part_1=models.CharField(max_length=50)
    part_2=models.CharField(max_length=50)
    
    class Meta:
        managed=False
        db_table='device_part'

#device location:  
class device_location(models.Model):
    branch_id=models.ForeignKey(branch_table,on_delete=models.CASCADE,db_column='branch_id')
    device_id=models.OneToOneField(device_part,on_delete=models.CASCADE,db_column='device_id',primary_key=True)
    line_1=models.CharField(max_length=20)
    line_2=models.CharField(max_length=20)
    pincode=models.CharField(max_length=6)
    install_date=models.CharField(max_length=20)
    location=models.CharField(max_length=30)

    class Meta:
        managed=False
        db_table='device_location'

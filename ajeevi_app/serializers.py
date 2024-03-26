from rest_framework import serializers
from .models import *

class user_admin_serializers(serializers.ModelSerializer):
    class Meta:
        model=user_admin
        fields='__all__'

class master_table_serializers(serializers.ModelSerializer):
    class Meta:
        model=master_table
        fields='__all__'
class address_serializers(serializers.ModelSerializer):
    class Meta:
        model=address
        fields='__all__'
class entity_type_serializers(serializers.ModelSerializer):
    class Meta:
        model=entity_type
        fields='__all__'
class contact_serializers(serializers.ModelSerializer):
    class Meta:
        model=contact
        fields='__all__'


class branch_table_serializers(serializers.ModelSerializer):
    class Meta:
        model=branch_table
        fields='__all__'
        
class branch_address_serializers(serializers.ModelSerializer):
    class Meta:
        model=branch_address
        fields='__all__'
class branch_contact_serializers(serializers.ModelSerializer):
    class Meta:
        model=branch_contact
        fields='__all__'
class device_master_table(serializers.ModelSerializer):
    class Meta:
        model=device_master_table
        fields='__all__'
class device_part_serializers(serializers.ModelSerializer):
    class Meta:
        model=device_part
        fields='__all__'
class device_location_serializers(serializers.ModelSerializer):
    model=device_location
    fields='__all__'
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(master_table)
admin.site.register(user_admin)
admin.site.register(address)
admin.site.register(entity_type)
admin.site.register(contact)
admin.site.register(branch_table)
admin.site.register(branch_address)
admin.site.register(branch_contact)
admin.site.register(device_master_table)
admin.site.register(device_part)
admin.site.register(device_location)
from django.urls import path,include
from . import views

urlpatterns=[
    path('test-data/', views.test_data),
    path('master-table/', views.master_table_data),
    path('address-table/', views.address_table),
    path('entity_type_data/',views.entity_type_table),
    path('contact_data/',views.contact_table),
    path('branch_table/',views.branch_table_data),
    path('branch-address-table-data/',views.branch_address_table),
    path('branch-contact-data/',views.branch_contact_table)
   
]

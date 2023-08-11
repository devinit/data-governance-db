from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('documents', views.DocumentList.as_view(), name='document_list'),
    path('documents/<int:pk>', views.DocumentDetail.as_view(), name='document_detail'),
    path('institutions', views.InstitutionList.as_view(), name='institution_list'),
    path('institutions/<int:pk>', views.InstitutionDetail.as_view(), name='institution_detail'),
    path('institution-types', views.InstitutionTypeList.as_view(), name='institution_type_list'),
    path('institution-types/<int:pk>', views.InstitutionTypeDetail.as_view(), name='institution_type_detail'),
    path('categories', views.CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>', views.CategoryDetail.as_view(), name='category_detail'),
    path('document-types', views.DocumentTypeList.as_view(), name='document_type_list'),
    path('document-types/<int:pk>', views.DocumentTypeDetail.as_view(), name='document_type_detail'),
]
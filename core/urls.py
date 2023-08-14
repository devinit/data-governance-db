from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('documents', views.DocumentList.as_view(), name='document_list'),
    path('documents/<int:pk>', views.DocumentDetail.as_view(), name='document_detail'),
    path('documents/add', views.DocumentAdd.as_view(), name='document_add'),
    path('documents/<int:pk>/delete', views.DocumentDelete.as_view(), name='document_delete'),
    path('documents/<int:pk>/edit', views.DocumentEdit.as_view(), name='document_edit'),
    path('institutions', views.InstitutionList.as_view(), name='institution_list'),
    path('institutions/<int:pk>', views.InstitutionDetail.as_view(), name='institution_detail'),
    path('institutions/add', views.InstitutionAdd.as_view(), name='institution_add'),
    path('institutions/<int:pk>/delete', views.InstitutionDelete.as_view(), name='institution_delete'),
    path('institutions/<int:pk>/edit', views.InstitutionEdit.as_view(), name='institution_edit'),
    path('institution-types', views.InstitutionTypeList.as_view(), name='institution_type_list'),
    path('institution-types/<int:pk>', views.InstitutionTypeDetail.as_view(), name='institution_type_detail'),
    path('institution-types/add', views.InstitutionTypeAdd.as_view(), name='institution_type_add'),
    path('institution-types/<int:pk>/delete', views.InstitutionTypeDelete.as_view(), name='institution_type_delete'),
    path('institution-types/<int:pk>/edit', views.InstitutionTypeEdit.as_view(), name='institution_type_edit'),
    path('categories', views.CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>', views.CategoryDetail.as_view(), name='category_detail'),
    path('categories/add', views.CategoryAdd.as_view(), name='category_add'),
    path('categories/<int:pk>/delete', views.CategoryDelete.as_view(), name='category_delete'),
    path('categories/<int:pk>/edit', views.CategoryEdit.as_view(), name='category_edit'),
    path('document-types', views.DocumentTypeList.as_view(), name='document_type_list'),
    path('document-types/<int:pk>', views.DocumentTypeDetail.as_view(), name='document_type_detail'),
    path('document-types/add', views.DocumentTypeAdd.as_view(), name='document_type_add'),
    path('document-types/<int:pk>/delete', views.DocumentTypeDelete.as_view(), name='document_type_delete'),
    path('document-types/<int:pk>/edit', views.DocumentTypeEdit.as_view(), name='document_type_edit'),
]
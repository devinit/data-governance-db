from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('projects', views.ProjectList.as_view(), name='project_list'),
    # path('project/<str:id>', views.ProjectView.as_view(), name='project_detail'),
    # path('projects/add', views.ProjectAdd.as_view(), name='project_add'),
    # path('projects/export', views.FullProjectCSVExport.as_view(), name='project_export'),
    # path('project/<str:id>/delete', views.ProjectDelete.as_view(), name='project_delete'),
    # path('project/<str:id>/edit', views.ProjectEdit.as_view(), name='project_edit'),
]
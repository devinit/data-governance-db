from datetime import datetime
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
import json
import csv
# from .models import (
#     Client,
#     Project
# )
# from .forms import (
#     ProjectAddForm,
#     ProjectEditForm
# )


class Home(generic.TemplateView):
    template_name = "core/home.html"


# class ClientList(LoginRequiredMixin, generic.ListView):
#     model = Client

#     def get_queryset(self):
#         all_param = self.request.GET.get('all', None)
#         if all_param:
#             return Client.objects.all()
#         return Client.objects.filter(active=True)


# class ClientView(LoginRequiredMixin, generic.DetailView):
#     model = Client
#     slug_field = slug_url_kwarg = "code"


# class ProjectList(LoginRequiredMixin, generic.ListView):
#     model = Project

#     def get_queryset(self):
#         all_param = self.request.GET.get('all', None)
#         self.company_param = self.request.GET.get('company', 'All')
#         if all_param:
#             results = Project.objects.all().order_by('-project_type', 'id')
#         else:
#             results = Project.objects.filter(status__in=Project.CURRENT_STATUSES).order_by('-project_type', 'id')
#         if self.company_param != 'All':
#             matching_company = Company.objects.filter(code=self.company_param)
#             if matching_company:
#                 return results.filter(company=self.company_param)
#         return results

#     def get_context_data(self, **kwargs):
#         context = super(ProjectList, self).get_context_data(**kwargs)
#         context["filter_companies"] = ['All'] + [company.code for company in Company.objects.all()]
#         context["selected_company"] = self.company_param
#         return context


# class ProjectView(LoginRequiredMixin, PermissionRequiredMixin, generic.edit.FormMixin, generic.DetailView):
#     model = Project
#     slug_field = slug_url_kwarg = "id"
#     form_class = ComponentForm
#     permission_required = 'core.add_component'

#     def get_success_url(self):
#         return reverse('core:project', kwargs={'id': self.object.id})

#     def get_initial(self):
#         return {"project": self.get_object() }

#     def get_context_data(self, **kwargs):
#         context = super(ProjectView, self).get_context_data(**kwargs)
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         form.save()
#         return super(ProjectView, self).form_valid(form)

#     def get_permission_required(self):
#         if self.request.method == 'POST':
#             return (self.permission_required, ) if isinstance(self.permission_required, str) else self.permission_required
#         return list()


# class ProjectAdd(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
#     model = Project
#     slug_field = slug_url_kwarg = "id"
#     form_class = ProjectAddForm
#     permission_required = 'core.add_project'

#     def get_success_url(self):
#         return reverse('core:project', kwargs={'id': self.object.id})


# class ProjectDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
#     model = Project
#     slug_field = slug_url_kwarg = "id"
#     permission_required = 'core.delete_project'

#     def get_success_url(self):
#         return reverse('core:projects')


# class ProjectEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
#     model = Project
#     slug_field = slug_url_kwarg = "id"
#     form_class = ProjectEditForm
#     permission_required = 'core.change_project'

#     def get_success_url(self):
#         return reverse('core:project', kwargs={'id': self.object.id})

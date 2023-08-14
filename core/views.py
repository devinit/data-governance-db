from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from .models import (
    Document,
    Institution,
    InstitutionType,
    Category,
    DocumentType
)
from .forms import (
    DocumentForm
)


class Home(generic.TemplateView):
    template_name = "core/home.html"


class DocumentList(LoginRequiredMixin, generic.ListView):
    model = Document

    def get_queryset(self):
        institution_param = self.request.GET.get('institution', None)
        category_param = self.request.GET.get('category', None)
        type_param = self.request.GET.get('type', None)
        documents = Document.objects.all()
        if institution_param is not None:
            documents = documents.filter(institution__id=institution_param)
        if category_param is not None:
            documents = documents.filter(category__id=category_param)
        if type_param is not None:
            documents = documents.filter(type__id=type_param)
        return documents


class DocumentDetail(LoginRequiredMixin, generic.DetailView):
    model = Document


class DocumentAdd(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Document
    form_class = DocumentForm
    permission_required = 'core.add_document'

    def get_success_url(self):
        return reverse('core:document_detail', kwargs={'pk': self.object.pk})


class DocumentDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Document
    permission_required = 'core.delete_document'

    def get_success_url(self):
        return reverse('core:document_list')


class DocumentEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Document
    form_class = DocumentForm
    permission_required = 'planner.change_document'

    def get_success_url(self):
        return reverse('core:document_detail', kwargs={'pk': self.object.pk})


class InstitutionList(LoginRequiredMixin, generic.ListView):
    model = Institution


class InstitutionDetail(LoginRequiredMixin, generic.DetailView):
    model = Institution


class InstitutionTypeList(LoginRequiredMixin, generic.ListView):
    model = InstitutionType


class InstitutionTypeDetail(LoginRequiredMixin, generic.DetailView):
    model = InstitutionType


class CategoryList(LoginRequiredMixin, generic.ListView):
    model = Category


class CategoryDetail(LoginRequiredMixin, generic.DetailView):
    model = Category


class DocumentTypeList(LoginRequiredMixin, generic.ListView):
    model = DocumentType


class DocumentTypeDetail(LoginRequiredMixin, generic.DetailView):
    model = DocumentType


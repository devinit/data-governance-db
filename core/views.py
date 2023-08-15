from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count
from .models import (
    Document,
    Institution,
    InstitutionType,
    Category,
    DocumentType
)
from .forms import (
    DocumentForm,
    InstitutionForm,
    InstitutionTypeForm,
    CategoryForm,
    DocumentTypeForm
)


class Home(generic.TemplateView):
    template_name = "core/home.html"


class DocumentList(LoginRequiredMixin, generic.ListView):
    model = Document

    def get_queryset(self):
        institution_param = self.request.GET.get('institution', None)
        category_param = self.request.GET.get('category', None)
        type_param = self.request.GET.get('type', None)
        documents = Document.objects.all().order_by('institution__name', 'category__name')
        if institution_param is not None:
            documents = documents.filter(institution__id=institution_param)
        if category_param is not None:
            documents = documents.filter(category__id=category_param)
        if type_param is not None:
            documents = documents.filter(type__id=type_param)
        return documents

    def get_context_data(self, **kwargs):
        context = super(DocumentList, self).get_context_data(**kwargs)
        documents = self.get_queryset()

        page_param = self.request.GET.get('p', 1)
        paginator = Paginator(documents, 100)
        context['document_list'] = paginator.get_page(page_param)

        return context


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

    def get_queryset(self):
        type_param = self.request.GET.get('type', None)
        institutions = Institution.objects.all() \
            .annotate(count_documents=Count('documents')) \
            .order_by('-count_documents')
        if type_param is not None:
            institutions = institutions.filter(type__id=type_param)
        return institutions


class InstitutionDetail(LoginRequiredMixin, generic.DetailView):
    model = Institution


class InstitutionAdd(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Institution
    form_class = InstitutionForm
    permission_required = 'core.add_institution'

    def get_success_url(self):
        return reverse('core:institution_detail', kwargs={'pk': self.object.pk})


class InstitutionDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Institution
    permission_required = 'core.delete_institution'

    def get_success_url(self):
        return reverse('core:institution_list')


class InstitutionEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Institution
    form_class = InstitutionForm
    permission_required = 'planner.change_institution'

    def get_success_url(self):
        return reverse('core:institution_detail', kwargs={'pk': self.object.pk})


class InstitutionTypeList(LoginRequiredMixin, generic.ListView):
    model = InstitutionType

    def get_queryset(self):
        return InstitutionType.objects.all() \
            .annotate(count_institutions=Count('institutions')) \
            .order_by('-count_institutions')


class InstitutionTypeDetail(LoginRequiredMixin, generic.DetailView):
    model = InstitutionType


class InstitutionTypeAdd(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = InstitutionType
    form_class = InstitutionTypeForm
    permission_required = 'core.add_institutiontype'

    def get_success_url(self):
        return reverse('core:institution_type_detail', kwargs={'pk': self.object.pk})


class InstitutionTypeDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = InstitutionType
    permission_required = 'core.delete_institutiontype'

    def get_success_url(self):
        return reverse('core:institution_type_list')


class InstitutionTypeEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = InstitutionType
    form_class = InstitutionTypeForm
    permission_required = 'planner.change_institutiontype'

    def get_success_url(self):
        return reverse('core:institution_type_detail', kwargs={'pk': self.object.pk})


class CategoryList(LoginRequiredMixin, generic.ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.all() \
            .annotate(count_documents=Count('documents')) \
            .order_by('-count_documents')


class CategoryDetail(LoginRequiredMixin, generic.DetailView):
    model = Category


class CategoryAdd(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Category
    form_class = CategoryForm
    permission_required = 'core.add_category'

    def get_success_url(self):
        return reverse('core:category_detail', kwargs={'pk': self.object.pk})


class CategoryDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Category
    permission_required = 'core.delete_category'

    def get_success_url(self):
        return reverse('core:category_list')


class CategoryEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Category
    form_class = CategoryForm
    permission_required = 'planner.change_category'

    def get_success_url(self):
        return reverse('core:category_detail', kwargs={'pk': self.object.pk})


class DocumentTypeList(LoginRequiredMixin, generic.ListView):
    model = DocumentType

    def get_queryset(self):
        return DocumentType.objects.all() \
            .annotate(count_documents=Count('documents')) \
            .order_by('-count_documents')


class DocumentTypeDetail(LoginRequiredMixin, generic.DetailView):
    model = DocumentType


class DocumentTypeAdd(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = DocumentType
    form_class = DocumentTypeForm
    permission_required = 'core.add_documenttype'

    def get_success_url(self):
        return reverse('core:document_type_detail', kwargs={'pk': self.object.pk})


class DocumentTypeDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = DocumentType
    permission_required = 'core.delete_documenttype'

    def get_success_url(self):
        return reverse('core:document_type_list')


class DocumentTypeEdit(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = DocumentType
    form_class = DocumentTypeForm
    permission_required = 'planner.change_documenttype'

    def get_success_url(self):
        return reverse('core:document_type_detail', kwargs={'pk': self.object.pk})


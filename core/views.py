from django.urls import reverse
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Count
from django.http import HttpResponse
from .models import (
    Document,
    Institution,
    InstitutionType,
    Category,
    DocumentType,
    HomePageSettings
)
from .forms import (
    DocumentForm,
    InstitutionForm,
    InstitutionTypeForm,
    CategoryForm,
    DocumentTypeForm
)
from .admin import (
    ExternalDocumentResource
)


class Home(generic.TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        home_page_settings = HomePageSettings.objects.all()
        if len(home_page_settings) == 0:
            context['home_page_settings'] = None
        else:
            context['home_page_settings'] = home_page_settings.first()

        return context


class DocumentCSVExport(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        institution_param = request.GET.get('institution', None)
        try:
            institution_param = int(institution_param)
        except (ValueError, TypeError) as e:
            institution_param = None
        category_param = request.GET.get('category', None)
        try:
            category_param = int(category_param)
        except (ValueError, TypeError) as e:
            category_param = None
        type_param = request.GET.get('type', None)
        try:
            type_param = int(type_param)
        except (ValueError, TypeError) as e:
            self.type_param = None
        scope_param = self.request.GET.get('scope', None)
        try:
            self.scope_param = int(scope_param)
        except (ValueError, TypeError) as e:
            self.scope_param = None
        documents = Document.objects.all().order_by('institution__name', 'category__name')
        if institution_param is not None:
            documents = documents.filter(institution__id=institution_param)
        if category_param is not None:
            documents = documents.filter(category__id=category_param)
        if type_param is not None:
            documents = documents.filter(type__id=type_param)
        if self.scope_param is not None:
            documents = documents.filter(institution__type__id=self.scope_param)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="documents.csv"'
        dataset = ExternalDocumentResource().export(documents)
        response.content = dataset.csv
        return response


class DocumentList(LoginRequiredMixin, generic.ListView):
    model = Document

    def get_queryset(self):
        institution_param = self.request.GET.get('institution', None)
        try:
            self.institution_param = int(institution_param)
        except (ValueError, TypeError) as e:
            self.institution_param = None
        category_param = self.request.GET.get('category', None)
        try:
            self.category_param = int(category_param)
        except (ValueError, TypeError) as e:
            self.category_param = None
        type_param = self.request.GET.get('type', None)
        try:
            self.type_param = int(type_param)
        except (ValueError, TypeError) as e:
            self.type_param = None
        scope_param = self.request.GET.get('scope', None)
        try:
            self.scope_param = int(scope_param)
        except (ValueError, TypeError) as e:
            self.scope_param = None
        documents = Document.objects.all().order_by('institution__name', 'category__name')
        if self.institution_param is not None:
            documents = documents.filter(institution__id=self.institution_param)
        if self.category_param is not None:
            documents = documents.filter(category__id=self.category_param)
        if self.type_param is not None:
            documents = documents.filter(type__id=self.type_param)
        if self.scope_param is not None:
            documents = documents.filter(institution__type__id=self.scope_param)
        return documents

    def get_context_data(self, **kwargs):
        context = super(DocumentList, self).get_context_data(**kwargs)
        documents = self.get_queryset()

        institutions = Institution.objects.all().order_by('name')
        context['institutions'] = institutions
        context['institution_param'] = self.institution_param
        categories = Category.objects.all().order_by('name')
        context['categories'] = categories
        context['category_param'] = self.category_param
        document_types = DocumentType.objects.all().order_by('name')
        context['document_types'] = document_types
        context['type_param'] = self.type_param
        scopes = InstitutionType.objects.all().order_by('name')
        context['scopes'] = scopes
        context['scope_param'] = self.scope_param

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

